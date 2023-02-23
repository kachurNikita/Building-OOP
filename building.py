from floor import Floor
from elevator import Elevator
from window import Window
from owner import Owner
from architector import Architector
from location.street import Street
from location.city import City
from manager import Manager
from apartment import Apartment


# Building
class Building:

    def __init__(self, created: int, floor: Floor, build_type: str, city: City, street: Street):
        self._created = created
        self.build_type = build_type
        self.floor = floor
        self.elevator = None
        self.window = None
        self.owner = None
        self.architector = None
        self.city = city
        self.street = street
        self.manager = None
        self.apartment = None
        self.apartments = []

    def set_apartments(self):
        if Apartment.apartments:
            self.apartments = Apartment.apartments

    def get_apartments(self):
        return self.apartments

    def __repr__(self):
        return f'{self.build_type} building'


my_building = Building(2023, Floor(1), 'ordinary', City('New-York'), Street('Pa-venue', 13))
# my_building.elevator = Elevator()
# my_building.window = Window()
# my_building.window.add_window(5)
# my_building.owner = Owner()
# my_building.owner.set_owner('Kachur Nikita')
# my_building.architector = Architector()
# my_building.architector.set_architector('Architector')
apartment_1 = my_building.apartment = Apartment()
my_building.apartment.add_tenant('Biden', 'k', 111)
my_building.apartment.add_tenant('Biden', 'k', 111)
my_building.apartment.add_tenant('Biden', 'k', 111)
my_building.apartment.add_tenant('Biden', 'k', 111)
print(apartment_1.tenants_in_apartment())
apartment_2 = my_building.apartment = Apartment()
my_building.apartment.add_tenant('Tramp', 's', 222)
my_building.apartment.add_tenant('Tramp', 's', 222)
my_building.apartment.add_tenant('Tramp', 's', 222)
my_building.apartment.add_tenant('Tramp', 's', 222)
print(apartment_2.tenants_in_apartment())
print(my_building.set_apartments())
print(my_building.get_apartments())




