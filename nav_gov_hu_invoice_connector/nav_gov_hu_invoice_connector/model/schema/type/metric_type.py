import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.metric_definition_type import \
    MetricDefinitionType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.metric_value_type import \
    MetricValueType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class MetricType(GeneratedsSuper):
    """MetricType -- Metrika típus
    Metric data type
    metricDefinition -- Metrika definíció
    Metric definition
    metricValues -- Metrika értékek
    Metric values

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, metricDefinition=None, metricValues=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.metricDefinition = metricDefinition
        self.metricDefinition_nsprefix_ = None
        if metricValues is None:
            self.metricValues = []
        else:
            self.metricValues = metricValues
        self.metricValues_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricType.subclass:
            return MetricType.subclass(*args_, **kwargs_)
        else:
            return MetricType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_metricDefinition(self):
        return self.metricDefinition
    def set_metricDefinition(self, metricDefinition):
        self.metricDefinition = metricDefinition
    def get_metricValues(self):
        return self.metricValues
    def set_metricValues(self, metricValues):
        self.metricValues = metricValues
    def add_metricValues(self, value):
        self.metricValues.append(value)
    def insert_metricValues_at(self, index, value):
        self.metricValues.insert(index, value)
    def replace_metricValues_at(self, index, value):
        self.metricValues[index] = value
    def _hasContent(self):
        if (
            self.metricDefinition is not None or
            self.metricValues
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.metricDefinition is not None:
            namespaceprefix_ = self.metricDefinition_nsprefix_ + ':' if (UseCapturedNS_ and self.metricDefinition_nsprefix_) else ''
            self.metricDefinition.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metricDefinition', pretty_print=pretty_print)
        for metricValues_ in self.metricValues:
            namespaceprefix_ = self.metricValues_nsprefix_ + ':' if (UseCapturedNS_ and self.metricValues_nsprefix_) else ''
            metricValues_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metricValues', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MetricType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.metricDefinition is not None:
            metricDefinition_ = self.metricDefinition
            metricDefinition_.to_etree(element, name_='metricDefinition', mapping_=mapping_, nsmap_=nsmap_)
        for metricValues_ in self.metricValues:
            metricValues_.to_etree(element, name_='metricValues', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.metricDefinition is not None:
            showIndent(outfile, level)
            outfile.write('metricDefinition=model_.MetricDefinitionType(\n')
            self.metricDefinition.exportLiteral(outfile, level, name_='metricDefinition')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('metricValues=[\n')
        level += 1
        for metricValues_ in self.metricValues:
            showIndent(outfile, level)
            outfile.write('model_.MetricValueType(\n')
            metricValues_.exportLiteral(outfile, level, name_='MetricValueType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'metricDefinition':
            obj_ = MetricDefinitionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metricDefinition = obj_
            obj_.original_tagname_ = 'metricDefinition'
        elif nodeName_ == 'metricValues':
            obj_ = MetricValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metricValues.append(obj_)
            obj_.original_tagname_ = 'metricValues'
