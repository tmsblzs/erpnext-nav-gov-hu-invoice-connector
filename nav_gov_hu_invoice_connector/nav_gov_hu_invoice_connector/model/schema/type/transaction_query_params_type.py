import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class TransactionQueryParamsType(GeneratedsSuper):
    """TransactionQueryParamsType -- A számla lekérdezés tranzakciós paraméterei
    Transactional params of the invoice query
    transactionId -- Az adatszolgáltatás tranzakció azonosítója
    Transaction identifier of the data exchange
    index -- A számla sorszáma a kérésen belül
    Sequence number of the invoice within the request
    invoiceOperation -- Számlaművelet típus
    Invoice operation type

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, transactionId=None, index=None, invoiceOperation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.transactionId = transactionId
        self.validate_EntityIdType(self.transactionId)
        self.transactionId_nsprefix_ = "common"
        self.index = index
        self.validate_InvoiceIndexType(self.index)
        self.index_nsprefix_ = "base"
        self.invoiceOperation = invoiceOperation
        self.validate_ManageInvoiceOperationType(self.invoiceOperation)
        self.invoiceOperation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransactionQueryParamsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransactionQueryParamsType.subclass:
            return TransactionQueryParamsType.subclass(*args_, **kwargs_)
        else:
            return TransactionQueryParamsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_invoiceOperation(self):
        return self.invoiceOperation
    def set_invoiceOperation(self, invoiceOperation):
        self.invoiceOperation = invoiceOperation
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
    def validate_InvoiceIndexType(self, value):
        result = True
        # Validate type InvoiceIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceIndexType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on InvoiceIndexType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_ManageInvoiceOperationType(self, value):
        result = True
        # Validate type ManageInvoiceOperationType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['CREATE', 'MODIFY', 'STORNO']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ManageInvoiceOperationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ManageInvoiceOperationType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ManageInvoiceOperationType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.transactionId is not None or
            self.index is not None or
            self.invoiceOperation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='TransactionQueryParamsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransactionQueryParamsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransactionQueryParamsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransactionQueryParamsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransactionQueryParamsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TransactionQueryParamsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='TransactionQueryParamsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transactionId), input_name='transactionId')), namespaceprefix_ , eol_))
        if self.index is not None:
            namespaceprefix_ = self.index_nsprefix_ + ':' if (UseCapturedNS_ and self.index_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindex>%s</%sindex>%s' % (namespaceprefix_ , self.gds_format_integer(self.index, input_name='index'), namespaceprefix_ , eol_))
        if self.invoiceOperation is not None:
            namespaceprefix_ = self.invoiceOperation_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceOperation>%s</%sinvoiceOperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceOperation), input_name='invoiceOperation')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TransactionQueryParamsType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.transactionId is not None:
            transactionId_ = self.transactionId
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}transactionId').text = self.gds_format_string(transactionId_)
        if self.index is not None:
            index_ = self.index
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}index').text = self.gds_format_integer(index_)
        if self.invoiceOperation is not None:
            invoiceOperation_ = self.invoiceOperation
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation').text = self.gds_format_string(invoiceOperation_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TransactionQueryParamsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.transactionId is not None:
            showIndent(outfile, level)
            outfile.write('transactionId=%s,\n' % self.gds_encode(quote_python(self.transactionId)))
        if self.index is not None:
            showIndent(outfile, level)
            outfile.write('index=%d,\n' % self.index)
        if self.invoiceOperation is not None:
            showIndent(outfile, level)
            outfile.write('invoiceOperation=%s,\n' % self.gds_encode(quote_python(self.invoiceOperation)))
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
        if nodeName_ == 'transactionId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transactionId')
            value_ = self.gds_validate_string(value_, node, 'transactionId')
            self.transactionId = value_
            self.transactionId_nsprefix_ = child_.prefix
            # validate type EntityIdType
            self.validate_EntityIdType(self.transactionId)
        elif nodeName_ == 'index' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'index')
            ival_ = self.gds_validate_integer(ival_, node, 'index')
            self.index = ival_
            self.index_nsprefix_ = child_.prefix
            # validate type InvoiceIndexType
            self.validate_InvoiceIndexType(self.index)
        elif nodeName_ == 'invoiceOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceOperation')
            value_ = self.gds_validate_string(value_, node, 'invoiceOperation')
            self.invoiceOperation = value_
            self.invoiceOperation_nsprefix_ = child_.prefix
            # validate type ManageInvoiceOperationType
            self.validate_ManageInvoiceOperationType(self.invoiceOperation)
