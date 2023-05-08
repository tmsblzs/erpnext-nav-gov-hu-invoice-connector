from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager import TokenManager


def on_update(doc, event_name):
    token_manager = TokenManager()
    token = token_manager.get_token()
