from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import SoftwareType


class SoftwareCreator:
    @staticmethod
    def create():
        software_type = SoftwareType()
        software_type.softwareId = "HU14701780-ERPNEXT"
        software_type.softwareOperation = "LOCAL_SOFTWARE"
        software_type.softwareName = "ERPNEXT-NAV-GOV-HU-INVOICE-CONNECTOR"
        software_type.softwareMainVersion = "1"
        software_type.softwareDevName = "PENSAV KFT"
        software_type.softwareDevContact = "coding@pensav.hu"
        software_type.softwareDevCountryCode = "HU"
        software_type.softwareDevTaxNumber = "17401780-2-15"
        return software_type
