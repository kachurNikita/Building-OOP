from random import randint


class Tenant:
    def __init__(self, name=None, surname=None, phone=False):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.tenant_id = randint(1, 10)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_full_name(self):
        return f'{self.name} {self.surname}'.title()

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    @staticmethod
    def tenants_in_apartment(base, apartment):
        print(f'In apartment {apartment} lives:')
        for tenant in base:
            print(base[tenant]['name'])

    @staticmethod
    def is_tenant(tenant_id, tenants):
        if tenant_id not in tenants:
            return True

    def __str__(self):
        return f'{self.name} {self.surname}'.title()

    def __repr__(self):
        return f'{self.name} {self.surname}'.title()
