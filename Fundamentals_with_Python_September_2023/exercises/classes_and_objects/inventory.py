class Inventory:
    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"
