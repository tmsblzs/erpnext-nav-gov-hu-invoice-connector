from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.header.basic_header_creator import BasicHeaderCreator
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.header.software_creator import SoftwareCreator
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.header.user_header_creator import UserHeaderCreator


class OnlineInvoiceRequestType:
    @staticmethod
    def set_request_with_defaults(request):
        request.user = UserHeaderCreator.create()
        request.software = SoftwareCreator.create()
        request.header = BasicHeaderCreator.create()
