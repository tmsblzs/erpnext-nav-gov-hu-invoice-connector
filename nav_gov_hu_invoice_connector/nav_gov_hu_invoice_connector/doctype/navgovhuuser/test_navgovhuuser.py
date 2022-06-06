# Copyright (c) 2022, tmsblzs and Contributors
# See license.txt

# import frappe
import hashlib

import frappe
from frappe.tests.utils import FrappeTestCase


class TestNavGovHuUser(FrappeTestCase):
	def tearDown(self):
		frappe.db.rollback()
		frappe.clear_cache()

	def test_password_hashed(self):
		password = "ad3w3rdfac"
		login = "asdasdkk3"
		doc = frappe.get_doc({
			"doctype": "NavGovHuUser",
			"login": login,
			"password": password,
			"xml_signing_signature": "asdfasdfa323"
		}).insert()
		frappe.db.commit()
		frappe.clear_cache()

		doc = frappe.get_doc("NavGovHuUser", frappe.db.get_value("NavGovHuUser", {"login": login}))
		password_hash = hashlib.sha512(password.encode("utf-8")).hexdigest()
		self.assertEqual(password_hash, doc.password, "Two password are not equal, probably has not working!")
