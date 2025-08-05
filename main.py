import os
import pandas as pd
from supervisor import Supervisor

def get_worker_name(worker_id, workers_df):
    row = workers_df[workers_df["worker_id"] == worker_id]
    return row["name"].values[0] if not row.empty else str(worker_id)

def main():
    workers = pd.read_csv("data/workers.csv")
    leave_requests = pd.read_csv("data/leave_requests.csv")
    workload = pd.read_csv("data/workload_schedule.csv")
    zones = ["zone_A", "zone_B", "zone_C", "sorting", "moving", "swapping"]

    sup = Supervisor(workers, leave_requests, workload, zones)
    os.makedirs("reports", exist_ok=True)
    dates = workload["date"].tolist()

    for date in dates:
        print(f"\n=== {date} ===")
        assignments, up_workers, notes = sup.run_day(date)
        # Save CSV
        report_rows = []
        for zone, worker_ids in assignments.items():
            for wid in worker_ids:
                report_rows.append({
                    "date": date,
                    "zone": zone,
                    "worker_id": wid,
                    "worker_name": get_worker_name(wid, workers)
                })
        for wid in up_workers:
            report_rows.append({
                "date": date,
                "zone": "unproductive",
                "worker_id": wid,
                "worker_name": get_worker_name(wid, workers)
            })
        df_report = pd.DataFrame(report_rows)
        csv_file = f"reports/assignment_{date}.csv"
        df_report.to_csv(csv_file, index=False)
        print(f"Assignments saved to {csv_file}")

        # Save TXT
        with open(f"reports/assignment_{date}.txt", "w", encoding="utf-8") as f:
            f.write(f"Date: {date}\n\n")
            for zone in assignments:
                names = [get_worker_name(wid, workers) for wid in assignments[zone]]
                f.write(f"Zone: {zone}: {', '.join(names)}\n")
            up_names = [get_worker_name(wid, workers) for wid in up_workers]
            f.write(f"\nUnproductive Day (UP): {', '.join(up_names)}\n")
            f.write("\nNotes:\n")
            for note in notes:
                f.write(f"- {note}\n")
        print(f"Human-readable report saved to reports/assignment_{date}.txt")

    print("\nAll days processed. Reports saved in the 'reports/' folder.")

if __name__ == "__main__":
    main()
