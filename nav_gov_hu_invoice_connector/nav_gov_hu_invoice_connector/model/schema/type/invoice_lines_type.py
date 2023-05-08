from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, raise_parse_error
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.new_created_lines_type import \
    NewCreatedLinesType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class InvoiceLinesType(GeneratedsSuper):
    """InvoiceLinesType -- A számlán vagy módosító okiraton szereplő tételek kivonatos adatai
    Product/service digest data appearing on the invoice or the modification document
    maxLineNumber -- A sorok száma közül a legmagasabb, amit a számla tartalmaz
            The highest line number value the invoice contains
    newCreatedLines -- A módosító okirat által újként létrehozott számlasorok
            New invoice lines created by the modification document

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, maxLineNumber=None, newCreatedLines=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.maxLineNumber = maxLineNumber
        self.validate_LineNumberType(self.maxLineNumber)
        self.maxLineNumber_nsprefix_ = "base"
        if newCreatedLines is None:
            self.newCreatedLines = []
        else:
            self.newCreatedLines = newCreatedLines
        self.newCreatedLines_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceLinesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceLinesType.subclass:
            return InvoiceLinesType.subclass(*args_, **kwargs_)
        else:
            return InvoiceLinesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_maxLineNumber(self):
        return self.maxLineNumber
    def set_maxLineNumber(self, maxLineNumber):
        self.maxLineNumber = maxLineNumber
    def get_newCreatedLines(self):
        return self.newCreatedLines
    def set_newCreatedLines(self, newCreatedLines):
        self.newCreatedLines = newCreatedLines
    def add_newCreatedLines(self, value):
        self.newCreatedLines.append(value)
    def insert_newCreatedLines_at(self, index, value):
        self.newCreatedLines.insert(index, value)
    def replace_newCreatedLines_at(self, index, value):
        self.newCreatedLines[index] = value
    def validate_LineNumberType(self, value):
        result = True
        # Validate type LineNumberType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.maxLineNumber is not None or
            self.newCreatedLines
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceLinesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceLinesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceLinesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceLinesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceLinesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceLinesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceLinesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.maxLineNumber is not None:
            namespaceprefix_ = self.maxLineNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.maxLineNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smaxLineNumber>%s</%smaxLineNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.maxLineNumber, input_name='maxLineNumber'), namespaceprefix_ , eol_))
        for newCreatedLines_ in self.newCreatedLines:
            namespaceprefix_ = self.newCreatedLines_nsprefix_ + ':' if (UseCapturedNS_ and self.newCreatedLines_nsprefix_) else ''
            newCreatedLines_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='newCreatedLines', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InvoiceLinesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.maxLineNumber is not None:
            maxLineNumber_ = self.maxLineNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}maxLineNumber').text = self.gds_format_integer(maxLineNumber_)
        for newCreatedLines_ in self.newCreatedLines:
            newCreatedLines_.to_etree(element, name_='newCreatedLines', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='InvoiceLinesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.maxLineNumber is not None:
            showIndent(outfile, level)
            outfile.write('maxLineNumber=%d,\n' % self.maxLineNumber)
        showIndent(outfile, level)
        outfile.write('newCreatedLines=[\n')
        level += 1
        for newCreatedLines_ in self.newCreatedLines:
            showIndent(outfile, level)
            outfile.write('model_.NewCreatedLinesType(\n')
            newCreatedLines_.exportLiteral(outfile, level, name_='NewCreatedLinesType')
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
        if nodeName_ == 'maxLineNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'maxLineNumber')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'maxLineNumber')
            self.maxLineNumber = ival_
            self.maxLineNumber_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.maxLineNumber)
        elif nodeName_ == 'newCreatedLines':
            obj_ = NewCreatedLinesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.newCreatedLines.append(obj_)
            obj_.original_tagname_ = 'newCreatedLines'
