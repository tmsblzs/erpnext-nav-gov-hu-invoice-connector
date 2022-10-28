import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ProductCodeType(GeneratedsSuper):
    """ProductCodeType -- Különböző termék- vagy szolgáltatáskódokat tartalmazó típus
    Field type including the different product and service codes
    productCodeCategory -- A termékkód fajtájának (pl. VTSZ, CsK, stb.) jelölése
    The kind of product code (f. ex. VTSZ, CsK, etc.)
    productCodeValue -- A termékkód értéke nem saját termékkód esetén
    The value of (not own) product code
    productCodeOwnValue -- Saját termékkód értéke
    Own product code value

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productCodeCategory=None, productCodeValue=None, productCodeOwnValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productCodeCategory = productCodeCategory
        self.validate_ProductCodeCategoryType(self.productCodeCategory)
        self.productCodeCategory_nsprefix_ = None
        self.productCodeValue = productCodeValue
        self.validate_ProductCodeValueType(self.productCodeValue)
        self.productCodeValue_nsprefix_ = None
        self.productCodeOwnValue = productCodeOwnValue
        self.validate_SimpleText255NotBlankType(self.productCodeOwnValue)
        self.productCodeOwnValue_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductCodeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductCodeType.subclass:
            return ProductCodeType.subclass(*args_, **kwargs_)
        else:
            return ProductCodeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productCodeCategory(self):
        return self.productCodeCategory
    def set_productCodeCategory(self, productCodeCategory):
        self.productCodeCategory = productCodeCategory
    def get_productCodeValue(self):
        return self.productCodeValue
    def set_productCodeValue(self, productCodeValue):
        self.productCodeValue = productCodeValue
    def get_productCodeOwnValue(self):
        return self.productCodeOwnValue
    def set_productCodeOwnValue(self, productCodeOwnValue):
        self.productCodeOwnValue = productCodeOwnValue
    def validate_ProductCodeCategoryType(self, value):
        result = True
        # Validate type ProductCodeCategoryType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['VTSZ', 'SZJ', 'KN', 'AHK', 'CSK', 'KT', 'EJ', 'TESZOR', 'OWN', 'OTHER']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductCodeCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeCategoryType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeCategoryType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeCategoryType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeCategoryType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_ProductCodeValueType(self, value):
        result = True
        # Validate type ProductCodeValueType, a restriction on common:AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeValueType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeValueType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeValueType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeValueType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ProductCodeValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ProductCodeValueType_patterns_, ))
                result = False
        return result
    validate_ProductCodeValueType_patterns_ = [['^([A-Z0-9]{2,30})$']]
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
    def _hasContent(self):
        if (
            self.productCodeCategory is not None or
            self.productCodeValue is not None or
            self.productCodeOwnValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ProductCodeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductCodeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductCodeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductCodeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductCodeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductCodeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ProductCodeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productCodeCategory is not None:
            namespaceprefix_ = self.productCodeCategory_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodeCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductCodeCategory>%s</%sproductCodeCategory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productCodeCategory), input_name='productCodeCategory')), namespaceprefix_ , eol_))
        if self.productCodeValue is not None:
            namespaceprefix_ = self.productCodeValue_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodeValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductCodeValue>%s</%sproductCodeValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productCodeValue), input_name='productCodeValue')), namespaceprefix_ , eol_))
        if self.productCodeOwnValue is not None:
            namespaceprefix_ = self.productCodeOwnValue_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodeOwnValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductCodeOwnValue>%s</%sproductCodeOwnValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productCodeOwnValue), input_name='productCodeOwnValue')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProductCodeType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productCodeCategory is not None:
            productCodeCategory_ = self.productCodeCategory
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productCodeCategory').text = self.gds_format_string(productCodeCategory_)
        if self.productCodeValue is not None:
            productCodeValue_ = self.productCodeValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productCodeValue').text = self.gds_format_string(productCodeValue_)
        if self.productCodeOwnValue is not None:
            productCodeOwnValue_ = self.productCodeOwnValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productCodeOwnValue').text = self.gds_format_string(productCodeOwnValue_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductCodeType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productCodeCategory is not None:
            showIndent(outfile, level)
            outfile.write('productCodeCategory=%s,\n' % self.gds_encode(quote_python(self.productCodeCategory)))
        if self.productCodeValue is not None:
            showIndent(outfile, level)
            outfile.write('productCodeValue=%s,\n' % self.gds_encode(quote_python(self.productCodeValue)))
        if self.productCodeOwnValue is not None:
            showIndent(outfile, level)
            outfile.write('productCodeOwnValue=%s,\n' % self.gds_encode(quote_python(self.productCodeOwnValue)))
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
        if nodeName_ == 'productCodeCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productCodeCategory')
            value_ = self.gds_validate_string(value_, node, 'productCodeCategory')
            self.productCodeCategory = value_
            self.productCodeCategory_nsprefix_ = child_.prefix
            # validate type ProductCodeCategoryType
            self.validate_ProductCodeCategoryType(self.productCodeCategory)
        elif nodeName_ == 'productCodeValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productCodeValue')
            value_ = self.gds_validate_string(value_, node, 'productCodeValue')
            self.productCodeValue = value_
            self.productCodeValue_nsprefix_ = child_.prefix
            # validate type ProductCodeValueType
            self.validate_ProductCodeValueType(self.productCodeValue)
        elif nodeName_ == 'productCodeOwnValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productCodeOwnValue')
            value_ = self.gds_validate_string(value_, node, 'productCodeOwnValue')
            self.productCodeOwnValue = value_
            self.productCodeOwnValue_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.productCodeOwnValue)
