class Taxpayer:
    def __init__(self):
        self.short_name = None
        self.name = None
        self.tax_number = None
        self.incorporation = None
        self.address_list = None

    def to_dict(self):
        return {
            'short_name': self.short_name,
            'name': self.name,
            'tax_number': self.tax_number,
            'incorporation': self.incorporation,
            'hq_address': self._address_to_dict()
        }

    def _address_to_dict(self):
        if self.address_list[0] is None:
            return ""
        return self.address_list[0].to_str()
