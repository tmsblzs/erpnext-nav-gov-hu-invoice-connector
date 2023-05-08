import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.customer_declaration_type import \
    CustomerDeclarationType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.product_fee_takeover_data_type import \
    ProductFeeTakeoverDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ProductFeeClauseType(GeneratedsSuper):
    """ProductFeeClauseType -- A környezetvédelmi termékdíjról szóló 2011. évi LXXXV. tv. szerinti,
        tételre vonatkozó záradékok
    Clauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)
    productFeeTakeoverData -- A környezetvédelmi termékdíj kötelezettség átvállalásával kapcsolatos adatok
    Data in connection with takeover of environmental protection product fee
    customerDeclaration -- Ha az eladó a vevő nyilatkozata alapján mentesül a termékdíj megfizetése alól,
        akkor az érintett termékáram
    Should the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productFeeTakeoverData=None, customerDeclaration=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productFeeTakeoverData = productFeeTakeoverData
        self.productFeeTakeoverData_nsprefix_ = None
        self.customerDeclaration = customerDeclaration
        self.customerDeclaration_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeClauseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeClauseType.subclass:
            return ProductFeeClauseType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeClauseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productFeeTakeoverData(self):
        return self.productFeeTakeoverData
    def set_productFeeTakeoverData(self, productFeeTakeoverData):
        self.productFeeTakeoverData = productFeeTakeoverData
    def get_customerDeclaration(self):
        return self.customerDeclaration
    def set_customerDeclaration(self, customerDeclaration):
        self.customerDeclaration = customerDeclaration
    def _hasContent(self):
        if (
            self.productFeeTakeoverData is not None or
            self.customerDeclaration is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProductFeeClauseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeClauseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeClauseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeClauseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeClauseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeClauseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProductFeeClauseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productFeeTakeoverData is not None:
            namespaceprefix_ = self.productFeeTakeoverData_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeTakeoverData_nsprefix_) else ''
            self.productFeeTakeoverData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeTakeoverData', pretty_print=pretty_print)
        if self.customerDeclaration is not None:
            namespaceprefix_ = self.customerDeclaration_nsprefix_ + ':' if (UseCapturedNS_ and self.customerDeclaration_nsprefix_) else ''
            self.customerDeclaration.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customerDeclaration', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProductFeeClauseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productFeeTakeoverData is not None:
            productFeeTakeoverData_ = self.productFeeTakeoverData
            productFeeTakeoverData_.to_etree(element, name_='productFeeTakeoverData', mapping_=mapping_, nsmap_=nsmap_)
        if self.customerDeclaration is not None:
            customerDeclaration_ = self.customerDeclaration
            customerDeclaration_.to_etree(element, name_='customerDeclaration', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeClauseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productFeeTakeoverData is not None:
            showIndent(outfile, level)
            outfile.write('productFeeTakeoverData=model_.ProductFeeTakeoverDataType(\n')
            self.productFeeTakeoverData.exportLiteral(outfile, level, name_='productFeeTakeoverData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.customerDeclaration is not None:
            showIndent(outfile, level)
            outfile.write('customerDeclaration=model_.CustomerDeclarationType(\n')
            self.customerDeclaration.exportLiteral(outfile, level, name_='customerDeclaration')
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
        if nodeName_ == 'productFeeTakeoverData':
            obj_ = ProductFeeTakeoverDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeTakeoverData = obj_
            obj_.original_tagname_ = 'productFeeTakeoverData'
        elif nodeName_ == 'customerDeclaration':
            obj_ = CustomerDeclarationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerDeclaration = obj_
            obj_.original_tagname_ = 'customerDeclaration'
