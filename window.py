class Window:
    def __init__(self, window: int = 0):
        self.window = window

    def add_window(self, window):
        if window > 0:
            self.window = window

    def remove_window(self):
        if self.window:
            self.window = not self.window

    def __str__(self):
        if self.window:
            return f'There is/are {self.window} windows in this building'
        return 'There are no windows in this building'
