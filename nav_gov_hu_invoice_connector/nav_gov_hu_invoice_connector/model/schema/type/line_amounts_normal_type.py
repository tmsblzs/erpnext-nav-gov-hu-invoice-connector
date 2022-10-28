import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.line_gross_amount_data_type import \
    LineGrossAmountDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.line_net_amount_data_type import \
    LineNetAmountDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.line_vat_data_type import \
    LineVatDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vat_rate_type import VatRateType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class LineAmountsNormalType(GeneratedsSuper):
    """LineAmountsNormalType -- Normál vagy gyűjtőszámla esetén kitöltendő tétel érték adatok
    Item value data to be completed in case of normal or aggregate invoice
    lineNetAmountData -- Tétel nettó adatok
    Line net data
    lineVatRate -- Adómérték vagy adómentesség jelölése
    Tax rate or tax exemption marking
    lineVatData -- Tétel ÁFA adatok
    Line VAT data
    lineGrossAmountData -- Tétel bruttó adatok
    Line gross data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineNetAmountData=None, lineVatRate=None, lineVatData=None, lineGrossAmountData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNetAmountData = lineNetAmountData
        self.lineNetAmountData_nsprefix_ = None
        self.lineVatRate = lineVatRate
        self.lineVatRate_nsprefix_ = None
        self.lineVatData = lineVatData
        self.lineVatData_nsprefix_ = None
        self.lineGrossAmountData = lineGrossAmountData
        self.lineGrossAmountData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineAmountsNormalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineAmountsNormalType.subclass:
            return LineAmountsNormalType.subclass(*args_, **kwargs_)
        else:
            return LineAmountsNormalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineNetAmountData(self):
        return self.lineNetAmountData
    def set_lineNetAmountData(self, lineNetAmountData):
        self.lineNetAmountData = lineNetAmountData
    def get_lineVatRate(self):
        return self.lineVatRate
    def set_lineVatRate(self, lineVatRate):
        self.lineVatRate = lineVatRate
    def get_lineVatData(self):
        return self.lineVatData
    def set_lineVatData(self, lineVatData):
        self.lineVatData = lineVatData
    def get_lineGrossAmountData(self):
        return self.lineGrossAmountData
    def set_lineGrossAmountData(self, lineGrossAmountData):
        self.lineGrossAmountData = lineGrossAmountData
    def _hasContent(self):
        if (
            self.lineNetAmountData is not None or
            self.lineVatRate is not None or
            self.lineVatData is not None or
            self.lineGrossAmountData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineAmountsNormalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineAmountsNormalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineAmountsNormalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineAmountsNormalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineAmountsNormalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineAmountsNormalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineAmountsNormalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNetAmountData is not None:
            namespaceprefix_ = self.lineNetAmountData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNetAmountData_nsprefix_) else ''
            self.lineNetAmountData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineNetAmountData', pretty_print=pretty_print)
        if self.lineVatRate is not None:
            namespaceprefix_ = self.lineVatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatRate_nsprefix_) else ''
            self.lineVatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineVatRate', pretty_print=pretty_print)
        if self.lineVatData is not None:
            namespaceprefix_ = self.lineVatData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatData_nsprefix_) else ''
            self.lineVatData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineVatData', pretty_print=pretty_print)
        if self.lineGrossAmountData is not None:
            namespaceprefix_ = self.lineGrossAmountData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountData_nsprefix_) else ''
            self.lineGrossAmountData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineGrossAmountData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LineAmountsNormalType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineNetAmountData is not None:
            lineNetAmountData_ = self.lineNetAmountData
            lineNetAmountData_.to_etree(element, name_='lineNetAmountData', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineVatRate is not None:
            lineVatRate_ = self.lineVatRate
            lineVatRate_.to_etree(element, name_='lineVatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineVatData is not None:
            lineVatData_ = self.lineVatData
            lineVatData_.to_etree(element, name_='lineVatData', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineGrossAmountData is not None:
            lineGrossAmountData_ = self.lineGrossAmountData
            lineGrossAmountData_.to_etree(element, name_='lineGrossAmountData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineAmountsNormalType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNetAmountData is not None:
            showIndent(outfile, level)
            outfile.write('lineNetAmountData=model_.LineNetAmountDataType(\n')
            self.lineNetAmountData.exportLiteral(outfile, level, name_='lineNetAmountData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineVatRate is not None:
            showIndent(outfile, level)
            outfile.write('lineVatRate=model_.VatRateType(\n')
            self.lineVatRate.exportLiteral(outfile, level, name_='lineVatRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineVatData is not None:
            showIndent(outfile, level)
            outfile.write('lineVatData=model_.LineVatDataType(\n')
            self.lineVatData.exportLiteral(outfile, level, name_='lineVatData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineGrossAmountData is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountData=model_.LineGrossAmountDataType(\n')
            self.lineGrossAmountData.exportLiteral(outfile, level, name_='lineGrossAmountData')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'lineNetAmountData':
            obj_ = LineNetAmountDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineNetAmountData = obj_
            obj_.original_tagname_ = 'lineNetAmountData'
        elif nodeName_ == 'lineVatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineVatRate = obj_
            obj_.original_tagname_ = 'lineVatRate'
        elif nodeName_ == 'lineVatData':
            obj_ = LineVatDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineVatData = obj_
            obj_.original_tagname_ = 'lineVatData'
        elif nodeName_ == 'lineGrossAmountData':
            obj_ = LineGrossAmountDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineGrossAmountData = obj_
            obj_.original_tagname_ = 'lineGrossAmountData'
