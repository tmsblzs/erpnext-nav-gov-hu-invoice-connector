import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class CustomerDeclarationType(GeneratedsSuper):
    """CustomerDeclarationType -- Ha az eladó a vevő nyilatkozata alapján mentesül a termékdíj megfizetése alól,
        akkor az érintett termék áram
    Should the supplier, based on statement given by the purchaser, be exempted from paying product fee,
        then the product stream affected
    productStream -- Termék áram
    Product stream
    productFeeWeight -- Termékdíj köteles termék tömege kilogrammban
    Weight of product fee obliged product in kilogram

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productStream=None, productFeeWeight=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productStream = productStream
        self.validate_ProductStreamType(self.productStream)
        self.productStream_nsprefix_ = None
        self.productFeeWeight = productFeeWeight
        self.validate_QuantityType(self.productFeeWeight)
        self.productFeeWeight_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CustomerDeclarationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CustomerDeclarationType.subclass:
            return CustomerDeclarationType.subclass(*args_, **kwargs_)
        else:
            return CustomerDeclarationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productStream(self):
        return self.productStream
    def set_productStream(self, productStream):
        self.productStream = productStream
    def get_productFeeWeight(self):
        return self.productFeeWeight
    def set_productFeeWeight(self, productFeeWeight):
        self.productFeeWeight = productFeeWeight
    def validate_ProductStreamType(self, value):
        result = True
        # Validate type ProductStreamType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['BATTERY', 'PACKAGING', 'OTHER_PETROL', 'ELECTRONIC', 'TIRE', 'COMMERCIAL', 'PLASTIC', 'OTHER_CHEMICAL', 'PAPER']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductStreamType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductStreamType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductStreamType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.productStream is not None or
            self.productFeeWeight is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='CustomerDeclarationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CustomerDeclarationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CustomerDeclarationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomerDeclarationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CustomerDeclarationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CustomerDeclarationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='CustomerDeclarationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productStream is not None:
            namespaceprefix_ = self.productStream_nsprefix_ + ':' if (UseCapturedNS_ and self.productStream_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductStream>%s</%sproductStream>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productStream), input_name='productStream')), namespaceprefix_ , eol_))
        if self.productFeeWeight is not None:
            namespaceprefix_ = self.productFeeWeight_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeWeight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeWeight>%s</%sproductFeeWeight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productFeeWeight, input_name='productFeeWeight'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='CustomerDeclarationType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productStream is not None:
            productStream_ = self.productStream
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productStream').text = self.gds_format_string(productStream_)
        if self.productFeeWeight is not None:
            productFeeWeight_ = self.productFeeWeight
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeWeight').text = self.gds_format_decimal(productFeeWeight_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CustomerDeclarationType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productStream is not None:
            showIndent(outfile, level)
            outfile.write('productStream=%s,\n' % self.gds_encode(quote_python(self.productStream)))
        if self.productFeeWeight is not None:
            showIndent(outfile, level)
            outfile.write('productFeeWeight=%f,\n' % self.productFeeWeight)
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
        if nodeName_ == 'productStream':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productStream')
            value_ = self.gds_validate_string(value_, node, 'productStream')
            self.productStream = value_
            self.productStream_nsprefix_ = child_.prefix
            # validate type ProductStreamType
            self.validate_ProductStreamType(self.productStream)
        elif nodeName_ == 'productFeeWeight' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productFeeWeight')
            fval_ = self.gds_validate_decimal(fval_, node, 'productFeeWeight')
            self.productFeeWeight = fval_
            self.productFeeWeight_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.productFeeWeight)
