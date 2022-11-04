from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.query_taxpayer_request import \
    QueryTaxpayerRequest
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.token_exchange_request import \
    TokenExchangeRequest
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper import RequestHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.query_invoice import QueryInvoice


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


def query_invoice_digest():
    invoice = QueryInvoice()
    invoice.query()

