import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.purchase_invoice import PurchaseInvoice


@frappe.whitelist()
def check_invoices():
    invoice = PurchaseInvoice()
    invoice.query()
