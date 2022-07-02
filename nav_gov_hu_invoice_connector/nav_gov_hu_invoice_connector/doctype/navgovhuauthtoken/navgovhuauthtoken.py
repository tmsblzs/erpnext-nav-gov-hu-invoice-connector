# Copyright (c) 2022, tmsblzs and contributors
# For license information, please see license.txt

# import frappe
import pytz

import frappe
from frappe.model.document import Document


class NavGovHuAuthToken(Document):
	@staticmethod
	def get_token_if_exists(nav_user_login):
		doc = None
		if frappe.db.exists("NavGovHuAuthToken", nav_user_login):
			doc = frappe.get_doc("NavGovHUAuthToken", nav_user_login)
		return doc

	@staticmethod
	def save_updated_token(nav_user_login, exchange_token, valid_from, valid_to):
		valid_from = frappe.utils.get_datetime_str(valid_from)
		valid_to = frappe.utils.get_datetime_str(valid_to)
		if frappe.db.exists("NavGovHuAuthToken", nav_user_login):
			doc = frappe.get_doc("NavGovHUAuthToken", nav_user_login)
			doc.exchange_token = exchange_token
			doc.valid_from = valid_from
			doc.valid_to = valid_to
			doc.save()
		else:
			doc = frappe.get_doc({
				"doctype": "NavGovHuAuthToken",
				"name": nav_user_login,
				"nav_user_login": nav_user_login,
				"exchange_token": exchange_token,
				"valid_from": valid_from,
				"valid_to": valid_to
			})
			doc.flags.name_set = True
			doc.insert()
		return doc

