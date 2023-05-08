import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AdditionalDataType(GeneratedsSuper):
    """AdditionalDataType -- További adat leírására szolgáló típus
    Type for additional data description
    dataName -- Az adatmező egyedi azonosítója
    Unique identification of the data field
    dataDescription -- Az adatmező tartalmának szöveges leírása
    Description of content of the data field
    dataValue -- Az adat értéke
    Value of the data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, dataName=None, dataDescription=None, dataValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.dataName = dataName
        self.validate_DataNameType(self.dataName)
        self.dataName_nsprefix_ = None
        self.dataDescription = dataDescription
        self.validate_SimpleText255NotBlankType(self.dataDescription)
        self.dataDescription_nsprefix_ = "common"
        self.dataValue = dataValue
        self.validate_SimpleText512NotBlankType(self.dataValue)
        self.dataValue_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdditionalDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdditionalDataType.subclass:
            return AdditionalDataType.subclass(*args_, **kwargs_)
        else:
            return AdditionalDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_dataName(self):
        return self.dataName
    def set_dataName(self, dataName):
        self.dataName = dataName
    def get_dataDescription(self):
        return self.dataDescription
    def set_dataDescription(self, dataDescription):
        self.dataDescription = dataDescription
    def get_dataValue(self):
        return self.dataValue
    def set_dataValue(self, dataValue):
        self.dataValue = dataValue
    def validate_DataNameType(self, value):
        result = True
        # Validate type DataNameType, a restriction on common:AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on DataNameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on DataNameType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on DataNameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on DataNameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_DataNameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_DataNameType_patterns_, ))
                result = False
        return result
    validate_DataNameType_patterns_ = [['^([A-Z][0-9]{5}[_][_A-Z0-9]{1,249})$']]
    def validate_SimpleText255NotBlankType(self, value):
        result = True
        # Validate type SimpleText255NotBlankType, a restriction on AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText255NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText255NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText255NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText255NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText255NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
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
            self.dataName is not None or
            self.dataDescription is not None or
            self.dataValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='AdditionalDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdditionalDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdditionalDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdditionalDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdditionalDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdditionalDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='AdditionalDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dataName is not None:
            namespaceprefix_ = self.dataName_nsprefix_ + ':' if (UseCapturedNS_ and self.dataName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdataName>%s</%sdataName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dataName), input_name='dataName')), namespaceprefix_ , eol_))
        if self.dataDescription is not None:
            namespaceprefix_ = self.dataDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.dataDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdataDescription>%s</%sdataDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dataDescription), input_name='dataDescription')), namespaceprefix_ , eol_))
        if self.dataValue is not None:
            namespaceprefix_ = self.dataValue_nsprefix_ + ':' if (UseCapturedNS_ and self.dataValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdataValue>%s</%sdataValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dataValue), input_name='dataValue')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AdditionalDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.dataName is not None:
            dataName_ = self.dataName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}dataName').text = self.gds_format_string(dataName_)
        if self.dataDescription is not None:
            dataDescription_ = self.dataDescription
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}dataDescription').text = self.gds_format_string(dataDescription_)
        if self.dataValue is not None:
            dataValue_ = self.dataValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}dataValue').text = self.gds_format_string(dataValue_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AdditionalDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.dataName is not None:
            showIndent(outfile, level)
            outfile.write('dataName=%s,\n' % self.gds_encode(quote_python(self.dataName)))
        if self.dataDescription is not None:
            showIndent(outfile, level)
            outfile.write('dataDescription=%s,\n' % self.gds_encode(quote_python(self.dataDescription)))
        if self.dataValue is not None:
            showIndent(outfile, level)
            outfile.write('dataValue=%s,\n' % self.gds_encode(quote_python(self.dataValue)))
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
        if nodeName_ == 'dataName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dataName')
            value_ = self.gds_validate_string(value_, node, 'dataName')
            self.dataName = value_
            self.dataName_nsprefix_ = child_.prefix
            # validate type DataNameType
            self.validate_DataNameType(self.dataName)
        elif nodeName_ == 'dataDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dataDescription')
            value_ = self.gds_validate_string(value_, node, 'dataDescription')
            self.dataDescription = value_
            self.dataDescription_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.dataDescription)
        elif nodeName_ == 'dataValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dataValue')
            value_ = self.gds_validate_string(value_, node, 'dataValue')
            self.dataValue = value_
            self.dataValue_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.dataValue)
