import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_request_type import \
    BasicOnlineInvoiceRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_query_params_type import \
    InvoiceQueryParamsType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class QueryInvoiceDigestRequestType(BasicOnlineInvoiceRequestType):
    """QueryInvoiceDigestRequestType -- A POST /queryInvoiceDigest REST operáció kérés típusa
    Request type of the POST /queryInvoiceDigest REST operation
    page -- A lekérdezni kívánt lap száma
    The queried page count
    invoiceDirection -- Kimenő vagy bejövő számla keresési paramétere
    Inbound or outbound invoice query parameter
    invoiceQueryParams -- Számla lekérdezési paraméterek
    Invoice query parameters

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceRequestType
    def __init__(self, header=None, user=None, software=None, page=None, invoiceDirection=None, invoiceQueryParams=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryInvoiceDigestRequestType"), self).__init__(header, user, software, extensiontype_,  **kwargs_)
        self.page = page
        self.validate_RequestPageType(self.page)
        self.page_nsprefix_ = "common"
        self.invoiceDirection = invoiceDirection
        self.validate_InvoiceDirectionType(self.invoiceDirection)
        self.invoiceDirection_nsprefix_ = None
        self.invoiceQueryParams = invoiceQueryParams
        self.invoiceQueryParams_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryInvoiceDigestRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryInvoiceDigestRequestType.subclass:
            return QueryInvoiceDigestRequestType.subclass(*args_, **kwargs_)
        else:
            return QueryInvoiceDigestRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_page(self):
        return self.page
    def set_page(self, page):
        self.page = page
    def get_invoiceDirection(self):
        return self.invoiceDirection
    def set_invoiceDirection(self, invoiceDirection):
        self.invoiceDirection = invoiceDirection
    def get_invoiceQueryParams(self):
        return self.invoiceQueryParams
    def set_invoiceQueryParams(self, invoiceQueryParams):
        self.invoiceQueryParams = invoiceQueryParams
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
    def validate_InvoiceDirectionType(self, value):
        result = True
        # Validate type InvoiceDirectionType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['INBOUND', 'OUTBOUND']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on InvoiceDirectionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on InvoiceDirectionType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on InvoiceDirectionType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.page is not None or
            self.invoiceDirection is not None or
            self.invoiceQueryParams is not None or
            super(QueryInvoiceDigestRequestType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryInvoiceDigestRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryInvoiceDigestRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryInvoiceDigestRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryInvoiceDigestRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryInvoiceDigestRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryInvoiceDigestRequestType'):
        super(QueryInvoiceDigestRequestType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryInvoiceDigestRequestType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryInvoiceDigestRequestType', fromsubclass_=False, pretty_print=True):
        super(QueryInvoiceDigestRequestType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.page is not None:
            namespaceprefix_ = self.page_nsprefix_ + ':' if (UseCapturedNS_ and self.page_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spage>%s</%spage>%s' % (namespaceprefix_ , self.gds_format_integer(self.page, input_name='page'), namespaceprefix_ , eol_))
        if self.invoiceDirection is not None:
            namespaceprefix_ = self.invoiceDirection_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceDirection_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceDirection>%s</%sinvoiceDirection>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceDirection), input_name='invoiceDirection')), namespaceprefix_ , eol_))
        if self.invoiceQueryParams is not None:
            namespaceprefix_ = self.invoiceQueryParams_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceQueryParams_nsprefix_) else ''
            self.invoiceQueryParams.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceQueryParams', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryInvoiceDigestRequestType', mapping_=None, nsmap_=None):
        element = super(QueryInvoiceDigestRequestType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.page is not None:
            page_ = self.page
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}page').text = self.gds_format_integer(page_)
        if self.invoiceDirection is not None:
            invoiceDirection_ = self.invoiceDirection
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDirection').text = self.gds_format_string(invoiceDirection_)
        if self.invoiceQueryParams is not None:
            invoiceQueryParams_ = self.invoiceQueryParams
            invoiceQueryParams_.to_etree(element, name_='invoiceQueryParams', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryInvoiceDigestRequestType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryInvoiceDigestRequestType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryInvoiceDigestRequestType, self)._exportLiteralChildren(outfile, level, name_)
        if self.page is not None:
            showIndent(outfile, level)
            outfile.write('page=%d,\n' % self.page)
        if self.invoiceDirection is not None:
            showIndent(outfile, level)
            outfile.write('invoiceDirection=%s,\n' % self.gds_encode(quote_python(self.invoiceDirection)))
        if self.invoiceQueryParams is not None:
            showIndent(outfile, level)
            outfile.write('invoiceQueryParams=model_.InvoiceQueryParamsType(\n')
            self.invoiceQueryParams.exportLiteral(outfile, level, name_='invoiceQueryParams')
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
        super(QueryInvoiceDigestRequestType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'page' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'page')
            ival_ = self.gds_validate_integer(ival_, node, 'page')
            self.page = ival_
            self.page_nsprefix_ = child_.prefix
            # validate type RequestPageType
            self.validate_RequestPageType(self.page)
        elif nodeName_ == 'invoiceDirection':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceDirection')
            value_ = self.gds_validate_string(value_, node, 'invoiceDirection')
            self.invoiceDirection = value_
            self.invoiceDirection_nsprefix_ = child_.prefix
            # validate type InvoiceDirectionType
            self.validate_InvoiceDirectionType(self.invoiceDirection)
        elif nodeName_ == 'invoiceQueryParams':
            obj_ = InvoiceQueryParamsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceQueryParams = obj_
            obj_.original_tagname_ = 'invoiceQueryParams'
        super(QueryInvoiceDigestRequestType, self)._buildChildren(child_, node, nodeName_, True)
