class Item:
    def __init__(self, id, name, status, description):
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.class_name = status.lower().replace(" ", "")

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card["id"], card["name"], list["name"], card["desc"])