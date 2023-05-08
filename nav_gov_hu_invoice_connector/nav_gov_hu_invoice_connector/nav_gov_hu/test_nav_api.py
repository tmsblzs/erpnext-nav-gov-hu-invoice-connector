from unittest import mock
from unittest.mock import ANY

from frappe.tests.utils import FrappeTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import NavApi


class TokenExchangeReponse:
    pass


class NavApiTestCase(FrappeTestCase):
    def setUp(self):
        self.sut = NavApi()

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api.OnlineInvoiceRequestType')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api.RequestHelper')
    def test_call_set_request_with_defaults(self, mock_request_helper, mock_online_invoice_request_type):
        mock_request_helper.send_request.return_value = self._create_return_value()

        self.sut.refresh_token()

        mock_online_invoice_request_type.set_request_with_defaults.assert_called()

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api.OnlineInvoiceRequestType')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api.RequestHelper')
    def test_call_send_request(self, mock_request_helper, mock_online_invoice_request_type):
        mock_request_helper.send_request.return_value = self._create_return_value()

        self.sut.refresh_token()

        mock_request_helper.send_request.assert_called_with("tokenExchange", ANY)

    @staticmethod
    def _create_return_value():
        return TokenExchangeReponse()
