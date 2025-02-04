class DataObject:
    def __init__(self, api, data):
        self._api = api
        self.id = data["_id"]
        self.type = data["_type"]
        self.version = data["_version"]

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} type={self.type} version={self.version}>"
