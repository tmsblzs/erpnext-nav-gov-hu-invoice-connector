import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class MetricDescriptionType(GeneratedsSuper):
    """MetricDescriptionType -- Metrika leírás típus
    Metric description type
    language -- Nyelv megnevezés
    Language naming
    localizedDescription -- Lokalizált leírás
    Localized description

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, language=None, localizedDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.language = language
        self.validate_LanguageType(self.language)
        self.language_nsprefix_ = None
        self.localizedDescription = localizedDescription
        self.validate_SimpleText512NotBlankType(self.localizedDescription)
        self.localizedDescription_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricDescriptionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricDescriptionType.subclass:
            return MetricDescriptionType.subclass(*args_, **kwargs_)
        else:
            return MetricDescriptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_language(self):
        return self.language
    def set_language(self, language):
        self.language = language
    def get_localizedDescription(self):
        return self.localizedDescription
    def set_localizedDescription(self, localizedDescription):
        self.localizedDescription = localizedDescription
    def validate_LanguageType(self, value):
        result = True
        # Validate type LanguageType, a restriction on common:AtomicStringType2.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['HU', 'EN', 'DE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LanguageType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LanguageType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LanguageType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.language is not None or
            self.localizedDescription is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MetricDescriptionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricDescriptionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricDescriptionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricDescriptionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricDescriptionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricDescriptionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MetricDescriptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.language is not None:
            namespaceprefix_ = self.language_nsprefix_ + ':' if (UseCapturedNS_ and self.language_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slanguage>%s</%slanguage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.language), input_name='language')), namespaceprefix_ , eol_))
        if self.localizedDescription is not None:
            namespaceprefix_ = self.localizedDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.localizedDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocalizedDescription>%s</%slocalizedDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.localizedDescription), input_name='localizedDescription')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='MetricDescriptionType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.language is not None:
            language_ = self.language
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}language').text = self.gds_format_string(language_)
        if self.localizedDescription is not None:
            localizedDescription_ = self.localizedDescription
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}localizedDescription').text = self.gds_format_string(localizedDescription_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricDescriptionType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.language is not None:
            showIndent(outfile, level)
            outfile.write('language=%s,\n' % self.gds_encode(quote_python(self.language)))
        if self.localizedDescription is not None:
            showIndent(outfile, level)
            outfile.write('localizedDescription=%s,\n' % self.gds_encode(quote_python(self.localizedDescription)))
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
        if nodeName_ == 'language':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'language')
            value_ = self.gds_validate_string(value_, node, 'language')
            self.language = value_
            self.language_nsprefix_ = child_.prefix
            # validate type LanguageType
            self.validate_LanguageType(self.language)
        elif nodeName_ == 'localizedDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'localizedDescription')
            value_ = self.gds_validate_string(value_, node, 'localizedDescription')
            self.localizedDescription = value_
            self.localizedDescription_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.localizedDescription)
