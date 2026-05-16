import os
from models import Task

FILE_PATH = "tasks.txt"

class TaskService:

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(FILE_PATH):
            return []
        with open(FILE_PATH, "r") as file:
            lines = file.read().splitlines()
            tasks = []
            for line in lines:
                if line.strip() == "":
                    continue
                if "|" in line:
                    title, date = line.split("|", 1)
                else:
                    title, date = line, ""
                tasks.append(Task(title, date))
            return tasks

    def save_tasks(self):
        with open(FILE_PATH, "w") as file:
            for task in self.tasks:
                file.write(task.to_string() + "\n")

    def add_task(self, title, date):
        task = Task(title, date)
        self.tasks.append(task)
        self.save_tasks()

    def get_all(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
