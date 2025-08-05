from agents.absence_agent import AbsenceAgent
from agents.zone_assignment_agent import ZoneAssignmentAgent
from agents.up_agent import UPAgent

class Supervisor:
    def __init__(self, workers_df, leave_requests_df, workload_df, zones):
        self.absence_agent = AbsenceAgent(workers_df, leave_requests_df)
        self.zone_agent = ZoneAssignmentAgent(zones)
        self.up_agent = UPAgent()
        self.workload_df = workload_df
        self.zones = zones

    def run_day(self, date):
        notes = []
        today_row = self.workload_df[self.workload_df["date"] == date]
        if today_row.empty:
            notes.append("No workload data for this day.")
            return {}, [], notes
        today_needs = today_row.iloc[0].to_dict()

        # Step 1: Get available workers (AbsenceAgent)
        available_workers = self.absence_agent.get_available_workers(date)
        notes.append(f"{len(available_workers)} workers available after leave handling.")

        # Step 2: Assign zones (ZoneAssignmentAgent)
        assignments, assigned_ids = self.zone_agent.assign(available_workers, today_needs)

        for zone in self.zones:
            need = int(today_needs[zone])
            actual = len(assignments[zone])
            if actual < need:
                notes.append(f"Zone {zone} short by {need - actual} worker(s)! (all extras called)")

        # Step 3: Assign UP days (UPAgent)
        up_workers = self.up_agent.assign_up(available_workers, assigned_ids)
        notes.append(f"{len(up_workers)} workers got unproductive (UP) day.")

        return assignments, up_workers, notes
