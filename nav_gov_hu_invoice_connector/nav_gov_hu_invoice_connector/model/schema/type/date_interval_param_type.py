import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class DateIntervalParamType(GeneratedsSuper):
    """DateIntervalParamType -- Dátumos számla kereső paraméter
    Date query params of invoice
    dateFrom -- Dátum intervallum nagyobb vagy egyenlő paramétere
            Date interval greater or equals parameter
    dateTo -- Dátum intervallum kisebb vagy egyenlő paramétere
            Date interval less or equals parameter

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, dateFrom=None, dateTo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(dateFrom, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateFrom, '%Y-%m-%d').date()
        else:
            initvalue_ = dateFrom
        self.dateFrom = initvalue_
        self.dateFrom_nsprefix_ = "base"
        if isinstance(dateTo, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTo, '%Y-%m-%d').date()
        else:
            initvalue_ = dateTo
        self.dateTo = initvalue_
        self.dateTo_nsprefix_ = "base"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DateIntervalParamType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DateIntervalParamType.subclass:
            return DateIntervalParamType.subclass(*args_, **kwargs_)
        else:
            return DateIntervalParamType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_dateFrom(self):
        return self.dateFrom

    def set_dateFrom(self, dateFrom):
        self.dateFrom = dateFrom

    def get_dateTo(self):
        return self.dateTo

    def set_dateTo(self, dateTo):
        self.dateTo = dateTo

    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_InvoiceDateType_patterns_,))
                result = False
        return result

    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]

    def _hasContent(self):
        if (
                self.dateFrom is not None or
                self.dateTo is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
               name_='DateIntervalParamType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DateIntervalParamType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DateIntervalParamType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DateIntervalParamType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DateIntervalParamType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DateIntervalParamType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
                        name_='DateIntervalParamType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dateFrom is not None:
            namespaceprefix_ = self.dateFrom_nsprefix_ + ':' if (UseCapturedNS_ and self.dateFrom_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateFrom>%s</%sdateFrom>%s' % (
            namespaceprefix_, self.gds_format_date(self.dateFrom, input_name='dateFrom'), namespaceprefix_, eol_))
        if self.dateTo is not None:
            namespaceprefix_ = self.dateTo_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTo>%s</%sdateTo>%s' % (
            namespaceprefix_, self.gds_format_date(self.dateTo, input_name='dateTo'), namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='DateIntervalParamType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.dateFrom is not None:
            dateFrom_ = self.dateFrom
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}dateFrom').text = self.gds_format_date(
                dateFrom_)
        if self.dateTo is not None:
            dateTo_ = self.dateTo
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}dateTo').text = self.gds_format_date(
                dateTo_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='DateIntervalParamType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.dateFrom is not None:
            showIndent(outfile, level)
            outfile.write(
                'dateFrom=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.dateFrom,
                                                                                                 input_name='dateFrom'))
        if self.dateTo is not None:
            showIndent(outfile, level)
            outfile.write('dateTo=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.dateTo,
                                                                                                         input_name='dateTo'))

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
        if nodeName_ == 'dateFrom':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dateFrom = dval_
            self.dateFrom_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.dateFrom)
        elif nodeName_ == 'dateTo':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dateTo = dval_
            self.dateTo_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.dateTo)
