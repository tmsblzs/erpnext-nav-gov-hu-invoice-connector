from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_chain_digest_type import \
    InvoiceChainDigestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_lines_type import \
    InvoiceLinesType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_reference_data_type import \
    InvoiceReferenceDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceChainElementType(GeneratedsSuper):
    """InvoiceChainElementType -- Számlalánc elem
    Invoice chain element
    invoiceChainDigest -- Számlalánc kivonat adatok
            Invoice chain digest data
    invoiceLines -- A számlán vagy módosító okiraton szereplő tételek kivonatos adatai
            Product/service digest data appearing on the invoice or the modification document
    invoiceReferenceData -- A módosítás vagy érvénytelenítés adatai
            Modification or cancellation data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, invoiceChainDigest=None, invoiceLines=None, invoiceReferenceData=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceChainDigest = invoiceChainDigest
        self.invoiceChainDigest_nsprefix_ = None
        self.invoiceLines = invoiceLines
        self.invoiceLines_nsprefix_ = None
        self.invoiceReferenceData = invoiceReferenceData
        self.invoiceReferenceData_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceChainElementType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceChainElementType.subclass:
            return InvoiceChainElementType.subclass(*args_, **kwargs_)
        else:
            return InvoiceChainElementType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_invoiceChainDigest(self):
        return self.invoiceChainDigest

    def set_invoiceChainDigest(self, invoiceChainDigest):
        self.invoiceChainDigest = invoiceChainDigest

    def get_invoiceLines(self):
        return self.invoiceLines

    def set_invoiceLines(self, invoiceLines):
        self.invoiceLines = invoiceLines

    def get_invoiceReferenceData(self):
        return self.invoiceReferenceData

    def set_invoiceReferenceData(self, invoiceReferenceData):
        self.invoiceReferenceData = invoiceReferenceData

    def _hasContent(self):
        if (
                self.invoiceChainDigest is not None or
                self.invoiceLines is not None or
                self.invoiceReferenceData is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='InvoiceChainElementType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceChainElementType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceChainElementType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceChainElementType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceChainElementType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='InvoiceChainElementType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='InvoiceChainElementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceChainDigest is not None:
            namespaceprefix_ = self.invoiceChainDigest_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceChainDigest_nsprefix_) else ''
            self.invoiceChainDigest.export(outfile, level, namespaceprefix_, namespacedef_='',
                                           name_='invoiceChainDigest', pretty_print=pretty_print)
        if self.invoiceLines is not None:
            namespaceprefix_ = self.invoiceLines_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceLines_nsprefix_) else ''
            self.invoiceLines.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceLines',
                                     pretty_print=pretty_print)
        if self.invoiceReferenceData is not None:
            namespaceprefix_ = self.invoiceReferenceData_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceReferenceData_nsprefix_) else ''
            self.invoiceReferenceData.export(outfile, level, namespaceprefix_, namespacedef_='',
                                             name_='invoiceReferenceData', pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='InvoiceChainElementType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.invoiceChainDigest is not None:
            invoiceChainDigest_ = self.invoiceChainDigest
            invoiceChainDigest_.to_etree(element, name_='invoiceChainDigest', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceLines is not None:
            invoiceLines_ = self.invoiceLines
            invoiceLines_.to_etree(element, name_='invoiceLines', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceReferenceData is not None:
            invoiceReferenceData_ = self.invoiceReferenceData
            invoiceReferenceData_.to_etree(element, name_='invoiceReferenceData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceChainElementType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceChainDigest is not None:
            showIndent(outfile, level)
            outfile.write('invoiceChainDigest=model_.InvoiceChainDigestType(\n')
            self.invoiceChainDigest.exportLiteral(outfile, level, name_='invoiceChainDigest')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.invoiceLines is not None:
            showIndent(outfile, level)
            outfile.write('invoiceLines=model_.InvoiceLinesType(\n')
            self.invoiceLines.exportLiteral(outfile, level, name_='invoiceLines')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.invoiceReferenceData is not None:
            showIndent(outfile, level)
            outfile.write('invoiceReferenceData=model_.InvoiceReferenceDataType(\n')
            self.invoiceReferenceData.exportLiteral(outfile, level, name_='invoiceReferenceData')
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
        if nodeName_ == 'invoiceChainDigest':
            obj_ = InvoiceChainDigestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceChainDigest = obj_
            obj_.original_tagname_ = 'invoiceChainDigest'
        elif nodeName_ == 'invoiceLines':
            obj_ = InvoiceLinesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceLines = obj_
            obj_.original_tagname_ = 'invoiceLines'
        elif nodeName_ == 'invoiceReferenceData':
            obj_ = InvoiceReferenceDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceReferenceData = obj_
            obj_.original_tagname_ = 'invoiceReferenceData'
