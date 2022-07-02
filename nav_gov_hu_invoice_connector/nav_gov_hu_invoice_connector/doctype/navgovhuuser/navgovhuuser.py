# Copyright (c) 2022, tmsblzs and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.password_hash import PasswordHash


class NavGovHuUser(Document):
    def insert(self, ignore_permissions=None, ignore_links=None, ignore_if_duplicate=False,
               ignore_mandatory=None, set_name=None, set_child_names=True):
        password = self.get("password")
        password_hash = PasswordHash.create(password)
        self.set("password", password_hash)
        login = self.get("login")
        self.set("name", login)
        self.flags.name_set = True
        super(NavGovHuUser, self).insert(ignore_permissions, ignore_links, ignore_if_duplicate,
                                         ignore_mandatory, set_name, set_child_names)

    @staticmethod
    def get_user():
        company = NavGovHuUser.get_default_company()
        doc = frappe.db.get_value("NavGovHuUser",
                                  {"user_id": frappe.session.user, "company_id": company.name})

        if not doc:
            settings = frappe.get_doc("NavGovHuSettings")
            doc = frappe.get_doc("NavGovHuUser", settings.default_user_id)
        return doc

    @staticmethod
    def get_default_company():
        company_name = frappe.defaults.get_user_default("Company") \
                       or frappe.defaults.get_global_default("Company")
        company = frappe.get_doc("Company", company_name)
        return company

