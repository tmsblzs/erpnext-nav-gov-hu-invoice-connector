import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_detail_type import \
    InvoiceDetailType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class InvoiceHeadType(GeneratedsSuper):
    """InvoiceHeadType -- Számla fejléc adatai
    Data in header of invoice
    supplierInfo -- Számla kibocsátó (eladó) adatai
    Data related to the issuer of the invoice (supplier)
    customerInfo -- Vevő adatai
    Data related to the customer
    fiscalRepresentativeInfo -- Pénzügyi képviselő adatai
    Data related to the fiscal representative
    invoiceDetail -- Számla részletező adatok
    Invoice detail adata

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, supplierInfo=None, customerInfo=None, fiscalRepresentativeInfo=None, invoiceDetail=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.supplierInfo = supplierInfo
        self.supplierInfo_nsprefix_ = None
        self.customerInfo = customerInfo
        self.customerInfo_nsprefix_ = None
        self.fiscalRepresentativeInfo = fiscalRepresentativeInfo
        self.fiscalRepresentativeInfo_nsprefix_ = None
        self.invoiceDetail = invoiceDetail
        self.invoiceDetail_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceHeadType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceHeadType.subclass:
            return InvoiceHeadType.subclass(*args_, **kwargs_)
        else:
            return InvoiceHeadType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_supplierInfo(self):
        return self.supplierInfo
    def set_supplierInfo(self, supplierInfo):
        self.supplierInfo = supplierInfo
    def get_customerInfo(self):
        return self.customerInfo
    def set_customerInfo(self, customerInfo):
        self.customerInfo = customerInfo
    def get_fiscalRepresentativeInfo(self):
        return self.fiscalRepresentativeInfo
    def set_fiscalRepresentativeInfo(self, fiscalRepresentativeInfo):
        self.fiscalRepresentativeInfo = fiscalRepresentativeInfo
    def get_invoiceDetail(self):
        return self.invoiceDetail
    def set_invoiceDetail(self, invoiceDetail):
        self.invoiceDetail = invoiceDetail
    def _hasContent(self):
        if (
            self.supplierInfo is not None or
            self.customerInfo is not None or
            self.fiscalRepresentativeInfo is not None or
            self.invoiceDetail is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceHeadType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceHeadType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceHeadType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceHeadType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceHeadType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceHeadType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceHeadType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.supplierInfo is not None:
            namespaceprefix_ = self.supplierInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierInfo_nsprefix_) else ''
            self.supplierInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplierInfo', pretty_print=pretty_print)
        if self.customerInfo is not None:
            namespaceprefix_ = self.customerInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.customerInfo_nsprefix_) else ''
            self.customerInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customerInfo', pretty_print=pretty_print)
        if self.fiscalRepresentativeInfo is not None:
            namespaceprefix_ = self.fiscalRepresentativeInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeInfo_nsprefix_) else ''
            self.fiscalRepresentativeInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fiscalRepresentativeInfo', pretty_print=pretty_print)
        if self.invoiceDetail is not None:
            namespaceprefix_ = self.invoiceDetail_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceDetail_nsprefix_) else ''
            self.invoiceDetail.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceDetail', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InvoiceHeadType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.supplierInfo is not None:
            supplierInfo_ = self.supplierInfo
            supplierInfo_.to_etree(element, name_='supplierInfo', mapping_=mapping_, nsmap_=nsmap_)
        if self.customerInfo is not None:
            customerInfo_ = self.customerInfo
            customerInfo_.to_etree(element, name_='customerInfo', mapping_=mapping_, nsmap_=nsmap_)
        if self.fiscalRepresentativeInfo is not None:
            fiscalRepresentativeInfo_ = self.fiscalRepresentativeInfo
            fiscalRepresentativeInfo_.to_etree(element, name_='fiscalRepresentativeInfo', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceDetail is not None:
            invoiceDetail_ = self.invoiceDetail
            invoiceDetail_.to_etree(element, name_='invoiceDetail', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='InvoiceHeadType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.supplierInfo is not None:
            showIndent(outfile, level)
            outfile.write('supplierInfo=model_.SupplierInfoType(\n')
            self.supplierInfo.exportLiteral(outfile, level, name_='supplierInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.customerInfo is not None:
            showIndent(outfile, level)
            outfile.write('customerInfo=model_.CustomerInfoType(\n')
            self.customerInfo.exportLiteral(outfile, level, name_='customerInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fiscalRepresentativeInfo is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeInfo=model_.FiscalRepresentativeType(\n')
            self.fiscalRepresentativeInfo.exportLiteral(outfile, level, name_='fiscalRepresentativeInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.invoiceDetail is not None:
            showIndent(outfile, level)
            outfile.write('invoiceDetail=model_.InvoiceDetailType(\n')
            self.invoiceDetail.exportLiteral(outfile, level, name_='invoiceDetail')
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
        if nodeName_ == 'supplierInfo':
            obj_ = SupplierInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplierInfo = obj_
            obj_.original_tagname_ = 'supplierInfo'
        elif nodeName_ == 'customerInfo':
            obj_ = CustomerInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerInfo = obj_
            obj_.original_tagname_ = 'customerInfo'
        elif nodeName_ == 'fiscalRepresentativeInfo':
            obj_ = FiscalRepresentativeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fiscalRepresentativeInfo = obj_
            obj_.original_tagname_ = 'fiscalRepresentativeInfo'
        elif nodeName_ == 'invoiceDetail':
            obj_ = InvoiceDetailType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceDetail = obj_
            obj_.original_tagname_ = 'invoiceDetail'
