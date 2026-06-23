from datetime import datetime

class Deadline:
    def __init__(self, start_date: datetime, end_date: datetime):
        if not isinstance(start_date, datetime):
            raise TypeError("start_date deve ser do tipo datetime")
        if not isinstance(end_date, datetime):
            raise TypeError("end_date deve ser do tipo datetime")
        if start_date > end_date:
            raise ValueError("A data de início não pode ser posterior à data de término.")
        self.start_date = start_date
        self.end_date = end_date

    @property
    def duration_days(self):
        result = self.end_date - self.start_date
        return result.days

    @property
    def is_overdue(self):
        return datetime.now() > self.end_date