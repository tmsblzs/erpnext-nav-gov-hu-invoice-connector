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
            "territory": cls._get_default_territory(),
            "tax_category": cls._get_default_tax_category(),
            "default_currency": cls._get_default_currency(),
            "default_price_list": cls._get_default_price_list(),
            "payment_terms": cls._get_default_payment_terms()
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
    def _get_default_payment_terms(cls):
        settings = cls._get_nav_gov_hu_settings()
        return settings.default_customer_payment_terms

    @classmethod
    def _get_default_tax_category(cls):
        settings = cls._get_nav_gov_hu_settings()
        return settings.default_customer_tax_category

    @classmethod
    def _get_default_currency(cls):
        settings = cls._get_nav_gov_hu_settings()
        return settings.default_customer_currency

    @classmethod
    def _get_default_price_list(cls):
        settings = cls._get_nav_gov_hu_settings()
        return settings.default_customer_price_list

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

