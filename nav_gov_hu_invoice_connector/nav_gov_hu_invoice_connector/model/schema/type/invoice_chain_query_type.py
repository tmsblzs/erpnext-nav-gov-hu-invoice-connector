from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceChainQueryType(GeneratedsSuper):
    """InvoiceChainQueryType -- Számlalánc kivonat lekérdezés számlaszám paramétere
    Invoice number param of the invoice chain digest query
    invoiceNumber -- Számla vagy módosító okirat sorszáma
            Sequential number of the original or modification invoice
    invoiceDirection -- Kimenő vagy bejövő számla keresési paramétere
            Inbound or outbound invoice query parameter
    taxNumber -- A számla kiállítójának vagy vevőjének adószáma
                    (a keresési feltétel az invoiceDirection tag értékétől függ)
            Tax number of the supplier or the customer of the invoice
                    (the search criteria depends on the value of the invoiceDirection tag)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, invoiceNumber=None, invoiceDirection=None, taxNumber=None, gds_collector_=None, **kwargs_):
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
        self.taxNumber = taxNumber
        self.validate_TaxpayerIdType(self.taxNumber)
        self.taxNumber_nsprefix_ = "common"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceChainQueryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceChainQueryType.subclass:
            return InvoiceChainQueryType.subclass(*args_, **kwargs_)
        else:
            return InvoiceChainQueryType(*args_, **kwargs_)

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

    def get_taxNumber(self):
        return self.taxNumber

    def set_taxNumber(self, taxNumber):
        self.taxNumber = taxNumber

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
                self.taxNumber is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='InvoiceChainQueryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceChainQueryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceChainQueryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceChainQueryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceChainQueryType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceChainQueryType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='InvoiceChainQueryType', fromsubclass_=False, pretty_print=True):
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
        if self.taxNumber is not None:
            namespaceprefix_ = self.taxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.taxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxNumber>%s</%staxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.taxNumber), input_name='taxNumber')), namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='InvoiceChainQueryType', mapping_=None, nsmap_=None):
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
        if self.taxNumber is not None:
            taxNumber_ = self.taxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}taxNumber').text = self.gds_format_string(
                taxNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceChainQueryType'):
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
        if self.taxNumber is not None:
            showIndent(outfile, level)
            outfile.write('taxNumber=%s,\n' % self.gds_encode(quote_python(self.taxNumber)))

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
        elif nodeName_ == 'taxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxNumber')
            value_ = self.gds_validate_string(value_, node, 'taxNumber')
            self.taxNumber = value_
            self.taxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.taxNumber)
