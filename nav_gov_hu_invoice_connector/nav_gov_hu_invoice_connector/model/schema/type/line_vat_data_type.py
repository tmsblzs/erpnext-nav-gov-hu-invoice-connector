import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class LineVatDataType(GeneratedsSuper):
    """LineVatDataType -- Tétel ÁFA adatok
    Line VAT data
    lineVatAmount -- Tétel ÁFA összege a számla pénznemében
    VAT amount of the item expressed in the currency of the invoice
    lineVatAmountHUF -- Tétel ÁFA összege forintban
    VAT amount of the item expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineVatAmount=None, lineVatAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineVatAmount = lineVatAmount
        self.validate_MonetaryType(self.lineVatAmount)
        self.lineVatAmount_nsprefix_ = "base"
        self.lineVatAmountHUF = lineVatAmountHUF
        self.validate_MonetaryType(self.lineVatAmountHUF)
        self.lineVatAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineVatDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineVatDataType.subclass:
            return LineVatDataType.subclass(*args_, **kwargs_)
        else:
            return LineVatDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineVatAmount(self):
        return self.lineVatAmount
    def set_lineVatAmount(self, lineVatAmount):
        self.lineVatAmount = lineVatAmount
    def get_lineVatAmountHUF(self):
        return self.lineVatAmountHUF
    def set_lineVatAmountHUF(self, lineVatAmountHUF):
        self.lineVatAmountHUF = lineVatAmountHUF
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
            self.lineVatAmount is not None or
            self.lineVatAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineVatDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineVatDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineVatDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineVatDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineVatDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineVatDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineVatDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineVatAmount is not None:
            namespaceprefix_ = self.lineVatAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineVatAmount>%s</%slineVatAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineVatAmount, input_name='lineVatAmount'), namespaceprefix_ , eol_))
        if self.lineVatAmountHUF is not None:
            namespaceprefix_ = self.lineVatAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineVatAmountHUF>%s</%slineVatAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineVatAmountHUF, input_name='lineVatAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineVatDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineVatAmount is not None:
            lineVatAmount_ = self.lineVatAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineVatAmount').text = self.gds_format_decimal(lineVatAmount_)
        if self.lineVatAmountHUF is not None:
            lineVatAmountHUF_ = self.lineVatAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineVatAmountHUF').text = self.gds_format_decimal(lineVatAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineVatDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineVatAmount is not None:
            showIndent(outfile, level)
            outfile.write('lineVatAmount=%f,\n' % self.lineVatAmount)
        if self.lineVatAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('lineVatAmountHUF=%f,\n' % self.lineVatAmountHUF)
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
        if nodeName_ == 'lineVatAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineVatAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineVatAmount')
            self.lineVatAmount = fval_
            self.lineVatAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineVatAmount)
        elif nodeName_ == 'lineVatAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineVatAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineVatAmountHUF')
            self.lineVatAmountHUF = fval_
            self.lineVatAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineVatAmountHUF)
