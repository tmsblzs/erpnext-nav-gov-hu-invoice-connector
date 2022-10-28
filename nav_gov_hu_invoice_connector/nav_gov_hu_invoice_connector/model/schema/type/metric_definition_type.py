import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.metric_description_type import \
    MetricDescriptionType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class MetricDefinitionType(GeneratedsSuper):
    """MetricDefinitionType -- Metrika definíciótípus
    Metric definition type
    metricName -- Metrika neve
    Metric's name
    metricType -- Metrika típusa
    Metric's type
    metricDescription -- Metrika leírása
    Metric's description

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, metricName=None, metricType=None, metricDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.metricName = metricName
        self.validate_SimpleText200NotBlankType(self.metricName)
        self.metricName_nsprefix_ = "common"
        self.metricType = metricType
        self.validate_MetricTypeType(self.metricType)
        self.metricType_nsprefix_ = None
        if metricDescription is None:
            self.metricDescription = []
        else:
            self.metricDescription = metricDescription
        self.metricDescription_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricDefinitionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricDefinitionType.subclass:
            return MetricDefinitionType.subclass(*args_, **kwargs_)
        else:
            return MetricDefinitionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_metricName(self):
        return self.metricName
    def set_metricName(self, metricName):
        self.metricName = metricName
    def get_metricType(self):
        return self.metricType
    def set_metricType(self, metricType):
        self.metricType = metricType
    def get_metricDescription(self):
        return self.metricDescription
    def set_metricDescription(self, metricDescription):
        self.metricDescription = metricDescription
    def add_metricDescription(self, value):
        self.metricDescription.append(value)
    def insert_metricDescription_at(self, index, value):
        self.metricDescription.insert(index, value)
    def replace_metricDescription_at(self, index, value):
        self.metricDescription[index] = value
    def validate_SimpleText200NotBlankType(self, value):
        result = True
        # Validate type SimpleText200NotBlankType, a restriction on AtomicStringType200.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText200NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText200NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText200NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText200NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText200NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_MetricTypeType(self, value):
        result = True
        # Validate type MetricTypeType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['COUNTER', 'GAUGE', 'HISTOGRAM', 'SUMMARY']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on MetricTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on MetricTypeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on MetricTypeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.metricName is not None or
            self.metricType is not None or
            self.metricDescription
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricDefinitionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricDefinitionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricDefinitionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricDefinitionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricDefinitionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricDefinitionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricDefinitionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.metricName is not None:
            namespaceprefix_ = self.metricName_nsprefix_ + ':' if (UseCapturedNS_ and self.metricName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smetricName>%s</%smetricName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.metricName), input_name='metricName')), namespaceprefix_ , eol_))
        if self.metricType is not None:
            namespaceprefix_ = self.metricType_nsprefix_ + ':' if (UseCapturedNS_ and self.metricType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smetricType>%s</%smetricType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.metricType), input_name='metricType')), namespaceprefix_ , eol_))
        for metricDescription_ in self.metricDescription:
            namespaceprefix_ = self.metricDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.metricDescription_nsprefix_) else ''
            metricDescription_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metricDescription', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MetricDefinitionType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.metricName is not None:
            metricName_ = self.metricName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}metricName').text = self.gds_format_string(metricName_)
        if self.metricType is not None:
            metricType_ = self.metricType
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}metricType').text = self.gds_format_string(metricType_)
        for metricDescription_ in self.metricDescription:
            metricDescription_.to_etree(element, name_='metricDescription', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricDefinitionType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.metricName is not None:
            showIndent(outfile, level)
            outfile.write('metricName=%s,\n' % self.gds_encode(quote_python(self.metricName)))
        if self.metricType is not None:
            showIndent(outfile, level)
            outfile.write('metricType=%s,\n' % self.gds_encode(quote_python(self.metricType)))
        showIndent(outfile, level)
        outfile.write('metricDescription=[\n')
        level += 1
        for metricDescription_ in self.metricDescription:
            showIndent(outfile, level)
            outfile.write('model_.MetricDescriptionType(\n')
            metricDescription_.exportLiteral(outfile, level, name_='MetricDescriptionType')
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
        if nodeName_ == 'metricName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'metricName')
            value_ = self.gds_validate_string(value_, node, 'metricName')
            self.metricName = value_
            self.metricName_nsprefix_ = child_.prefix
            # validate type SimpleText200NotBlankType
            self.validate_SimpleText200NotBlankType(self.metricName)
        elif nodeName_ == 'metricType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'metricType')
            value_ = self.gds_validate_string(value_, node, 'metricType')
            self.metricType = value_
            self.metricType_nsprefix_ = child_.prefix
            # validate type MetricTypeType
            self.validate_MetricTypeType(self.metricType)
        elif nodeName_ == 'metricDescription':
            obj_ = MetricDescriptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metricDescription.append(obj_)
            obj_.original_tagname_ = 'metricDescription'