
class Architector:
    def __init__(self, architector: str = None):
        self.architector = architector

    def set_architector(self, architector):
        self.architector = architector

    def get_architector(self):
        return self.architector

    def __str__(self):
        return f'Architector {self.architector}'
