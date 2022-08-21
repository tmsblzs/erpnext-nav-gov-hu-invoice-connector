from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, Validate_simpletypes_, encode_str_2_3, quote_xml, \
    quote_python

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AdditionalQueryParamsType(GeneratedsSuper):
    """AdditionalQueryParamsType -- A számla lekérdezés kiegészítő paraméterei
    Additional params of the invoice query
    taxNumber -- A számla kiállítójának vagy vevőjének adószáma
                    (a keresési feltétel az invoiceDirection tag értékétől függ)
            Tax number of the supplier or the customer of the invoice
                    (the search criteria depends on the value of the invoiceDirection tag)
    groupMemberTaxNumber -- A számla kiállítójának vagy vevőjének csoport tag adószáma
                    (a keresési feltétel az invoiceDirection tag értékétől függ)
            Tax number of group member of the supplier or the customer of the invoice
                    (the search criteria depends on the value of the invoiceDirection tag)
    name -- A számla kiállítójának vagy vevőjének kereső paramétere szóeleji egyezőségre
                    (a keresési feltétel az invoiceDirection tag értékétől függ)
            Query param of the supplier or the customer of the invoice for leading match pattern
                    (the search criteria depends on the value of the invoiceDirection tag)
    invoiceCategory -- A számla típusa
            Type of invoice
    paymentMethod -- Fizetés módja
            Method of payment
    invoiceAppearance -- A számla megjelenési formája
            Form of appearance of the invoice
    source -- Az adatszolgáltatás forrása
            Data exchange source
    currency -- A számla pénzneme
            Currency of the invoice

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, taxNumber=None, groupMemberTaxNumber=None, name=None, invoiceCategory=None, paymentMethod=None, invoiceAppearance=None, source=None, currency=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.taxNumber = taxNumber
        self.validate_TaxpayerIdType(self.taxNumber)
        self.taxNumber_nsprefix_ = "common"
        self.groupMemberTaxNumber = groupMemberTaxNumber
        self.validate_TaxpayerIdType(self.groupMemberTaxNumber)
        self.groupMemberTaxNumber_nsprefix_ = "common"
        self.name = name
        self.validate_QueryNameType(self.name)
        self.name_nsprefix_ = None
        self.invoiceCategory = invoiceCategory
        self.validate_InvoiceCategoryType(self.invoiceCategory)
        self.invoiceCategory_nsprefix_ = "base"
        self.paymentMethod = paymentMethod
        self.validate_PaymentMethodType(self.paymentMethod)
        self.paymentMethod_nsprefix_ = "base"
        self.invoiceAppearance = invoiceAppearance
        self.validate_InvoiceAppearanceType(self.invoiceAppearance)
        self.invoiceAppearance_nsprefix_ = "base"
        self.source = source
        self.validate_SourceType(self.source)
        self.source_nsprefix_ = None
        self.currency = currency
        self.validate_CurrencyType(self.currency)
        self.currency_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdditionalQueryParamsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdditionalQueryParamsType.subclass:
            return AdditionalQueryParamsType.subclass(*args_, **kwargs_)
        else:
            return AdditionalQueryParamsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_taxNumber(self):
        return self.taxNumber
    def set_taxNumber(self, taxNumber):
        self.taxNumber = taxNumber
    def get_groupMemberTaxNumber(self):
        return self.groupMemberTaxNumber
    def set_groupMemberTaxNumber(self, groupMemberTaxNumber):
        self.groupMemberTaxNumber = groupMemberTaxNumber
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_invoiceCategory(self):
        return self.invoiceCategory
    def set_invoiceCategory(self, invoiceCategory):
        self.invoiceCategory = invoiceCategory
    def get_paymentMethod(self):
        return self.paymentMethod
    def set_paymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod
    def get_invoiceAppearance(self):
        return self.invoiceAppearance
    def set_invoiceAppearance(self, invoiceAppearance):
        self.invoiceAppearance = invoiceAppearance
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_currency(self):
        return self.currency
    def set_currency(self, currency):
        self.currency = currency
    def validate_TaxpayerIdType(self, value):
        result = True
        # Validate type TaxpayerIdType, a restriction on AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TaxpayerIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TaxpayerIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TaxpayerIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TaxpayerIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TaxpayerIdType_patterns_, ))
                result = False
        return result
    validate_TaxpayerIdType_patterns_ = [['^([0-9]{8})$']]
    def validate_QueryNameType(self, value):
        result = True
        # Validate type QueryNameType, a restriction on common:SimpleText512NotBlankType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) < 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on QueryNameType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on QueryNameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on QueryNameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_QueryNameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_QueryNameType_patterns_, ))
                result = False
        return result
    validate_QueryNameType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_InvoiceCategoryType(self, value):
        result = True
        # Validate type InvoiceCategoryType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['NORMAL', 'SIMPLIFIED', 'AGGREGATE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on InvoiceCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on InvoiceCategoryType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on InvoiceCategoryType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_PaymentMethodType(self, value):
        result = True
        # Validate type PaymentMethodType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['TRANSFER', 'CASH', 'CARD', 'VOUCHER', 'OTHER']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on PaymentMethodType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PaymentMethodType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PaymentMethodType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_InvoiceAppearanceType(self, value):
        result = True
        # Validate type InvoiceAppearanceType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['PAPER', 'ELECTRONIC', 'EDI', 'UNKNOWN']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on InvoiceAppearanceType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on InvoiceAppearanceType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on InvoiceAppearanceType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_SourceType(self, value):
        result = True
        # Validate type SourceType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['WEB', 'XML', 'MGM', 'OPG', 'OSZ']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on SourceType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SourceType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SourceType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_CurrencyType(self, value):
        result = True
        # Validate type CurrencyType, a restriction on AtomicStringType4.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on CurrencyType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CurrencyType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CurrencyType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CurrencyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CurrencyType_patterns_, ))
                result = False
        return result
    validate_CurrencyType_patterns_ = [['^([A-Z]{3})$']]
    def _hasContent(self):
        if (
            self.taxNumber is not None or
            self.groupMemberTaxNumber is not None or
            self.name is not None or
            self.invoiceCategory is not None or
            self.paymentMethod is not None or
            self.invoiceAppearance is not None or
            self.source is not None or
            self.currency is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='AdditionalQueryParamsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdditionalQueryParamsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdditionalQueryParamsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdditionalQueryParamsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdditionalQueryParamsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdditionalQueryParamsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='AdditionalQueryParamsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.taxNumber is not None:
            namespaceprefix_ = self.taxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.taxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxNumber>%s</%staxNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxNumber), input_name='taxNumber')), namespaceprefix_ , eol_))
        if self.groupMemberTaxNumber is not None:
            namespaceprefix_ = self.groupMemberTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.groupMemberTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgroupMemberTaxNumber>%s</%sgroupMemberTaxNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.groupMemberTaxNumber), input_name='groupMemberTaxNumber')), namespaceprefix_ , eol_))
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.invoiceCategory is not None:
            namespaceprefix_ = self.invoiceCategory_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceCategory>%s</%sinvoiceCategory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceCategory), input_name='invoiceCategory')), namespaceprefix_ , eol_))
        if self.paymentMethod is not None:
            namespaceprefix_ = self.paymentMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.paymentMethod_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaymentMethod>%s</%spaymentMethod>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.paymentMethod), input_name='paymentMethod')), namespaceprefix_ , eol_))
        if self.invoiceAppearance is not None:
            namespaceprefix_ = self.invoiceAppearance_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceAppearance_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceAppearance>%s</%sinvoiceAppearance>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceAppearance), input_name='invoiceAppearance')), namespaceprefix_ , eol_))
        if self.source is not None:
            namespaceprefix_ = self.source_nsprefix_ + ':' if (UseCapturedNS_ and self.source_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssource>%s</%ssource>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.source), input_name='source')), namespaceprefix_ , eol_))
        if self.currency is not None:
            namespaceprefix_ = self.currency_nsprefix_ + ':' if (UseCapturedNS_ and self.currency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrency>%s</%scurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.currency), input_name='currency')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AdditionalQueryParamsType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.taxNumber is not None:
            taxNumber_ = self.taxNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}taxNumber').text = self.gds_format_string(taxNumber_)
        if self.groupMemberTaxNumber is not None:
            groupMemberTaxNumber_ = self.groupMemberTaxNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}groupMemberTaxNumber').text = self.gds_format_string(groupMemberTaxNumber_)
        if self.name is not None:
            name_ = self.name
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}name').text = self.gds_format_string(name_)
        if self.invoiceCategory is not None:
            invoiceCategory_ = self.invoiceCategory
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceCategory').text = self.gds_format_string(invoiceCategory_)
        if self.paymentMethod is not None:
            paymentMethod_ = self.paymentMethod
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}paymentMethod').text = self.gds_format_string(paymentMethod_)
        if self.invoiceAppearance is not None:
            invoiceAppearance_ = self.invoiceAppearance
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceAppearance').text = self.gds_format_string(invoiceAppearance_)
        if self.source is not None:
            source_ = self.source
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}source').text = self.gds_format_string(source_)
        if self.currency is not None:
            currency_ = self.currency
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}currency').text = self.gds_format_string(currency_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AdditionalQueryParamsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.taxNumber is not None:
            showIndent(outfile, level)
            outfile.write('taxNumber=%s,\n' % self.gds_encode(quote_python(self.taxNumber)))
        if self.groupMemberTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('groupMemberTaxNumber=%s,\n' % self.gds_encode(quote_python(self.groupMemberTaxNumber)))
        if self.name is not None:
            showIndent(outfile, level)
            outfile.write('name=%s,\n' % self.gds_encode(quote_python(self.name)))
        if self.invoiceCategory is not None:
            showIndent(outfile, level)
            outfile.write('invoiceCategory=%s,\n' % self.gds_encode(quote_python(self.invoiceCategory)))
        if self.paymentMethod is not None:
            showIndent(outfile, level)
            outfile.write('paymentMethod=%s,\n' % self.gds_encode(quote_python(self.paymentMethod)))
        if self.invoiceAppearance is not None:
            showIndent(outfile, level)
            outfile.write('invoiceAppearance=%s,\n' % self.gds_encode(quote_python(self.invoiceAppearance)))
        if self.source is not None:
            showIndent(outfile, level)
            outfile.write('source=%s,\n' % self.gds_encode(quote_python(self.source)))
        if self.currency is not None:
            showIndent(outfile, level)
            outfile.write('currency=%s,\n' % self.gds_encode(quote_python(self.currency)))
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
        if nodeName_ == 'taxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxNumber')
            value_ = self.gds_validate_string(value_, node, 'taxNumber')
            self.taxNumber = value_
            self.taxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.taxNumber)
        elif nodeName_ == 'groupMemberTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'groupMemberTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'groupMemberTaxNumber')
            self.groupMemberTaxNumber = value_
            self.groupMemberTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.groupMemberTaxNumber)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type QueryNameType
            self.validate_QueryNameType(self.name)
        elif nodeName_ == 'invoiceCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceCategory')
            value_ = self.gds_validate_string(value_, node, 'invoiceCategory')
            self.invoiceCategory = value_
            self.invoiceCategory_nsprefix_ = child_.prefix
            # validate type InvoiceCategoryType
            self.validate_InvoiceCategoryType(self.invoiceCategory)
        elif nodeName_ == 'paymentMethod':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'paymentMethod')
            value_ = self.gds_validate_string(value_, node, 'paymentMethod')
            self.paymentMethod = value_
            self.paymentMethod_nsprefix_ = child_.prefix
            # validate type PaymentMethodType
            self.validate_PaymentMethodType(self.paymentMethod)
        elif nodeName_ == 'invoiceAppearance':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceAppearance')
            value_ = self.gds_validate_string(value_, node, 'invoiceAppearance')
            self.invoiceAppearance = value_
            self.invoiceAppearance_nsprefix_ = child_.prefix
            # validate type InvoiceAppearanceType
            self.validate_InvoiceAppearanceType(self.invoiceAppearance)
        elif nodeName_ == 'source':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'source')
            value_ = self.gds_validate_string(value_, node, 'source')
            self.source = value_
            self.source_nsprefix_ = child_.prefix
            # validate type SourceType
            self.validate_SourceType(self.source)
        elif nodeName_ == 'currency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currency')
            value_ = self.gds_validate_string(value_, node, 'currency')
            self.currency = value_
            self.currency_nsprefix_ = child_.prefix
            # validate type CurrencyType
            self.validate_CurrencyType(self.currency)
