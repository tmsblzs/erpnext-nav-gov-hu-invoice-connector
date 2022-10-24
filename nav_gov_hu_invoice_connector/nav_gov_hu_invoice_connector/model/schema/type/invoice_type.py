import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_head_type import \
    InvoiceHeadType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_reference_type import \
    InvoiceReferenceType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class InvoiceType(GeneratedsSuper):
    """InvoiceType -- Egy számla vagy módosító okirat adatai
    Data of a single invoice or modification document
    invoiceReference -- A módosítás vagy érvénytelenítés adatai
    Modification or cancellation data
    invoiceHead -- A számla egészét jellemző adatok
    Data concerning the whole invoice
    invoiceLines -- A számlán szereplőtételek adatai
    Product/service data appearing on the invoice
    productFeeSummary -- Termékdíjjal kapcsolatos összesítő adatok
    Summary data of product charges
    invoiceSummary -- Az ÁFA törvény szerinti összesítő adatok
    Summary data according to VAT law

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoiceReference=None, invoiceHead=None, invoiceLines=None, productFeeSummary=None, invoiceSummary=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceReference = invoiceReference
        self.invoiceReference_nsprefix_ = None
        self.invoiceHead = invoiceHead
        self.invoiceHead_nsprefix_ = None
        self.invoiceLines = invoiceLines
        self.invoiceLines_nsprefix_ = None
        if productFeeSummary is None:
            self.productFeeSummary = []
        else:
            self.productFeeSummary = productFeeSummary
        self.productFeeSummary_nsprefix_ = None
        self.invoiceSummary = invoiceSummary
        self.invoiceSummary_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceType.subclass:
            return InvoiceType.subclass(*args_, **kwargs_)
        else:
            return InvoiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceReference(self):
        return self.invoiceReference
    def set_invoiceReference(self, invoiceReference):
        self.invoiceReference = invoiceReference
    def get_invoiceHead(self):
        return self.invoiceHead
    def set_invoiceHead(self, invoiceHead):
        self.invoiceHead = invoiceHead
    def get_invoiceLines(self):
        return self.invoiceLines
    def set_invoiceLines(self, invoiceLines):
        self.invoiceLines = invoiceLines
    def get_productFeeSummary(self):
        return self.productFeeSummary
    def set_productFeeSummary(self, productFeeSummary):
        self.productFeeSummary = productFeeSummary
    def add_productFeeSummary(self, value):
        self.productFeeSummary.append(value)
    def insert_productFeeSummary_at(self, index, value):
        self.productFeeSummary.insert(index, value)
    def replace_productFeeSummary_at(self, index, value):
        self.productFeeSummary[index] = value
    def get_invoiceSummary(self):
        return self.invoiceSummary
    def set_invoiceSummary(self, invoiceSummary):
        self.invoiceSummary = invoiceSummary
    def _hasContent(self):
        if (
            self.invoiceReference is not None or
            self.invoiceHead is not None or
            self.invoiceLines is not None or
            self.productFeeSummary or
            self.invoiceSummary is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceReference is not None:
            namespaceprefix_ = self.invoiceReference_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceReference_nsprefix_) else ''
            self.invoiceReference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceReference', pretty_print=pretty_print)
        if self.invoiceHead is not None:
            namespaceprefix_ = self.invoiceHead_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceHead_nsprefix_) else ''
            self.invoiceHead.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceHead', pretty_print=pretty_print)
        if self.invoiceLines is not None:
            namespaceprefix_ = self.invoiceLines_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceLines_nsprefix_) else ''
            self.invoiceLines.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceLines', pretty_print=pretty_print)
        for productFeeSummary_ in self.productFeeSummary:
            namespaceprefix_ = self.productFeeSummary_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeSummary_nsprefix_) else ''
            productFeeSummary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeSummary', pretty_print=pretty_print)
        if self.invoiceSummary is not None:
            namespaceprefix_ = self.invoiceSummary_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceSummary_nsprefix_) else ''
            self.invoiceSummary.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceSummary', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InvoiceType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.invoiceReference is not None:
            invoiceReference_ = self.invoiceReference
            invoiceReference_.to_etree(element, name_='invoiceReference', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceHead is not None:
            invoiceHead_ = self.invoiceHead
            invoiceHead_.to_etree(element, name_='invoiceHead', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceLines is not None:
            invoiceLines_ = self.invoiceLines
            invoiceLines_.to_etree(element, name_='invoiceLines', mapping_=mapping_, nsmap_=nsmap_)
        for productFeeSummary_ in self.productFeeSummary:
            productFeeSummary_.to_etree(element, name_='productFeeSummary', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceSummary is not None:
            invoiceSummary_ = self.invoiceSummary
            invoiceSummary_.to_etree(element, name_='invoiceSummary', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='InvoiceType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceReference is not None:
            showIndent(outfile, level)
            outfile.write('invoiceReference=model_.InvoiceReferenceType(\n')
            self.invoiceReference.exportLiteral(outfile, level, name_='invoiceReference')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.invoiceHead is not None:
            showIndent(outfile, level)
            outfile.write('invoiceHead=model_.InvoiceHeadType(\n')
            self.invoiceHead.exportLiteral(outfile, level, name_='invoiceHead')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.invoiceLines is not None:
            showIndent(outfile, level)
            outfile.write('invoiceLines=model_.LinesType(\n')
            self.invoiceLines.exportLiteral(outfile, level, name_='invoiceLines')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('productFeeSummary=[\n')
        level += 1
        for productFeeSummary_ in self.productFeeSummary:
            showIndent(outfile, level)
            outfile.write('model_.ProductFeeSummaryType(\n')
            productFeeSummary_.exportLiteral(outfile, level, name_='ProductFeeSummaryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.invoiceSummary is not None:
            showIndent(outfile, level)
            outfile.write('invoiceSummary=model_.SummaryType(\n')
            self.invoiceSummary.exportLiteral(outfile, level, name_='invoiceSummary')
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
        if nodeName_ == 'invoiceReference':
            obj_ = InvoiceReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceReference = obj_
            obj_.original_tagname_ = 'invoiceReference'
        elif nodeName_ == 'invoiceHead':
            obj_ = InvoiceHeadType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceHead = obj_
            obj_.original_tagname_ = 'invoiceHead'
        elif nodeName_ == 'invoiceLines':
            obj_ = LinesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceLines = obj_
            obj_.original_tagname_ = 'invoiceLines'
        elif nodeName_ == 'productFeeSummary':
            obj_ = ProductFeeSummaryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeSummary.append(obj_)
            obj_.original_tagname_ = 'productFeeSummary'
        elif nodeName_ == 'invoiceSummary':
            obj_ = SummaryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceSummary = obj_
            obj_.original_tagname_ = 'invoiceSummary'
