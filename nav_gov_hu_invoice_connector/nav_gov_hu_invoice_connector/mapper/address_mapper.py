import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.address_type import AddressType


class AddressMapper:
    @staticmethod
    def get_name(customer_name, address):
        address_name = customer_name + " (" + \
                       address.type + ") " + \
                       address.city + " " + \
                       address.street_name + " " + \
                       address.public_place_category + " " + \
                       address.number
        return address_name

    @staticmethod
    def from_address(customer_name, address):
        address_name = AddressMapper.get_name(customer_name, address)
        customer_address = frappe.get_doc(
            {
                "name": address_name,
                "address_title": address_name,
                "doctype": "Address",
                "street_name": address.street_name,
                "public_place_category": address.public_place_category,
                "number": address.number,
                "city": address.city,
                "state": address.region,
                "pincode": address.postal_code,
                "building": address.building,
                "staircase": address.staircase,
                "floor": address.floor,
                "door": address.door,
                "lot_number": address.lot_number,
                "address_type": AddressMapper._get_address_type(address.type),
                "country": AddressMapper._get_country(address.country_code),
                "links": [{"link_doctype": "Customer", "link_name": customer_name}],
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
            return "Warehouse"
        if address_type == AddressType.BRANCH:
            return "Subsidiary"
