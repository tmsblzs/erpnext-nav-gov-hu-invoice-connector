import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class BatchInvoiceType(GeneratedsSuper):
    """BatchInvoiceType -- Kötegelt módosító okirat adatai
    Data of a batch of modification documents
    batchIndex -- A módosító okirat sorszáma a kötegen belül
    Sequence number of the modification document within the batch
    invoice -- Egy számla vagy módosító okirat adatai
    Data of a single invoice or modification document

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, batchIndex=None, invoice=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.batchIndex = batchIndex
        self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        self.batchIndex_nsprefix_ = "base"
        self.invoice = invoice
        self.invoice_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BatchInvoiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BatchInvoiceType.subclass:
            return BatchInvoiceType.subclass(*args_, **kwargs_)
        else:
            return BatchInvoiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_batchIndex(self):
        return self.batchIndex
    def set_batchIndex(self, batchIndex):
        self.batchIndex = batchIndex
    def get_invoice(self):
        return self.invoice
    def set_invoice(self, invoice):
        self.invoice = invoice
    def validate_InvoiceUnboundedIndexType(self, value):
        result = True
        # Validate type InvoiceUnboundedIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceUnboundedIndexType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.batchIndex is not None or
            self.invoice is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='BatchInvoiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BatchInvoiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BatchInvoiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BatchInvoiceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BatchInvoiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BatchInvoiceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='BatchInvoiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.batchIndex is not None:
            namespaceprefix_ = self.batchIndex_nsprefix_ + ':' if (UseCapturedNS_ and self.batchIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbatchIndex>%s</%sbatchIndex>%s' % (namespaceprefix_ , self.gds_format_integer(self.batchIndex, input_name='batchIndex'), namespaceprefix_ , eol_))
        if self.invoice is not None:
            namespaceprefix_ = self.invoice_nsprefix_ + ':' if (UseCapturedNS_ and self.invoice_nsprefix_) else ''
            self.invoice.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoice', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='BatchInvoiceType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.batchIndex is not None:
            batchIndex_ = self.batchIndex
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}batchIndex').text = self.gds_format_integer(batchIndex_)
        if self.invoice is not None:
            invoice_ = self.invoice
            invoice_.to_etree(element, name_='invoice', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='BatchInvoiceType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.batchIndex is not None:
            showIndent(outfile, level)
            outfile.write('batchIndex=%d,\n' % self.batchIndex)
        if self.invoice is not None:
            showIndent(outfile, level)
            outfile.write('invoice=model_.InvoiceType(\n')
            self.invoice.exportLiteral(outfile, level, name_='invoice')
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
        if nodeName_ == 'batchIndex' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'batchIndex')
            ival_ = self.gds_validate_integer(ival_, node, 'batchIndex')
            self.batchIndex = ival_
            self.batchIndex_nsprefix_ = child_.prefix
            # validate type InvoiceUnboundedIndexType
            self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        elif nodeName_ == 'invoice':
            obj_ = InvoiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoice = obj_
            obj_.original_tagname_ = 'invoice'
