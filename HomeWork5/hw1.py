import datetime
from abc import ABC


class Homework(ABC):
    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self):
        return self.created + self.deadline >= datetime.datetime.now()
