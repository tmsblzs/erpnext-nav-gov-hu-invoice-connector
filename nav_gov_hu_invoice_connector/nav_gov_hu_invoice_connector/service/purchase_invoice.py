import datetime

from frappe.utils import add_to_date
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.function_code_type import \
    FunctionCodeType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_direction_type import \
    InvoiceDirectionType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import NavApi


class PurchaseInvoice:
    def query(self):
        from_date = add_to_date(datetime.datetime.now(), days=-30)
        to_date = datetime.datetime.now()
        page_num = 1
        response = NavApi().query_invoice_digest(from_date, to_date, page_num, InvoiceDirectionType.INBOUND)
        if response.result.funcCode != FunctionCodeType.OK:
            return
        if response.invoiceDigestResult.availablePage == 0:
            return
        return response

