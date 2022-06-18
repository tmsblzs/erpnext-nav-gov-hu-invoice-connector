from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper import RequestHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeRequest


class NavApi:
    @staticmethod
    def refresh_token():
        request = TokenExchangeRequest()
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        return RequestHelper.send_request("tokenExchange", request)
