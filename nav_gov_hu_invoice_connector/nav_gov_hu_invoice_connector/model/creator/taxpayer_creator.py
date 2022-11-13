from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.creator.address_creator import AddressCreator
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.creator.taxnumber_creator import TaxNumberCreator
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.taxpayer import Taxpayer


class TaxPayerCreator:
    @staticmethod
    def create_from_nav_gov_hu_response(response):
        taxpayer = Taxpayer()
        taxpayer_data = response.taxpayerData
        taxpayer.short_name = taxpayer_data.taxpayerShortName
        taxpayer.name = taxpayer_data.taxpayerName
        taxpayer.incorporation = taxpayer_data.incorporation
        taxpayer.tax_number = TaxNumberCreator.create_from_taxpayer_data(taxpayer_data)
        taxpayer.address_list = AddressCreator.create_list_from_taxpayer_data(taxpayer_data)
        return taxpayer
