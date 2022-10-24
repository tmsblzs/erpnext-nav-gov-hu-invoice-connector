import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AdvancePaymentDataType(GeneratedsSuper):
    """AdvancePaymentDataType -- Előlegfizetéshez kapcsolódó adatok
    Advance payment related data
    advanceOriginalInvoice -- Az előlegszámlának a sorszáma, amelyben az előlegfizetés történt
    Invoice number containing the advance payment
    advancePaymentDate -- Az előleg fizetésének dátuma
    Payment date of the advance
    advanceExchangeRate -- Az előlegfizet és során alkalmazott árfolyam
    Applied exchange rate of the advance

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, advanceOriginalInvoice=None, advancePaymentDate=None, advanceExchangeRate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.advanceOriginalInvoice = advanceOriginalInvoice
        self.validate_SimpleText50NotBlankType(self.advanceOriginalInvoice)
        self.advanceOriginalInvoice_nsprefix_ = "common"
        if isinstance(advancePaymentDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(advancePaymentDate, '%Y-%m-%d').date()
        else:
            initvalue_ = advancePaymentDate
        self.advancePaymentDate = initvalue_
        self.advancePaymentDate_nsprefix_ = "base"
        self.advanceExchangeRate = advanceExchangeRate
        self.validate_ExchangeRateType(self.advanceExchangeRate)
        self.advanceExchangeRate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdvancePaymentDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdvancePaymentDataType.subclass:
            return AdvancePaymentDataType.subclass(*args_, **kwargs_)
        else:
            return AdvancePaymentDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_advanceOriginalInvoice(self):
        return self.advanceOriginalInvoice
    def set_advanceOriginalInvoice(self, advanceOriginalInvoice):
        self.advanceOriginalInvoice = advanceOriginalInvoice
    def get_advancePaymentDate(self):
        return self.advancePaymentDate
    def set_advancePaymentDate(self, advancePaymentDate):
        self.advancePaymentDate = advancePaymentDate
    def get_advanceExchangeRate(self):
        return self.advanceExchangeRate
    def set_advanceExchangeRate(self, advanceExchangeRate):
        self.advanceExchangeRate = advanceExchangeRate
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
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
    def validate_ExchangeRateType(self, value):
        result = True
        # Validate type ExchangeRateType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on ExchangeRateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on ExchangeRateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.advanceOriginalInvoice is not None or
            self.advancePaymentDate is not None or
            self.advanceExchangeRate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AdvancePaymentDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdvancePaymentDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdvancePaymentDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdvancePaymentDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdvancePaymentDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdvancePaymentDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AdvancePaymentDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.advanceOriginalInvoice is not None:
            namespaceprefix_ = self.advanceOriginalInvoice_nsprefix_ + ':' if (UseCapturedNS_ and self.advanceOriginalInvoice_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadvanceOriginalInvoice>%s</%sadvanceOriginalInvoice>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.advanceOriginalInvoice), input_name='advanceOriginalInvoice')), namespaceprefix_ , eol_))
        if self.advancePaymentDate is not None:
            namespaceprefix_ = self.advancePaymentDate_nsprefix_ + ':' if (UseCapturedNS_ and self.advancePaymentDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadvancePaymentDate>%s</%sadvancePaymentDate>%s' % (namespaceprefix_ , self.gds_format_date(self.advancePaymentDate, input_name='advancePaymentDate'), namespaceprefix_ , eol_))
        if self.advanceExchangeRate is not None:
            namespaceprefix_ = self.advanceExchangeRate_nsprefix_ + ':' if (UseCapturedNS_ and self.advanceExchangeRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadvanceExchangeRate>%s</%sadvanceExchangeRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.advanceExchangeRate, input_name='advanceExchangeRate'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AdvancePaymentDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.advanceOriginalInvoice is not None:
            advanceOriginalInvoice_ = self.advanceOriginalInvoice
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}advanceOriginalInvoice').text = self.gds_format_string(advanceOriginalInvoice_)
        if self.advancePaymentDate is not None:
            advancePaymentDate_ = self.advancePaymentDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}advancePaymentDate').text = self.gds_format_date(advancePaymentDate_)
        if self.advanceExchangeRate is not None:
            advanceExchangeRate_ = self.advanceExchangeRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}advanceExchangeRate').text = self.gds_format_decimal(advanceExchangeRate_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AdvancePaymentDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.advanceOriginalInvoice is not None:
            showIndent(outfile, level)
            outfile.write('advanceOriginalInvoice=%s,\n' % self.gds_encode(quote_python(self.advanceOriginalInvoice)))
        if self.advancePaymentDate is not None:
            showIndent(outfile, level)
            outfile.write('advancePaymentDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.advancePaymentDate, input_name='advancePaymentDate'))
        if self.advanceExchangeRate is not None:
            showIndent(outfile, level)
            outfile.write('advanceExchangeRate=%f,\n' % self.advanceExchangeRate)
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
        if nodeName_ == 'advanceOriginalInvoice':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'advanceOriginalInvoice')
            value_ = self.gds_validate_string(value_, node, 'advanceOriginalInvoice')
            self.advanceOriginalInvoice = value_
            self.advanceOriginalInvoice_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.advanceOriginalInvoice)
        elif nodeName_ == 'advancePaymentDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.advancePaymentDate = dval_
            self.advancePaymentDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.advancePaymentDate)
        elif nodeName_ == 'advanceExchangeRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'advanceExchangeRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'advanceExchangeRate')
            self.advanceExchangeRate = fval_
            self.advanceExchangeRate_nsprefix_ = child_.prefix
            # validate type ExchangeRateType
            self.validate_ExchangeRateType(self.advanceExchangeRate)
