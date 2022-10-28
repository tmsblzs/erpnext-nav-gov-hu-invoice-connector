import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.payment_evidence_document_data_type import \
    PaymentEvidenceDocumentDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.product_fee_data_type import \
    ProductFeeDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ProductFeeSummaryType(GeneratedsSuper):
    """ProductFeeSummaryType -- Termékdíj összegzés adatok
    Summary of product charges
    productFeeOperation -- Annak jelzése, hogy a termékdíj összesítés visszaigénylésre (REFUND)
        vagy raktárba történő beszállításra (DEPOSIT) vonatkozik
    Indicating whether the the product fee summary concerns refund or deposit
    productFeeData -- Termékdíj adatok
    Product charges data
    productChargeSum -- Termékdíj összesen
    Aggregate product charges
    paymentEvidenceDocumentData -- A termékdíj bevallását igazoló dokumentum adatai
        a 2011. évi LXXXV. tv. 13. § (3) szerint és a 25. § (3) szerint
    Data of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productFeeOperation=None, productFeeData=None, productChargeSum=None, paymentEvidenceDocumentData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productFeeOperation = productFeeOperation
        self.validate_ProductFeeOperationType(self.productFeeOperation)
        self.productFeeOperation_nsprefix_ = None
        if productFeeData is None:
            self.productFeeData = []
        else:
            self.productFeeData = productFeeData
        self.productFeeData_nsprefix_ = None
        self.productChargeSum = productChargeSum
        self.validate_MonetaryType(self.productChargeSum)
        self.productChargeSum_nsprefix_ = "base"
        self.paymentEvidenceDocumentData = paymentEvidenceDocumentData
        self.paymentEvidenceDocumentData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeSummaryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeSummaryType.subclass:
            return ProductFeeSummaryType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeSummaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productFeeOperation(self):
        return self.productFeeOperation
    def set_productFeeOperation(self, productFeeOperation):
        self.productFeeOperation = productFeeOperation
    def get_productFeeData(self):
        return self.productFeeData
    def set_productFeeData(self, productFeeData):
        self.productFeeData = productFeeData
    def add_productFeeData(self, value):
        self.productFeeData.append(value)
    def insert_productFeeData_at(self, index, value):
        self.productFeeData.insert(index, value)
    def replace_productFeeData_at(self, index, value):
        self.productFeeData[index] = value
    def get_productChargeSum(self):
        return self.productChargeSum
    def set_productChargeSum(self, productChargeSum):
        self.productChargeSum = productChargeSum
    def get_paymentEvidenceDocumentData(self):
        return self.paymentEvidenceDocumentData
    def set_paymentEvidenceDocumentData(self, paymentEvidenceDocumentData):
        self.paymentEvidenceDocumentData = paymentEvidenceDocumentData
    def validate_ProductFeeOperationType(self, value):
        result = True
        # Validate type ProductFeeOperationType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['REFUND', 'DEPOSIT']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductFeeOperationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductFeeOperationType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductFeeOperationType' % {"value" : value, "lineno": lineno} )
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
            self.productFeeOperation is not None or
            self.productFeeData or
            self.productChargeSum is not None or
            self.paymentEvidenceDocumentData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeSummaryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeSummaryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeSummaryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeSummaryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeSummaryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeSummaryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeSummaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productFeeOperation is not None:
            namespaceprefix_ = self.productFeeOperation_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeOperation>%s</%sproductFeeOperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productFeeOperation), input_name='productFeeOperation')), namespaceprefix_ , eol_))
        for productFeeData_ in self.productFeeData:
            namespaceprefix_ = self.productFeeData_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeData_nsprefix_) else ''
            productFeeData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeData', pretty_print=pretty_print)
        if self.productChargeSum is not None:
            namespaceprefix_ = self.productChargeSum_nsprefix_ + ':' if (UseCapturedNS_ and self.productChargeSum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductChargeSum>%s</%sproductChargeSum>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productChargeSum, input_name='productChargeSum'), namespaceprefix_ , eol_))
        if self.paymentEvidenceDocumentData is not None:
            namespaceprefix_ = self.paymentEvidenceDocumentData_nsprefix_ + ':' if (UseCapturedNS_ and self.paymentEvidenceDocumentData_nsprefix_) else ''
            self.paymentEvidenceDocumentData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='paymentEvidenceDocumentData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProductFeeSummaryType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productFeeOperation is not None:
            productFeeOperation_ = self.productFeeOperation
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeOperation').text = self.gds_format_string(productFeeOperation_)
        for productFeeData_ in self.productFeeData:
            productFeeData_.to_etree(element, name_='productFeeData', mapping_=mapping_, nsmap_=nsmap_)
        if self.productChargeSum is not None:
            productChargeSum_ = self.productChargeSum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productChargeSum').text = self.gds_format_decimal(productChargeSum_)
        if self.paymentEvidenceDocumentData is not None:
            paymentEvidenceDocumentData_ = self.paymentEvidenceDocumentData
            paymentEvidenceDocumentData_.to_etree(element, name_='paymentEvidenceDocumentData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeSummaryType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productFeeOperation is not None:
            showIndent(outfile, level)
            outfile.write('productFeeOperation=%s,\n' % self.gds_encode(quote_python(self.productFeeOperation)))
        showIndent(outfile, level)
        outfile.write('productFeeData=[\n')
        level += 1
        for productFeeData_ in self.productFeeData:
            showIndent(outfile, level)
            outfile.write('model_.ProductFeeDataType(\n')
            productFeeData_.exportLiteral(outfile, level, name_='ProductFeeDataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.productChargeSum is not None:
            showIndent(outfile, level)
            outfile.write('productChargeSum=%f,\n' % self.productChargeSum)
        if self.paymentEvidenceDocumentData is not None:
            showIndent(outfile, level)
            outfile.write('paymentEvidenceDocumentData=model_.PaymentEvidenceDocumentDataType(\n')
            self.paymentEvidenceDocumentData.exportLiteral(outfile, level, name_='paymentEvidenceDocumentData')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'productFeeOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productFeeOperation')
            value_ = self.gds_validate_string(value_, node, 'productFeeOperation')
            self.productFeeOperation = value_
            self.productFeeOperation_nsprefix_ = child_.prefix
            # validate type ProductFeeOperationType
            self.validate_ProductFeeOperationType(self.productFeeOperation)
        elif nodeName_ == 'productFeeData':
            obj_ = ProductFeeDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeData.append(obj_)
            obj_.original_tagname_ = 'productFeeData'
        elif nodeName_ == 'productChargeSum' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productChargeSum')
            fval_ = self.gds_validate_decimal(fval_, node, 'productChargeSum')
            self.productChargeSum = fval_
            self.productChargeSum_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.productChargeSum)
        elif nodeName_ == 'paymentEvidenceDocumentData':
            obj_ = PaymentEvidenceDocumentDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.paymentEvidenceDocumentData = obj_
            obj_.original_tagname_ = 'paymentEvidenceDocumentData'
