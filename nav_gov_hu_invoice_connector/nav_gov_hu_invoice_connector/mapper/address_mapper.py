import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.address_type import AddressType


class AddressMapper:
    @staticmethod
    def get_name(customer_name, address):
        address_type = address.type if address.type is not None else ""
        city = address.city if address.city is not None else ""
        street_name = address.street_name if address.street_name is not None else ""
        public_place_category = address.public_place_category if address.public_place_category is not None else ""
        number = address.number if address.number is not None else ""

        address_name = f'{customer_name} ({address_type}) {city} {street_name} {public_place_category} {number}'
        return address_name

    @staticmethod
    def from_address(customer_name, address):
        address_name = AddressMapper.get_name(customer_name, address)
        customer_address = frappe.get_doc(
            {
                "name": address_name,
                "address_title": address_name,
                "doctype": "Address",
                "address_line1": f'{address.street_name} {address.public_place_category} {address.number}',
                "street_name": address.street_name if address.street_name is not None else "N/A",
                "public_place_category": address.public_place_category if address.public_place_category is not None else "N/A",
                "number": address.number if address.number is not None else "N/A",
                "city": address.city if address.city is not None else "",
                "state": address.region if address.region is not None else "",
                "pincode": address.postal_code if address.postal_code is not None else "",
                "building": address.building if address.building is not None else "",
                "staircase": address.staircase if address.staircase is not None else "",
                "floor": address.floor if address.floor is not None else "",
                "door": address.door if address.door is not None else "",
                "lot_number": address.lot_number if address.lot_number is not None else "",
                "address_type": AddressMapper._get_address_type(address.type),
                "country": AddressMapper._get_country(address.country_code),
                "links": [{"link_doctype": "Customer", "link_name": customer_name}],
                "is_primary_address": True if address.type == AddressType.HQ else False,
            })
        customer_address.flags.name_set = True
        return customer_address

    @staticmethod
    def _get_country(country_code):
        countries = frappe.db.get_list("Country", filters={'code': country_code}, fields={'name'})
        if countries is None or countries[0] is None:
            raise frappe._("Country code is not exists (" + country_code + ") !")
        return countries[0].name

    @staticmethod
    def _get_address_type(address_type):
        if address_type == AddressType.HQ:
            return "Billing"
        if address_type == AddressType.SITE:
            return "Shipping"
        if address_type == AddressType.BRANCH:
            return "Subsidiary"
