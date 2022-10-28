import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.summary_gross_data_type import \
    SummaryGrossDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.summary_normal_type import \
    SummaryNormalType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.summary_simplified_type import \
    SummarySimplifiedType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class SummaryType(GeneratedsSuper):
    """SummaryType -- Számla összesítés adatai
    Data of calculation of invoice totals
    summaryNormal -- Számla összesítés (nem egyszerűsített számla esetén)
    Calculation of invoice totals (not simplified invoice)
    summarySimplified -- Egyszerűsített számla összesítés
    Calculation of simplified invoice totals
    summaryGrossData -- A számla összesítő bruttó adatai
    Gross data of the invoice summary

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, summaryNormal=None, summarySimplified=None, summaryGrossData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.summaryNormal = summaryNormal
        self.summaryNormal_nsprefix_ = None
        if summarySimplified is None:
            self.summarySimplified = []
        else:
            self.summarySimplified = summarySimplified
        self.summarySimplified_nsprefix_ = None
        self.summaryGrossData = summaryGrossData
        self.summaryGrossData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryType.subclass:
            return SummaryType.subclass(*args_, **kwargs_)
        else:
            return SummaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_summaryNormal(self):
        return self.summaryNormal
    def set_summaryNormal(self, summaryNormal):
        self.summaryNormal = summaryNormal
    def get_summarySimplified(self):
        return self.summarySimplified
    def set_summarySimplified(self, summarySimplified):
        self.summarySimplified = summarySimplified
    def add_summarySimplified(self, value):
        self.summarySimplified.append(value)
    def insert_summarySimplified_at(self, index, value):
        self.summarySimplified.insert(index, value)
    def replace_summarySimplified_at(self, index, value):
        self.summarySimplified[index] = value
    def get_summaryGrossData(self):
        return self.summaryGrossData
    def set_summaryGrossData(self, summaryGrossData):
        self.summaryGrossData = summaryGrossData
    def _hasContent(self):
        if (
            self.summaryNormal is not None or
            self.summarySimplified or
            self.summaryGrossData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.summaryNormal is not None:
            namespaceprefix_ = self.summaryNormal_nsprefix_ + ':' if (UseCapturedNS_ and self.summaryNormal_nsprefix_) else ''
            self.summaryNormal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summaryNormal', pretty_print=pretty_print)
        for summarySimplified_ in self.summarySimplified:
            namespaceprefix_ = self.summarySimplified_nsprefix_ + ':' if (UseCapturedNS_ and self.summarySimplified_nsprefix_) else ''
            summarySimplified_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summarySimplified', pretty_print=pretty_print)
        if self.summaryGrossData is not None:
            namespaceprefix_ = self.summaryGrossData_nsprefix_ + ':' if (UseCapturedNS_ and self.summaryGrossData_nsprefix_) else ''
            self.summaryGrossData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summaryGrossData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SummaryType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.summaryNormal is not None:
            summaryNormal_ = self.summaryNormal
            summaryNormal_.to_etree(element, name_='summaryNormal', mapping_=mapping_, nsmap_=nsmap_)
        for summarySimplified_ in self.summarySimplified:
            summarySimplified_.to_etree(element, name_='summarySimplified', mapping_=mapping_, nsmap_=nsmap_)
        if self.summaryGrossData is not None:
            summaryGrossData_ = self.summaryGrossData
            summaryGrossData_.to_etree(element, name_='summaryGrossData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.summaryNormal is not None:
            showIndent(outfile, level)
            outfile.write('summaryNormal=model_.SummaryNormalType(\n')
            self.summaryNormal.exportLiteral(outfile, level, name_='summaryNormal')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('summarySimplified=[\n')
        level += 1
        for summarySimplified_ in self.summarySimplified:
            showIndent(outfile, level)
            outfile.write('model_.SummarySimplifiedType(\n')
            summarySimplified_.exportLiteral(outfile, level, name_='SummarySimplifiedType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.summaryGrossData is not None:
            showIndent(outfile, level)
            outfile.write('summaryGrossData=model_.SummaryGrossDataType(\n')
            self.summaryGrossData.exportLiteral(outfile, level, name_='summaryGrossData')
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
        if nodeName_ == 'summaryNormal':
            obj_ = SummaryNormalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summaryNormal = obj_
            obj_.original_tagname_ = 'summaryNormal'
        elif nodeName_ == 'summarySimplified':
            obj_ = SummarySimplifiedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summarySimplified.append(obj_)
            obj_.original_tagname_ = 'summarySimplified'
        elif nodeName_ == 'summaryGrossData':
            obj_ = SummaryGrossDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summaryGrossData = obj_
            obj_.original_tagname_ = 'summaryGrossData'
