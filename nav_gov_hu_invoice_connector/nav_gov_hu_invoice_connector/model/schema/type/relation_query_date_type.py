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


class RelationQueryDateType(GeneratedsSuper):
    """RelationQueryDateType -- Kereső paraméter dátum értékekhez
    Query parameter for date values
    queryOperator -- Kereső operátor
    Query operator
    queryValue -- Kereső érték
    Query value

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, queryOperator=None, queryValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.queryOperator = queryOperator
        self.validate_QueryOperatorType(self.queryOperator)
        self.queryOperator_nsprefix_ = None
        if isinstance(queryValue, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(queryValue, '%Y-%m-%d').date()
        else:
            initvalue_ = queryValue
        self.queryValue = initvalue_
        self.queryValue_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RelationQueryDateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RelationQueryDateType.subclass:
            return RelationQueryDateType.subclass(*args_, **kwargs_)
        else:
            return RelationQueryDateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_queryOperator(self):
        return self.queryOperator
    def set_queryOperator(self, queryOperator):
        self.queryOperator = queryOperator
    def get_queryValue(self):
        return self.queryValue
    def set_queryValue(self, queryValue):
        self.queryValue = queryValue
    def validate_QueryOperatorType(self, value):
        result = True
        # Validate type QueryOperatorType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['EQ', 'GT', 'GTE', 'LT', 'LTE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on QueryOperatorType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on QueryOperatorType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on QueryOperatorType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
    def _hasContent(self):
        if (
            self.queryOperator is not None or
            self.queryValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='RelationQueryDateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RelationQueryDateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RelationQueryDateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelationQueryDateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RelationQueryDateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RelationQueryDateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='RelationQueryDateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.queryOperator is not None:
            namespaceprefix_ = self.queryOperator_nsprefix_ + ':' if (UseCapturedNS_ and self.queryOperator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squeryOperator>%s</%squeryOperator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.queryOperator), input_name='queryOperator')), namespaceprefix_ , eol_))
        if self.queryValue is not None:
            namespaceprefix_ = self.queryValue_nsprefix_ + ':' if (UseCapturedNS_ and self.queryValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squeryValue>%s</%squeryValue>%s' % (namespaceprefix_ , self.gds_format_date(self.queryValue, input_name='queryValue'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='RelationQueryDateType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.queryOperator is not None:
            queryOperator_ = self.queryOperator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}queryOperator').text = self.gds_format_string(queryOperator_)
        if self.queryValue is not None:
            queryValue_ = self.queryValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}queryValue').text = self.gds_format_date(queryValue_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='RelationQueryDateType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.queryOperator is not None:
            showIndent(outfile, level)
            outfile.write('queryOperator=%s,\n' % self.gds_encode(quote_python(self.queryOperator)))
        if self.queryValue is not None:
            showIndent(outfile, level)
            outfile.write('queryValue=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.queryValue, input_name='queryValue'))
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
        if nodeName_ == 'queryOperator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'queryOperator')
            value_ = self.gds_validate_string(value_, node, 'queryOperator')
            self.queryOperator = value_
            self.queryOperator_nsprefix_ = child_.prefix
            # validate type QueryOperatorType
            self.validate_QueryOperatorType(self.queryOperator)
        elif nodeName_ == 'queryValue':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.queryValue = dval_
            self.queryValue_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.queryValue)
