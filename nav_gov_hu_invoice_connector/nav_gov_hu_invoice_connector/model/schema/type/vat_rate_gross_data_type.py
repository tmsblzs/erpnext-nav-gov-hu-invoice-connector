import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class VatRateGrossDataType(GeneratedsSuper):
    """VatRateGrossDataType -- Adott adómértékhez tartozó bruttó adatok
    Gross data of given tax rate
    vatRateGrossAmount -- Az adott adómértékhez tartozó értékesítés
        vagy szolgáltatásnyújtás bruttó összege a számla pénznemében
    Gross amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    vatRateGrossAmountHUF -- Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege forintban
    Gross amount of sales or service delivery under a given tax rate expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRateGrossAmount=None, vatRateGrossAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRateGrossAmount = vatRateGrossAmount
        self.validate_MonetaryType(self.vatRateGrossAmount)
        self.vatRateGrossAmount_nsprefix_ = "base"
        self.vatRateGrossAmountHUF = vatRateGrossAmountHUF
        self.validate_MonetaryType(self.vatRateGrossAmountHUF)
        self.vatRateGrossAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateGrossDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateGrossDataType.subclass:
            return VatRateGrossDataType.subclass(*args_, **kwargs_)
        else:
            return VatRateGrossDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRateGrossAmount(self):
        return self.vatRateGrossAmount
    def set_vatRateGrossAmount(self, vatRateGrossAmount):
        self.vatRateGrossAmount = vatRateGrossAmount
    def get_vatRateGrossAmountHUF(self):
        return self.vatRateGrossAmountHUF
    def set_vatRateGrossAmountHUF(self, vatRateGrossAmountHUF):
        self.vatRateGrossAmountHUF = vatRateGrossAmountHUF
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
            self.vatRateGrossAmount is not None or
            self.vatRateGrossAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateGrossDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateGrossDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateGrossDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateGrossDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateGrossDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateGrossDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateGrossDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRateGrossAmount is not None:
            namespaceprefix_ = self.vatRateGrossAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateGrossAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateGrossAmount>%s</%svatRateGrossAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateGrossAmount, input_name='vatRateGrossAmount'), namespaceprefix_ , eol_))
        if self.vatRateGrossAmountHUF is not None:
            namespaceprefix_ = self.vatRateGrossAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateGrossAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateGrossAmountHUF>%s</%svatRateGrossAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateGrossAmountHUF, input_name='vatRateGrossAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateGrossDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRateGrossAmount is not None:
            vatRateGrossAmount_ = self.vatRateGrossAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateGrossAmount').text = self.gds_format_decimal(vatRateGrossAmount_)
        if self.vatRateGrossAmountHUF is not None:
            vatRateGrossAmountHUF_ = self.vatRateGrossAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateGrossAmountHUF').text = self.gds_format_decimal(vatRateGrossAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateGrossDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRateGrossAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatRateGrossAmount=%f,\n' % self.vatRateGrossAmount)
        if self.vatRateGrossAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatRateGrossAmountHUF=%f,\n' % self.vatRateGrossAmountHUF)
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
        if nodeName_ == 'vatRateGrossAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateGrossAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateGrossAmount')
            self.vatRateGrossAmount = fval_
            self.vatRateGrossAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateGrossAmount)
        elif nodeName_ == 'vatRateGrossAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateGrossAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateGrossAmountHUF')
            self.vatRateGrossAmountHUF = fval_
            self.vatRateGrossAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateGrossAmountHUF)
