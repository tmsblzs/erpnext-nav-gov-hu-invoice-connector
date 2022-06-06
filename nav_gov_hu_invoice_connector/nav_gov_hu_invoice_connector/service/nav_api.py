import hashlib
from datetime import datetime
from io import StringIO
from typing import TextIO

import requests

import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import CryptoType


class NavApi:
    @staticmethod
    def send_request(endpoint, data_xml):
        settings = frappe.get_doc("NavGovHuSettings")
        url = settings.api_url.rstrip('/') + "/invoiceService/" + settings.version_string + "/" + endpoint
        data_xml.user.requestSignature = CryptoType("SHA3-512", NavApi.calculate_request_signature(data_xml))
        headers = {"content-type": "application/xml", "accept": "application/xml"}
        f = StringIO()
        data_xml.export(f, 0, pretty_print=True)
        data_str = f.getvalue()
        f.close()
        response = requests.post(url, data=data_str.encode('utf-8'), headers=headers)
        return response

    @staticmethod
    def calculate_request_signature(data_xml):
        request_signature = data_xml.header.requestId
        request_signature += data_xml.header.timestamp.strftime("%Y%m%d%H%M%S")
        users = frappe.db.get_list("NavGovHuUser", filters={"login": data_xml.user.login},
                                   fields=['xml_signing_signature', 'login'])
        user = users[0]
        request_signature += user.xml_signing_signature
        return hashlib.sha3_512(request_signature.encode('utf-8')).hexdigest().upper()