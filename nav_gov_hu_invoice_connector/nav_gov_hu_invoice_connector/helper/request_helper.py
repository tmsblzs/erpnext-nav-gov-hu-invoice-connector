import os
from io import StringIO
from pathlib import Path

import requests

import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.file_helper import FileHelper

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.request_signature import RequestSignature
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.response_helper import parse_response
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.crypto_type import CryptoType


class RequestHelper:
    _headers = {"content-type": "application/xml", "accept": "application/xml"}

    @classmethod
    def send_request(cls, endpoint, data_xml):
        url = cls._get_url(endpoint)
        data_xml.user.requestSignature = CryptoType("SHA3-512", RequestSignature.calculate(data_xml))
        data_str = cls._request_to_string(data_xml)
        response = requests.post(url, data=data_str, headers=RequestHelper._headers)
        response_obj = parse_response(response)
        #cls._save_to_file(response, response_obj)
        return response_obj

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
    def _save_to_file(response, response_obj):
        file_name = f'response/{response_obj.__class__.__name__}-{response_obj.header.requestId}.xml'
        file = FileHelper()
        file.save_to_file(file_name, str(response.text))
