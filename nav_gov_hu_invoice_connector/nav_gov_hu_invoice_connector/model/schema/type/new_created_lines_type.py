from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, raise_parse_error

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class NewCreatedLinesType(GeneratedsSuper):
    """NewCreatedLinesType -- A módosító okirat által újként létrehozott számlasorok
    New invoice lines created by the modification document
    lineNumberIntervalStart -- Számla sor intervallum kezdete
            Invoice line interval start
    lineNumberIntervalEnd -- Számla sor intervallum vége (inkluzív)
            Invoice line interval end (inclusive)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, lineNumberIntervalStart=None, lineNumberIntervalEnd=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNumberIntervalStart = lineNumberIntervalStart
        self.validate_LineNumberType(self.lineNumberIntervalStart)
        self.lineNumberIntervalStart_nsprefix_ = "base"
        self.lineNumberIntervalEnd = lineNumberIntervalEnd
        self.validate_LineNumberType(self.lineNumberIntervalEnd)
        self.lineNumberIntervalEnd_nsprefix_ = "base"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NewCreatedLinesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NewCreatedLinesType.subclass:
            return NewCreatedLinesType.subclass(*args_, **kwargs_)
        else:
            return NewCreatedLinesType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_lineNumberIntervalStart(self):
        return self.lineNumberIntervalStart

    def set_lineNumberIntervalStart(self, lineNumberIntervalStart):
        self.lineNumberIntervalStart = lineNumberIntervalStart

    def get_lineNumberIntervalEnd(self):
        return self.lineNumberIntervalEnd

    def set_lineNumberIntervalEnd(self, lineNumberIntervalEnd):
        self.lineNumberIntervalEnd = lineNumberIntervalEnd

    def validate_LineNumberType(self, value):
        result = True
        # Validate type LineNumberType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on LineNumberType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on LineNumberType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.lineNumberIntervalStart is not None or
                self.lineNumberIntervalEnd is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
               name_='NewCreatedLinesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NewCreatedLinesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NewCreatedLinesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NewCreatedLinesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NewCreatedLinesType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NewCreatedLinesType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
                        name_='NewCreatedLinesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNumberIntervalStart is not None:
            namespaceprefix_ = self.lineNumberIntervalStart_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.lineNumberIntervalStart_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNumberIntervalStart>%s</%slineNumberIntervalStart>%s' % (namespaceprefix_,
                                                                                           self.gds_format_integer(
                                                                                               self.lineNumberIntervalStart,
                                                                                               input_name='lineNumberIntervalStart'),
                                                                                           namespaceprefix_, eol_))
        if self.lineNumberIntervalEnd is not None:
            namespaceprefix_ = self.lineNumberIntervalEnd_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.lineNumberIntervalEnd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNumberIntervalEnd>%s</%slineNumberIntervalEnd>%s' % (
            namespaceprefix_, self.gds_format_integer(self.lineNumberIntervalEnd, input_name='lineNumberIntervalEnd'),
            namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='NewCreatedLinesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.lineNumberIntervalStart is not None:
            lineNumberIntervalStart_ = self.lineNumberIntervalStart
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}lineNumberIntervalStart').text = self.gds_format_integer(
                lineNumberIntervalStart_)
        if self.lineNumberIntervalEnd is not None:
            lineNumberIntervalEnd_ = self.lineNumberIntervalEnd
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}lineNumberIntervalEnd').text = self.gds_format_integer(
                lineNumberIntervalEnd_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='NewCreatedLinesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNumberIntervalStart is not None:
            showIndent(outfile, level)
            outfile.write('lineNumberIntervalStart=%d,\n' % self.lineNumberIntervalStart)
        if self.lineNumberIntervalEnd is not None:
            showIndent(outfile, level)
            outfile.write('lineNumberIntervalEnd=%d,\n' % self.lineNumberIntervalEnd)

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
        if nodeName_ == 'lineNumberIntervalStart' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'lineNumberIntervalStart')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'lineNumberIntervalStart')
            self.lineNumberIntervalStart = ival_
            self.lineNumberIntervalStart_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.lineNumberIntervalStart)
        elif nodeName_ == 'lineNumberIntervalEnd' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'lineNumberIntervalEnd')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'lineNumberIntervalEnd')
            self.lineNumberIntervalEnd = ival_
            self.lineNumberIntervalEnd_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.lineNumberIntervalEnd)
