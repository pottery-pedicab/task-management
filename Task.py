# Task.py
class Task:
    def __init__(self, task_id, title, description, category):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.category = category

    def display_info(self):
        print(f"Task ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Category: {self.category}")
