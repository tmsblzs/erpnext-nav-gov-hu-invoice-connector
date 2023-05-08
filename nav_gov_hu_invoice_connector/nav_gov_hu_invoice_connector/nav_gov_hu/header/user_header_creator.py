import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.crypto_type import CryptoType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.user_header_type import UserHeaderType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.header.user_error import UserError
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.doctype.navgovhuuser.navgovhuuser import NavGovHuUser


class UserHeaderCreator:
    _user = None

    @staticmethod
    def get_user():
        if not UserHeaderCreator._user:
            user = NavGovHuUser.get_user()
            if not user:
                raise UserError("No nav gov hu user set!")
            UserHeaderCreator._user = user
        return UserHeaderCreator._user

    @staticmethod
    def create():
        company = NavGovHuUser.get_default_company()
        user = UserHeaderCreator.get_user()

        user_header = UserHeaderType()
        user_header.login = user.login
        user_header.passwordHash = CryptoType("SHA-512", user.password)
        user_header.taxNumber = company.tax_id[:8]
        return user_header
