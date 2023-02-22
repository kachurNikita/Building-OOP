
class Manager:
    def __init__(self, manager=False):
        self.manager = manager

    def set_manager(self):
        self.manager = True

    def remove_manager(self):
        self.manager = False

    def social_event(self):
        print('Social event created...')

    def __str__(self):
        return 'Manager'

