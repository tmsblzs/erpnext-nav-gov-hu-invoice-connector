from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import parseString


XML_HEADER = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'


def parse_response(response):
    if hasattr(response, 'text'):
        xml_text = response.text.replace(XML_HEADER, '')
    else:
        xml_text = response.replace(XML_HEADER, '')
    return parseString(str(xml_text), True, False)
