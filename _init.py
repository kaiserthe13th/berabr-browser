import json

stgdct = json.load(open("settings.json"))

class Settings():
    def __init__(self):
        self.theme = stgdct["theme"]
        self.home = stgdct["home"]
        self.starting_page = stgdct["starting_page"]