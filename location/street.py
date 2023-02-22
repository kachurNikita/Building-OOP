
class Street:
    def __init__(self, street, build):
        self.build = build
        self.street = street

    def set_street(self, street):
        self.street = street

    def get_street(self):
        return self.street

    def __str__(self):
        return f'Street {self.street}'