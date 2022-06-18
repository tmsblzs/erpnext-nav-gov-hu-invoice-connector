import datetime
from unittest import mock

from frappe.tests.utils import FrappeTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.doctype.navgovhuuser.test_navgovhuuser import \
    NavGovHuUserTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_signature import RequestSignature
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeRequest


class RequestSignatureTestCase(FrappeTestCase):
    user_login = "test_user"
    request_id = "TSTKFT1222564"
    timestamp_str = "2017-12-30T18:25:45.000"
    xml_signature = "ce-8f5e-215119fa7dd621DLMRHRLH2S"
    request_signature = "0493F2F0247A2DF076775631FFDFA8B6D39D051F4928D26426CD29895EEDB24960A23E4C6443A54806EA8B0E126A7B97940169FEADE6EE42FC99E3BE6F74AB04"

    def setUp(self):
        self.user = self._create_nav_gov_hu_user()

    @mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_signature.frappe')
    def test_calculate_signature(self, mock_frappe):
        request_xml = self._create_request_xml(self.user)
        mock_frappe.db.get_list.return_value = [self.user]

        result = RequestSignature.calculate(request_xml)

        self.assertEqual(result.encode('utf-8'), self.request_signature.encode('utf-8'))

    @staticmethod
    def _create_request_xml(user):
        request = TokenExchangeRequest()
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        request.user.login = user.login
        request.header.requestId = RequestSignatureTestCase.request_id
        request.header.timestamp = datetime.datetime \
            .fromisoformat(RequestSignatureTestCase.timestamp_str)
        return request

    @staticmethod
    def _create_nav_gov_hu_user():
        user = NavGovHuUserTestCase.create_nav_gov_hu_user(
            RequestSignatureTestCase.user_login,
            xml_signing_signature=RequestSignatureTestCase.xml_signature,
            is_insert=False
        )
        return user
