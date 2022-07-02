from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper import RequestHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeRequest, \
    QueryTaxpayerRequest


class NavApi:
    @staticmethod
    def refresh_token():
        request = TokenExchangeRequest()
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        return RequestHelper.send_request("tokenExchange", request)

    @staticmethod
    def query_taxpayer(tax_number):
        request = QueryTaxpayerRequest()
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        request.taxNumber = tax_number[:8]
        response = RequestHelper.send_request("queryTaxpayer", request)
        return response
