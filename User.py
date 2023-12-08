# User.py
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print("Tasks:")
        for task in self.tasks:
            task.display_info()
            print()
