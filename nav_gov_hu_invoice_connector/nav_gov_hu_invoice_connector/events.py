import json

import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.token_manager import TokenManager
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.query_taxpayer import QueryTaxpayer


def on_submit(doc, event_name):
    token_manager = TokenManager()
    token = token_manager.get_token()


@frappe.whitelist()
def click_check_taxpayer(tax_number):
    query_taxpayer = QueryTaxpayer(tax_number)
    taxpayer = query_taxpayer.query_and_save_customer()
    return json.dumps(taxpayer.to_json())
