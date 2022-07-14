import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.taxpayer_incorporation import TaxpayerIncorporation


class CustomerMapper:
    def from_taxpayer(self, taxpayer):
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": taxpayer.short_name,
            "customer_long_name": taxpayer.name,
            "tax_id": taxpayer.tax_number,
            "type": self._get_customer_type(taxpayer.incorporation)
        })
        return customer

    @staticmethod
    def _get_customer_type(taxpayer_type):
        if taxpayer_type == TaxpayerIncorporation.ORGANIZATION:
            return "Company"
        if taxpayer_type == TaxpayerIncorporation.SELF_EMPLOYED:
            return "Self Employed"
        return "Individual"
