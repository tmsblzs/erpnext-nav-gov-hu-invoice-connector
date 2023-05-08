import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, find_attr_value_, GenerateDSNamespaceTypePrefixes_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_request_type import \
    BasicOnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_chain_query_type import \
    InvoiceChainQueryType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_

class QueryInvoiceChainDigestRequestType(BasicOnlineInvoiceRequestType):
    """QueryInvoiceChainDigestRequestType -- A POST /queryInvoiceChainDigest REST operációkérés típusa
    Request type of the POST /queryInvoiceChainDigest REST operation
    page -- A lekérdezni kívánt lap száma
    The queried page count
    invoiceChainQuery -- Számlalánc kivonat lekérdezés számlaszám paramétere
    Invoice number param of the invoice chain digest query

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceRequestType
    def __init__(self, header=None, user=None, software=None, page=None, invoiceChainQuery=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryInvoiceChainDigestRequestType"), self).__init__(header, user, software, extensiontype_,  **kwargs_)
        self.page = page
        self.validate_RequestPageType(self.page)
        self.page_nsprefix_ = "common"
        self.invoiceChainQuery = invoiceChainQuery
        self.invoiceChainQuery_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryInvoiceChainDigestRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryInvoiceChainDigestRequestType.subclass:
            return QueryInvoiceChainDigestRequestType.subclass(*args_, **kwargs_)
        else:
            return QueryInvoiceChainDigestRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_page(self):
        return self.page
    def set_page(self, page):
        self.page = page
    def get_invoiceChainQuery(self):
        return self.invoiceChainQuery
    def set_invoiceChainQuery(self, invoiceChainQuery):
        self.invoiceChainQuery = invoiceChainQuery
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_RequestPageType(self, value):
        result = True
        # Validate type RequestPageType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on RequestPageType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.page is not None or
            self.invoiceChainQuery is not None or
            super(QueryInvoiceChainDigestRequestType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryInvoiceChainDigestRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryInvoiceChainDigestRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryInvoiceChainDigestRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryInvoiceChainDigestRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryInvoiceChainDigestRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryInvoiceChainDigestRequestType'):
        super(QueryInvoiceChainDigestRequestType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryInvoiceChainDigestRequestType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryInvoiceChainDigestRequestType', fromsubclass_=False, pretty_print=True):
        super(QueryInvoiceChainDigestRequestType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.page is not None:
            namespaceprefix_ = self.page_nsprefix_ + ':' if (UseCapturedNS_ and self.page_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spage>%s</%spage>%s' % (namespaceprefix_ , self.gds_format_integer(self.page, input_name='page'), namespaceprefix_ , eol_))
        if self.invoiceChainQuery is not None:
            namespaceprefix_ = self.invoiceChainQuery_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceChainQuery_nsprefix_) else ''
            self.invoiceChainQuery.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceChainQuery', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryInvoiceChainDigestRequestType', mapping_=None, nsmap_=None):
        element = super(QueryInvoiceChainDigestRequestType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.page is not None:
            page_ = self.page
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}page').text = self.gds_format_integer(page_)
        if self.invoiceChainQuery is not None:
            invoiceChainQuery_ = self.invoiceChainQuery
            invoiceChainQuery_.to_etree(element, name_='invoiceChainQuery', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryInvoiceChainDigestRequestType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryInvoiceChainDigestRequestType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryInvoiceChainDigestRequestType, self)._exportLiteralChildren(outfile, level, name_)
        if self.page is not None:
            showIndent(outfile, level)
            outfile.write('page=%d,\n' % self.page)
        if self.invoiceChainQuery is not None:
            showIndent(outfile, level)
            outfile.write('invoiceChainQuery=model_.InvoiceChainQueryType(\n')
            self.invoiceChainQuery.exportLiteral(outfile, level, name_='invoiceChainQuery')
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
        super(QueryInvoiceChainDigestRequestType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'page' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'page')
            ival_ = self.gds_validate_integer(ival_, node, 'page')
            self.page = ival_
            self.page_nsprefix_ = child_.prefix
            # validate type RequestPageType
            self.validate_RequestPageType(self.page)
        elif nodeName_ == 'invoiceChainQuery':
            obj_ = InvoiceChainQueryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceChainQuery = obj_
            obj_.original_tagname_ = 'invoiceChainQuery'
        super(QueryInvoiceChainDigestRequestType, self)._buildChildren(child_, node, nodeName_, True)
