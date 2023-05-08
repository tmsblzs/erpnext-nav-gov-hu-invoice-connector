from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.query_invoice_digest_request import \
    QueryInvoiceDigestRequest
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.query_taxpayer_request import \
    QueryTaxpayerRequest
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.token_exchange_request import \
    TokenExchangeRequest
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.date_interval_param_type import \
    DateIntervalParamType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_direction_type import \
    InvoiceDirectionType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_query_params_type import \
    InvoiceQueryParamsType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.mandatory_query_params_type import \
    MandatoryQueryParamsType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper import RequestHelper


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

    @staticmethod
    def query_invoice_digest(from_date, to_date, page_num, direction_type=InvoiceDirectionType.INBOUND):
        invoice_issue_date_range = DateIntervalParamType(
            from_date,
            to_date)
        mandatory_params = MandatoryQueryParamsType(invoiceIssueDate=invoice_issue_date_range)
        query_params = InvoiceQueryParamsType(mandatoryQueryParams=mandatory_params)
        request = QueryInvoiceDigestRequest(invoiceQueryParams=query_params)
        request.invoiceDirection = direction_type
        request.page = page_num
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        response = RequestHelper.send_request("queryInvoiceDigest", request)
        return response

