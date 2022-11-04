from unittest import mock
from unittest.mock import ANY

from frappe.tests.utils import FrappeTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.file_helper import FileHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.response_helper import parse_response
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_direction_type import \
    InvoiceDirectionType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.purchase_invoice import PurchaseInvoice


class PurchaseInvoiceTestCase(FrappeTestCase):
    DEFAULT_XML_PATH = "/home/frappe/frappe-bench/apps/nav_gov_hu_invoice_connector/features/drivers"

    def setUp(self):
        self.SUT = PurchaseInvoice()

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.purchase_invoice.NavApi')
    def test_no_invoice_to_import(self, mock_nav_api):
        filename = FileHelper().get_abs_path(PurchaseInvoiceTestCase.DEFAULT_XML_PATH, 'no-purchase-invoice.xml')
        with open(filename, 'r') as file:
            xml_data = file.read()
        mock_nav_api.query_invoice_digest.assert_called_once_with(ANY, ANY, 1, InvoiceDirectionType.INBOUND)
        mock_nav_api.query_invoice_digest.return_value = parse_response(xml_data)
        self.SUT.query()


