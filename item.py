# item.py

class Item:
    def __init__(self, id, name, type, price, location):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.location = location

    def __repr__(self):
        return f"Item({self.id}, {self.name}, {self.type}, {self.price}, {self.location})"
