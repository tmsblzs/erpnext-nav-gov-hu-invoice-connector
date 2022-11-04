import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import query_invoice_digest


@frappe.whitelist()
def check_invoices():
    query_invoice_digest()
