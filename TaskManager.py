# TaskManager.py
from Task import Task
from Category import Category
from User import User

# Create categories
category1 = Category(1, "Work")
category2 = Category(2, "Personal")

# Create tasks
task1 = Task(101, "Complete project report", "Finish the project report by end of the week.", category1)
task2 = Task(102, "Grocery shopping", "Buy fruits, vegetables, and milk.", category2)

# Create users
user1 = User(1, "john_doe", "john.doe@example.com")
user2 = User(2, "jane_smith", "jane.smith@example.com")

# Users add tasks to their lists
user1.add_task(task1)
user2.add_task(task2)

# Display information
user1.display_info()
print("\n" + "=" * 50 + "\n")
user2.display_info()
