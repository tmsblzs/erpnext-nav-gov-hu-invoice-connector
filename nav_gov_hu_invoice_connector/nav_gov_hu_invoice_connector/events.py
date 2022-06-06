from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.token_manager import TokenManager


def on_submit(doc, event_name):
    token_manager = TokenManager()
    token = token_manager.get_token()
