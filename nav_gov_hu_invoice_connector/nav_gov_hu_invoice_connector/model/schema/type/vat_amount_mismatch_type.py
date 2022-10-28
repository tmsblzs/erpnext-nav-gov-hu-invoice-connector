import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class VatAmountMismatchType(GeneratedsSuper):
    """VatAmountMismatchType -- Adóalap és felszámított adóeltérésének adatai
    Data of mismatching tax base and levied tax
    vatRate -- Adó mérték, adótartalom
    VAT rate, VAT content
    case -- Az eset leírása kóddal
    Case notation with code

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRate=None, case=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRate = vatRate
        self.validate_RateType(self.vatRate)
        self.vatRate_nsprefix_ = None
        self.case = case
        self.validate_SimpleText50NotBlankType(self.case)
        self.case_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatAmountMismatchType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatAmountMismatchType.subclass:
            return VatAmountMismatchType.subclass(*args_, **kwargs_)
        else:
            return VatAmountMismatchType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRate(self):
        return self.vatRate
    def set_vatRate(self, vatRate):
        self.vatRate = vatRate
    def get_case(self):
        return self.case
    def set_case(self, case):
        self.case = case
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
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.vatRate is not None or
            self.case is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='VatAmountMismatchType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatAmountMismatchType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatAmountMismatchType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatAmountMismatchType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatAmountMismatchType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatAmountMismatchType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='VatAmountMismatchType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRate is not None:
            namespaceprefix_ = self.vatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRate>%s</%svatRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRate, input_name='vatRate'), namespaceprefix_ , eol_))
        if self.case is not None:
            namespaceprefix_ = self.case_nsprefix_ + ':' if (UseCapturedNS_ and self.case_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scase>%s</%scase>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.case), input_name='case')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatAmountMismatchType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRate is not None:
            vatRate_ = self.vatRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRate').text = self.gds_format_decimal(vatRate_)
        if self.case is not None:
            case_ = self.case
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}case').text = self.gds_format_string(case_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatAmountMismatchType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRate is not None:
            showIndent(outfile, level)
            outfile.write('vatRate=%f,\n' % self.vatRate)
        if self.case is not None:
            showIndent(outfile, level)
            outfile.write('case=%s,\n' % self.gds_encode(quote_python(self.case)))
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
        if nodeName_ == 'vatRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRate')
            self.vatRate = fval_
            self.vatRate_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.vatRate)
        elif nodeName_ == 'case':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'case')
            value_ = self.gds_validate_string(value_, node, 'case')
            self.case = value_
            self.case_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.case)
