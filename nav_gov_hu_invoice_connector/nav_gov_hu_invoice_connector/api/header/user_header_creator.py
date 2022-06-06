import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.header.user_error import UserError
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import UserHeaderType, CryptoType


class UserHeaderCreator:
    __user = None

    @staticmethod
    def get_user():
        if not UserHeaderCreator.__user:
            user = UserHeaderCreator.__get_user_from_db()
            if not user:
                raise UserError("No nav gov hu user set!")
            UserHeaderCreator.__user = user
        return UserHeaderCreator.__user

    @staticmethod
    def __get_user_from_db():
        company = UserHeaderCreator.__get_default_company()
        doc = frappe.db.get_value("NavGovHuUser",
                                  {"user_id": frappe.session.user, "company_id": company.name})

        if not doc:
            settings = frappe.get_doc("NavGovHuSettings")
            doc = frappe.get_doc("NavGovHuUser", settings.default_user_id)
        return doc

    @staticmethod
    def __get_default_company():
        company_name = frappe.defaults.get_user_default("Company") \
                       or frappe.defaults.get_global_default("Company")
        company = frappe.get_doc("Company", company_name)
        return company

    @staticmethod
    def create():
        company = UserHeaderCreator.__get_default_company()
        user = UserHeaderCreator.get_user()

        user_header = UserHeaderType()
        user_header.login = user.login
        user_header.passwordHash = CryptoType("SHA-512", user.password)
        user_header.taxNumber = company.tax_id[:8]
        return user_header
