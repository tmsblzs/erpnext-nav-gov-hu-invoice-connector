import datetime

import xmldict
from pyxb.utils import domutils

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeRequest
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.nav_api import NavApi


class TokenManager:
    def __init__(self):
        self._exchange_token = None
        self._valid_from = None
        self._valid_to = None

    def get_token(self):
        utc_now = datetime.datetime.utcnow()
        utc_check = utc_now + datetime.timedelta(seconds=-30)
        if self._exchange_token is None or self._valid_to < utc_check:
            self._refresh_token()

        return self._exchange_token

    def _refresh_token(self):
        response = NavApi.refresh_token()
        self._exchange_token = response.encodedExchangeToken
        self._valid_from = response.tokenValidityFrom
        self._valid_to = response.tokenValidityTo

