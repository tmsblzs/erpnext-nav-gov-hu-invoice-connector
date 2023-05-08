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


class SummarySimplifiedType(GeneratedsSuper):
    """SummarySimplifiedType -- Egyszerűsített számla összesítés
    Calculation of simplified invoice totals
    vatRate -- Adó mérték vagy adómentesség jelölése
    Marking the tax rate or the fact of tax exemption
    vatContentGrossAmount -- Az adott adótartalomhoz tartozó értékesítés
        vagy szolgáltatásnyújtás bruttó összege a számla pénznemében
    The gross amount of the sale or service for the given tax amount in the currency of the invoice
    vatContentGrossAmountHUF -- Az adott adótartalomhoz tartozó értékesítés
        vagy szolgáltatásnyújtás bruttó összege forintban
    The gross amount of the sale or service for the given tax amount in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRate=None, vatContentGrossAmount=None, vatContentGrossAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRate = vatRate
        self.vatRate_nsprefix_ = None
        self.vatContentGrossAmount = vatContentGrossAmount
        self.validate_MonetaryType(self.vatContentGrossAmount)
        self.vatContentGrossAmount_nsprefix_ = "base"
        self.vatContentGrossAmountHUF = vatContentGrossAmountHUF
        self.validate_MonetaryType(self.vatContentGrossAmountHUF)
        self.vatContentGrossAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummarySimplifiedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummarySimplifiedType.subclass:
            return SummarySimplifiedType.subclass(*args_, **kwargs_)
        else:
            return SummarySimplifiedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRate(self):
        return self.vatRate
    def set_vatRate(self, vatRate):
        self.vatRate = vatRate
    def get_vatContentGrossAmount(self):
        return self.vatContentGrossAmount
    def set_vatContentGrossAmount(self, vatContentGrossAmount):
        self.vatContentGrossAmount = vatContentGrossAmount
    def get_vatContentGrossAmountHUF(self):
        return self.vatContentGrossAmountHUF
    def set_vatContentGrossAmountHUF(self, vatContentGrossAmountHUF):
        self.vatContentGrossAmountHUF = vatContentGrossAmountHUF
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
            self.vatRate is not None or
            self.vatContentGrossAmount is not None or
            self.vatContentGrossAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummarySimplifiedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummarySimplifiedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummarySimplifiedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummarySimplifiedType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummarySimplifiedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummarySimplifiedType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummarySimplifiedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRate is not None:
            namespaceprefix_ = self.vatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRate_nsprefix_) else ''
            self.vatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRate', pretty_print=pretty_print)
        if self.vatContentGrossAmount is not None:
            namespaceprefix_ = self.vatContentGrossAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatContentGrossAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatContentGrossAmount>%s</%svatContentGrossAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatContentGrossAmount, input_name='vatContentGrossAmount'), namespaceprefix_ , eol_))
        if self.vatContentGrossAmountHUF is not None:
            namespaceprefix_ = self.vatContentGrossAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatContentGrossAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatContentGrossAmountHUF>%s</%svatContentGrossAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatContentGrossAmountHUF, input_name='vatContentGrossAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SummarySimplifiedType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRate is not None:
            vatRate_ = self.vatRate
            vatRate_.to_etree(element, name_='vatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatContentGrossAmount is not None:
            vatContentGrossAmount_ = self.vatContentGrossAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatContentGrossAmount').text = self.gds_format_decimal(vatContentGrossAmount_)
        if self.vatContentGrossAmountHUF is not None:
            vatContentGrossAmountHUF_ = self.vatContentGrossAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatContentGrossAmountHUF').text = self.gds_format_decimal(vatContentGrossAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummarySimplifiedType'):
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
            outfile.write('vatRate=model_.VatRateType(\n')
            self.vatRate.exportLiteral(outfile, level, name_='vatRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatContentGrossAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatContentGrossAmount=%f,\n' % self.vatContentGrossAmount)
        if self.vatContentGrossAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatContentGrossAmountHUF=%f,\n' % self.vatContentGrossAmountHUF)
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
        if nodeName_ == 'vatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRate = obj_
            obj_.original_tagname_ = 'vatRate'
        elif nodeName_ == 'vatContentGrossAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatContentGrossAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatContentGrossAmount')
            self.vatContentGrossAmount = fval_
            self.vatContentGrossAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatContentGrossAmount)
        elif nodeName_ == 'vatContentGrossAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatContentGrossAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatContentGrossAmountHUF')
            self.vatContentGrossAmountHUF = fval_
            self.vatContentGrossAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatContentGrossAmountHUF)
