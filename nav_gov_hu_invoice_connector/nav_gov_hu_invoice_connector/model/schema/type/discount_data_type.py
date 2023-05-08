import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class DiscountDataType(GeneratedsSuper):
    """DiscountDataType -- Árengedmény adatok
    Discount data
    discountDescription -- Az árengedmény leírása
    Description of the discount
    discountValue -- Tételhez tartozó árengedmény összege a számla pénznemében, ha az egységár nem tartalmazza
    Total amount of discount per item expressed in the currency of the invoice if not included in the unit price
    discountRate -- Tételhez tartozó árengedmény aránya, ha az egységár nem tartalmazza
    Rate of discount per item expressed in the currency of the invoice if not included in the unit price

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, discountDescription=None, discountValue=None, discountRate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.discountDescription = discountDescription
        self.validate_SimpleText255NotBlankType(self.discountDescription)
        self.discountDescription_nsprefix_ = "common"
        self.discountValue = discountValue
        self.validate_MonetaryType(self.discountValue)
        self.discountValue_nsprefix_ = "base"
        self.discountRate = discountRate
        self.validate_RateType(self.discountRate)
        self.discountRate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DiscountDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DiscountDataType.subclass:
            return DiscountDataType.subclass(*args_, **kwargs_)
        else:
            return DiscountDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_discountDescription(self):
        return self.discountDescription
    def set_discountDescription(self, discountDescription):
        self.discountDescription = discountDescription
    def get_discountValue(self):
        return self.discountValue
    def set_discountValue(self, discountValue):
        self.discountValue = discountValue
    def get_discountRate(self):
        return self.discountRate
    def set_discountRate(self, discountRate):
        self.discountRate = discountRate
    def validate_SimpleText255NotBlankType(self, value):
        result = True
        # Validate type SimpleText255NotBlankType, a restriction on AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText255NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText255NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText255NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText255NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText255NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_RateType(self, value):
        result = True
        # Validate type RateType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.discountDescription is not None or
            self.discountValue is not None or
            self.discountRate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DiscountDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DiscountDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DiscountDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DiscountDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DiscountDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DiscountDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DiscountDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.discountDescription is not None:
            namespaceprefix_ = self.discountDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.discountDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscountDescription>%s</%sdiscountDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.discountDescription), input_name='discountDescription')), namespaceprefix_ , eol_))
        if self.discountValue is not None:
            namespaceprefix_ = self.discountValue_nsprefix_ + ':' if (UseCapturedNS_ and self.discountValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscountValue>%s</%sdiscountValue>%s' % (namespaceprefix_ , self.gds_format_decimal(self.discountValue, input_name='discountValue'), namespaceprefix_ , eol_))
        if self.discountRate is not None:
            namespaceprefix_ = self.discountRate_nsprefix_ + ':' if (UseCapturedNS_ and self.discountRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscountRate>%s</%sdiscountRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.discountRate, input_name='discountRate'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='DiscountDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.discountDescription is not None:
            discountDescription_ = self.discountDescription
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}discountDescription').text = self.gds_format_string(discountDescription_)
        if self.discountValue is not None:
            discountValue_ = self.discountValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}discountValue').text = self.gds_format_decimal(discountValue_)
        if self.discountRate is not None:
            discountRate_ = self.discountRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}discountRate').text = self.gds_format_decimal(discountRate_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DiscountDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.discountDescription is not None:
            showIndent(outfile, level)
            outfile.write('discountDescription=%s,\n' % self.gds_encode(quote_python(self.discountDescription)))
        if self.discountValue is not None:
            showIndent(outfile, level)
            outfile.write('discountValue=%f,\n' % self.discountValue)
        if self.discountRate is not None:
            showIndent(outfile, level)
            outfile.write('discountRate=%f,\n' % self.discountRate)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'discountDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'discountDescription')
            value_ = self.gds_validate_string(value_, node, 'discountDescription')
            self.discountDescription = value_
            self.discountDescription_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.discountDescription)
        elif nodeName_ == 'discountValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'discountValue')
            fval_ = self.gds_validate_decimal(fval_, node, 'discountValue')
            self.discountValue = fval_
            self.discountValue_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.discountValue)
        elif nodeName_ == 'discountRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'discountRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'discountRate')
            self.discountRate = fval_
            self.discountRate_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.discountRate)
