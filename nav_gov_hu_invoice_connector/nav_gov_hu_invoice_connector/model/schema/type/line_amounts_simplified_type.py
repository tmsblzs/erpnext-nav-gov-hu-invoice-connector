import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vat_rate_type import VatRateType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class LineAmountsSimplifiedType(GeneratedsSuper):
    """LineAmountsSimplifiedType -- Egyszerűsített számla esetén kitöltendő tétel érték adatok
    Item value data to be completed in case of simplified invoice
    lineVatRate -- Adó mérték vagy adómentesség jelölése
    Tax rate or tax exemption marking
    lineGrossAmountSimplified -- Tétel bruttó értéke a számla pénznemében
    Gross amount of the item expressed in the currency of the invoice
    lineGrossAmountSimplifiedHUF -- Tétel bruttó értéke forintban
    Gross amount of the item expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineVatRate=None, lineGrossAmountSimplified=None, lineGrossAmountSimplifiedHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineVatRate = lineVatRate
        self.lineVatRate_nsprefix_ = None
        self.lineGrossAmountSimplified = lineGrossAmountSimplified
        self.validate_MonetaryType(self.lineGrossAmountSimplified)
        self.lineGrossAmountSimplified_nsprefix_ = "base"
        self.lineGrossAmountSimplifiedHUF = lineGrossAmountSimplifiedHUF
        self.validate_MonetaryType(self.lineGrossAmountSimplifiedHUF)
        self.lineGrossAmountSimplifiedHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineAmountsSimplifiedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineAmountsSimplifiedType.subclass:
            return LineAmountsSimplifiedType.subclass(*args_, **kwargs_)
        else:
            return LineAmountsSimplifiedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineVatRate(self):
        return self.lineVatRate
    def set_lineVatRate(self, lineVatRate):
        self.lineVatRate = lineVatRate
    def get_lineGrossAmountSimplified(self):
        return self.lineGrossAmountSimplified
    def set_lineGrossAmountSimplified(self, lineGrossAmountSimplified):
        self.lineGrossAmountSimplified = lineGrossAmountSimplified
    def get_lineGrossAmountSimplifiedHUF(self):
        return self.lineGrossAmountSimplifiedHUF
    def set_lineGrossAmountSimplifiedHUF(self, lineGrossAmountSimplifiedHUF):
        self.lineGrossAmountSimplifiedHUF = lineGrossAmountSimplifiedHUF
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
            self.lineVatRate is not None or
            self.lineGrossAmountSimplified is not None or
            self.lineGrossAmountSimplifiedHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineAmountsSimplifiedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineAmountsSimplifiedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineAmountsSimplifiedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineAmountsSimplifiedType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineAmountsSimplifiedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineAmountsSimplifiedType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineAmountsSimplifiedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineVatRate is not None:
            namespaceprefix_ = self.lineVatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatRate_nsprefix_) else ''
            self.lineVatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineVatRate', pretty_print=pretty_print)
        if self.lineGrossAmountSimplified is not None:
            namespaceprefix_ = self.lineGrossAmountSimplified_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountSimplified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineGrossAmountSimplified>%s</%slineGrossAmountSimplified>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineGrossAmountSimplified, input_name='lineGrossAmountSimplified'), namespaceprefix_ , eol_))
        if self.lineGrossAmountSimplifiedHUF is not None:
            namespaceprefix_ = self.lineGrossAmountSimplifiedHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountSimplifiedHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineGrossAmountSimplifiedHUF>%s</%slineGrossAmountSimplifiedHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineGrossAmountSimplifiedHUF, input_name='lineGrossAmountSimplifiedHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineAmountsSimplifiedType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineVatRate is not None:
            lineVatRate_ = self.lineVatRate
            lineVatRate_.to_etree(element, name_='lineVatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineGrossAmountSimplified is not None:
            lineGrossAmountSimplified_ = self.lineGrossAmountSimplified
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountSimplified').text = self.gds_format_decimal(lineGrossAmountSimplified_)
        if self.lineGrossAmountSimplifiedHUF is not None:
            lineGrossAmountSimplifiedHUF_ = self.lineGrossAmountSimplifiedHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountSimplifiedHUF').text = self.gds_format_decimal(lineGrossAmountSimplifiedHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineAmountsSimplifiedType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineVatRate is not None:
            showIndent(outfile, level)
            outfile.write('lineVatRate=model_.VatRateType(\n')
            self.lineVatRate.exportLiteral(outfile, level, name_='lineVatRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineGrossAmountSimplified is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountSimplified=%f,\n' % self.lineGrossAmountSimplified)
        if self.lineGrossAmountSimplifiedHUF is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountSimplifiedHUF=%f,\n' % self.lineGrossAmountSimplifiedHUF)
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
        if nodeName_ == 'lineVatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineVatRate = obj_
            obj_.original_tagname_ = 'lineVatRate'
        elif nodeName_ == 'lineGrossAmountSimplified' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineGrossAmountSimplified')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineGrossAmountSimplified')
            self.lineGrossAmountSimplified = fval_
            self.lineGrossAmountSimplified_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineGrossAmountSimplified)
        elif nodeName_ == 'lineGrossAmountSimplifiedHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineGrossAmountSimplifiedHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineGrossAmountSimplifiedHUF')
            self.lineGrossAmountSimplifiedHUF = fval_
            self.lineGrossAmountSimplifiedHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineGrossAmountSimplifiedHUF)
