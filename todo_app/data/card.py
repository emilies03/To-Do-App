class Card:
    def __init__(self, id, name, status, description):
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.class_name = status.lower().replace(" ", "")