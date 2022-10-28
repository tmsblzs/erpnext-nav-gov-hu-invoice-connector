import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.line_type import LineType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class LinesType(GeneratedsSuper):
    """LinesType -- Termék/szolgáltatás tételek
    Product / service items
    mergedItemIndicator -- Jelöli, ha az adatszolgáltatás méretcsökkentés miatt összevont soradatokat tartalmaz
    Indicates whether the data exchange contains merged line data due to size reduction
    line -- Termék/szolgáltatás tétel
    Product / service item

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, mergedItemIndicator=None, line=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.mergedItemIndicator = mergedItemIndicator
        self.mergedItemIndicator_nsprefix_ = "xs"
        if line is None:
            self.line = []
        else:
            self.line = line
        self.line_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LinesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LinesType.subclass:
            return LinesType.subclass(*args_, **kwargs_)
        else:
            return LinesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_mergedItemIndicator(self):
        return self.mergedItemIndicator
    def set_mergedItemIndicator(self, mergedItemIndicator):
        self.mergedItemIndicator = mergedItemIndicator
    def get_line(self):
        return self.line
    def set_line(self, line):
        self.line = line
    def add_line(self, value):
        self.line.append(value)
    def insert_line_at(self, index, value):
        self.line.insert(index, value)
    def replace_line_at(self, index, value):
        self.line[index] = value
    def _hasContent(self):
        if (
            self.mergedItemIndicator is not None or
            self.line
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LinesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LinesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LinesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LinesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LinesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LinesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LinesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.mergedItemIndicator is not None:
            namespaceprefix_ = self.mergedItemIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.mergedItemIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smergedItemIndicator>%s</%smergedItemIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.mergedItemIndicator, input_name='mergedItemIndicator'), namespaceprefix_ , eol_))
        for line_ in self.line:
            namespaceprefix_ = self.line_nsprefix_ + ':' if (UseCapturedNS_ and self.line_nsprefix_) else ''
            line_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='line', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LinesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.mergedItemIndicator is not None:
            mergedItemIndicator_ = self.mergedItemIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}mergedItemIndicator').text = self.gds_format_boolean(mergedItemIndicator_)
        for line_ in self.line:
            line_.to_etree(element, name_='line', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LinesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.mergedItemIndicator is not None:
            showIndent(outfile, level)
            outfile.write('mergedItemIndicator=%s,\n' % self.mergedItemIndicator)
        showIndent(outfile, level)
        outfile.write('line=[\n')
        level += 1
        for line_ in self.line:
            showIndent(outfile, level)
            outfile.write('model_.LineType(\n')
            line_.exportLiteral(outfile, level, name_='LineType')
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
        if nodeName_ == 'mergedItemIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'mergedItemIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'mergedItemIndicator')
            self.mergedItemIndicator = ival_
            self.mergedItemIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'line':
            obj_ = LineType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.line.append(obj_)
            obj_.original_tagname_ = 'line'
