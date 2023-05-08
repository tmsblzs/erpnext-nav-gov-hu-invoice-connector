import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.product_code_type import \
    ProductCodeType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ProductFeeDataType(GeneratedsSuper):
    """ProductFeeDataType -- Termékdíj adatok
    Product charges data
    productFeeCode -- Termékdíj kód (Kt vagy Csk)
    Product charges code (Kt or Csk code)
    productFeeQuantity -- A termékdíjjal érintett termék mennyisége
    Quantity of product, according to product charge
    productFeeMeasuringUnit -- A díjtétel egysége (kg vagy darab)
    Unit of the rate (kg or piece)
    productFeeRate -- A termékdíj díjtétele (HUF/egység)
    Product fee rate (HUF/unit)
    productFeeAmount -- Termékdíj összege forintban
    Amount in Hungarian forints of the product fee

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productFeeCode=None, productFeeQuantity=None, productFeeMeasuringUnit=None, productFeeRate=None, productFeeAmount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productFeeCode = productFeeCode
        self.productFeeCode_nsprefix_ = None
        self.productFeeQuantity = productFeeQuantity
        self.validate_QuantityType(self.productFeeQuantity)
        self.productFeeQuantity_nsprefix_ = None
        self.productFeeMeasuringUnit = productFeeMeasuringUnit
        self.validate_ProductFeeMeasuringUnitType(self.productFeeMeasuringUnit)
        self.productFeeMeasuringUnit_nsprefix_ = None
        self.productFeeRate = productFeeRate
        self.validate_MonetaryType(self.productFeeRate)
        self.productFeeRate_nsprefix_ = "base"
        self.productFeeAmount = productFeeAmount
        self.validate_MonetaryType(self.productFeeAmount)
        self.productFeeAmount_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeDataType.subclass:
            return ProductFeeDataType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productFeeCode(self):
        return self.productFeeCode
    def set_productFeeCode(self, productFeeCode):
        self.productFeeCode = productFeeCode
    def get_productFeeQuantity(self):
        return self.productFeeQuantity
    def set_productFeeQuantity(self, productFeeQuantity):
        self.productFeeQuantity = productFeeQuantity
    def get_productFeeMeasuringUnit(self):
        return self.productFeeMeasuringUnit
    def set_productFeeMeasuringUnit(self, productFeeMeasuringUnit):
        self.productFeeMeasuringUnit = productFeeMeasuringUnit
    def get_productFeeRate(self):
        return self.productFeeRate
    def set_productFeeRate(self, productFeeRate):
        self.productFeeRate = productFeeRate
    def get_productFeeAmount(self):
        return self.productFeeAmount
    def set_productFeeAmount(self, productFeeAmount):
        self.productFeeAmount = productFeeAmount
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_ProductFeeMeasuringUnitType(self, value):
        result = True
        # Validate type ProductFeeMeasuringUnitType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['DARAB', 'KG']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductFeeMeasuringUnitType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductFeeMeasuringUnitType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductFeeMeasuringUnitType' % {"value" : value, "lineno": lineno} )
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
            self.productFeeCode is not None or
            self.productFeeQuantity is not None or
            self.productFeeMeasuringUnit is not None or
            self.productFeeRate is not None or
            self.productFeeAmount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productFeeCode is not None:
            namespaceprefix_ = self.productFeeCode_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeCode_nsprefix_) else ''
            self.productFeeCode.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeCode', pretty_print=pretty_print)
        if self.productFeeQuantity is not None:
            namespaceprefix_ = self.productFeeQuantity_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeQuantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeQuantity>%s</%sproductFeeQuantity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productFeeQuantity, input_name='productFeeQuantity'), namespaceprefix_ , eol_))
        if self.productFeeMeasuringUnit is not None:
            namespaceprefix_ = self.productFeeMeasuringUnit_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeMeasuringUnit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeMeasuringUnit>%s</%sproductFeeMeasuringUnit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productFeeMeasuringUnit), input_name='productFeeMeasuringUnit')), namespaceprefix_ , eol_))
        if self.productFeeRate is not None:
            namespaceprefix_ = self.productFeeRate_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeRate>%s</%sproductFeeRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productFeeRate, input_name='productFeeRate'), namespaceprefix_ , eol_))
        if self.productFeeAmount is not None:
            namespaceprefix_ = self.productFeeAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeAmount>%s</%sproductFeeAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productFeeAmount, input_name='productFeeAmount'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProductFeeDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productFeeCode is not None:
            productFeeCode_ = self.productFeeCode
            productFeeCode_.to_etree(element, name_='productFeeCode', mapping_=mapping_, nsmap_=nsmap_)
        if self.productFeeQuantity is not None:
            productFeeQuantity_ = self.productFeeQuantity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeQuantity').text = self.gds_format_decimal(productFeeQuantity_)
        if self.productFeeMeasuringUnit is not None:
            productFeeMeasuringUnit_ = self.productFeeMeasuringUnit
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeMeasuringUnit').text = self.gds_format_string(productFeeMeasuringUnit_)
        if self.productFeeRate is not None:
            productFeeRate_ = self.productFeeRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeRate').text = self.gds_format_decimal(productFeeRate_)
        if self.productFeeAmount is not None:
            productFeeAmount_ = self.productFeeAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeAmount').text = self.gds_format_decimal(productFeeAmount_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productFeeCode is not None:
            showIndent(outfile, level)
            outfile.write('productFeeCode=model_.ProductCodeType(\n')
            self.productFeeCode.exportLiteral(outfile, level, name_='productFeeCode')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.productFeeQuantity is not None:
            showIndent(outfile, level)
            outfile.write('productFeeQuantity=%f,\n' % self.productFeeQuantity)
        if self.productFeeMeasuringUnit is not None:
            showIndent(outfile, level)
            outfile.write('productFeeMeasuringUnit=%s,\n' % self.gds_encode(quote_python(self.productFeeMeasuringUnit)))
        if self.productFeeRate is not None:
            showIndent(outfile, level)
            outfile.write('productFeeRate=%f,\n' % self.productFeeRate)
        if self.productFeeAmount is not None:
            showIndent(outfile, level)
            outfile.write('productFeeAmount=%f,\n' % self.productFeeAmount)
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
        if nodeName_ == 'productFeeCode':
            obj_ = ProductCodeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeCode = obj_
            obj_.original_tagname_ = 'productFeeCode'
        elif nodeName_ == 'productFeeQuantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productFeeQuantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'productFeeQuantity')
            self.productFeeQuantity = fval_
            self.productFeeQuantity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.productFeeQuantity)
        elif nodeName_ == 'productFeeMeasuringUnit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productFeeMeasuringUnit')
            value_ = self.gds_validate_string(value_, node, 'productFeeMeasuringUnit')
            self.productFeeMeasuringUnit = value_
            self.productFeeMeasuringUnit_nsprefix_ = child_.prefix
            # validate type ProductFeeMeasuringUnitType
            self.validate_ProductFeeMeasuringUnitType(self.productFeeMeasuringUnit)
        elif nodeName_ == 'productFeeRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productFeeRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'productFeeRate')
            self.productFeeRate = fval_
            self.productFeeRate_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.productFeeRate)
        elif nodeName_ == 'productFeeAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productFeeAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'productFeeAmount')
            self.productFeeAmount = fval_
            self.productFeeAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.productFeeAmount)
