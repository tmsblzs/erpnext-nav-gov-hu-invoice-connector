import datetime

import xmldict
from pyxb.utils import domutils

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.header.online_invoice_request_type import \
    OnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import TokenExchangeRequest, \
    parseString
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.nav_api import NavApi


class TokenManager:
    def __init__(self):
        self.exchange_token = None

    def get_token(self):
        utc_now = datetime.datetime.utcnow()
        utc_check = utc_now + datetime.timedelta(seconds=-30)
        if self.exchange_token is None or self.exchange_token.valid_to < utc_check:
            self.refresh_token()

        return self.exchange_token

    def refresh_token(self):
        request = TokenExchangeRequest()
        OnlineInvoiceRequestType.set_request_with_defaults(request)
        response = NavApi.send_request("tokenExchange", request)
        xml_text = response.text.replace('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', '')
        response_xml = parseString(str(xml_text))
        self.exchange_token = response_xml.encodedExchangeToken

