import pandas as pd

class AbsenceAgent:
    def __init__(self, workers_df, leave_requests_df):
        self.workers_df = workers_df
        self.leave_requests_df = leave_requests_df

    def get_available_workers(self, date):
        leave_set = set(self.leave_requests_df[self.leave_requests_df["date"] == date]["worker_id"].tolist())
        available = self.workers_df[~self.workers_df["worker_id"].isin(leave_set)]
        return available
