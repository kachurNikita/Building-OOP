from tenant import Tenant


class Apartment:
    max_people = 4
    apartment_id = 0
    animals = False
    smoke = False
    apartments = []

    def __init__(self, tenant=False):
        self.tenant = tenant
        self.tenants = []
        self.base = {}
        Apartment.apartment_id += 1
        self.apartment_id = Apartment.apartment_id
        Apartment.apartments.append(self)

    def add_tenant(self, name, surname, phone):
        tenant = Tenant(name, surname, phone)
        quantity = [tenant]
        if Tenant.is_tenant(tenant.tenant_id, self.base):
            if len(quantity) == 1 and len(self.tenants) < Apartment.max_people:
                self.base[tenant.tenant_id] = {
                    'name': name,
                    'surname': surname,
                    'phone': phone,
                    'apartment_id': self.apartment_id
                }
                self.tenants.append(quantity.pop())

    def tenants_in_apartment(self,):
        return Tenant.tenants_in_apartment(self.base, self.apartment_id)

    def __str__(self):
        return f'Apartment: N:{self.apartment_id}'

    def __repr__(self):
        return f'Apartment:  {self.apartment_id}'


