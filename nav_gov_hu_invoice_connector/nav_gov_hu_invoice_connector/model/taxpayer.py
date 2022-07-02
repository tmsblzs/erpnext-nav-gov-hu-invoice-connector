class Taxpayer:
    short_name = None
    name = None
    tax_number = None
    incorporation = None

    def to_json(self):
        return {
            'short_name': self.short_name,
            'name': self.name,
            'tax_number': self.tax_number,
            'incorporation': self.incorporation
        }