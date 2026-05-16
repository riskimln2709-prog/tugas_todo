class Task:

    def __init__(self, title, date):
        self.title = title
        self.date = date

    def to_string(self):
        return f"{self.title}|{self.date}"
