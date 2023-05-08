import hashlib

import frappe


class RequestSignature:
    @staticmethod
    def calculate(data_xml):
        request_signature = data_xml.header.requestId
        request_signature += data_xml.header.timestamp.strftime("%Y%m%d%H%M%S")
        users = frappe.db.get_list("NavGovHuUser", filters={"login": data_xml.user.login},
                                   fields=['xml_signing_signature', 'login'])
        user = users[0]
        request_signature += user.xml_signing_signature
        return hashlib.sha3_512(request_signature.encode('utf-8')).hexdigest().upper()
