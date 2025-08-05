import pandas as pd

class ZoneAssignmentAgent:
    def __init__(self, zones):
        self.zones = zones  # List of zone names

    def assign(self, available_workers, today_needs):
        assignments = {}
        assigned_ids = set()

        for zone in self.zones:
            need = int(today_needs[zone])
            regulars = available_workers[(available_workers["is_extra"] == False) & (~available_workers["worker_id"].isin(assigned_ids))]
            extras = available_workers[(available_workers["is_extra"] == True) & (~available_workers["worker_id"].isin(assigned_ids))]
            selected = regulars.sample(min(need, len(regulars)), random_state=42) if len(regulars) else pd.DataFrame()
            assigned_ids.update(selected["worker_id"].tolist())

            if len(selected) < need and len(extras):
                n_needed = need - len(selected)
                selected_extras = extras.sample(min(n_needed, len(extras)), random_state=42)
                selected = pd.concat([selected, selected_extras])
                assigned_ids.update(selected_extras["worker_id"].tolist())

            assignments[zone] = selected["worker_id"].tolist()

        return assignments, assigned_ids
