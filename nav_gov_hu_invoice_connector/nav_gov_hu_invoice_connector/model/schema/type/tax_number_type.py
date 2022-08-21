from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, Validate_simpletypes_, encode_str_2_3, quote_xml, \
    quote_python, GenerateDSNamespaceTypePrefixes_, find_attr_value_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_

class TaxNumberType(GeneratedsSuper):
    """TaxNumberType -- Adószám típus
    Tax number type
    taxpayerId -- Az adóalany adótörzsszáma. Csoportos adóalany esetén csoport azonosítószám
            Core tax number of the taxable person. In case of group taxation arrangement the group identification number
    vatCode -- ÁFA kód az adóalanyiság típusának jelzésére. Egy számjegy
            VAT code to indicate taxation type of the taxpayer. One digit
    countyCode -- Megyekód, két számjegy
            County code, two digits

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, taxpayerId=None, vatCode=None, countyCode=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.taxpayerId = taxpayerId
        self.validate_TaxpayerIdType(self.taxpayerId)
        self.taxpayerId_nsprefix_ = "common"
        self.vatCode = vatCode
        self.validate_VatCodeType(self.vatCode)
        self.vatCode_nsprefix_ = "common"
        self.countyCode = countyCode
        self.validate_CountyCodeType(self.countyCode)
        self.countyCode_nsprefix_ = "common"
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TaxNumberType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TaxNumberType.subclass:
            return TaxNumberType.subclass(*args_, **kwargs_)
        else:
            return TaxNumberType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_taxpayerId(self):
        return self.taxpayerId
    def set_taxpayerId(self, taxpayerId):
        self.taxpayerId = taxpayerId
    def get_vatCode(self):
        return self.vatCode
    def set_vatCode(self, vatCode):
        self.vatCode = vatCode
    def get_countyCode(self):
        return self.countyCode
    def set_countyCode(self, countyCode):
        self.countyCode = countyCode
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
    def validate_VatCodeType(self, value):
        result = True
        # Validate type VatCodeType, a restriction on AtomicStringType2.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on VatCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on VatCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on VatCodeType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_VatCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_VatCodeType_patterns_, ))
                result = False
        return result
    validate_VatCodeType_patterns_ = [['^([1-5]{1})$']]
    def validate_CountyCodeType(self, value):
        result = True
        # Validate type CountyCodeType, a restriction on AtomicStringType2.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on CountyCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CountyCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CountyCodeType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CountyCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CountyCodeType_patterns_, ))
                result = False
        return result
    validate_CountyCodeType_patterns_ = [['^([0-9]{2})$']]
    def _hasContent(self):
        if (
            self.taxpayerId is not None or
            self.vatCode is not None or
            self.countyCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='TaxNumberType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TaxNumberType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TaxNumberType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TaxNumberType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TaxNumberType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TaxNumberType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='TaxNumberType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.taxpayerId is not None:
            namespaceprefix_ = self.taxpayerId_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxpayerId>%s</%staxpayerId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxpayerId), input_name='taxpayerId')), namespaceprefix_ , eol_))
        if self.vatCode is not None:
            namespaceprefix_ = self.vatCode_nsprefix_ + ':' if (UseCapturedNS_ and self.vatCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatCode>%s</%svatCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.vatCode), input_name='vatCode')), namespaceprefix_ , eol_))
        if self.countyCode is not None:
            namespaceprefix_ = self.countyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.countyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountyCode>%s</%scountyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.countyCode), input_name='countyCode')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TaxNumberType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/base}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/base}' + name_, nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.taxpayerId is not None:
            taxpayerId_ = self.taxpayerId
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}taxpayerId').text = self.gds_format_string(taxpayerId_)
        if self.vatCode is not None:
            vatCode_ = self.vatCode
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}vatCode').text = self.gds_format_string(vatCode_)
        if self.countyCode is not None:
            countyCode_ = self.countyCode
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}countyCode').text = self.gds_format_string(countyCode_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TaxNumberType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.taxpayerId is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerId=%s,\n' % self.gds_encode(quote_python(self.taxpayerId)))
        if self.vatCode is not None:
            showIndent(outfile, level)
            outfile.write('vatCode=%s,\n' % self.gds_encode(quote_python(self.vatCode)))
        if self.countyCode is not None:
            showIndent(outfile, level)
            outfile.write('countyCode=%s,\n' % self.gds_encode(quote_python(self.countyCode)))
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
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'taxpayerId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxpayerId')
            value_ = self.gds_validate_string(value_, node, 'taxpayerId')
            self.taxpayerId = value_
            self.taxpayerId_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.taxpayerId)
        elif nodeName_ == 'vatCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'vatCode')
            value_ = self.gds_validate_string(value_, node, 'vatCode')
            self.vatCode = value_
            self.vatCode_nsprefix_ = child_.prefix
            # validate type VatCodeType
            self.validate_VatCodeType(self.vatCode)
        elif nodeName_ == 'countyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countyCode')
            value_ = self.gds_validate_string(value_, node, 'countyCode')
            self.countyCode = value_
            self.countyCode_nsprefix_ = child_.prefix
            # validate type CountyCodeType
            self.validate_CountyCodeType(self.countyCode)
