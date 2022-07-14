import datetime
from unittest import mock
from unittest.mock import MagicMock

from Crypto.Cipher import AES

import frappe
from frappe.tests.utils import FrappeTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.doctype.navgovhuauthtoken.navgovhuauthtoken import \
    NavGovHuAuthToken
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import NavApi
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager import TokenManager
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeResponse


class TokenManagerTestCase(FrappeTestCase):
    def setUp(self):
        self.user_exchange_key = "123456890abcdefA"
        self.user_login = "Test User"
        self.user = self._create_nav_gov_hu_user(self.user_exchange_key, self.user_login)
        self.sut = TokenManager(self.user)

    @mock.patch.object(
        NavGovHuAuthToken,
        'get_token_if_exists',
        return_value=None)
    @mock.patch.object(
        NavGovHuAuthToken,
        'save_updated_token')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavApi')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavGovHuUser')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.DecodeHelper')
    def test_get_token_call_nav_api_token_exchange(self,
                                                   mock_decode_helper,
                                                   mock_nav_gov_hu_user,
                                                   mock_nav_api,
                                                   mock_save_updated_token,
                                                   mock_get_token_if_exists,
                                                   ):
        mock_nav_api.refresh_token.return_value = self._create_token_exchange_response()
        mock_nav_gov_hu_user.get_user.return_value = self._create_nav_gov_hu_user()
        mock_decode_helper.token.return_value = ""

        self.sut.get_token()

        mock_nav_api.refresh_token.assert_called()

    @mock.patch(
        'nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavApi'
    )
    @mock.patch.object(
        NavGovHuAuthToken,
        'get_token_if_exists',
        return_value=None)
    @mock.patch.object(
        NavGovHuAuthToken,
        'save_updated_token')
    def test_get_token_returned_the_token_of_nav(self,
                                                 mock_save_updated_token,
                                                 mock_get_token_if_exists,
                                                 mock_nav_api):
        asserted_token = "adfadfasdfasdfas"
        asserted_valid_from = datetime.datetime.utcnow()
        asserted_valid_to = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        mock_nav_api.refresh_token.return_value = self._create_token_exchange_response(
            self._get_encoded_token(asserted_token, self.user_exchange_key),
            asserted_valid_from,
            asserted_valid_to)

        self.sut.get_token()

        self._asserted_returned_values_set_at_properties(asserted_token, asserted_valid_from, asserted_valid_to)

    @staticmethod
    def _get_encoded_token(token, key):
        aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return aes.encrypt(token.encode('utf-8'))

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

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavApi')
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

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.DecodeHelper')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavGovHuAuthToken')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavApi')
    def test_get_token_from_db_if_is_any(self,
                                         mock_nav_api,
                                         mock_nav_gov_hu_auth_token,
                                         mock_decode_helper
                                         ):
        asserted_token = "adfasdfasdf"
        mock_nav_api.refresh_token.return_value = self._create_token_exchange_response()
        mock_nav_gov_hu_auth_token.get_token_if_exists.return_value = self._create_nav_gov_hu_auth_token(asserted_token)

        result = self.sut.get_token()

        self._assert_get_token_from_db(
            mock_nav_gov_hu_auth_token,
            mock_nav_api,
            result,
            asserted_token
        )

    def _assert_get_token_from_db(self, mock_nav_gov_hu_auth_token, mock_nav_api, result, asserted_token):
        mock_nav_gov_hu_auth_token.get_token_if_exists.assert_called_with(self.user_login)
        mock_nav_api.refresh_token.assert_not_called()
        self.assertEqual(result, asserted_token)

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.DecodeHelper')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavGovHuAuthToken')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.token_manager.NavApi')
    def test_save_token_to_db(self,
                              mock_nav_api,
                              mock_nav_gov_hu_auth_token,
                              mock_decode_helper
                              ):
        asserted_token = "adfadfasdfasdfas"
        asserted_valid_from = datetime.datetime.utcnow()
        asserted_valid_to = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        mock_nav_api.refresh_token.return_value = self._create_token_exchange_response(
            self._get_encoded_token(asserted_token, self.user_exchange_key),
            asserted_valid_from,
            asserted_valid_to)
        mock_nav_gov_hu_auth_token.get_token_if_exists.return_value = None
        mock_decode_helper.token.return_value = asserted_token

        self.sut.get_token()

        mock_nav_gov_hu_auth_token.save_updated_token.assert_called_with(
            self.user_login,
            asserted_token,
            asserted_valid_from,
            asserted_valid_to)

    def _setup_token_manager(self, token="", valid_from=None, valid_to=None):
        if token:
            self.sut._exchange_token = token
        else:
            self.sut._exchange_token = "adfasdfasdfa"
        self.sut._valid_from = valid_from
        self.sut._valid_to = valid_to

    @staticmethod
    def _create_nav_gov_hu_user(exchange_key="", login=""):
        nav_gov_hu_user = frappe.get_doc({
            "doctype": "NavGovHuUser",
            "login": login,
            "exchange_key": exchange_key
        })
        return nav_gov_hu_user

    @staticmethod
    def _create_nav_gov_hu_auth_token(asserted_token="", valid_from="", valid_to=""):
        if len(valid_from) == 0:
            valid_from = (datetime.datetime.utcnow() - datetime.timedelta(hours=1)).isoformat()
        if len(valid_to) == 0:
            valid_to = datetime.datetime.utcnow().isoformat()

        nav_gov_hu_user = frappe.get_doc({
            "doctype": "NavGovHuAuthToken",
            "exchange_token": asserted_token,
            "valid_from": valid_from,
            "valid_to": valid_to
        })
        return nav_gov_hu_user

    @staticmethod
    def _create_token_exchange_response(token=None, valid_from=None, valid_to=None):
        response = TokenExchangeResponse()
        response.encodedExchangeToken = token
        response.tokenValidityFrom = valid_from
        response.tokenValidityTo = valid_to
        return response
