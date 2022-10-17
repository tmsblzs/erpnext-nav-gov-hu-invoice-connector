import base64
import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, raise_parse_error
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.business_validation_result_type import \
    BusinessValidationResultType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.technical_validation_result_type import \
    TechnicalValidationResultType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ProcessingResultType(GeneratedsSuper):
    """ProcessingResultType -- Számla feldolgozási eredmény
    Invoice processing result
    index -- A számla sorszáma a kérésen belül
    Sequence number of the invoice within the request
    batchIndex -- A módosító okirat sorszáma a kötegen belül
    Sequence number of the modification document within the batch
    invoiceStatus -- A számla feldolgozási státusza
    Processing status of the invoice
    technicalValidationMessages -- Technikai validációs üzenetek
    Technical validation messages
    businessValidationMessages -- Üzleti validációs üzenetek
    Business validation messages
    compressedContentIndicator -- Jelöli, ha az originalRequest tartalmát a BASE64 dekódolást követően
        még ki kell tömöríteni az olvasáshoz
    Indicates if the content of the originalRequest needs to be decompressed to be read following the BASE64 decoding
    originalRequest -- Számla adatok BASE64-ben kódolt tartalma
    Invoice data in BASE64 encoded form

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, index=None, batchIndex=None, invoiceStatus=None, technicalValidationMessages=None, businessValidationMessages=None, compressedContentIndicator=None, originalRequest=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.index = index
        self.validate_InvoiceIndexType(self.index)
        self.index_nsprefix_ = "base"
        self.batchIndex = batchIndex
        self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        self.batchIndex_nsprefix_ = "base"
        self.invoiceStatus = invoiceStatus
        self.validate_InvoiceStatusType(self.invoiceStatus)
        self.invoiceStatus_nsprefix_ = None
        if technicalValidationMessages is None:
            self.technicalValidationMessages = []
        else:
            self.technicalValidationMessages = technicalValidationMessages
        self.technicalValidationMessages_nsprefix_ = "common"
        if businessValidationMessages is None:
            self.businessValidationMessages = []
        else:
            self.businessValidationMessages = businessValidationMessages
        self.businessValidationMessages_nsprefix_ = None
        self.compressedContentIndicator = compressedContentIndicator
        self.compressedContentIndicator_nsprefix_ = "xs"
        self.originalRequest = originalRequest
        self.originalRequest_nsprefix_ = "xs"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProcessingResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProcessingResultType.subclass:
            return ProcessingResultType.subclass(*args_, **kwargs_)
        else:
            return ProcessingResultType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_batchIndex(self):
        return self.batchIndex
    def set_batchIndex(self, batchIndex):
        self.batchIndex = batchIndex
    def get_invoiceStatus(self):
        return self.invoiceStatus
    def set_invoiceStatus(self, invoiceStatus):
        self.invoiceStatus = invoiceStatus
    def get_technicalValidationMessages(self):
        return self.technicalValidationMessages
    def set_technicalValidationMessages(self, technicalValidationMessages):
        self.technicalValidationMessages = technicalValidationMessages
    def add_technicalValidationMessages(self, value):
        self.technicalValidationMessages.append(value)
    def insert_technicalValidationMessages_at(self, index, value):
        self.technicalValidationMessages.insert(index, value)
    def replace_technicalValidationMessages_at(self, index, value):
        self.technicalValidationMessages[index] = value
    def get_businessValidationMessages(self):
        return self.businessValidationMessages
    def set_businessValidationMessages(self, businessValidationMessages):
        self.businessValidationMessages = businessValidationMessages
    def add_businessValidationMessages(self, value):
        self.businessValidationMessages.append(value)
    def insert_businessValidationMessages_at(self, index, value):
        self.businessValidationMessages.insert(index, value)
    def replace_businessValidationMessages_at(self, index, value):
        self.businessValidationMessages[index] = value
    def get_compressedContentIndicator(self):
        return self.compressedContentIndicator
    def set_compressedContentIndicator(self, compressedContentIndicator):
        self.compressedContentIndicator = compressedContentIndicator
    def get_originalRequest(self):
        return self.originalRequest
    def set_originalRequest(self, originalRequest):
        self.originalRequest = originalRequest
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
    def validate_InvoiceUnboundedIndexType(self, value):
        result = True
        # Validate type InvoiceUnboundedIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceUnboundedIndexType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_InvoiceStatusType(self, value):
        result = True
        # Validate type InvoiceStatusType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['RECEIVED', 'PROCESSING', 'SAVED', 'DONE', 'ABORTED']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on InvoiceStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on InvoiceStatusType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on InvoiceStatusType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.index is not None or
            self.batchIndex is not None or
            self.invoiceStatus is not None or
            self.technicalValidationMessages or
            self.businessValidationMessages or
            self.compressedContentIndicator is not None or
            self.originalRequest is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='ProcessingResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProcessingResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProcessingResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProcessingResultType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProcessingResultType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProcessingResultType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='ProcessingResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.index is not None:
            namespaceprefix_ = self.index_nsprefix_ + ':' if (UseCapturedNS_ and self.index_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindex>%s</%sindex>%s' % (namespaceprefix_ , self.gds_format_integer(self.index, input_name='index'), namespaceprefix_ , eol_))
        if self.batchIndex is not None:
            namespaceprefix_ = self.batchIndex_nsprefix_ + ':' if (UseCapturedNS_ and self.batchIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbatchIndex>%s</%sbatchIndex>%s' % (namespaceprefix_ , self.gds_format_integer(self.batchIndex, input_name='batchIndex'), namespaceprefix_ , eol_))
        if self.invoiceStatus is not None:
            namespaceprefix_ = self.invoiceStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceStatus>%s</%sinvoiceStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceStatus), input_name='invoiceStatus')), namespaceprefix_ , eol_))
        for technicalValidationMessages_ in self.technicalValidationMessages:
            namespaceprefix_ = self.technicalValidationMessages_nsprefix_ + ':' if (UseCapturedNS_ and self.technicalValidationMessages_nsprefix_) else ''
            technicalValidationMessages_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='technicalValidationMessages', pretty_print=pretty_print)
        for businessValidationMessages_ in self.businessValidationMessages:
            namespaceprefix_ = self.businessValidationMessages_nsprefix_ + ':' if (UseCapturedNS_ and self.businessValidationMessages_nsprefix_) else ''
            businessValidationMessages_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='businessValidationMessages', pretty_print=pretty_print)
        if self.compressedContentIndicator is not None:
            namespaceprefix_ = self.compressedContentIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.compressedContentIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompressedContentIndicator>%s</%scompressedContentIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.compressedContentIndicator, input_name='compressedContentIndicator'), namespaceprefix_ , eol_))
        if self.originalRequest is not None:
            namespaceprefix_ = self.originalRequest_nsprefix_ + ':' if (UseCapturedNS_ and self.originalRequest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalRequest>%s</%soriginalRequest>%s' % (namespaceprefix_ , self.gds_format_base64(self.originalRequest, input_name='originalRequest'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProcessingResultType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.index is not None:
            index_ = self.index
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}index').text = self.gds_format_integer(index_)
        if self.batchIndex is not None:
            batchIndex_ = self.batchIndex
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex').text = self.gds_format_integer(batchIndex_)
        if self.invoiceStatus is not None:
            invoiceStatus_ = self.invoiceStatus
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceStatus').text = self.gds_format_string(invoiceStatus_)
        for technicalValidationMessages_ in self.technicalValidationMessages:
            technicalValidationMessages_.to_etree(element, name_='technicalValidationMessages', mapping_=mapping_, nsmap_=nsmap_)
        for businessValidationMessages_ in self.businessValidationMessages:
            businessValidationMessages_.to_etree(element, name_='businessValidationMessages', mapping_=mapping_, nsmap_=nsmap_)
        if self.compressedContentIndicator is not None:
            compressedContentIndicator_ = self.compressedContentIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}compressedContentIndicator').text = self.gds_format_boolean(compressedContentIndicator_)
        if self.originalRequest is not None:
            originalRequest_ = self.originalRequest
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}originalRequest').text = self.gds_format_base64(originalRequest_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProcessingResultType'):
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
        if self.batchIndex is not None:
            showIndent(outfile, level)
            outfile.write('batchIndex=%d,\n' % self.batchIndex)
        if self.invoiceStatus is not None:
            showIndent(outfile, level)
            outfile.write('invoiceStatus=%s,\n' % self.gds_encode(quote_python(self.invoiceStatus)))
        showIndent(outfile, level)
        outfile.write('technicalValidationMessages=[\n')
        level += 1
        for technicalValidationMessages_ in self.technicalValidationMessages:
            showIndent(outfile, level)
            outfile.write('model_.TechnicalValidationResultType(\n')
            technicalValidationMessages_.exportLiteral(outfile, level, name_='TechnicalValidationResultType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('businessValidationMessages=[\n')
        level += 1
        for businessValidationMessages_ in self.businessValidationMessages:
            showIndent(outfile, level)
            outfile.write('model_.BusinessValidationResultType(\n')
            businessValidationMessages_.exportLiteral(outfile, level, name_='BusinessValidationResultType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.compressedContentIndicator is not None:
            showIndent(outfile, level)
            outfile.write('compressedContentIndicator=%s,\n' % self.compressedContentIndicator)
        if self.originalRequest is not None:
            showIndent(outfile, level)
            outfile.write('originalRequest=model_.base64Binary(\n')
            self.originalRequest.exportLiteral(outfile, level, name_='originalRequest')
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
        elif nodeName_ == 'batchIndex' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'batchIndex')
            ival_ = self.gds_validate_integer(ival_, node, 'batchIndex')
            self.batchIndex = ival_
            self.batchIndex_nsprefix_ = child_.prefix
            # validate type InvoiceUnboundedIndexType
            self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        elif nodeName_ == 'invoiceStatus':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceStatus')
            value_ = self.gds_validate_string(value_, node, 'invoiceStatus')
            self.invoiceStatus = value_
            self.invoiceStatus_nsprefix_ = child_.prefix
            # validate type InvoiceStatusType
            self.validate_InvoiceStatusType(self.invoiceStatus)
        elif nodeName_ == 'technicalValidationMessages':
            obj_ = TechnicalValidationResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.technicalValidationMessages.append(obj_)
            obj_.original_tagname_ = 'technicalValidationMessages'
        elif nodeName_ == 'businessValidationMessages':
            obj_ = BusinessValidationResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.businessValidationMessages.append(obj_)
            obj_.original_tagname_ = 'businessValidationMessages'
        elif nodeName_ == 'compressedContentIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'compressedContentIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'compressedContentIndicator')
            self.compressedContentIndicator = ival_
            self.compressedContentIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'originalRequest':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'originalRequest')
            else:
                bval_ = None
            self.originalRequest = bval_
            self.originalRequest_nsprefix_ = child_.prefix
