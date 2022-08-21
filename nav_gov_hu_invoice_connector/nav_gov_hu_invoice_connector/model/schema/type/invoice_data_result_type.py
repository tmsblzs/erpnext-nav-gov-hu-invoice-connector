import base64

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, raise_parse_error
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.audit_data_type import AuditDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.crypto_type import CryptoType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceDataResultType(GeneratedsSuper):
    """InvoiceDataResultType -- Számlaszámra történőlekérdezés eredménye
    Invoice number based query result
    invoiceData -- Számla adatok BASE64-ben kódolt tartalma
            Invoice data in BASE64 encoded form
    auditData -- A számla audit adatai
            Invoice audit data
    compressedContentIndicator -- Jelöli, ha az invoice tartalmát a BASE64 dekódolást követően még ki kell tömöríteni az olvasáshoz
            Indicates if the content of the invoice needs to be decompressed to be read following the BASE64 decoding
    electronicInvoiceHash -- Elektronikus számla vagy módosító okirat állomány hash lenyomata
            Electronic invoice or modification document file hash value

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, invoiceData=None, auditData=None, compressedContentIndicator=None, electronicInvoiceHash=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceData = invoiceData
        self.invoiceData_nsprefix_ = "xs"
        self.auditData = auditData
        self.auditData_nsprefix_ = None
        self.compressedContentIndicator = compressedContentIndicator
        self.compressedContentIndicator_nsprefix_ = "xs"
        self.electronicInvoiceHash = electronicInvoiceHash
        self.electronicInvoiceHash_nsprefix_ = "common"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceDataResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceDataResultType.subclass:
            return InvoiceDataResultType.subclass(*args_, **kwargs_)
        else:
            return InvoiceDataResultType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_invoiceData(self):
        return self.invoiceData

    def set_invoiceData(self, invoiceData):
        self.invoiceData = invoiceData

    def get_auditData(self):
        return self.auditData

    def set_auditData(self, auditData):
        self.auditData = auditData

    def get_compressedContentIndicator(self):
        return self.compressedContentIndicator

    def set_compressedContentIndicator(self, compressedContentIndicator):
        self.compressedContentIndicator = compressedContentIndicator

    def get_electronicInvoiceHash(self):
        return self.electronicInvoiceHash

    def set_electronicInvoiceHash(self, electronicInvoiceHash):
        self.electronicInvoiceHash = electronicInvoiceHash

    def _hasContent(self):
        if (
                self.invoiceData is not None or
                self.auditData is not None or
                self.compressedContentIndicator is not None or
                self.electronicInvoiceHash is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
               name_='InvoiceDataResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceDataResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceDataResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceDataResultType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceDataResultType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceDataResultType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
                        name_='InvoiceDataResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceData is not None:
            namespaceprefix_ = self.invoiceData_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceData_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceData>%s</%sinvoiceData>%s' % (
            namespaceprefix_, self.gds_format_base64(self.invoiceData, input_name='invoiceData'), namespaceprefix_,
            eol_))
        if self.auditData is not None:
            namespaceprefix_ = self.auditData_nsprefix_ + ':' if (UseCapturedNS_ and self.auditData_nsprefix_) else ''
            self.auditData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='auditData',
                                  pretty_print=pretty_print)
        if self.compressedContentIndicator is not None:
            namespaceprefix_ = self.compressedContentIndicator_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.compressedContentIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompressedContentIndicator>%s</%scompressedContentIndicator>%s' % (namespaceprefix_,
                                                                                                 self.gds_format_boolean(
                                                                                                     self.compressedContentIndicator,
                                                                                                     input_name='compressedContentIndicator'),
                                                                                                 namespaceprefix_,
                                                                                                 eol_))
        if self.electronicInvoiceHash is not None:
            namespaceprefix_ = self.electronicInvoiceHash_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.electronicInvoiceHash_nsprefix_) else ''
            self.electronicInvoiceHash.export(outfile, level, namespaceprefix_, namespacedef_='',
                                              name_='electronicInvoiceHash', pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='InvoiceDataResultType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.invoiceData is not None:
            invoiceData_ = self.invoiceData
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceData').text = self.gds_format_base64(
                invoiceData_)
        if self.auditData is not None:
            auditData_ = self.auditData
            auditData_.to_etree(element, name_='auditData', mapping_=mapping_, nsmap_=nsmap_)
        if self.compressedContentIndicator is not None:
            compressedContentIndicator_ = self.compressedContentIndicator
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}compressedContentIndicator').text = self.gds_format_boolean(
                compressedContentIndicator_)
        if self.electronicInvoiceHash is not None:
            electronicInvoiceHash_ = self.electronicInvoiceHash
            electronicInvoiceHash_.to_etree(element, name_='electronicInvoiceHash', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceDataResultType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceData is not None:
            showIndent(outfile, level)
            outfile.write('invoiceData=model_.base64Binary(\n')
            self.invoiceData.exportLiteral(outfile, level, name_='invoiceData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.auditData is not None:
            showIndent(outfile, level)
            outfile.write('auditData=model_.AuditDataType(\n')
            self.auditData.exportLiteral(outfile, level, name_='auditData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.compressedContentIndicator is not None:
            showIndent(outfile, level)
            outfile.write('compressedContentIndicator=%s,\n' % self.compressedContentIndicator)
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
        if nodeName_ == 'invoiceData':
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
        elif nodeName_ == 'auditData':
            obj_ = AuditDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.auditData = obj_
            obj_.original_tagname_ = 'auditData'
        elif nodeName_ == 'compressedContentIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'compressedContentIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'compressedContentIndicator')
            self.compressedContentIndicator = ival_
            self.compressedContentIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'electronicInvoiceHash':
            obj_ = CryptoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.electronicInvoiceHash = obj_
            obj_.original_tagname_ = 'electronicInvoiceHash'
