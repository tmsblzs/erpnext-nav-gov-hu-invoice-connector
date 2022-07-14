class TaxNumberCreator:
    @staticmethod
    def create_from_taxpayer_data(taxpayer_data):
        tax_number_detail = taxpayer_data.taxNumberDetail
        return tax_number_detail.taxpayerId + \
               "-" + tax_number_detail.vatCode + \
               "-" + tax_number_detail.countyCode
