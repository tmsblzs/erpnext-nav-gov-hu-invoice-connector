import datetime

from frappe.utils import add_to_date
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper import RequestHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.query_invoice_digest_request import \
    QueryInvoiceDigestRequest
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


class QueryInvoice:
    def query(self):
        invoice_issue_date_range = DateIntervalParamType(
            add_to_date(datetime.datetime.now(), days=-30),
            datetime.datetime.now())
        mandatory_params = MandatoryQueryParamsType(invoiceIssueDate=invoice_issue_date_range)
        query_params = InvoiceQueryParamsType(mandatoryQueryParams=mandatory_params)
        request = QueryInvoiceDigestRequest(invoiceQueryParams=query_params)
        request.invoiceDirection = InvoiceDirectionType.INBOUND
        request.page = 1
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        response = RequestHelper.send_request("queryInvoiceDigest", request)
        return response

