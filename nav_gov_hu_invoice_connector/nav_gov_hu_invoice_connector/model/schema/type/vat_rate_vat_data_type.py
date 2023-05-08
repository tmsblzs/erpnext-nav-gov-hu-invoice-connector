import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class VatRateVatDataType(GeneratedsSuper):
    """VatRateVatDataType -- Adott adómértékhez tartozó ÁFA adatok
    VAT data of given tax rate
    vatRateVatAmount -- Az adott adómértékhez tartozó értékesítés
        vagy szolgáltatásnyújtás ÁFA összege a számla pénznemében
    VAT amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    vatRateVatAmountHUF -- Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás ÁFA összege forintban
    VAT amount of sales or service delivery under a given tax rate expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRateVatAmount=None, vatRateVatAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRateVatAmount = vatRateVatAmount
        self.validate_MonetaryType(self.vatRateVatAmount)
        self.vatRateVatAmount_nsprefix_ = "base"
        self.vatRateVatAmountHUF = vatRateVatAmountHUF
        self.validate_MonetaryType(self.vatRateVatAmountHUF)
        self.vatRateVatAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateVatDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateVatDataType.subclass:
            return VatRateVatDataType.subclass(*args_, **kwargs_)
        else:
            return VatRateVatDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRateVatAmount(self):
        return self.vatRateVatAmount
    def set_vatRateVatAmount(self, vatRateVatAmount):
        self.vatRateVatAmount = vatRateVatAmount
    def get_vatRateVatAmountHUF(self):
        return self.vatRateVatAmountHUF
    def set_vatRateVatAmountHUF(self, vatRateVatAmountHUF):
        self.vatRateVatAmountHUF = vatRateVatAmountHUF
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
            self.vatRateVatAmount is not None or
            self.vatRateVatAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateVatDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateVatDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateVatDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateVatDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateVatDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateVatDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateVatDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRateVatAmount is not None:
            namespaceprefix_ = self.vatRateVatAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateVatAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateVatAmount>%s</%svatRateVatAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateVatAmount, input_name='vatRateVatAmount'), namespaceprefix_ , eol_))
        if self.vatRateVatAmountHUF is not None:
            namespaceprefix_ = self.vatRateVatAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateVatAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateVatAmountHUF>%s</%svatRateVatAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateVatAmountHUF, input_name='vatRateVatAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateVatDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRateVatAmount is not None:
            vatRateVatAmount_ = self.vatRateVatAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateVatAmount').text = self.gds_format_decimal(vatRateVatAmount_)
        if self.vatRateVatAmountHUF is not None:
            vatRateVatAmountHUF_ = self.vatRateVatAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateVatAmountHUF').text = self.gds_format_decimal(vatRateVatAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateVatDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRateVatAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatRateVatAmount=%f,\n' % self.vatRateVatAmount)
        if self.vatRateVatAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatRateVatAmountHUF=%f,\n' % self.vatRateVatAmountHUF)
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
        if nodeName_ == 'vatRateVatAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateVatAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateVatAmount')
            self.vatRateVatAmount = fval_
            self.vatRateVatAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateVatAmount)
        elif nodeName_ == 'vatRateVatAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateVatAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateVatAmountHUF')
            self.vatRateVatAmountHUF = fval_
            self.vatRateVatAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateVatAmountHUF)
