import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.mapper.address_mapper import AddressMapper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.mapper.customer_mapper import CustomerMapper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.address_type import AddressType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.creator.taxpayer_creator import TaxPayerCreator
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import NavApi


class TaxpayerQuery:
    def __init__(self, tax_number):
        if tax_number is None or len(tax_number) < 8:
            message = frappe._("Please specify a valid tax number (tax ID) !")
            frappe.throw(message)
        self._tax_number = tax_number

    def query(self):
        response = NavApi.query_taxpayer(self._tax_number)
        taxpayer = TaxPayerCreator.create_from_nav_gov_hu_response(response)
        return taxpayer

    def save(self, taxpayer):
        mapper = CustomerMapper()
        customer = mapper.from_taxpayer(taxpayer)
        customer.insert()
        if taxpayer.address_list is not None:
            for address in taxpayer.address_list:
                address_name = AddressMapper.get_name(customer.name, address)
                if not self._check_address_is_already_exists(address_name):
                    customer_address = AddressMapper.from_address(customer.name, address)
                    customer_address.insert()
        return customer

    def check_if_duplicate(self, customer_name):
        if frappe.db.exists("Customer", customer_name):
            return frappe._("Customer already exists with name") + " : '" + customer_name + "'"
        addresses = frappe.db.get("Customer", filters={"tax_id": self._tax_number})
        if len(addresses) > 0:
            return frappe._("Customer already exists with tax number") + " : '" + self._tax_number + "'"
        return False

    @staticmethod
    def _check_address_is_already_exists(name):
        return frappe.db.exists("Address", name)

    @staticmethod
    def _find_hq_address(address_list):
        if address_list is None or len(address_list) == 0:
            return None
        for address in address_list:
            if address.type == AddressType.HQ:
                return address
        return address_list[0]

