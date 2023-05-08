from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.purchase_invoice import PurchaseInvoice


def import_purchase_invoices():
    invoice = PurchaseInvoice()
    return invoice.query()
