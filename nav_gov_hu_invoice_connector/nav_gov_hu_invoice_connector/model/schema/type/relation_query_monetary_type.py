import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class RelationQueryMonetaryType(GeneratedsSuper):
    """RelationQueryMonetaryType -- Kereső paraméter monetáris értékekhez
    Query parameter for monetary values
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
        self.queryValue = queryValue
        self.validate_MonetaryType(self.queryValue)
        self.queryValue_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RelationQueryMonetaryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RelationQueryMonetaryType.subclass:
            return RelationQueryMonetaryType.subclass(*args_, **kwargs_)
        else:
            return RelationQueryMonetaryType(*args_, **kwargs_)
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
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.queryOperator is not None or
            self.queryValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='RelationQueryMonetaryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RelationQueryMonetaryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RelationQueryMonetaryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelationQueryMonetaryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RelationQueryMonetaryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RelationQueryMonetaryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='RelationQueryMonetaryType', fromsubclass_=False, pretty_print=True):
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
            outfile.write('<%squeryValue>%s</%squeryValue>%s' % (namespaceprefix_ , self.gds_format_decimal(self.queryValue, input_name='queryValue'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='RelationQueryMonetaryType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.queryOperator is not None:
            queryOperator_ = self.queryOperator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}queryOperator').text = self.gds_format_string(queryOperator_)
        if self.queryValue is not None:
            queryValue_ = self.queryValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}queryValue').text = self.gds_format_decimal(queryValue_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='RelationQueryMonetaryType'):
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
            outfile.write('queryValue=%f,\n' % self.queryValue)
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
        elif nodeName_ == 'queryValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'queryValue')
            fval_ = self.gds_validate_decimal(fval_, node, 'queryValue')
            self.queryValue = fval_
            self.queryValue_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.queryValue)
