import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vat_rate_gross_data_type import \
    VatRateGrossDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vat_rate_net_data_type import \
    VatRateNetDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vat_rate_type import VatRateType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vat_rate_vat_data_type import \
    VatRateVatDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class SummaryByVatRateType(GeneratedsSuper):
    """SummaryByVatRateType -- ÁFA mértékek szerinti összesítés
    Summary according to VAT rates
    vatRate -- Adómérték vagy adómentesség jelölése
    Marking the tax rate or the fact of tax exemption
    vatRateNetData -- Adott adómértékhez tartozó nettó adatok
    Net data of given tax rate
    vatRateVatData -- Adott adómértékhez tartozó ÁFA adatok
    VAT data of given tax rate
    vatRateGrossData -- Adott adómértékhez tartozó bruttó adatok
    Gross data of given tax rate

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRate=None, vatRateNetData=None, vatRateVatData=None, vatRateGrossData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRate = vatRate
        self.vatRate_nsprefix_ = None
        self.vatRateNetData = vatRateNetData
        self.vatRateNetData_nsprefix_ = None
        self.vatRateVatData = vatRateVatData
        self.vatRateVatData_nsprefix_ = None
        self.vatRateGrossData = vatRateGrossData
        self.vatRateGrossData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryByVatRateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryByVatRateType.subclass:
            return SummaryByVatRateType.subclass(*args_, **kwargs_)
        else:
            return SummaryByVatRateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRate(self):
        return self.vatRate
    def set_vatRate(self, vatRate):
        self.vatRate = vatRate
    def get_vatRateNetData(self):
        return self.vatRateNetData
    def set_vatRateNetData(self, vatRateNetData):
        self.vatRateNetData = vatRateNetData
    def get_vatRateVatData(self):
        return self.vatRateVatData
    def set_vatRateVatData(self, vatRateVatData):
        self.vatRateVatData = vatRateVatData
    def get_vatRateGrossData(self):
        return self.vatRateGrossData
    def set_vatRateGrossData(self, vatRateGrossData):
        self.vatRateGrossData = vatRateGrossData
    def _hasContent(self):
        if (
            self.vatRate is not None or
            self.vatRateNetData is not None or
            self.vatRateVatData is not None or
            self.vatRateGrossData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryByVatRateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryByVatRateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryByVatRateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryByVatRateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryByVatRateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryByVatRateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryByVatRateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRate is not None:
            namespaceprefix_ = self.vatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRate_nsprefix_) else ''
            self.vatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRate', pretty_print=pretty_print)
        if self.vatRateNetData is not None:
            namespaceprefix_ = self.vatRateNetData_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateNetData_nsprefix_) else ''
            self.vatRateNetData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRateNetData', pretty_print=pretty_print)
        if self.vatRateVatData is not None:
            namespaceprefix_ = self.vatRateVatData_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateVatData_nsprefix_) else ''
            self.vatRateVatData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRateVatData', pretty_print=pretty_print)
        if self.vatRateGrossData is not None:
            namespaceprefix_ = self.vatRateGrossData_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateGrossData_nsprefix_) else ''
            self.vatRateGrossData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRateGrossData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SummaryByVatRateType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRate is not None:
            vatRate_ = self.vatRate
            vatRate_.to_etree(element, name_='vatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatRateNetData is not None:
            vatRateNetData_ = self.vatRateNetData
            vatRateNetData_.to_etree(element, name_='vatRateNetData', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatRateVatData is not None:
            vatRateVatData_ = self.vatRateVatData
            vatRateVatData_.to_etree(element, name_='vatRateVatData', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatRateGrossData is not None:
            vatRateGrossData_ = self.vatRateGrossData
            vatRateGrossData_.to_etree(element, name_='vatRateGrossData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryByVatRateType'):
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
        if self.vatRateNetData is not None:
            showIndent(outfile, level)
            outfile.write('vatRateNetData=model_.VatRateNetDataType(\n')
            self.vatRateNetData.exportLiteral(outfile, level, name_='vatRateNetData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatRateVatData is not None:
            showIndent(outfile, level)
            outfile.write('vatRateVatData=model_.VatRateVatDataType(\n')
            self.vatRateVatData.exportLiteral(outfile, level, name_='vatRateVatData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatRateGrossData is not None:
            showIndent(outfile, level)
            outfile.write('vatRateGrossData=model_.VatRateGrossDataType(\n')
            self.vatRateGrossData.exportLiteral(outfile, level, name_='vatRateGrossData')
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
        if nodeName_ == 'vatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRate = obj_
            obj_.original_tagname_ = 'vatRate'
        elif nodeName_ == 'vatRateNetData':
            obj_ = VatRateNetDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRateNetData = obj_
            obj_.original_tagname_ = 'vatRateNetData'
        elif nodeName_ == 'vatRateVatData':
            obj_ = VatRateVatDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRateVatData = obj_
            obj_.original_tagname_ = 'vatRateVatData'
        elif nodeName_ == 'vatRateGrossData':
            obj_ = VatRateGrossDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRateGrossData = obj_
            obj_.original_tagname_ = 'vatRateGrossData'
