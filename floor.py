class Floor:
    def __init__(self, floor: int):
        self.floor = floor
        assert self.floor > 0, 'Floor cant be less then 1'

    def set_floor(self, floor):
        if floor < 1:
            raise Exception('Floor cant be less then 1')
        self.floor = floor

    def get_floor(self):
        return self.floor

    def __str__(self):
        return f'Floors: {self.floor}'
