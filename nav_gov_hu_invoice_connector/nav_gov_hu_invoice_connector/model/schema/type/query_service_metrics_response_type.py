import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_result_type import \
    BasicResultType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.metric_type import MetricType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class QueryServiceMetricsResponseType(GeneratedsSuper):
    """QueryServiceMetricsResponseType -- A GET /queryServiceMetrics REST operáció válasz típusa
    Response type of the GET /queryServiceMetrics REST operation
    result -- Alap válaszeredmény adatok
    Basic result data
    metricsLastUpdateTime -- A metrikák utolsó frissítésének időpontja UTC időben
    Last update time of metrics in UTC time
    metric -- Metrika adatai
    Metric data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, result=None, metricsLastUpdateTime=None, metric=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.result = result
        self.result_nsprefix_ = "common"
        if isinstance(metricsLastUpdateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(metricsLastUpdateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = metricsLastUpdateTime
        self.metricsLastUpdateTime = initvalue_
        self.metricsLastUpdateTime_nsprefix_ = "base"
        if metric is None:
            self.metric = []
        else:
            self.metric = metric
        self.metric_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryServiceMetricsResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryServiceMetricsResponseType.subclass:
            return QueryServiceMetricsResponseType.subclass(*args_, **kwargs_)
        else:
            return QueryServiceMetricsResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_result(self):
        return self.result
    def set_result(self, result):
        self.result = result
    def get_metricsLastUpdateTime(self):
        return self.metricsLastUpdateTime
    def set_metricsLastUpdateTime(self, metricsLastUpdateTime):
        self.metricsLastUpdateTime = metricsLastUpdateTime
    def get_metric(self):
        return self.metric
    def set_metric(self, metric):
        self.metric = metric
    def add_metric(self, value):
        self.metric.append(value)
    def insert_metric_at(self, index, value):
        self.metric.insert(index, value)
    def replace_metric_at(self, index, value):
        self.metric[index] = value
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_, ))
                result = False
        return result
    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]
    def _hasContent(self):
        if (
            self.result is not None or
            self.metricsLastUpdateTime is not None or
            self.metric
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryServiceMetricsResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryServiceMetricsResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryServiceMetricsResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryServiceMetricsResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryServiceMetricsResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryServiceMetricsResponseType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryServiceMetricsResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.result is not None:
            namespaceprefix_ = self.result_nsprefix_ + ':' if (UseCapturedNS_ and self.result_nsprefix_) else ''
            self.result.export(outfile, level, namespaceprefix_, namespacedef_='', name_='result', pretty_print=pretty_print)
        if self.metricsLastUpdateTime is not None:
            namespaceprefix_ = self.metricsLastUpdateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.metricsLastUpdateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smetricsLastUpdateTime>%s</%smetricsLastUpdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.metricsLastUpdateTime, input_name='metricsLastUpdateTime'), namespaceprefix_ , eol_))
        for metric_ in self.metric:
            namespaceprefix_ = self.metric_nsprefix_ + ':' if (UseCapturedNS_ and self.metric_nsprefix_) else ''
            metric_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metric', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryServiceMetricsResponseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.result is not None:
            result_ = self.result
            result_.to_etree(element, name_='result', mapping_=mapping_, nsmap_=nsmap_)
        if self.metricsLastUpdateTime is not None:
            metricsLastUpdateTime_ = self.metricsLastUpdateTime
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}metricsLastUpdateTime').text = self.gds_format_datetime(metricsLastUpdateTime_)
        for metric_ in self.metric:
            metric_.to_etree(element, name_='metric', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryServiceMetricsResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.result is not None:
            showIndent(outfile, level)
            outfile.write('result=model_.BasicResultType(\n')
            self.result.exportLiteral(outfile, level, name_='result')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.metricsLastUpdateTime is not None:
            showIndent(outfile, level)
            outfile.write('metricsLastUpdateTime=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.metricsLastUpdateTime, input_name='metricsLastUpdateTime'))
        showIndent(outfile, level)
        outfile.write('metric=[\n')
        level += 1
        for metric_ in self.metric:
            showIndent(outfile, level)
            outfile.write('model_.MetricType(\n')
            metric_.exportLiteral(outfile, level, name_='MetricType')
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'result':
            class_obj_ = self.get_class_obj_(child_, BasicResultType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.result = obj_
            obj_.original_tagname_ = 'result'
        elif nodeName_ == 'metricsLastUpdateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.metricsLastUpdateTime = dval_
            self.metricsLastUpdateTime_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.metricsLastUpdateTime)
        elif nodeName_ == 'metric':
            obj_ = MetricType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metric.append(obj_)
            obj_.original_tagname_ = 'metric'
