class City:
    def __init__(self, city: str):
        self.city = city

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def __str__(self):
        return f'City {self.city}'
