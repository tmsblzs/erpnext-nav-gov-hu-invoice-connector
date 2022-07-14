import json

import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.taxpayer_query import TaxpayerQuery


@frappe.whitelist()
def check_taxpayer(tax_number):
    query_taxpayer = TaxpayerQuery(tax_number)
    taxpayer = query_taxpayer.query()
    return json.dumps(taxpayer.to_dict())


@frappe.whitelist()
def save_taxpayer(tax_number):
    query_taxpayer = TaxpayerQuery(tax_number)
    taxpayer = query_taxpayer.query()
    customer = query_taxpayer.save(taxpayer)
    return customer.name


@frappe.whitelist()
def check_if_duplicate(tax_number, customer_name):
    query_taxpayer = TaxpayerQuery(tax_number)
    result = query_taxpayer.check_if_duplicate(customer_name)
    return result
