class Item:
    def __init__(self, id, name, status, description):
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.class_name = status.lower().replace(" ", "")

    @classmethod
    def from_database_entry(self, dbEntry):
        return self(dbEntry["_id"], dbEntry["name"], dbEntry["status"], dbEntry["description"])