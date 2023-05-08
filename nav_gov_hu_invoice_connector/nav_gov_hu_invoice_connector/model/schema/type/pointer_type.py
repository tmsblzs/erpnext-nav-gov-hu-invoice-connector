from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, raise_parse_error

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class PointerType(GeneratedsSuper):
    """PointerType -- Feldolgozási kurzor adatok
    Processing cursor data
    tag -- Tag hivatkozás
            Tag reference
    value -- Érték hivatkozás
            Value reference
    line -- Sorhivatkozás
            Line reference
    originalInvoiceNumber -- Kötegelt számla művelet esetén az eredeti számla sorszáma, melyre a módosítás vonatkozik
            In case of a batch operation, the sequence number of the original invoice, on which the modification occurs

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, tag=None, value=None, line=None, originalInvoiceNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.tag = tag
        self.validate_SimpleText1024NotBlankType(self.tag)
        self.tag_nsprefix_ = "common"
        self.value = value
        self.validate_SimpleText1024NotBlankType(self.value)
        self.value_nsprefix_ = "common"
        self.line = line
        self.validate_LineNumberType(self.line)
        self.line_nsprefix_ = "base"
        self.originalInvoiceNumber = originalInvoiceNumber
        self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
        self.originalInvoiceNumber_nsprefix_ = "common"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PointerType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PointerType.subclass:
            return PointerType.subclass(*args_, **kwargs_)
        else:
            return PointerType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        self.tag = tag

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_line(self):
        return self.line

    def set_line(self, line):
        self.line = line

    def get_originalInvoiceNumber(self):
        return self.originalInvoiceNumber

    def set_originalInvoiceNumber(self, originalInvoiceNumber):
        self.originalInvoiceNumber = originalInvoiceNumber

    def validate_SimpleText1024NotBlankType(self, value):
        result = True
        # Validate type SimpleText1024NotBlankType, a restriction on AtomicStringType1024.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 1024:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText1024NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText1024NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText1024NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText1024NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText1024NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

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

    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def _hasContent(self):
        if (
                self.tag is not None or
                self.value is not None or
                self.line is not None or
                self.originalInvoiceNumber is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
               name_='PointerType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PointerType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PointerType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PointerType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PointerType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PointerType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
                        name_='PointerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tag is not None:
            namespaceprefix_ = self.tag_nsprefix_ + ':' if (UseCapturedNS_ and self.tag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stag>%s</%stag>%s' % (
            namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.tag), input_name='tag')),
            namespaceprefix_, eol_))
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
            namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.value), input_name='value')),
            namespaceprefix_, eol_))
        if self.line is not None:
            namespaceprefix_ = self.line_nsprefix_ + ':' if (UseCapturedNS_ and self.line_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sline>%s</%sline>%s' % (
            namespaceprefix_, self.gds_format_integer(self.line, input_name='line'), namespaceprefix_, eol_))
        if self.originalInvoiceNumber is not None:
            namespaceprefix_ = self.originalInvoiceNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.originalInvoiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalInvoiceNumber>%s</%soriginalInvoiceNumber>%s' % (namespaceprefix_,
                                                                                       self.gds_encode(
                                                                                           self.gds_format_string(
                                                                                               quote_xml(
                                                                                                   self.originalInvoiceNumber),
                                                                                               input_name='originalInvoiceNumber')),
                                                                                       namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='PointerType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.tag is not None:
            tag_ = self.tag
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}tag').text = self.gds_format_string(tag_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}value').text = self.gds_format_string(
                value_)
        if self.line is not None:
            line_ = self.line
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}line').text = self.gds_format_integer(
                line_)
        if self.originalInvoiceNumber is not None:
            originalInvoiceNumber_ = self.originalInvoiceNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber').text = self.gds_format_string(
                originalInvoiceNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='PointerType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.tag is not None:
            showIndent(outfile, level)
            outfile.write('tag=%s,\n' % self.gds_encode(quote_python(self.tag)))
        if self.value is not None:
            showIndent(outfile, level)
            outfile.write('value=%s,\n' % self.gds_encode(quote_python(self.value)))
        if self.line is not None:
            showIndent(outfile, level)
            outfile.write('line=%d,\n' % self.line)
        if self.originalInvoiceNumber is not None:
            showIndent(outfile, level)
            outfile.write('originalInvoiceNumber=%s,\n' % self.gds_encode(quote_python(self.originalInvoiceNumber)))

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
        if nodeName_ == 'tag':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tag')
            value_ = self.gds_validate_string(value_, node, 'tag')
            self.tag = value_
            self.tag_nsprefix_ = child_.prefix
            # validate type SimpleText1024NotBlankType
            self.validate_SimpleText1024NotBlankType(self.tag)
        elif nodeName_ == 'value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'value')
            value_ = self.gds_validate_string(value_, node, 'value')
            self.value = value_
            self.value_nsprefix_ = child_.prefix
            # validate type SimpleText1024NotBlankType
            self.validate_SimpleText1024NotBlankType(self.value)
        elif nodeName_ == 'line' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'line')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'line')
            self.line = ival_
            self.line_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.line)
        elif nodeName_ == 'originalInvoiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalInvoiceNumber')
            value_ = self.gds_validate_string(value_, node, 'originalInvoiceNumber')
            self.originalInvoiceNumber = value_
            self.originalInvoiceNumber_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
