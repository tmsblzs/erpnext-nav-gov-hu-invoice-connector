import base64
import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_, raise_parse_error
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_response_type import \
    BasicOnlineInvoiceResponseType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class TokenExchangeResponseType(BasicOnlineInvoiceResponseType):
    """TokenExchangeResponseType -- A POST /tokenExchange REST operáció válasz típusa
    Response type of the POST /tokenExchange REST operation
    encodedExchangeToken -- A kiadott exchange token AES-128 ECB algoritmussal kódolt alakja
    The issued exchange token in AES-128 ECB encoded form
    tokenValidityFrom -- A kiadott token érvényességének kezdete
    Validity start of the issued exchange token
    tokenValidityTo -- A kiadott token érvényességének vége
    Validity end of the issued exchange token

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceResponseType
    def __init__(self, header=None, result=None, software=None, encodedExchangeToken=None, tokenValidityFrom=None, tokenValidityTo=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("TokenExchangeResponseType"), self).__init__(header, result, software, extensiontype_,  **kwargs_)
        self.encodedExchangeToken = encodedExchangeToken
        self.encodedExchangeToken_nsprefix_ = "xs"
        if isinstance(tokenValidityFrom, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(tokenValidityFrom, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = tokenValidityFrom
        self.tokenValidityFrom = initvalue_
        self.tokenValidityFrom_nsprefix_ = "base"
        if isinstance(tokenValidityTo, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(tokenValidityTo, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = tokenValidityTo
        self.tokenValidityTo = initvalue_
        self.tokenValidityTo_nsprefix_ = "base"
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TokenExchangeResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TokenExchangeResponseType.subclass:
            return TokenExchangeResponseType.subclass(*args_, **kwargs_)
        else:
            return TokenExchangeResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_encodedExchangeToken(self):
        return self.encodedExchangeToken
    def set_encodedExchangeToken(self, encodedExchangeToken):
        self.encodedExchangeToken = encodedExchangeToken
    def get_tokenValidityFrom(self):
        return self.tokenValidityFrom
    def set_tokenValidityFrom(self, tokenValidityFrom):
        self.tokenValidityFrom = tokenValidityFrom
    def get_tokenValidityTo(self):
        return self.tokenValidityTo
    def set_tokenValidityTo(self, tokenValidityTo):
        self.tokenValidityTo = tokenValidityTo
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.fromisoformat('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {"value": value, "lineno": lineno} )
                result = False
            if not isinstance(value, datetime_.datetime):
                result = False
            else:
                iso_format = value.isoformat()[:-9]+"Z"
                if not self.gds_validate_simple_patterns(
                       self.validate_InvoiceTimestampType_patterns_, iso_format):
                    self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (iso_format, self.validate_InvoiceTimestampType_patterns_, ))
                    result = False
        return result
    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]
    def _hasContent(self):
        if (
            self.encodedExchangeToken is not None or
            self.tokenValidityFrom is not None or
            self.tokenValidityTo is not None or
            super(TokenExchangeResponseType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='TokenExchangeResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TokenExchangeResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TokenExchangeResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TokenExchangeResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TokenExchangeResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TokenExchangeResponseType'):
        super(TokenExchangeResponseType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TokenExchangeResponseType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='TokenExchangeResponseType', fromsubclass_=False, pretty_print=True):
        super(TokenExchangeResponseType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.encodedExchangeToken is not None:
            namespaceprefix_ = self.encodedExchangeToken_nsprefix_ + ':' if (UseCapturedNS_ and self.encodedExchangeToken_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sencodedExchangeToken>%s</%sencodedExchangeToken>%s' % (namespaceprefix_ , self.gds_format_base64(self.encodedExchangeToken, input_name='encodedExchangeToken'), namespaceprefix_ , eol_))
        if self.tokenValidityFrom is not None:
            namespaceprefix_ = self.tokenValidityFrom_nsprefix_ + ':' if (UseCapturedNS_ and self.tokenValidityFrom_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stokenValidityFrom>%s</%stokenValidityFrom>%s' % (namespaceprefix_ , self.gds_format_datetime(self.tokenValidityFrom, input_name='tokenValidityFrom'), namespaceprefix_ , eol_))
        if self.tokenValidityTo is not None:
            namespaceprefix_ = self.tokenValidityTo_nsprefix_ + ':' if (UseCapturedNS_ and self.tokenValidityTo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stokenValidityTo>%s</%stokenValidityTo>%s' % (namespaceprefix_ , self.gds_format_datetime(self.tokenValidityTo, input_name='tokenValidityTo'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TokenExchangeResponseType', mapping_=None, nsmap_=None):
        element = super(TokenExchangeResponseType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.encodedExchangeToken is not None:
            encodedExchangeToken_ = self.encodedExchangeToken
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}encodedExchangeToken').text = self.gds_format_base64(encodedExchangeToken_)
        if self.tokenValidityFrom is not None:
            tokenValidityFrom_ = self.tokenValidityFrom
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}tokenValidityFrom').text = self.gds_format_datetime(tokenValidityFrom_)
        if self.tokenValidityTo is not None:
            tokenValidityTo_ = self.tokenValidityTo
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}tokenValidityTo').text = self.gds_format_datetime(tokenValidityTo_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TokenExchangeResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(TokenExchangeResponseType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(TokenExchangeResponseType, self)._exportLiteralChildren(outfile, level, name_)
        if self.encodedExchangeToken is not None:
            showIndent(outfile, level)
            outfile.write('encodedExchangeToken=model_.base64Binary(\n')
            self.encodedExchangeToken.exportLiteral(outfile, level, name_='encodedExchangeToken')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.tokenValidityFrom is not None:
            showIndent(outfile, level)
            outfile.write('tokenValidityFrom=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.tokenValidityFrom, input_name='tokenValidityFrom'))
        if self.tokenValidityTo is not None:
            showIndent(outfile, level)
            outfile.write('tokenValidityTo=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.tokenValidityTo, input_name='tokenValidityTo'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
        super(TokenExchangeResponseType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'encodedExchangeToken':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'encodedExchangeToken')
            else:
                bval_ = None
            self.encodedExchangeToken = bval_
            self.encodedExchangeToken_nsprefix_ = child_.prefix
        elif nodeName_ == 'tokenValidityFrom':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.tokenValidityFrom = dval_
            self.tokenValidityFrom_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.tokenValidityFrom)
        elif nodeName_ == 'tokenValidityTo':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.tokenValidityTo = dval_
            self.tokenValidityTo_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.tokenValidityTo)
        super(TokenExchangeResponseType, self)._buildChildren(child_, node, nodeName_, True)
