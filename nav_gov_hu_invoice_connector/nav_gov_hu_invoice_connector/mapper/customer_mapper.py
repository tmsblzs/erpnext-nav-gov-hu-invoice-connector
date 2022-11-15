import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.taxpayer_incorporation import TaxpayerIncorporation


class CustomerMapper:
    _settings = None

    @classmethod
    def from_taxpayer(cls, taxpayer):
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": taxpayer.short_name,
            "customer_long_name": taxpayer.name,
            "tax_id": taxpayer.tax_number,
            "type": cls._get_customer_type(taxpayer.incorporation),
            "customer_group": cls._get_default_customer_group(),
            "territory": cls._get_default_territory()
        })
        return customer

    @staticmethod
    def _get_customer_type(taxpayer_type):
        if taxpayer_type == TaxpayerIncorporation.ORGANIZATION:
            return "Company"
        if taxpayer_type == TaxpayerIncorporation.SELF_EMPLOYED:
            return "Self Employed"
        return "Individual"

    @classmethod
    def _get_default_customer_group(cls):
        settings = cls._get_nav_gov_hu_settings()
        return settings.default_customer_group

    @classmethod
    def _get_default_territory(cls):
        settings = cls._get_nav_gov_hu_settings()
        return settings.default_territory

    @classmethod
    def _get_nav_gov_hu_settings(cls):
        if cls._settings is None:
            cls._settings = frappe.get_doc("NavGovHuSettings")
        return cls._settings

