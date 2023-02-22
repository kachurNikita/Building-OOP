

class Owner:
    def __init__(self):
        self.owner = None

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def __str__(self):
        return f'Owner : {self.owner}'



