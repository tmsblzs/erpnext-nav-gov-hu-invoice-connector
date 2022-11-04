from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import parseString


def parse_response(response):
    xml_text = response.text.replace('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', '')
    return parseString(str(xml_text), True, False)
