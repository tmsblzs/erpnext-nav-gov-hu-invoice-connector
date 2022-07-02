import frappe
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.taxpayer import Taxpayer
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.nav_api import NavApi


class QueryTaxpayer():
    def __init__(self, tax_number):
        if tax_number is None or len(tax_number) < 8:
            message = frappe._("Please specify a valid tax number (tax ID) !")
            frappe.throw(message)
        self._tax_number = tax_number

    def query_and_save_customer(self):
        response = NavApi.query_taxpayer(self._tax_number)
        taxpayer = self._create_taxpayer_data(response)
        return taxpayer

    def _create_taxpayer_data(self, response):
        taxpayer = Taxpayer()
        taxpayer_data = response.taxpayerData
        taxpayer.short_name = taxpayer_data.taxpayerShortName
        taxpayer.name = taxpayer_data.taxpayerName
        taxpayer.incorporation = taxpayer_data.incorporation
        taxpayer.tax_number = self._create_tax_number(taxpayer_data)
        return taxpayer

    @staticmethod
    def _create_tax_number(taxpayer_data):
        tax_number_detail = taxpayer_data.taxNumberDetail
        return tax_number_detail.taxpayerId + \
               "-" + tax_number_detail.vatCode + \
               "-" + tax_number_detail.countyCode
