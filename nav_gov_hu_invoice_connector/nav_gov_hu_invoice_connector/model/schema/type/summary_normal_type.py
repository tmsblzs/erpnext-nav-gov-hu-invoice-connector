import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.summary_by_vat_rate_type import \
    SummaryByVatRateType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class SummaryNormalType(GeneratedsSuper):
    """SummaryNormalType -- Számla összesítés (nem egyszerűsített számla esetén)
    Calculation of invoice totals (not simplified invoice)
    summaryByVatRate -- Összesítés ÁFA-m érték szerint
    Calculation of invoice totals per VAT rates
    invoiceNetAmount -- A számla nettó összege a számla pénznemében
    Net amount of the invoice expressed in the currency of the invoice
    invoiceNetAmountHUF -- A számla nettó összege forintban
    Net amount of the invoice expressed in HUF
    invoiceVatAmount -- A számla ÁFA összege a számla pénznemében
    VAT amount of the invoice expressed in the currency of the invoice
    invoiceVatAmountHUF -- A számla ÁFA összege forintban
    VAT amount of the invoice expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, summaryByVatRate=None, invoiceNetAmount=None, invoiceNetAmountHUF=None, invoiceVatAmount=None, invoiceVatAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if summaryByVatRate is None:
            self.summaryByVatRate = []
        else:
            self.summaryByVatRate = summaryByVatRate
        self.summaryByVatRate_nsprefix_ = None
        self.invoiceNetAmount = invoiceNetAmount
        self.validate_MonetaryType(self.invoiceNetAmount)
        self.invoiceNetAmount_nsprefix_ = "base"
        self.invoiceNetAmountHUF = invoiceNetAmountHUF
        self.validate_MonetaryType(self.invoiceNetAmountHUF)
        self.invoiceNetAmountHUF_nsprefix_ = "base"
        self.invoiceVatAmount = invoiceVatAmount
        self.validate_MonetaryType(self.invoiceVatAmount)
        self.invoiceVatAmount_nsprefix_ = "base"
        self.invoiceVatAmountHUF = invoiceVatAmountHUF
        self.validate_MonetaryType(self.invoiceVatAmountHUF)
        self.invoiceVatAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryNormalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryNormalType.subclass:
            return SummaryNormalType.subclass(*args_, **kwargs_)
        else:
            return SummaryNormalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_summaryByVatRate(self):
        return self.summaryByVatRate
    def set_summaryByVatRate(self, summaryByVatRate):
        self.summaryByVatRate = summaryByVatRate
    def add_summaryByVatRate(self, value):
        self.summaryByVatRate.append(value)
    def insert_summaryByVatRate_at(self, index, value):
        self.summaryByVatRate.insert(index, value)
    def replace_summaryByVatRate_at(self, index, value):
        self.summaryByVatRate[index] = value
    def get_invoiceNetAmount(self):
        return self.invoiceNetAmount
    def set_invoiceNetAmount(self, invoiceNetAmount):
        self.invoiceNetAmount = invoiceNetAmount
    def get_invoiceNetAmountHUF(self):
        return self.invoiceNetAmountHUF
    def set_invoiceNetAmountHUF(self, invoiceNetAmountHUF):
        self.invoiceNetAmountHUF = invoiceNetAmountHUF
    def get_invoiceVatAmount(self):
        return self.invoiceVatAmount
    def set_invoiceVatAmount(self, invoiceVatAmount):
        self.invoiceVatAmount = invoiceVatAmount
    def get_invoiceVatAmountHUF(self):
        return self.invoiceVatAmountHUF
    def set_invoiceVatAmountHUF(self, invoiceVatAmountHUF):
        self.invoiceVatAmountHUF = invoiceVatAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.summaryByVatRate or
            self.invoiceNetAmount is not None or
            self.invoiceNetAmountHUF is not None or
            self.invoiceVatAmount is not None or
            self.invoiceVatAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryNormalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryNormalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryNormalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryNormalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryNormalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryNormalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryNormalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for summaryByVatRate_ in self.summaryByVatRate:
            namespaceprefix_ = self.summaryByVatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.summaryByVatRate_nsprefix_) else ''
            summaryByVatRate_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summaryByVatRate', pretty_print=pretty_print)
        if self.invoiceNetAmount is not None:
            namespaceprefix_ = self.invoiceNetAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceNetAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNetAmount>%s</%sinvoiceNetAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceNetAmount, input_name='invoiceNetAmount'), namespaceprefix_ , eol_))
        if self.invoiceNetAmountHUF is not None:
            namespaceprefix_ = self.invoiceNetAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceNetAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNetAmountHUF>%s</%sinvoiceNetAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceNetAmountHUF, input_name='invoiceNetAmountHUF'), namespaceprefix_ , eol_))
        if self.invoiceVatAmount is not None:
            namespaceprefix_ = self.invoiceVatAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceVatAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceVatAmount>%s</%sinvoiceVatAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceVatAmount, input_name='invoiceVatAmount'), namespaceprefix_ , eol_))
        if self.invoiceVatAmountHUF is not None:
            namespaceprefix_ = self.invoiceVatAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceVatAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceVatAmountHUF>%s</%sinvoiceVatAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceVatAmountHUF, input_name='invoiceVatAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SummaryNormalType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for summaryByVatRate_ in self.summaryByVatRate:
            summaryByVatRate_.to_etree(element, name_='summaryByVatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceNetAmount is not None:
            invoiceNetAmount_ = self.invoiceNetAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNetAmount').text = self.gds_format_decimal(invoiceNetAmount_)
        if self.invoiceNetAmountHUF is not None:
            invoiceNetAmountHUF_ = self.invoiceNetAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNetAmountHUF').text = self.gds_format_decimal(invoiceNetAmountHUF_)
        if self.invoiceVatAmount is not None:
            invoiceVatAmount_ = self.invoiceVatAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceVatAmount').text = self.gds_format_decimal(invoiceVatAmount_)
        if self.invoiceVatAmountHUF is not None:
            invoiceVatAmountHUF_ = self.invoiceVatAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceVatAmountHUF').text = self.gds_format_decimal(invoiceVatAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryNormalType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('summaryByVatRate=[\n')
        level += 1
        for summaryByVatRate_ in self.summaryByVatRate:
            showIndent(outfile, level)
            outfile.write('model_.SummaryByVatRateType(\n')
            summaryByVatRate_.exportLiteral(outfile, level, name_='SummaryByVatRateType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.invoiceNetAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNetAmount=%f,\n' % self.invoiceNetAmount)
        if self.invoiceNetAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNetAmountHUF=%f,\n' % self.invoiceNetAmountHUF)
        if self.invoiceVatAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceVatAmount=%f,\n' % self.invoiceVatAmount)
        if self.invoiceVatAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceVatAmountHUF=%f,\n' % self.invoiceVatAmountHUF)
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
        if nodeName_ == 'summaryByVatRate':
            obj_ = SummaryByVatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summaryByVatRate.append(obj_)
            obj_.original_tagname_ = 'summaryByVatRate'
        elif nodeName_ == 'invoiceNetAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceNetAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceNetAmount')
            self.invoiceNetAmount = fval_
            self.invoiceNetAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceNetAmount)
        elif nodeName_ == 'invoiceNetAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceNetAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceNetAmountHUF')
            self.invoiceNetAmountHUF = fval_
            self.invoiceNetAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceNetAmountHUF)
        elif nodeName_ == 'invoiceVatAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceVatAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceVatAmount')
            self.invoiceVatAmount = fval_
            self.invoiceVatAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceVatAmount)
        elif nodeName_ == 'invoiceVatAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceVatAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceVatAmountHUF')
            self.invoiceVatAmountHUF = fval_
            self.invoiceVatAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceVatAmountHUF)
