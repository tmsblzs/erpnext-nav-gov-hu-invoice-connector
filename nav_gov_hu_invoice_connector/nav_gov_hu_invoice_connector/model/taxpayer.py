class Taxpayer:
    def __init__(self):
        self.short_name = None
        self.name = None
        self.tax_number = None
        self.incorporation = None
        self.address = None

    def to_dict(self):
        return {
            'short_name': self.short_name,
            'name': self.name,
            'tax_number': self.tax_number,
            'incorporation': self.incorporation,
            'hq_address': self._address_to_dict()
        }

    def _address_to_dict(self):
        if self.address[0] is None:
            return ""
        return self.address[0].postal_code + " " + \
               self.address[0].city + " " + \
               self.address[0].street_name + " " + \
               self.address[0].public_place_category + " " + \
               self.address[0].number
