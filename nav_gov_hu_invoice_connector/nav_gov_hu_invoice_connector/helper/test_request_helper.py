import datetime
import encodings
from unittest import mock
from unittest.mock import ANY

import pytz
from requests import Response

from frappe.tests.utils import FrappeTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.doctype.navgovhusettings.navgovhusettings import \
    NavGovHuSettings
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.doctype.navgovhuuser.navgovhuuser import NavGovHuUser
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper import RequestHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_signature import RequestSignature
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeRequest, \
    CryptoType


class RequestHelperTestCase(FrappeTestCase):
    loginName = "testuser"
    passwordHash = "test_password_hash"
    taxNumber = "test_tax_number"
    requestId = "RIDRb3Oi1Gs6Wv4"
    timestampStr = "2022-06-18T13:58:46.817"
    requestSignature = "EE06C1667DD0E5CDDB7FF5D8C2D63E6D65F2E210DC79EDD0173540B9DE5B1BBC8CDE98B3B7DC70F26C17C63193C6F2D7C98238AC300D84C26D80DE7F97E35A01"
    token_exchange_request = '<TokenExchangeRequest xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common">' + \
                             '<common:header>' + \
                             '<common:requestId>' + requestId + '</common:requestId>' + \
                             '<common:timestamp>' + timestampStr + 'Z</common:timestamp>' + \
                             '<common:requestVersion>3.0</common:requestVersion>' + \
                             '<common:headerVersion>1.0</common:headerVersion>' + \
                             '</common:header>' + \
                             '<common:user>' + \
                             '<common:login>' + loginName + '</common:login>' + \
                             '<common:passwordHash cryptoType="SHA-512">' + \
                             passwordHash + \
                             '</common:passwordHash>' + \
                             '<common:taxNumber>' + taxNumber + '</common:taxNumber>' + \
                             '<common:requestSignature cryptoType="SHA3-512">' + \
                             requestSignature + \
                             '</common:requestSignature>' + \
                             '</common:user>' + \
                             '<software>' + \
                             '<softwareId>HU14701780-ERPNEXT</softwareId>' + \
                             '<softwareName>ERPNEXT-NAV-GOV-HU-INVOICE-CONNECTOR</softwareName>' + \
                             '<softwareOperation>LOCAL_SOFTWARE</softwareOperation>' + \
                             '<softwareMainVersion>1</softwareMainVersion>' + \
                             '<softwareDevName>PENSAV KFT</softwareDevName>' + \
                             '<softwareDevContact>coding@pensav.hu</softwareDevContact>' + \
                             '<softwareDevCountryCode>HU</softwareDevCountryCode>' + \
                             '<softwareDevTaxNumber>14701780-2-15</softwareDevTaxNumber>' + \
                             '</software>' + \
                             '</TokenExchangeRequest>'

    token_exchange_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + \
                              '<TokenExchangeResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" ' \
                              'xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common" ' \
                              'xmlns:ns3="http://schemas.nav.gov.hu/OSA/3.0/base" ' \
                              'xmlns:ns4="http://schemas.nav.gov.hu/OSA/3.0/data">' + \
                              '<ns2:header>' + \
                              '<ns2:requestId>' + requestId + '</ns2:requestId>' + \
                              '<ns2:timestamp>' + timestampStr + 'Z</ns2:timestamp>' + \
                              '<ns2:requestVersion>3.0</ns2:requestVersion>' + \
                              '<ns2:headerVersion>1.0</ns2:headerVersion>' + \
                              '</ns2:header>' + \
                              '<ns2:result>' + \
                              '<ns2:funcCode>OK</ns2:funcCode>' + \
                              '</ns2:result>' + \
                              '<software>' + \
                              '<softwareId>HU14701780-ERPNEXT</softwareId>' + \
                              '<softwareName>ERPNEXT-NAV-GOV-HU-INVOICE-CONNECTOR</softwareName>' + \
                              '<softwareOperation>LOCAL_SOFTWARE</softwareOperation>' + \
                              '<softwareMainVersion>3.0</softwareMainVersion>' + \
                              '<softwareDevName>PENSAV KFT</softwareDevName>' + \
                              '<softwareDevContact>coding@pensav.hu</softwareDevContact>' + \
                              '<softwareDevCountryCode>HU</softwareDevCountryCode>' + \
                              '<softwareDevTaxNumber>14701780-2-15</softwareDevTaxNumber>' + \
                              '</software>' + \
                              '<encodedExchangeToken>wQsrKdBzFq1dxYElViQaEK4O+69YFFbmsG6zLrtNSBHEzN8eCsax0H++Wqppy7lz91BCVUgVzjSz3SfTnU6oSQ==</encodedExchangeToken>' + \
                              '<tokenValidityFrom>2022-06-18T13:58:48.139Z</tokenValidityFrom>' + \
                              '<tokenValidityTo>2022-06-18T14:03:48.139Z</tokenValidityTo>' + \
                              '</TokenExchangeResponse>'

    def setUp(self):
        self.api_url = "http://test-url.hu"
        self.version_string = "v3"
        self.default_user_id = "dcasdfasdf"
        self.settings = self._create_nav_gov_hu_settings(
            self.api_url,
            self.version_string,
            self.default_user_id
        )
        # self.user = self._create_nav_gov_hu_user()

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.frappe')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.RequestSignature')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.requests')
    def test_call_requests_post_with_the_correct_url(self, mock_requests, mock_request_signature,
                                                     mock_frappe):
        endpoint = "tokenExchange"
        request = self._create_token_exchange_request()
        asserted_url = self.api_url + \
                       "/invoiceService/" + \
                       self.version_string + \
                       "/" + endpoint
        mock_frappe.get_doc.return_value = self.settings
        mock_request_signature.calculate.return_value = RequestHelperTestCase.requestSignature
        mock_requests.post.return_value = self._setup_token_exchange_response()

        RequestHelper.send_request(endpoint, request)

        mock_requests.post.assert_called_with(asserted_url, data=ANY, headers=ANY)

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.frappe')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.RequestSignature')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.requests')
    def test_call_requests_post_to_valid_xml(self, mock_requests, mock_request_signature,
                                             mock_frappe):
        endpoint = "tokenExchange"
        request = self._create_token_exchange_request()
        mock_frappe.get_doc.return_value = self.settings
        mock_request_signature.calculate.return_value = RequestHelperTestCase.requestSignature
        mock_requests.post.return_value = self._setup_token_exchange_response()

        RequestHelper.send_request(endpoint, request)

        mock_requests.post.assert_called_with(ANY,
                                              data=RequestHelperTestCase.token_exchange_request.encode('utf-8'),
                                              headers=ANY)

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.frappe')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.RequestSignature')
    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_helper.requests')
    def test_call_requests_post_to_correct_headers(self, mock_requests, mock_request_signature,
                                                   mock_frappe):
        endpoint = "tokenExchange"
        request = self._create_token_exchange_request()
        mock_frappe.get_doc.return_value = self.settings
        mock_request_signature.calculate.return_value = RequestHelperTestCase.requestSignature
        mock_requests.post.return_value = self._setup_token_exchange_response()

        RequestHelper.send_request(endpoint, request)

        mock_requests.post.assert_called_with(ANY,
                                              data=ANY,
                                              headers=RequestHelper._headers)

    @staticmethod
    def _setup_token_exchange_response():
        response = Response()
        response._content = RequestHelperTestCase \
            .token_exchange_response \
            .encode('utf-8')
        return response

    @staticmethod
    def _create_token_exchange_request():
        request = TokenExchangeRequest()
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        request.user.login = RequestHelperTestCase.loginName
        request.user.passwordHash = CryptoType("SHA-512", RequestHelperTestCase.passwordHash)
        request.user.taxNumber = RequestHelperTestCase.taxNumber
        request.user.requestSignature = CryptoType("SHA3-512", RequestHelperTestCase.requestSignature)
        request.header.requestId = RequestHelperTestCase.requestId
        request.header.timestamp = datetime.datetime \
            .fromisoformat(RequestHelperTestCase.timestampStr)
        return request

    @staticmethod
    def _create_nav_gov_hu_settings(api_url, version_string, default_user_id):
        settings = NavGovHuSettings("NavGovHuSettings")
        settings.api_url = api_url
        settings.version_string = version_string
        settings.default_user_id = default_user_id
        return settings

