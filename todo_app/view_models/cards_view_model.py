class CardsViewModel:
    def __init__(self, cards):
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    @property
    def todo_items(self):
        return [c for c in self.cards if c.status == "To Do"]

    @property
    def started_items(self):
        return [c for c in self.cards if c.status == "Started"]

    @property
    def done_items(self):
        return [c for c in self.cards if c.status == "Done"]    