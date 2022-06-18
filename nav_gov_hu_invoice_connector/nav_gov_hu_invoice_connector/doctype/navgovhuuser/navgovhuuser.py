# Copyright (c) 2022, tmsblzs and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.password_hash import PasswordHash


class NavGovHuUser(Document):
    def insert(self, ignore_permissions=None, ignore_links=None, ignore_if_duplicate=False,
               ignore_mandatory=None, set_name=None, set_child_names=True):
        password = self.get("password")
        password_hash = PasswordHash.create(password)
        self.set("password", password_hash)
        super(NavGovHuUser, self).insert(ignore_permissions, ignore_links, ignore_if_duplicate,
                                         ignore_mandatory, set_name, set_child_names)
