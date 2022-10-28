import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class VatRateNetDataType(GeneratedsSuper):
    """VatRateNetDataType -- Adott adómértékhez tartozó nettó adatok
    Net data of given tax rate
    vatRateNetAmount -- Az adott adómértékhez tartozó értékesítés
        vagy szolgáltatásnyújtás nettó összege a számla pénznemében
    Net amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    vatRateNetAmountHUF -- Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás nettó összege forintban
    Net amount of sales or service delivery under a given tax rate expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRateNetAmount=None, vatRateNetAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRateNetAmount = vatRateNetAmount
        self.validate_MonetaryType(self.vatRateNetAmount)
        self.vatRateNetAmount_nsprefix_ = "base"
        self.vatRateNetAmountHUF = vatRateNetAmountHUF
        self.validate_MonetaryType(self.vatRateNetAmountHUF)
        self.vatRateNetAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateNetDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateNetDataType.subclass:
            return VatRateNetDataType.subclass(*args_, **kwargs_)
        else:
            return VatRateNetDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRateNetAmount(self):
        return self.vatRateNetAmount
    def set_vatRateNetAmount(self, vatRateNetAmount):
        self.vatRateNetAmount = vatRateNetAmount
    def get_vatRateNetAmountHUF(self):
        return self.vatRateNetAmountHUF
    def set_vatRateNetAmountHUF(self, vatRateNetAmountHUF):
        self.vatRateNetAmountHUF = vatRateNetAmountHUF
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
            self.vatRateNetAmount is not None or
            self.vatRateNetAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateNetDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateNetDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateNetDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateNetDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateNetDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateNetDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateNetDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRateNetAmount is not None:
            namespaceprefix_ = self.vatRateNetAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateNetAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateNetAmount>%s</%svatRateNetAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateNetAmount, input_name='vatRateNetAmount'), namespaceprefix_ , eol_))
        if self.vatRateNetAmountHUF is not None:
            namespaceprefix_ = self.vatRateNetAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateNetAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateNetAmountHUF>%s</%svatRateNetAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateNetAmountHUF, input_name='vatRateNetAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateNetDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRateNetAmount is not None:
            vatRateNetAmount_ = self.vatRateNetAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateNetAmount').text = self.gds_format_decimal(vatRateNetAmount_)
        if self.vatRateNetAmountHUF is not None:
            vatRateNetAmountHUF_ = self.vatRateNetAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateNetAmountHUF').text = self.gds_format_decimal(vatRateNetAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateNetDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRateNetAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatRateNetAmount=%f,\n' % self.vatRateNetAmount)
        if self.vatRateNetAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatRateNetAmountHUF=%f,\n' % self.vatRateNetAmountHUF)
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
        if nodeName_ == 'vatRateNetAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateNetAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateNetAmount')
            self.vatRateNetAmount = fval_
            self.vatRateNetAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateNetAmount)
        elif nodeName_ == 'vatRateNetAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateNetAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateNetAmountHUF')
            self.vatRateNetAmountHUF = fval_
            self.vatRateNetAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateNetAmountHUF)
