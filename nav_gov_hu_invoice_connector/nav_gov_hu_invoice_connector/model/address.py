class Address:
    def __init__(self):
        self.country_code = None
        self.region = None
        self.postal_code = None
        self.city = None
        self.street_name = None
        self.public_place_category = None
        self.number = None
        self.building = None
        self.staircase = None
        self.floor = None
        self.door = None
        self.lot_number = None
        self.type = None

    def to_str(self):
        return self.postal_code if self.postal_code else "" + " " + \
               self.city + " " if self.city else "" + \
               self.street_name + " " if self.street_name else "" + \
               self.public_place_category if self.public_place_category else "" + " " + \
               self.number if self.number else ""
