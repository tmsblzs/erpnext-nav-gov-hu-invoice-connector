import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.batch_invoice_type import \
    BatchInvoiceType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_type import InvoiceType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class InvoiceMainType(GeneratedsSuper):
    """InvoiceMainType -- Számlaadatok leírására szolgáló közös típus
    A common type to describe invoice information
    invoice -- Egy számla vagy módosító okirat adatai
    Data of a single invoice or modification document
    batchInvoice -- Kötegelt módosító okirat adatai
    Data of a batch of modification documents

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoice=None, batchInvoice=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoice = invoice
        self.invoice_nsprefix_ = None
        if batchInvoice is None:
            self.batchInvoice = []
        else:
            self.batchInvoice = batchInvoice
        self.batchInvoice_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceMainType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceMainType.subclass:
            return InvoiceMainType.subclass(*args_, **kwargs_)
        else:
            return InvoiceMainType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoice(self):
        return self.invoice
    def set_invoice(self, invoice):
        self.invoice = invoice
    def get_batchInvoice(self):
        return self.batchInvoice
    def set_batchInvoice(self, batchInvoice):
        self.batchInvoice = batchInvoice
    def add_batchInvoice(self, value):
        self.batchInvoice.append(value)
    def insert_batchInvoice_at(self, index, value):
        self.batchInvoice.insert(index, value)
    def replace_batchInvoice_at(self, index, value):
        self.batchInvoice[index] = value
    def _hasContent(self):
        if (
            self.invoice is not None or
            self.batchInvoice
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceMainType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceMainType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceMainType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceMainType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceMainType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceMainType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceMainType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoice is not None:
            namespaceprefix_ = self.invoice_nsprefix_ + ':' if (UseCapturedNS_ and self.invoice_nsprefix_) else ''
            self.invoice.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoice', pretty_print=pretty_print)
        for batchInvoice_ in self.batchInvoice:
            namespaceprefix_ = self.batchInvoice_nsprefix_ + ':' if (UseCapturedNS_ and self.batchInvoice_nsprefix_) else ''
            batchInvoice_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='batchInvoice', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InvoiceMainType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.invoice is not None:
            invoice_ = self.invoice
            invoice_.to_etree(element, name_='invoice', mapping_=mapping_, nsmap_=nsmap_)
        for batchInvoice_ in self.batchInvoice:
            batchInvoice_.to_etree(element, name_='batchInvoice', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='InvoiceMainType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoice is not None:
            showIndent(outfile, level)
            outfile.write('invoice=model_.InvoiceType(\n')
            self.invoice.exportLiteral(outfile, level, name_='invoice')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('batchInvoice=[\n')
        level += 1
        for batchInvoice_ in self.batchInvoice:
            showIndent(outfile, level)
            outfile.write('model_.BatchInvoiceType(\n')
            batchInvoice_.exportLiteral(outfile, level, name_='BatchInvoiceType')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'invoice':
            obj_ = InvoiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoice = obj_
            obj_.original_tagname_ = 'invoice'
        elif nodeName_ == 'batchInvoice':
            obj_ = BatchInvoiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.batchInvoice.append(obj_)
            obj_.original_tagname_ = 'batchInvoice'
