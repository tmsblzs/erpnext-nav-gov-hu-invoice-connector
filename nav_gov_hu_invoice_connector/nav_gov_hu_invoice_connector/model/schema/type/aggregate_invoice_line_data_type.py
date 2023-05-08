import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AggregateInvoiceLineDataType(GeneratedsSuper):
    """AggregateInvoiceLineDataType -- A gyűjtő számlára vonatkozó speciális adatokat tartalmazó típus
    Field type including aggregate invoice special data
    lineExchangeRate -- A tételhez tartozó árfolyam, 1 (egy) egységre vonatkoztatva.
            Csak külföldi pénznemben kiállított gyűjtő számla esetén kitöltendő
    The exchange rate applied to the item, pertaining to 1 (one) unit. This should be filled in only if an aggregate invoice in foreign currency is issued
    lineDeliveryDate -- Gyűjtő számla esetén az adott tétel teljesítési dátuma
    Delivery date of the given item in the case of an aggregate invoice

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineExchangeRate=None, lineDeliveryDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineExchangeRate = lineExchangeRate
        self.validate_ExchangeRateType(self.lineExchangeRate)
        self.lineExchangeRate_nsprefix_ = None
        if isinstance(lineDeliveryDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(lineDeliveryDate, '%Y-%m-%d').date()
        else:
            initvalue_ = lineDeliveryDate
        self.lineDeliveryDate = initvalue_
        self.lineDeliveryDate_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AggregateInvoiceLineDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AggregateInvoiceLineDataType.subclass:
            return AggregateInvoiceLineDataType.subclass(*args_, **kwargs_)
        else:
            return AggregateInvoiceLineDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineExchangeRate(self):
        return self.lineExchangeRate
    def set_lineExchangeRate(self, lineExchangeRate):
        self.lineExchangeRate = lineExchangeRate
    def get_lineDeliveryDate(self):
        return self.lineDeliveryDate
    def set_lineDeliveryDate(self, lineDeliveryDate):
        self.lineDeliveryDate = lineDeliveryDate
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
    def _hasContent(self):
        if (
            self.lineExchangeRate is not None or
            self.lineDeliveryDate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='AggregateInvoiceLineDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AggregateInvoiceLineDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AggregateInvoiceLineDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AggregateInvoiceLineDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AggregateInvoiceLineDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AggregateInvoiceLineDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='AggregateInvoiceLineDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineExchangeRate is not None:
            namespaceprefix_ = self.lineExchangeRate_nsprefix_ + ':' if (UseCapturedNS_ and self.lineExchangeRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineExchangeRate>%s</%slineExchangeRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineExchangeRate, input_name='lineExchangeRate'), namespaceprefix_ , eol_))
        if self.lineDeliveryDate is not None:
            namespaceprefix_ = self.lineDeliveryDate_nsprefix_ + ':' if (UseCapturedNS_ and self.lineDeliveryDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineDeliveryDate>%s</%slineDeliveryDate>%s' % (namespaceprefix_ , self.gds_format_date(self.lineDeliveryDate, input_name='lineDeliveryDate'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AggregateInvoiceLineDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineExchangeRate is not None:
            lineExchangeRate_ = self.lineExchangeRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineExchangeRate').text = self.gds_format_decimal(lineExchangeRate_)
        if self.lineDeliveryDate is not None:
            lineDeliveryDate_ = self.lineDeliveryDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineDeliveryDate').text = self.gds_format_date(lineDeliveryDate_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AggregateInvoiceLineDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineExchangeRate is not None:
            showIndent(outfile, level)
            outfile.write('lineExchangeRate=%f,\n' % self.lineExchangeRate)
        if self.lineDeliveryDate is not None:
            showIndent(outfile, level)
            outfile.write('lineDeliveryDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.lineDeliveryDate, input_name='lineDeliveryDate'))
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
        if nodeName_ == 'lineExchangeRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineExchangeRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineExchangeRate')
            self.lineExchangeRate = fval_
            self.lineExchangeRate_nsprefix_ = child_.prefix
            # validate type ExchangeRateType
            self.validate_ExchangeRateType(self.lineExchangeRate)
        elif nodeName_ == 'lineDeliveryDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.lineDeliveryDate = dval_
            self.lineDeliveryDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.lineDeliveryDate)
