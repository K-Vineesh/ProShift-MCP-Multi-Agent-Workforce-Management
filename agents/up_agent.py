class UPAgent:
    def assign_up(self, available_workers, assigned_ids):
        up_workers = available_workers[~available_workers["worker_id"].isin(assigned_ids)]["worker_id"].tolist()
        return up_workers
