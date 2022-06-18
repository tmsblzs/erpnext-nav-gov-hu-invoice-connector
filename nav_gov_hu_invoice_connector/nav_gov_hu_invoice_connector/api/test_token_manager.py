import datetime
from unittest import mock

from frappe.tests.utils import FrappeTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.token_manager import TokenManager
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeResponse


class TokenManagerTestCase(FrappeTestCase):
    def setUp(self):
        self.sut = TokenManager()

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.token_manager.NavApi')
    def test_get_token_call_nav_api_token_exchange(self, mock_nav_api):
        mock_nav_api.refresh_token.return_value = self._create_token_exchange_response()

        self.sut.get_token()

        mock_nav_api.refresh_token.assert_called()

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.token_manager.NavApi')
    def test_get_token_returned_the_token_of_nav(self, mock_nav_api):
        asserted_token = "adfadfasdfasdfas"
        asserted_valid_from = datetime.datetime.utcnow()
        asserted_valid_to = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        response = self._create_token_exchange_response(
            asserted_token,
            asserted_valid_from,
            asserted_valid_to)
        mock_nav_api.refresh_token.return_value = response

        self.sut.get_token()

        self._asserted_returned_values_set_at_properties(asserted_token, asserted_valid_from, asserted_valid_to)

    def _asserted_returned_values_set_at_properties(self, asserted_token, asserted_valid_from, asserted_valid_to):
        self.assertEqual(self.sut._exchange_token, asserted_token,
                         "Two tokens are not equals "
                         "( asserted token:" + asserted_token +
                         ", token: " + self.sut._exchange_token)
        self.assertEqual(self.sut._valid_from, asserted_valid_from,
                         "Two dates are not equals "
                         "( asserted valid from:" + str(asserted_valid_from) +
                         ", valid from: " + str(self.sut._valid_from))
        self.assertEqual(self.sut._valid_to, asserted_valid_to,
                         "Two dates are not equals "
                         "( asserted valid to:" + str(asserted_valid_to) +
                         ", valid to: " + str(self.sut._valid_to))

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.token_manager.NavApi')
    def test_not_call_nav_token_exchange_if_token_is_valid(self, mock_nav_api):
        valid_from = datetime.datetime.utcnow()
        valid_to = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        self._setup_token_manager(
            valid_from=valid_from,
            valid_to=valid_to
        )
        mock_nav_api.refresh_token.return_value = self._create_token_exchange_response()

        self.sut.get_token()

        mock_nav_api.refresh_token.assert_not_called()

    def _setup_token_manager(self, token="", valid_from=None, valid_to=None):
        if token:
            self.sut._exchange_token = token
        else:
            self.sut._exchange_token = "adfasdfasdfa"
        self.sut._valid_from = valid_from
        self.sut._valid_to = valid_to

    @staticmethod
    def _create_token_exchange_response(token="", valid_from=None , valid_to=None):
        response = TokenExchangeResponse()
        response.encodedExchangeToken = token
        response.tokenValidityFrom = valid_from
        response.tokenValidityTo = valid_to
        return response
