import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class SummaryGrossDataType(GeneratedsSuper):
    """SummaryGrossDataType -- A számla összesítő bruttó adatai
    Gross data of the invoice summary
    invoiceGrossAmount -- A számla bruttó összege a számla pénznemében
    Gross amount of the invoice expressed in the currency of the invoice
    invoiceGrossAmountHUF -- A számla bruttó összege forintban
    Gross amount of the invoice expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoiceGrossAmount=None, invoiceGrossAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceGrossAmount = invoiceGrossAmount
        self.validate_MonetaryType(self.invoiceGrossAmount)
        self.invoiceGrossAmount_nsprefix_ = "base"
        self.invoiceGrossAmountHUF = invoiceGrossAmountHUF
        self.validate_MonetaryType(self.invoiceGrossAmountHUF)
        self.invoiceGrossAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryGrossDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryGrossDataType.subclass:
            return SummaryGrossDataType.subclass(*args_, **kwargs_)
        else:
            return SummaryGrossDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceGrossAmount(self):
        return self.invoiceGrossAmount
    def set_invoiceGrossAmount(self, invoiceGrossAmount):
        self.invoiceGrossAmount = invoiceGrossAmount
    def get_invoiceGrossAmountHUF(self):
        return self.invoiceGrossAmountHUF
    def set_invoiceGrossAmountHUF(self, invoiceGrossAmountHUF):
        self.invoiceGrossAmountHUF = invoiceGrossAmountHUF
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
            self.invoiceGrossAmount is not None or
            self.invoiceGrossAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryGrossDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryGrossDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryGrossDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryGrossDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryGrossDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryGrossDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryGrossDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceGrossAmount is not None:
            namespaceprefix_ = self.invoiceGrossAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceGrossAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceGrossAmount>%s</%sinvoiceGrossAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceGrossAmount, input_name='invoiceGrossAmount'), namespaceprefix_ , eol_))
        if self.invoiceGrossAmountHUF is not None:
            namespaceprefix_ = self.invoiceGrossAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceGrossAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceGrossAmountHUF>%s</%sinvoiceGrossAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceGrossAmountHUF, input_name='invoiceGrossAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SummaryGrossDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.invoiceGrossAmount is not None:
            invoiceGrossAmount_ = self.invoiceGrossAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceGrossAmount').text = self.gds_format_decimal(invoiceGrossAmount_)
        if self.invoiceGrossAmountHUF is not None:
            invoiceGrossAmountHUF_ = self.invoiceGrossAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceGrossAmountHUF').text = self.gds_format_decimal(invoiceGrossAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryGrossDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceGrossAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceGrossAmount=%f,\n' % self.invoiceGrossAmount)
        if self.invoiceGrossAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceGrossAmountHUF=%f,\n' % self.invoiceGrossAmountHUF)
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
        if nodeName_ == 'invoiceGrossAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceGrossAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceGrossAmount')
            self.invoiceGrossAmount = fval_
            self.invoiceGrossAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceGrossAmount)
        elif nodeName_ == 'invoiceGrossAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceGrossAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceGrossAmountHUF')
            self.invoiceGrossAmountHUF = fval_
            self.invoiceGrossAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceGrossAmountHUF)
