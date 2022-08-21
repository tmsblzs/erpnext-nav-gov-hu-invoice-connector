from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceNumberQueryType(GeneratedsSuper):
    """InvoiceNumberQueryType -- Számla lekérdezés számlaszám paramétere
    Invoice number param of the Invoice query
    invoiceNumber -- Számla vagy módosító okirat sorszáma
            Sequential number of the original or modification invoice
    invoiceDirection -- Kimenő vagy bejövő számla keresési paramétere
            Inbound or outbound invoice query parameter
    batchIndex -- A módosító okirat sorszáma a kötegen belül
            Sequence number of the modification document within the batch
    supplierTaxNumber -- Vevő oldali lekérdezés esetén a számla kiállítójának adószáma,
                        ha több érvényes számla is megtalálható azonos sorszámmal
            The supplier's tax number in case of querying as customer,
                        if the query result found more than one valid invoices with the same invoice number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, invoiceNumber=None, invoiceDirection=None, batchIndex=None, supplierTaxNumber=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceNumber = invoiceNumber
        self.validate_SimpleText50NotBlankType(self.invoiceNumber)
        self.invoiceNumber_nsprefix_ = "common"
        self.invoiceDirection = invoiceDirection
        self.validate_InvoiceDirectionType(self.invoiceDirection)
        self.invoiceDirection_nsprefix_ = None
        self.batchIndex = batchIndex
        self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        self.batchIndex_nsprefix_ = "base"
        self.supplierTaxNumber = supplierTaxNumber
        self.validate_TaxpayerIdType(self.supplierTaxNumber)
        self.supplierTaxNumber_nsprefix_ = "common"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceNumberQueryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceNumberQueryType.subclass:
            return InvoiceNumberQueryType.subclass(*args_, **kwargs_)
        else:
            return InvoiceNumberQueryType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_invoiceNumber(self):
        return self.invoiceNumber

    def set_invoiceNumber(self, invoiceNumber):
        self.invoiceNumber = invoiceNumber

    def get_invoiceDirection(self):
        return self.invoiceDirection

    def set_invoiceDirection(self, invoiceDirection):
        self.invoiceDirection = invoiceDirection

    def get_batchIndex(self):
        return self.batchIndex

    def set_batchIndex(self, batchIndex):
        self.batchIndex = batchIndex

    def get_supplierTaxNumber(self):
        return self.supplierTaxNumber

    def set_supplierTaxNumber(self, supplierTaxNumber):
        self.supplierTaxNumber = supplierTaxNumber

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

    def validate_InvoiceDirectionType(self, value):
        result = True
        # Validate type InvoiceDirectionType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['INBOUND', 'OUTBOUND']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on InvoiceDirectionType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on InvoiceDirectionType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on InvoiceDirectionType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

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

    def _hasContent(self):
        if (
                self.invoiceNumber is not None or
                self.invoiceDirection is not None or
                self.batchIndex is not None or
                self.supplierTaxNumber is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
               name_='InvoiceNumberQueryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceNumberQueryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceNumberQueryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceNumberQueryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceNumberQueryType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceNumberQueryType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
                        name_='InvoiceNumberQueryType', fromsubclass_=False, pretty_print=True):
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
        if self.invoiceDirection is not None:
            namespaceprefix_ = self.invoiceDirection_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceDirection_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceDirection>%s</%sinvoiceDirection>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.invoiceDirection), input_name='invoiceDirection')),
                                                                             namespaceprefix_, eol_))
        if self.batchIndex is not None:
            namespaceprefix_ = self.batchIndex_nsprefix_ + ':' if (UseCapturedNS_ and self.batchIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbatchIndex>%s</%sbatchIndex>%s' % (
            namespaceprefix_, self.gds_format_integer(self.batchIndex, input_name='batchIndex'), namespaceprefix_,
            eol_))
        if self.supplierTaxNumber is not None:
            namespaceprefix_ = self.supplierTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.supplierTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierTaxNumber>%s</%ssupplierTaxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.supplierTaxNumber), input_name='supplierTaxNumber')),
                                                                               namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='InvoiceNumberQueryType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.invoiceNumber is not None:
            invoiceNumber_ = self.invoiceNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumber').text = self.gds_format_string(
                invoiceNumber_)
        if self.invoiceDirection is not None:
            invoiceDirection_ = self.invoiceDirection
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDirection').text = self.gds_format_string(
                invoiceDirection_)
        if self.batchIndex is not None:
            batchIndex_ = self.batchIndex
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex').text = self.gds_format_integer(
                batchIndex_)
        if self.supplierTaxNumber is not None:
            supplierTaxNumber_ = self.supplierTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}supplierTaxNumber').text = self.gds_format_string(
                supplierTaxNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceNumberQueryType'):
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
        if self.invoiceDirection is not None:
            showIndent(outfile, level)
            outfile.write('invoiceDirection=%s,\n' % self.gds_encode(quote_python(self.invoiceDirection)))
        if self.batchIndex is not None:
            showIndent(outfile, level)
            outfile.write('batchIndex=%d,\n' % self.batchIndex)
        if self.supplierTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('supplierTaxNumber=%s,\n' % self.gds_encode(quote_python(self.supplierTaxNumber)))

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
        elif nodeName_ == 'invoiceDirection':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceDirection')
            value_ = self.gds_validate_string(value_, node, 'invoiceDirection')
            self.invoiceDirection = value_
            self.invoiceDirection_nsprefix_ = child_.prefix
            # validate type InvoiceDirectionType
            self.validate_InvoiceDirectionType(self.invoiceDirection)
        elif nodeName_ == 'batchIndex' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'batchIndex')
            ival_ = self.gds_validate_integer(ival_, node, 'batchIndex')
            self.batchIndex = ival_
            self.batchIndex_nsprefix_ = child_.prefix
            # validate type InvoiceUnboundedIndexType
            self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        elif nodeName_ == 'supplierTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'supplierTaxNumber')
            self.supplierTaxNumber = value_
            self.supplierTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.supplierTaxNumber)
