# Copyright (c) 2022, tmsblzs and contributors
# For license information, please see license.txt

# import frappe
import hashlib

from frappe.model.document import Document


class NavGovHuUser(Document):
    def insert(self, ignore_permissions=None, ignore_links=None, ignore_if_duplicate=False,
               ignore_mandatory=None, set_name=None, set_child_names=True):
        password = self.get("password")
        password_hash = hashlib.sha512(password.encode("utf-8")).hexdigest().upper()
        self.set("password", password_hash)
        super(NavGovHuUser, self).insert(ignore_permissions, ignore_links, ignore_if_duplicate,
                                         ignore_mandatory, set_name, set_child_names)
