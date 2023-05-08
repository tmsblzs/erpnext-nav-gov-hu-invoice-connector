import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_response_type import \
    BasicOnlineInvoiceResponseType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_change_digest_result_type import \
    InvoiceChainDigestResultType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class QueryInvoiceChainDigestResponseType(BasicOnlineInvoiceResponseType):
    """QueryInvoiceChainDigestResponseType -- A POST /queryInvoiceChainDigest REST operáció válasz típusa
    Response type of the POST /queryInvoiceChainDigest REST operation
    invoiceChainDigestResult -- Számlalánc kivonat lekérdezés eredményei
    Invoice chain digest query result

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceResponseType
    def __init__(self, header=None, result=None, software=None, invoiceChainDigestResult=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryInvoiceChainDigestResponseType"), self).__init__(header, result, software, extensiontype_,  **kwargs_)
        self.invoiceChainDigestResult = invoiceChainDigestResult
        self.invoiceChainDigestResult_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryInvoiceChainDigestResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryInvoiceChainDigestResponseType.subclass:
            return QueryInvoiceChainDigestResponseType.subclass(*args_, **kwargs_)
        else:
            return QueryInvoiceChainDigestResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceChainDigestResult(self):
        return self.invoiceChainDigestResult
    def set_invoiceChainDigestResult(self, invoiceChainDigestResult):
        self.invoiceChainDigestResult = invoiceChainDigestResult
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.invoiceChainDigestResult is not None or
            super(QueryInvoiceChainDigestResponseType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryInvoiceChainDigestResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryInvoiceChainDigestResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryInvoiceChainDigestResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryInvoiceChainDigestResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryInvoiceChainDigestResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryInvoiceChainDigestResponseType'):
        super(QueryInvoiceChainDigestResponseType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryInvoiceChainDigestResponseType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryInvoiceChainDigestResponseType', fromsubclass_=False, pretty_print=True):
        super(QueryInvoiceChainDigestResponseType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceChainDigestResult is not None:
            namespaceprefix_ = self.invoiceChainDigestResult_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceChainDigestResult_nsprefix_) else ''
            self.invoiceChainDigestResult.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceChainDigestResult', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryInvoiceChainDigestResponseType', mapping_=None, nsmap_=None):
        element = super(QueryInvoiceChainDigestResponseType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.invoiceChainDigestResult is not None:
            invoiceChainDigestResult_ = self.invoiceChainDigestResult
            invoiceChainDigestResult_.to_etree(element, name_='invoiceChainDigestResult', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryInvoiceChainDigestResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryInvoiceChainDigestResponseType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryInvoiceChainDigestResponseType, self)._exportLiteralChildren(outfile, level, name_)
        if self.invoiceChainDigestResult is not None:
            showIndent(outfile, level)
            outfile.write('invoiceChainDigestResult=model_.InvoiceChainDigestResultType(\n')
            self.invoiceChainDigestResult.exportLiteral(outfile, level, name_='invoiceChainDigestResult')
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
        super(QueryInvoiceChainDigestResponseType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'invoiceChainDigestResult':
            obj_ = InvoiceChainDigestResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceChainDigestResult = obj_
            obj_.original_tagname_ = 'invoiceChainDigestResult'
        super(QueryInvoiceChainDigestResponseType, self)._buildChildren(child_, node, nodeName_, True)
