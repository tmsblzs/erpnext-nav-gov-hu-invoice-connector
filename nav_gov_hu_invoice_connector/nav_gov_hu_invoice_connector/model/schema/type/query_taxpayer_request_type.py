import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_request_type import \
    BasicOnlineInvoiceRequestType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class QueryTaxpayerRequestType(BasicOnlineInvoiceRequestType):
    """QueryTaxpayerRequestType -- A POST /queryTaxpayer REST operációkérés típusa
        Request type of the POST /queryTaxpayer REST operation
    taxNumber -- A lekérdezett adózó adószáma
    Tax number of the queried taxpayer

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceRequestType
    def __init__(self, header=None, user=None, software=None, taxNumber=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryTaxpayerRequestType"), self).__init__(header, user, software, extensiontype_,  **kwargs_)
        self.taxNumber = taxNumber
        self.validate_TaxpayerIdType(self.taxNumber)
        self.taxNumber_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryTaxpayerRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryTaxpayerRequestType.subclass:
            return QueryTaxpayerRequestType.subclass(*args_, **kwargs_)
        else:
            return QueryTaxpayerRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_taxNumber(self):
        return self.taxNumber
    def set_taxNumber(self, taxNumber):
        self.taxNumber = taxNumber
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_TaxpayerIdType(self, value):
        result = True
        # Validate type TaxpayerIdType, a restriction on AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TaxpayerIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TaxpayerIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TaxpayerIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TaxpayerIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TaxpayerIdType_patterns_, ))
                result = False
        return result
    validate_TaxpayerIdType_patterns_ = [['^([0-9]{8})$']]
    def _hasContent(self):
        if (
            self.taxNumber is not None or
            super(QueryTaxpayerRequestType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='QueryTaxpayerRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryTaxpayerRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryTaxpayerRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryTaxpayerRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryTaxpayerRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryTaxpayerRequestType'):
        super(QueryTaxpayerRequestType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryTaxpayerRequestType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='QueryTaxpayerRequestType', fromsubclass_=False, pretty_print=True):
        super(QueryTaxpayerRequestType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.taxNumber is not None:
            namespaceprefix_ = self.taxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.taxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxNumber>%s</%staxNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxNumber), input_name='taxNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='QueryTaxpayerRequestType', mapping_=None, nsmap_=None):
        element = super(QueryTaxpayerRequestType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.taxNumber is not None:
            taxNumber_ = self.taxNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}taxNumber').text = self.gds_format_string(taxNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryTaxpayerRequestType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryTaxpayerRequestType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryTaxpayerRequestType, self)._exportLiteralChildren(outfile, level, name_)
        if self.taxNumber is not None:
            showIndent(outfile, level)
            outfile.write('taxNumber=%s,\n' % self.gds_encode(quote_python(self.taxNumber)))
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
        super(QueryTaxpayerRequestType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'taxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxNumber')
            value_ = self.gds_validate_string(value_, node, 'taxNumber')
            self.taxNumber = value_
            self.taxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.taxNumber)
        super(QueryTaxpayerRequestType, self)._buildChildren(child_, node, nodeName_, True)
