# Copyright (c) 2022, tmsblzs and Contributors
# See license.txt

# import frappe

import frappe
from frappe.tests.utils import FrappeTestCase
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.password_hash import PasswordHash


class NavGovHuUserTestCase(FrappeTestCase):
    def tearDown(self):
        frappe.db.rollback()

    def test_password_hashed(self):
        password = "ad3w3rdfac"
        login = "asdasdkk3"
        asserted_password = PasswordHash.create(password)
        self.create_nav_gov_hu_user(login, password)

        doc = self._get_nav_gov_hu_user_by_login(login)
        self.assertEqual(asserted_password, doc.password,
                         "Two password are not equal, probably has not working!"
                         "( asserted password" + asserted_password +
                         "," + doc.password + ")")

    @staticmethod
    def create_nav_gov_hu_user(login=None,
                                password=None,
                                xml_signing_signature=None,
                                is_insert=True):
        if not login:
            login = "test_login"
        if not password:
            password = "test_password"
        if not xml_signing_signature:
            xml_signing_signature = "test_signature"

        doc = frappe.get_doc({
            "doctype": "NavGovHuUser",
            "login": login,
            "password": password,
            "xml_signing_signature": xml_signing_signature
        })
        if is_insert:
            doc.insert()
        return doc

    @staticmethod
    def _get_nav_gov_hu_user_by_login(login):
        return frappe.get_doc("NavGovHuUser",
                              frappe.db.get_value("NavGovHuUser", {"login": login}))
