class ItemsViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        return [c for c in self.items if c.status == "To Do"]

    @property
    def started_items(self):
        return [c for c in self.items if c.status == "Started"]

    @property
    def done_items(self):
        return [c for c in self.items if c.status == "Done"]    