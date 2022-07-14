import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.address import Address
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.address_type import AddressType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.taxpayer import Taxpayer
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.taxpayer_incorporation import TaxpayerIncorporation
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import NavApi


class QueryTaxpayer():
    def __init__(self, tax_number):
        if tax_number is None or len(tax_number) < 8:
            message = frappe._("Please specify a valid tax number (tax ID) !")
            frappe.throw(message)
        self._tax_number = tax_number

    def query(self):
        response = NavApi.query_taxpayer(self._tax_number)
        taxpayer = self._create_taxpayer_data(response)
        return taxpayer

    def _create_taxpayer_data(self, response):
        taxpayer = Taxpayer()
        taxpayer_data = response.taxpayerData
        taxpayer.short_name = taxpayer_data.taxpayerShortName
        taxpayer.name = taxpayer_data.taxpayerName
        taxpayer.incorporation = taxpayer_data.incorporation
        taxpayer.tax_number = self._create_tax_number(taxpayer_data)
        taxpayer.address = self._create_addresses(taxpayer_data)
        return taxpayer

    @staticmethod
    def _create_tax_number(taxpayer_data):
        tax_number_detail = taxpayer_data.taxNumberDetail
        return tax_number_detail.taxpayerId + \
               "-" + tax_number_detail.vatCode + \
               "-" + tax_number_detail.countyCode

    @staticmethod
    def _create_addresses(taxpayer_data):
        result = []
        address_list = taxpayer_data.taxpayerAddressList
        for address in address_list.taxpayerAddressItem:
            result.append(QueryTaxpayer._create_address(address))
        return result

    @staticmethod
    def _create_address(address_item):
        address_detail = address_item.taxpayerAddress
        address = Address()
        address.type = address_item.taxpayerAddressType
        address.country_code = address_detail.countryCode
        address.postal_code = address_detail.postalCode
        address.city = address_detail.city.capitalize()
        address.street_name = address_detail.streetName.capitalize()
        address.public_place_category = address_detail.publicPlaceCategory.lower()
        address.number = address_detail.number
        return address

    def save(self, taxpayer):
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": taxpayer.short_name,
            "customer_long_name": taxpayer.name,
            "tax_id": taxpayer.tax_number,
            "type": self._get_customer_type(taxpayer.incorporation)
        })
        customer.insert()
        if taxpayer.address is not None:
            for idx, a in enumerate(taxpayer.address):
                address = taxpayer.address[idx]
                address_name = customer.name + " (" + \
                               address.type + ") " + \
                               address.city + " " + \
                               address.street_name + " " + \
                               address.public_place_category + " " + \
                               address.number
                if not frappe.db.exists("Address", address_name):
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
                            "address_type": self._get_address_type(address.type),
                            "country": self._get_country(address.country_code),
                            "links": [{"link_doctype": "Customer", "link_name": customer.name}],
                        })
                    customer_address.flags.name_set = True
                    customer_address.insert()
        return customer

    @staticmethod
    def _check_address_is_already_exists(name):
        return frappe.db.exists("Address", name)

    @staticmethod
    def _get_customer_type(taxpayer_type):
        if taxpayer_type == TaxpayerIncorporation.ORGANIZATION:
            return "Company"
        if taxpayer_type == TaxpayerIncorporation.SELF_EMPLOYED:
            return "Self Employed"
        return "Individual"

    @staticmethod
    def _get_country(country_code):
        countries = frappe.db.get_list("Country", filters={'code': country_code}, fields={'name'})
        if countries is None or countries[0] is None:
            raise frappe._("Country code is not exists (" + country_code + ") !")
        return countries[0].name

    @staticmethod
    def _find_hq_address(address_list):
        if address_list is None or len(address_list) == 0:
            return None
        for address in address_list:
            if address.type == AddressType.HQ:
                return address
        return address_list[0]

    @staticmethod
    def _get_address_type(address_type):
        if address_type == AddressType.HQ:
            return "Billing"
        if address_type == AddressType.SITE:
            return "Warehouse"
        if address_type == AddressType.BRANCH:
            return "Subsidiary"
