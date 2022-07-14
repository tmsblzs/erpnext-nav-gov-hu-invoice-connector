import datetime

import frappe.utils
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.doctype.navgovhuauthtoken.navgovhuauthtoken import \
    NavGovHuAuthToken
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.doctype.navgovhuuser.navgovhuuser import NavGovHuUser
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.decode_helper import DecodeHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api import NavApi


class TokenManager:
    def __init__(self, user=None):
        self._user = user
        self._exchange_token = None
        self._valid_from = None
        self._valid_to = None

    def get_token(self):
        utc_now = datetime.datetime.utcnow()
        utc_check = utc_now + datetime.timedelta(seconds=-30)
        if self._exchange_token is None:
            self._check_token_in_db()

        if self._exchange_token is None \
                or (self._valid_to is not None
                    and self._valid_to < utc_check):
            self._refresh_token()

        return self._exchange_token

    def _get_user(self):
        if self._user is None:
            self._user = NavGovHuUser.get_user()
        return self._user

    def _check_token_in_db(self):
        user = self._get_user()
        doc = NavGovHuAuthToken.get_token_if_exists(user.login)
        if doc is None:
            return
        self._valid_from = frappe.utils.get_datetime(doc.valid_from)
        self._valid_to = frappe.utils.get_datetime(doc.valid_to)
        self._exchange_token = doc.exchange_token

    def _refresh_token(self):
        response = NavApi.refresh_token()
        user = self._get_user()
        exchange_token = DecodeHelper.token(response.encodedExchangeToken, user.exchange_key)
        NavGovHuAuthToken.save_updated_token(user.login, exchange_token, response.tokenValidityFrom,
                                             response.tokenValidityTo)
        self._exchange_token = exchange_token
        self._valid_from = response.tokenValidityFrom
        self._valid_to = response.tokenValidityTo


