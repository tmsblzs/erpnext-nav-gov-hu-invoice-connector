import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class SupplierCompanyCodesType(GeneratedsSuper):
    """SupplierCompanyCodesType -- Az eladó vállalati kódjai
    Company codes of the supplier
    supplierCompanyCode -- Az eladó vállalati kódja
    Company code of the supplier

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, supplierCompanyCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if supplierCompanyCode is None:
            self.supplierCompanyCode = []
        else:
            self.supplierCompanyCode = supplierCompanyCode
        self.supplierCompanyCode_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SupplierCompanyCodesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SupplierCompanyCodesType.subclass:
            return SupplierCompanyCodesType.subclass(*args_, **kwargs_)
        else:
            return SupplierCompanyCodesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_supplierCompanyCode(self):
        return self.supplierCompanyCode
    def set_supplierCompanyCode(self, supplierCompanyCode):
        self.supplierCompanyCode = supplierCompanyCode
    def add_supplierCompanyCode(self, value):
        self.supplierCompanyCode.append(value)
    def insert_supplierCompanyCode_at(self, index, value):
        self.supplierCompanyCode.insert(index, value)
    def replace_supplierCompanyCode_at(self, index, value):
        self.supplierCompanyCode[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.supplierCompanyCode
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='SupplierCompanyCodesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SupplierCompanyCodesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SupplierCompanyCodesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SupplierCompanyCodesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SupplierCompanyCodesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SupplierCompanyCodesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='SupplierCompanyCodesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for supplierCompanyCode_ in self.supplierCompanyCode:
            namespaceprefix_ = self.supplierCompanyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierCompanyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierCompanyCode>%s</%ssupplierCompanyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(supplierCompanyCode_), input_name='supplierCompanyCode')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SupplierCompanyCodesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for supplierCompanyCode_ in self.supplierCompanyCode:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}supplierCompanyCode').text = self.gds_format_string(supplierCompanyCode_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SupplierCompanyCodesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('supplierCompanyCode=[\n')
        level += 1
        for supplierCompanyCode_ in self.supplierCompanyCode:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(supplierCompanyCode_)))
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
        if nodeName_ == 'supplierCompanyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierCompanyCode')
            value_ = self.gds_validate_string(value_, node, 'supplierCompanyCode')
            self.supplierCompanyCode.append(value_)
            self.supplierCompanyCode_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.supplierCompanyCode[-1])
