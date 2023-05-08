import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class MetricValueType(GeneratedsSuper):
    """MetricValueType -- Metrika érték típus
    Metric value type
    value -- Metrika értéke
    Metric's value
    timestamp -- Metrika értékének időpontja UTC időben
    Time of metric value in UTC time

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, value=None, timestamp=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.validate_GenericDecimalType(self.value)
        self.value_nsprefix_ = "common"
        if isinstance(timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = timestamp
        self.timestamp = initvalue_
        self.timestamp_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricValueType.subclass:
            return MetricValueType.subclass(*args_, **kwargs_)
        else:
            return MetricValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_timestamp(self):
        return self.timestamp
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
    def validate_GenericDecimalType(self, value):
        result = True
        # Validate type GenericDecimalType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
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
            self.value is not None or
            self.timestamp is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='MetricValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricValueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='MetricValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_format_decimal(self.value, input_name='value'), namespaceprefix_ , eol_))
        if self.timestamp is not None:
            namespaceprefix_ = self.timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stimestamp>%s</%stimestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.timestamp, input_name='timestamp'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='MetricValueType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}value').text = self.gds_format_decimal(value_)
        if self.timestamp is not None:
            timestamp_ = self.timestamp
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}timestamp').text = self.gds_format_datetime(timestamp_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricValueType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.value is not None:
            showIndent(outfile, level)
            outfile.write('value=%f,\n' % self.value)
        if self.timestamp is not None:
            showIndent(outfile, level)
            outfile.write('timestamp=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
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
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'value')
            fval_ = self.gds_validate_decimal(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
            # validate type GenericDecimalType
            self.validate_GenericDecimalType(self.value)
        elif nodeName_ == 'timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.timestamp = dval_
            self.timestamp_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.timestamp)
