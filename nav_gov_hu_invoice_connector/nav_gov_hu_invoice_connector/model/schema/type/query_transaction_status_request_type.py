import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_request_type import \
    BasicOnlineInvoiceRequestType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class QueryTransactionStatusRequestType(BasicOnlineInvoiceRequestType):
    """QueryTransactionStatusRequestType -- A POST /queryTransactionStatus REST operáció kérés típusa
    Request type of the POST /queryTransactionStatus REST operation
    transactionId -- Az adatszolgáltatás tranzakció azonosítója
    Transaction identifier of the data exchange
    returnOriginalRequest -- Jelöli, ha a kliensáltal beküldött eredeti tartalmat is vissza kell adni a válaszban
    Indicates if the original client data should also be returned in the response

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceRequestType
    def __init__(self, header=None, user=None, software=None, transactionId=None, returnOriginalRequest=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryTransactionStatusRequestType"), self).__init__(header, user, software, extensiontype_,  **kwargs_)
        self.transactionId = transactionId
        self.validate_EntityIdType(self.transactionId)
        self.transactionId_nsprefix_ = "common"
        self.returnOriginalRequest = returnOriginalRequest
        self.returnOriginalRequest_nsprefix_ = "xs"
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryTransactionStatusRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryTransactionStatusRequestType.subclass:
            return QueryTransactionStatusRequestType.subclass(*args_, **kwargs_)
        else:
            return QueryTransactionStatusRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_returnOriginalRequest(self):
        return self.returnOriginalRequest
    def set_returnOriginalRequest(self, returnOriginalRequest):
        self.returnOriginalRequest = returnOriginalRequest
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_EntityIdType(self, value):
        result = True
        # Validate type EntityIdType, a restriction on AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EntityIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_EntityIdType_patterns_, ))
                result = False
        return result
    validate_EntityIdType_patterns_ = [['^([+a-zA-Z0-9_]{1,30})$']]
    def _hasContent(self):
        if (
            self.transactionId is not None or
            self.returnOriginalRequest is not None or
            super(QueryTransactionStatusRequestType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='QueryTransactionStatusRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryTransactionStatusRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryTransactionStatusRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryTransactionStatusRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryTransactionStatusRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryTransactionStatusRequestType'):
        super(QueryTransactionStatusRequestType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryTransactionStatusRequestType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='QueryTransactionStatusRequestType', fromsubclass_=False, pretty_print=True):
        super(QueryTransactionStatusRequestType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transactionId), input_name='transactionId')), namespaceprefix_ , eol_))
        if self.returnOriginalRequest is not None:
            namespaceprefix_ = self.returnOriginalRequest_nsprefix_ + ':' if (UseCapturedNS_ and self.returnOriginalRequest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreturnOriginalRequest>%s</%sreturnOriginalRequest>%s' % (namespaceprefix_ , self.gds_format_boolean(self.returnOriginalRequest, input_name='returnOriginalRequest'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='QueryTransactionStatusRequestType', mapping_=None, nsmap_=None):
        element = super(QueryTransactionStatusRequestType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.transactionId is not None:
            transactionId_ = self.transactionId
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}transactionId').text = self.gds_format_string(transactionId_)
        if self.returnOriginalRequest is not None:
            returnOriginalRequest_ = self.returnOriginalRequest
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}returnOriginalRequest').text = self.gds_format_boolean(returnOriginalRequest_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryTransactionStatusRequestType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryTransactionStatusRequestType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryTransactionStatusRequestType, self)._exportLiteralChildren(outfile, level, name_)
        if self.transactionId is not None:
            showIndent(outfile, level)
            outfile.write('transactionId=%s,\n' % self.gds_encode(quote_python(self.transactionId)))
        if self.returnOriginalRequest is not None:
            showIndent(outfile, level)
            outfile.write('returnOriginalRequest=%s,\n' % self.returnOriginalRequest)
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
        super(QueryTransactionStatusRequestType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'transactionId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transactionId')
            value_ = self.gds_validate_string(value_, node, 'transactionId')
            self.transactionId = value_
            self.transactionId_nsprefix_ = child_.prefix
            # validate type EntityIdType
            self.validate_EntityIdType(self.transactionId)
        elif nodeName_ == 'returnOriginalRequest':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'returnOriginalRequest')
            ival_ = self.gds_validate_boolean(ival_, node, 'returnOriginalRequest')
            self.returnOriginalRequest = ival_
            self.returnOriginalRequest_nsprefix_ = child_.prefix
        super(QueryTransactionStatusRequestType, self)._buildChildren(child_, node, nodeName_, True)
