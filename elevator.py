
class Elevator:
    def __init__(self):
        self.elevator = False

    def set_elevator(self):
        self.elevator = True

    def remove_elevator(self):
        self.elevator = False

    def __str__(self):
        if self.elevator:
            return 'Elevator exist'
        return 'Elevator doesnt exist'

