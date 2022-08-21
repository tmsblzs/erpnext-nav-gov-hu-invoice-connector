import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceChainDigestType(GeneratedsSuper):
    """InvoiceChainDigestType -- Számlalánc kivonat adatok
    Invoice chain digest data
    invoiceNumber -- Számla vagy módosító okirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pont
            Sequential number of the original invoice or modification document
                - section 169 (b) or section 170 (1) b) of the VAT law
    batchIndex -- A módosító okirat sorszáma a kötegen belül
            Sequence number of the modification document within the batch
    invoiceOperation -- Számlaművelet típus
            Invoice operation type
    supplierTaxNumber -- A kibocsátó adószáma
            The supplier's tax number
    customerTaxNumber -- A vevő adószáma
            The buyer's tax number
    insDate -- A beszúrás időpontja UTC időben
            Insert date in UTC time
    originalRequestVersion -- Az adatszolgáltatás requestVersion értéke
            requestVersion value of the invoice exchange

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, invoiceNumber=None, batchIndex=None, invoiceOperation=None, supplierTaxNumber=None,
                 customerTaxNumber=None, insDate=None, originalRequestVersion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceNumber = invoiceNumber
        self.validate_SimpleText50NotBlankType(self.invoiceNumber)
        self.invoiceNumber_nsprefix_ = "common"
        self.batchIndex = batchIndex
        self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        self.batchIndex_nsprefix_ = "base"
        self.invoiceOperation = invoiceOperation
        self.validate_ManageInvoiceOperationType(self.invoiceOperation)
        self.invoiceOperation_nsprefix_ = None
        self.supplierTaxNumber = supplierTaxNumber
        self.validate_TaxpayerIdType(self.supplierTaxNumber)
        self.supplierTaxNumber_nsprefix_ = "common"
        self.customerTaxNumber = customerTaxNumber
        self.validate_TaxpayerIdType(self.customerTaxNumber)
        self.customerTaxNumber_nsprefix_ = "common"
        if isinstance(insDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(insDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = insDate
        self.insDate = initvalue_
        self.insDate_nsprefix_ = "base"
        self.originalRequestVersion = originalRequestVersion
        self.validate_OriginalRequestVersionType(self.originalRequestVersion)
        self.originalRequestVersion_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceChainDigestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceChainDigestType.subclass:
            return InvoiceChainDigestType.subclass(*args_, **kwargs_)
        else:
            return InvoiceChainDigestType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_invoiceNumber(self):
        return self.invoiceNumber

    def set_invoiceNumber(self, invoiceNumber):
        self.invoiceNumber = invoiceNumber

    def get_batchIndex(self):
        return self.batchIndex

    def set_batchIndex(self, batchIndex):
        self.batchIndex = batchIndex

    def get_invoiceOperation(self):
        return self.invoiceOperation

    def set_invoiceOperation(self, invoiceOperation):
        self.invoiceOperation = invoiceOperation

    def get_supplierTaxNumber(self):
        return self.supplierTaxNumber

    def set_supplierTaxNumber(self, supplierTaxNumber):
        self.supplierTaxNumber = supplierTaxNumber

    def get_customerTaxNumber(self):
        return self.customerTaxNumber

    def set_customerTaxNumber(self, customerTaxNumber):
        self.customerTaxNumber = customerTaxNumber

    def get_insDate(self):
        return self.insDate

    def set_insDate(self, insDate):
        self.insDate = insDate

    def get_originalRequestVersion(self):
        return self.originalRequestVersion

    def set_originalRequestVersion(self, originalRequestVersion):
        self.originalRequestVersion = originalRequestVersion

    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def validate_InvoiceUnboundedIndexType(self, value):
        result = True
        # Validate type InvoiceUnboundedIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceUnboundedIndexType' % {
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

    def validate_TaxpayerIdType(self, value):
        result = True
        # Validate type TaxpayerIdType, a restriction on AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on TaxpayerIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TaxpayerIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TaxpayerIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TaxpayerIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_TaxpayerIdType_patterns_,))
                result = False
        return result

    validate_TaxpayerIdType_patterns_ = [['^([0-9]{8})$']]

    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_,))
                result = False
        return result

    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]

    def validate_OriginalRequestVersionType(self, value):
        result = True
        # Validate type OriginalRequestVersionType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['1.0', '1.1', '2.0', '3.0']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on OriginalRequestVersionType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on OriginalRequestVersionType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on OriginalRequestVersionType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.invoiceNumber is not None or
                self.batchIndex is not None or
                self.invoiceOperation is not None or
                self.supplierTaxNumber is not None or
                self.customerTaxNumber is not None or
                self.insDate is not None or
                self.originalRequestVersion is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='InvoiceChainDigestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceChainDigestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceChainDigestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceChainDigestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceChainDigestType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceChainDigestType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='InvoiceChainDigestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceNumber is not None:
            namespaceprefix_ = self.invoiceNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNumber>%s</%sinvoiceNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.invoiceNumber), input_name='invoiceNumber')), namespaceprefix_,
                                                                       eol_))
        if self.batchIndex is not None:
            namespaceprefix_ = self.batchIndex_nsprefix_ + ':' if (UseCapturedNS_ and self.batchIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbatchIndex>%s</%sbatchIndex>%s' % (
            namespaceprefix_, self.gds_format_integer(self.batchIndex, input_name='batchIndex'), namespaceprefix_,
            eol_))
        if self.invoiceOperation is not None:
            namespaceprefix_ = self.invoiceOperation_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceOperation>%s</%sinvoiceOperation>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.invoiceOperation), input_name='invoiceOperation')),
                                                                             namespaceprefix_, eol_))
        if self.supplierTaxNumber is not None:
            namespaceprefix_ = self.supplierTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.supplierTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierTaxNumber>%s</%ssupplierTaxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.supplierTaxNumber), input_name='supplierTaxNumber')),
                                                                               namespaceprefix_, eol_))
        if self.customerTaxNumber is not None:
            namespaceprefix_ = self.customerTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.customerTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerTaxNumber>%s</%scustomerTaxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.customerTaxNumber), input_name='customerTaxNumber')),
                                                                               namespaceprefix_, eol_))
        if self.insDate is not None:
            namespaceprefix_ = self.insDate_nsprefix_ + ':' if (UseCapturedNS_ and self.insDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinsDate>%s</%sinsDate>%s' % (
            namespaceprefix_, self.gds_format_datetime(self.insDate, input_name='insDate'), namespaceprefix_, eol_))
        if self.originalRequestVersion is not None:
            namespaceprefix_ = self.originalRequestVersion_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.originalRequestVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalRequestVersion>%s</%soriginalRequestVersion>%s' % (namespaceprefix_,
                                                                                         self.gds_encode(
                                                                                             self.gds_format_string(
                                                                                                 quote_xml(
                                                                                                     self.originalRequestVersion),
                                                                                                 input_name='originalRequestVersion')),
                                                                                         namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='InvoiceChainDigestType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.invoiceNumber is not None:
            invoiceNumber_ = self.invoiceNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumber').text = self.gds_format_string(
                invoiceNumber_)
        if self.batchIndex is not None:
            batchIndex_ = self.batchIndex
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex').text = self.gds_format_integer(
                batchIndex_)
        if self.invoiceOperation is not None:
            invoiceOperation_ = self.invoiceOperation
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation').text = self.gds_format_string(
                invoiceOperation_)
        if self.supplierTaxNumber is not None:
            supplierTaxNumber_ = self.supplierTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}supplierTaxNumber').text = self.gds_format_string(
                supplierTaxNumber_)
        if self.customerTaxNumber is not None:
            customerTaxNumber_ = self.customerTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}customerTaxNumber').text = self.gds_format_string(
                customerTaxNumber_)
        if self.insDate is not None:
            insDate_ = self.insDate
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}insDate').text = self.gds_format_datetime(
                insDate_)
        if self.originalRequestVersion is not None:
            originalRequestVersion_ = self.originalRequestVersion
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion').text = self.gds_format_string(
                originalRequestVersion_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceChainDigestType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceNumber is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNumber=%s,\n' % self.gds_encode(quote_python(self.invoiceNumber)))
        if self.batchIndex is not None:
            showIndent(outfile, level)
            outfile.write('batchIndex=%d,\n' % self.batchIndex)
        if self.invoiceOperation is not None:
            showIndent(outfile, level)
            outfile.write('invoiceOperation=%s,\n' % self.gds_encode(quote_python(self.invoiceOperation)))
        if self.supplierTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('supplierTaxNumber=%s,\n' % self.gds_encode(quote_python(self.supplierTaxNumber)))
        if self.customerTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('customerTaxNumber=%s,\n' % self.gds_encode(quote_python(self.customerTaxNumber)))
        if self.insDate is not None:
            showIndent(outfile, level)
            outfile.write(
                'insDate=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.insDate,
                                                                                                        input_name='insDate'))
        if self.originalRequestVersion is not None:
            showIndent(outfile, level)
            outfile.write('originalRequestVersion=%s,\n' % self.gds_encode(quote_python(self.originalRequestVersion)))

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
        if nodeName_ == 'invoiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceNumber')
            value_ = self.gds_validate_string(value_, node, 'invoiceNumber')
            self.invoiceNumber = value_
            self.invoiceNumber_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.invoiceNumber)
        elif nodeName_ == 'batchIndex' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'batchIndex')
            ival_ = self.gds_validate_integer(ival_, node, 'batchIndex')
            self.batchIndex = ival_
            self.batchIndex_nsprefix_ = child_.prefix
            # validate type InvoiceUnboundedIndexType
            self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        elif nodeName_ == 'invoiceOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceOperation')
            value_ = self.gds_validate_string(value_, node, 'invoiceOperation')
            self.invoiceOperation = value_
            self.invoiceOperation_nsprefix_ = child_.prefix
            # validate type ManageInvoiceOperationType
            self.validate_ManageInvoiceOperationType(self.invoiceOperation)
        elif nodeName_ == 'supplierTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'supplierTaxNumber')
            self.supplierTaxNumber = value_
            self.supplierTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.supplierTaxNumber)
        elif nodeName_ == 'customerTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'customerTaxNumber')
            self.customerTaxNumber = value_
            self.customerTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.customerTaxNumber)
        elif nodeName_ == 'insDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.insDate = dval_
            self.insDate_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.insDate)
        elif nodeName_ == 'originalRequestVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalRequestVersion')
            value_ = self.gds_validate_string(value_, node, 'originalRequestVersion')
            self.originalRequestVersion = value_
            self.originalRequestVersion_nsprefix_ = child_.prefix
            # validate type OriginalRequestVersionType
            self.validate_OriginalRequestVersionType(self.originalRequestVersion)
