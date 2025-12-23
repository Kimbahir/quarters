from datetime import date, timedelta

class Quarter:
    def __init__(self, year: int, quarter: int):
        if quarter not in {1, 2, 3, 4}:
            raise ValueError("quarter must be 1, 2, 3, or 4")
        self.year = year
        self.quarter = quarter

    @classmethod
    def from_date(cls, dt: date):
        q = (dt.month - 1) // 3 + 1
        return cls(dt.year, q)

    def to_date(self) -> date:
        month = (self.quarter - 1) * 3 + 1
        return date(self.year, month, 1)

    def __str__(self):
        return f"{self.year}Q{self.quarter}"

    def __repr__(self):
        return f"Quarter(year={self.year}, quarter={self.quarter})"

    def add_quarters(self, n: int):
        total = (self.year * 4 + self.quarter - 1) + n
        year, quarter = divmod(total, 4)
        return Quarter(year, quarter + 1)
    
    def first_day(self) -> date:
        return self.to_date()
    
    def last_day(self) -> date:
        month = self.quarter * 3
        if month == 12:
            return date(self.year, month, 31)
        else:
            next_month_first_day = date(self.year, month + 1, 1)
            return next_month_first_day.replace(day=1) - timedelta(days=1)

    def __eq__(self, other):
        return isinstance(other, Quarter) and self.year == other.year and self.quarter == other.quarter
