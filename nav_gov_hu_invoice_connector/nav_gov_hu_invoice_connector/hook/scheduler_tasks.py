from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import query_invoice_digest


def every_five_minutes():
    query_invoice_digest()
