# Category.py
class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def display_info(self):
        print(f"Category ID: {self.category_id}")
        print(f"Name: {self.name}")
