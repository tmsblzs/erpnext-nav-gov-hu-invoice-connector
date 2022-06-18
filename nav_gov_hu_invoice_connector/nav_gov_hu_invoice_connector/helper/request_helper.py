from io import StringIO

import requests

import frappe

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_signature import RequestSignature
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import CryptoType, parseString


class RequestHelper:
    _headers = {"content-type": "application/xml", "accept": "application/xml"}

    @staticmethod
    def send_request(endpoint, data_xml):
        url = RequestHelper._get_url(endpoint)
        data_xml.user.requestSignature = CryptoType("SHA3-512", RequestSignature.calculate(data_xml))
        data_str = RequestHelper._request_to_string(data_xml)
        response = requests.post(url, data=data_str, headers=RequestHelper._headers)
        return RequestHelper._parse_response(response)

    @staticmethod
    def _request_to_string(xml):
        f = StringIO()
        xml.export(f, 0, pretty_print=False)
        result_str = f.getvalue()
        f.close()
        return result_str.encode('utf-8')

    @staticmethod
    def _get_url(endpoint):
        settings = frappe.get_doc("NavGovHuSettings")
        return settings.api_url.rstrip('/') + \
               "/invoiceService/" + \
               settings.version_string + \
               "/" + endpoint

    @staticmethod
    def _parse_response(response_str):
        xml_text = response_str.text.replace('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', '')
        return parseString(str(xml_text), True, False)
