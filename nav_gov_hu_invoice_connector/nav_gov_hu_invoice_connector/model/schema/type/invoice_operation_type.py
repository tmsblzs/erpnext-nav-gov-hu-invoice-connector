import base64

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, raise_parse_error
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.crypto_type import CryptoType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceOperationType(GeneratedsSuper):
    """InvoiceOperationType -- A kéréshez tartozó számlaművelet
    Invoice operation of the request
    index -- A számla sorszáma a kérésen belül
            Sequence number of the invoice within the request
    invoiceOperation -- A kért számla művelet típusa
            Type of the desired invoice operation
    invoiceData -- Számla adatok BASE64-ben kódolt tartalma
            Invoice data in BASE64 encoded form
    electronicInvoiceHash -- Elektronikus számla vagy módosító okirat állomány hash lenyomata
            Electronic invoice or modification document file hash value

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, index=None, invoiceOperation=None, invoiceData=None, electronicInvoiceHash=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.index = index
        self.validate_InvoiceIndexType(self.index)
        self.index_nsprefix_ = "base"
        self.invoiceOperation = invoiceOperation
        self.validate_ManageInvoiceOperationType(self.invoiceOperation)
        self.invoiceOperation_nsprefix_ = None
        self.invoiceData = invoiceData
        self.invoiceData_nsprefix_ = "xs"
        self.electronicInvoiceHash = electronicInvoiceHash
        self.electronicInvoiceHash_nsprefix_ = "common"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceOperationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceOperationType.subclass:
            return InvoiceOperationType.subclass(*args_, **kwargs_)
        else:
            return InvoiceOperationType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_invoiceOperation(self):
        return self.invoiceOperation

    def set_invoiceOperation(self, invoiceOperation):
        self.invoiceOperation = invoiceOperation

    def get_invoiceData(self):
        return self.invoiceData

    def set_invoiceData(self, invoiceData):
        self.invoiceData = invoiceData

    def get_electronicInvoiceHash(self):
        return self.electronicInvoiceHash

    def set_electronicInvoiceHash(self, electronicInvoiceHash):
        self.electronicInvoiceHash = electronicInvoiceHash

    def validate_InvoiceIndexType(self, value):
        result = True
        # Validate type InvoiceIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceIndexType' % {
                        "value": value, "lineno": lineno})
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on InvoiceIndexType' % {
                        "value": value, "lineno": lineno})
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
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ManageInvoiceOperationType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ManageInvoiceOperationType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ManageInvoiceOperationType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.index is not None or
                self.invoiceOperation is not None or
                self.invoiceData is not None or
                self.electronicInvoiceHash is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
               name_='InvoiceOperationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceOperationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceOperationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceOperationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceOperationType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceOperationType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
                        name_='InvoiceOperationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.index is not None:
            namespaceprefix_ = self.index_nsprefix_ + ':' if (UseCapturedNS_ and self.index_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindex>%s</%sindex>%s' % (
            namespaceprefix_, self.gds_format_integer(self.index, input_name='index'), namespaceprefix_, eol_))
        if self.invoiceOperation is not None:
            namespaceprefix_ = self.invoiceOperation_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceOperation>%s</%sinvoiceOperation>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.invoiceOperation), input_name='invoiceOperation')),
                                                                             namespaceprefix_, eol_))
        if self.invoiceData is not None:
            namespaceprefix_ = self.invoiceData_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceData_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceData>%s</%sinvoiceData>%s' % (
            namespaceprefix_, self.gds_format_base64(self.invoiceData, input_name='invoiceData'), namespaceprefix_,
            eol_))
        if self.electronicInvoiceHash is not None:
            namespaceprefix_ = self.electronicInvoiceHash_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.electronicInvoiceHash_nsprefix_) else ''
            self.electronicInvoiceHash.export(outfile, level, namespaceprefix_, namespacedef_='',
                                              name_='electronicInvoiceHash', pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='InvoiceOperationType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.index is not None:
            index_ = self.index
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}index').text = self.gds_format_integer(
                index_)
        if self.invoiceOperation is not None:
            invoiceOperation_ = self.invoiceOperation
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation').text = self.gds_format_string(
                invoiceOperation_)
        if self.invoiceData is not None:
            invoiceData_ = self.invoiceData
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceData').text = self.gds_format_base64(
                invoiceData_)
        if self.electronicInvoiceHash is not None:
            electronicInvoiceHash_ = self.electronicInvoiceHash
            electronicInvoiceHash_.to_etree(element, name_='electronicInvoiceHash', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceOperationType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.index is not None:
            showIndent(outfile, level)
            outfile.write('index=%d,\n' % self.index)
        if self.invoiceOperation is not None:
            showIndent(outfile, level)
            outfile.write('invoiceOperation=%s,\n' % self.gds_encode(quote_python(self.invoiceOperation)))
        if self.invoiceData is not None:
            showIndent(outfile, level)
            outfile.write('invoiceData=model_.base64Binary(\n')
            self.invoiceData.exportLiteral(outfile, level, name_='invoiceData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.electronicInvoiceHash is not None:
            showIndent(outfile, level)
            outfile.write('electronicInvoiceHash=model_.CryptoType(\n')
            self.electronicInvoiceHash.exportLiteral(outfile, level, name_='electronicInvoiceHash')
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
        if nodeName_ == 'index' and child_.text:
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
        elif nodeName_ == 'invoiceData':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'invoiceData')
            else:
                bval_ = None
            self.invoiceData = bval_
            self.invoiceData_nsprefix_ = child_.prefix
        elif nodeName_ == 'electronicInvoiceHash':
            obj_ = CryptoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.electronicInvoiceHash = obj_
            obj_.original_tagname_ = 'electronicInvoiceHash'
