import datetime as datetime_

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class DateTimeIntervalParamType(GeneratedsSuper):
    """DateTimeIntervalParamType -- Időpontos számla kereső paraméter
    Datestamp query params of invoice
    dateTimeFrom -- Időpontos intervallum nagyobb vagy egyenlő paramétere UTC idő szerint
            Datetime interval greater or equals parameter
    dateTimeTo -- Idő pontos intervallum kisebb vagy egyenlő paramétere UTC idő szerint
            Datetime interval less or equals parameter

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, dateTimeFrom=None, dateTimeTo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(dateTimeFrom, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTimeFrom, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTimeFrom
        self.dateTimeFrom = initvalue_
        self.dateTimeFrom_nsprefix_ = "base"
        if isinstance(dateTimeTo, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTimeTo, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTimeTo
        self.dateTimeTo = initvalue_
        self.dateTimeTo_nsprefix_ = "base"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DateTimeIntervalParamType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DateTimeIntervalParamType.subclass:
            return DateTimeIntervalParamType.subclass(*args_, **kwargs_)
        else:
            return DateTimeIntervalParamType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_dateTimeFrom(self):
        return self.dateTimeFrom

    def set_dateTimeFrom(self, dateTimeFrom):
        self.dateTimeFrom = dateTimeFrom

    def get_dateTimeTo(self):
        return self.dateTimeTo

    def set_dateTimeTo(self, dateTimeTo):
        self.dateTimeTo = dateTimeTo

    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_,))
                result = False
        return result

    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]

    def _hasContent(self):
        if (
                self.dateTimeFrom is not None or
                self.dateTimeTo is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
               name_='DateTimeIntervalParamType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DateTimeIntervalParamType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DateTimeIntervalParamType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DateTimeIntervalParamType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DateTimeIntervalParamType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='DateTimeIntervalParamType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
                        name_='DateTimeIntervalParamType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dateTimeFrom is not None:
            namespaceprefix_ = self.dateTimeFrom_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.dateTimeFrom_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTimeFrom>%s</%sdateTimeFrom>%s' % (
            namespaceprefix_, self.gds_format_datetime(self.dateTimeFrom, input_name='dateTimeFrom'), namespaceprefix_,
            eol_))
        if self.dateTimeTo is not None:
            namespaceprefix_ = self.dateTimeTo_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTimeTo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTimeTo>%s</%sdateTimeTo>%s' % (
            namespaceprefix_, self.gds_format_datetime(self.dateTimeTo, input_name='dateTimeTo'), namespaceprefix_,
            eol_))

    def to_etree(self, parent_element=None, name_='DateTimeIntervalParamType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.dateTimeFrom is not None:
            dateTimeFrom_ = self.dateTimeFrom
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}dateTimeFrom').text = self.gds_format_datetime(
                dateTimeFrom_)
        if self.dateTimeTo is not None:
            dateTimeTo_ = self.dateTimeTo
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}dateTimeTo').text = self.gds_format_datetime(
                dateTimeTo_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='DateTimeIntervalParamType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.dateTimeFrom is not None:
            showIndent(outfile, level)
            outfile.write('dateTimeFrom=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(
                self.dateTimeFrom, input_name='dateTimeFrom'))
        if self.dateTimeTo is not None:
            showIndent(outfile, level)
            outfile.write('dateTimeTo=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(
                self.dateTimeTo, input_name='dateTimeTo'))

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
        if nodeName_ == 'dateTimeFrom':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTimeFrom = dval_
            self.dateTimeFrom_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.dateTimeFrom)
        elif nodeName_ == 'dateTimeTo':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTimeTo = dval_
            self.dateTimeTo_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.dateTimeTo)
