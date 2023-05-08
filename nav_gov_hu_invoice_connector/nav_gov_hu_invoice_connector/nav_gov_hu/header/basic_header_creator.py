import datetime

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_header_type import \
    BasicHeaderType


class BasicHeaderCreator:
    @staticmethod
    def create():
        header = BasicHeaderType()
        header.requestId = datetime.datetime.utcnow().strftime("ERP%Y%m%d%H%M%S%f")
        header.timestamp = datetime.datetime.utcnow()
        header.requestVersion = "3.0"
        header.headerVersion = "1.0"
        return header

