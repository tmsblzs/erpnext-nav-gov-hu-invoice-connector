import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.additional_data_type import \
    AdditionalDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.conventional_invoice_info_type import \
    ConventionalInvoiceInfoType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class InvoiceDetailType(GeneratedsSuper):
    """InvoiceDetailType -- Számla részletező adatok
    Invoice detail data
    invoiceCategory -- A számla típusa, módosító okirat esetén az eredeti számla típusa
    Type of invoice. In case of modification document the type of original invoice
    invoiceDeliveryDate -- Teljesítés dátuma (ha nem szerepel a számlán, akkor azonos a számla keltével) - ÁFA tv. 169. § g)
    Delivery date (if this field does not exist on the invoice, the date of the invoice should be considered as such) - section 169 (g) of the VAT law
    invoiceDeliveryPeriodStart -- Amennyiben a számla egy időszakra vonatkozik, akkor az időszak első napja
    The first day of the delivery, if the invoice delivery is a period
    invoiceDeliveryPeriodEnd -- Amennyiben a számla egy időszakra vonatkozik, akkor az időszak utolsó napja
    The last day of the delivery, if the invoice delivery is a period
    invoiceAccountingDeliveryDate -- Számviteli teljesítés dátuma. Időszak esetén az időszak utolsó napja
    Date of accounting accomplishment. In the event of a period, the last day of the period
    periodicalSettlement -- Annak jelzése, ha a felek a termék értékesítés, szolgáltatás nyújtás során időszakonkénti
        elszámolásban vagy fizetésben állapodnak meg, vagy a termék értékesítés, szolgáltatás nyújtás ellenértékét
        meghatározott időpontra állapítják meg.
    Indicates where by agreement of the parties it gives rise to successive statements of account or successive
        payments relating to the supply of goods, or the supply of services, or if the consideration agreed upon for such goods and/or services applies to specific periods.
    smallBusinessIndicator -- Kisadózó jelzése
    Marking of low tax-bracket enterprise
    currencyCode -- A számla pénzneme az ISO 4217 szabvány szerint
    ISO 4217 currency code on the invoice
    exchangeRate -- HUF-tól különböző pénznem esetén az alkalmazott árfolyam: egy egység értéke HUF-ban
    In case any currency is used other than HUF, the applied exchange rate should be mentioned: 1 unit of the foreign currency expressed in HUF
    utilitySettlementIndicator -- Közmű elszámoló számla jelölése (2013. évi CLXXXVIII törvény szerinti elszámoló számla)
    Marking the fact of utility settlement invoice (invoice according to Act CLXXXVIII of 2013)
    selfBillingIndicator -- Önszámlázás jelölése (önszámlázás esetén true)
    Marking the fact of self-billing (in the case of self-billing the value is true)
    paymentMethod -- Fizetés módja
    Method of payment
    paymentDate -- Fizet ési határidő
    Deadline for payment
    cashAccountingIndicator -- Pénzforgalmi elszámolás jelölése, ha az szerepel a számlán - ÁFA tv. 169. § h).
        Értéke true pénzforgalmi elszámolás esetén
    Marking the fact of cash accounting if this is indicated on the invoice - section 169 (h) of the VAT law. The value is true in case of cash accounting
    invoiceAppearance -- A számla vagy módosítóokirat megjelenési formája
    Form of appearance of the invoice or modification document
    conventionalInvoiceInfo -- A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatok
    Other conventionally named data to assist in invoice processing
    additionalInvoiceData -- A számlára vonatkozó egyéb adat
    Other data in relation to the invoice

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoiceCategory=None, invoiceDeliveryDate=None, invoiceDeliveryPeriodStart=None, invoiceDeliveryPeriodEnd=None, invoiceAccountingDeliveryDate=None, periodicalSettlement=None, smallBusinessIndicator=None, currencyCode=None, exchangeRate=None, utilitySettlementIndicator=None, selfBillingIndicator=None, paymentMethod=None, paymentDate=None, cashAccountingIndicator=None, invoiceAppearance=None, conventionalInvoiceInfo=None, additionalInvoiceData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceCategory = invoiceCategory
        self.validate_InvoiceCategoryType(self.invoiceCategory)
        self.invoiceCategory_nsprefix_ = "base"
        if isinstance(invoiceDeliveryDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(invoiceDeliveryDate, '%Y-%m-%d').date()
        else:
            initvalue_ = invoiceDeliveryDate
        self.invoiceDeliveryDate = initvalue_
        self.invoiceDeliveryDate_nsprefix_ = "base"
        if isinstance(invoiceDeliveryPeriodStart, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(invoiceDeliveryPeriodStart, '%Y-%m-%d').date()
        else:
            initvalue_ = invoiceDeliveryPeriodStart
        self.invoiceDeliveryPeriodStart = initvalue_
        self.invoiceDeliveryPeriodStart_nsprefix_ = "base"
        if isinstance(invoiceDeliveryPeriodEnd, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(invoiceDeliveryPeriodEnd, '%Y-%m-%d').date()
        else:
            initvalue_ = invoiceDeliveryPeriodEnd
        self.invoiceDeliveryPeriodEnd = initvalue_
        self.invoiceDeliveryPeriodEnd_nsprefix_ = "base"
        if isinstance(invoiceAccountingDeliveryDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(invoiceAccountingDeliveryDate, '%Y-%m-%d').date()
        else:
            initvalue_ = invoiceAccountingDeliveryDate
        self.invoiceAccountingDeliveryDate = initvalue_
        self.invoiceAccountingDeliveryDate_nsprefix_ = "base"
        self.periodicalSettlement = periodicalSettlement
        self.periodicalSettlement_nsprefix_ = "xs"
        self.smallBusinessIndicator = smallBusinessIndicator
        self.smallBusinessIndicator_nsprefix_ = "xs"
        self.currencyCode = currencyCode
        self.validate_CurrencyType(self.currencyCode)
        self.currencyCode_nsprefix_ = "common"
        self.exchangeRate = exchangeRate
        self.validate_ExchangeRateType(self.exchangeRate)
        self.exchangeRate_nsprefix_ = None
        self.utilitySettlementIndicator = utilitySettlementIndicator
        self.utilitySettlementIndicator_nsprefix_ = "xs"
        self.selfBillingIndicator = selfBillingIndicator
        self.selfBillingIndicator_nsprefix_ = "xs"
        self.paymentMethod = paymentMethod
        self.validate_PaymentMethodType(self.paymentMethod)
        self.paymentMethod_nsprefix_ = "base"
        if isinstance(paymentDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(paymentDate, '%Y-%m-%d').date()
        else:
            initvalue_ = paymentDate
        self.paymentDate = initvalue_
        self.paymentDate_nsprefix_ = "base"
        self.cashAccountingIndicator = cashAccountingIndicator
        self.cashAccountingIndicator_nsprefix_ = "xs"
        self.invoiceAppearance = invoiceAppearance
        self.validate_InvoiceAppearanceType(self.invoiceAppearance)
        self.invoiceAppearance_nsprefix_ = "base"
        self.conventionalInvoiceInfo = conventionalInvoiceInfo
        self.conventionalInvoiceInfo_nsprefix_ = None
        if additionalInvoiceData is None:
            self.additionalInvoiceData = []
        else:
            self.additionalInvoiceData = additionalInvoiceData
        self.additionalInvoiceData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceDetailType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceDetailType.subclass:
            return InvoiceDetailType.subclass(*args_, **kwargs_)
        else:
            return InvoiceDetailType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceCategory(self):
        return self.invoiceCategory
    def set_invoiceCategory(self, invoiceCategory):
        self.invoiceCategory = invoiceCategory
    def get_invoiceDeliveryDate(self):
        return self.invoiceDeliveryDate
    def set_invoiceDeliveryDate(self, invoiceDeliveryDate):
        self.invoiceDeliveryDate = invoiceDeliveryDate
    def get_invoiceDeliveryPeriodStart(self):
        return self.invoiceDeliveryPeriodStart
    def set_invoiceDeliveryPeriodStart(self, invoiceDeliveryPeriodStart):
        self.invoiceDeliveryPeriodStart = invoiceDeliveryPeriodStart
    def get_invoiceDeliveryPeriodEnd(self):
        return self.invoiceDeliveryPeriodEnd
    def set_invoiceDeliveryPeriodEnd(self, invoiceDeliveryPeriodEnd):
        self.invoiceDeliveryPeriodEnd = invoiceDeliveryPeriodEnd
    def get_invoiceAccountingDeliveryDate(self):
        return self.invoiceAccountingDeliveryDate
    def set_invoiceAccountingDeliveryDate(self, invoiceAccountingDeliveryDate):
        self.invoiceAccountingDeliveryDate = invoiceAccountingDeliveryDate
    def get_periodicalSettlement(self):
        return self.periodicalSettlement
    def set_periodicalSettlement(self, periodicalSettlement):
        self.periodicalSettlement = periodicalSettlement
    def get_smallBusinessIndicator(self):
        return self.smallBusinessIndicator
    def set_smallBusinessIndicator(self, smallBusinessIndicator):
        self.smallBusinessIndicator = smallBusinessIndicator
    def get_currencyCode(self):
        return self.currencyCode
    def set_currencyCode(self, currencyCode):
        self.currencyCode = currencyCode
    def get_exchangeRate(self):
        return self.exchangeRate
    def set_exchangeRate(self, exchangeRate):
        self.exchangeRate = exchangeRate
    def get_utilitySettlementIndicator(self):
        return self.utilitySettlementIndicator
    def set_utilitySettlementIndicator(self, utilitySettlementIndicator):
        self.utilitySettlementIndicator = utilitySettlementIndicator
    def get_selfBillingIndicator(self):
        return self.selfBillingIndicator
    def set_selfBillingIndicator(self, selfBillingIndicator):
        self.selfBillingIndicator = selfBillingIndicator
    def get_paymentMethod(self):
        return self.paymentMethod
    def set_paymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod
    def get_paymentDate(self):
        return self.paymentDate
    def set_paymentDate(self, paymentDate):
        self.paymentDate = paymentDate
    def get_cashAccountingIndicator(self):
        return self.cashAccountingIndicator
    def set_cashAccountingIndicator(self, cashAccountingIndicator):
        self.cashAccountingIndicator = cashAccountingIndicator
    def get_invoiceAppearance(self):
        return self.invoiceAppearance
    def set_invoiceAppearance(self, invoiceAppearance):
        self.invoiceAppearance = invoiceAppearance
    def get_conventionalInvoiceInfo(self):
        return self.conventionalInvoiceInfo
    def set_conventionalInvoiceInfo(self, conventionalInvoiceInfo):
        self.conventionalInvoiceInfo = conventionalInvoiceInfo
    def get_additionalInvoiceData(self):
        return self.additionalInvoiceData
    def set_additionalInvoiceData(self, additionalInvoiceData):
        self.additionalInvoiceData = additionalInvoiceData
    def add_additionalInvoiceData(self, value):
        self.additionalInvoiceData.append(value)
    def insert_additionalInvoiceData_at(self, index, value):
        self.additionalInvoiceData.insert(index, value)
    def replace_additionalInvoiceData_at(self, index, value):
        self.additionalInvoiceData[index] = value
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
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
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
    def validate_ExchangeRateType(self, value):
        result = True
        # Validate type ExchangeRateType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on ExchangeRateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on ExchangeRateType' % {"value": value, "lineno": lineno} )
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
    def _hasContent(self):
        if (
            self.invoiceCategory is not None or
            self.invoiceDeliveryDate is not None or
            self.invoiceDeliveryPeriodStart is not None or
            self.invoiceDeliveryPeriodEnd is not None or
            self.invoiceAccountingDeliveryDate is not None or
            self.periodicalSettlement is not None or
            self.smallBusinessIndicator is not None or
            self.currencyCode is not None or
            self.exchangeRate is not None or
            self.utilitySettlementIndicator is not None or
            self.selfBillingIndicator is not None or
            self.paymentMethod is not None or
            self.paymentDate is not None or
            self.cashAccountingIndicator is not None or
            self.invoiceAppearance is not None or
            self.conventionalInvoiceInfo is not None or
            self.additionalInvoiceData
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceDetailType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceDetailType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceDetailType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceDetailType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceDetailType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceDetailType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceDetailType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceCategory is not None:
            namespaceprefix_ = self.invoiceCategory_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceCategory>%s</%sinvoiceCategory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceCategory), input_name='invoiceCategory')), namespaceprefix_ , eol_))
        if self.invoiceDeliveryDate is not None:
            namespaceprefix_ = self.invoiceDeliveryDate_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceDeliveryDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceDeliveryDate>%s</%sinvoiceDeliveryDate>%s' % (namespaceprefix_ , self.gds_format_date(self.invoiceDeliveryDate, input_name='invoiceDeliveryDate'), namespaceprefix_ , eol_))
        if self.invoiceDeliveryPeriodStart is not None:
            namespaceprefix_ = self.invoiceDeliveryPeriodStart_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceDeliveryPeriodStart_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceDeliveryPeriodStart>%s</%sinvoiceDeliveryPeriodStart>%s' % (namespaceprefix_ , self.gds_format_date(self.invoiceDeliveryPeriodStart, input_name='invoiceDeliveryPeriodStart'), namespaceprefix_ , eol_))
        if self.invoiceDeliveryPeriodEnd is not None:
            namespaceprefix_ = self.invoiceDeliveryPeriodEnd_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceDeliveryPeriodEnd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceDeliveryPeriodEnd>%s</%sinvoiceDeliveryPeriodEnd>%s' % (namespaceprefix_ , self.gds_format_date(self.invoiceDeliveryPeriodEnd, input_name='invoiceDeliveryPeriodEnd'), namespaceprefix_ , eol_))
        if self.invoiceAccountingDeliveryDate is not None:
            namespaceprefix_ = self.invoiceAccountingDeliveryDate_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceAccountingDeliveryDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceAccountingDeliveryDate>%s</%sinvoiceAccountingDeliveryDate>%s' % (namespaceprefix_ , self.gds_format_date(self.invoiceAccountingDeliveryDate, input_name='invoiceAccountingDeliveryDate'), namespaceprefix_ , eol_))
        if self.periodicalSettlement is not None:
            namespaceprefix_ = self.periodicalSettlement_nsprefix_ + ':' if (UseCapturedNS_ and self.periodicalSettlement_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%speriodicalSettlement>%s</%speriodicalSettlement>%s' % (namespaceprefix_ , self.gds_format_boolean(self.periodicalSettlement, input_name='periodicalSettlement'), namespaceprefix_ , eol_))
        if self.smallBusinessIndicator is not None:
            namespaceprefix_ = self.smallBusinessIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.smallBusinessIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssmallBusinessIndicator>%s</%ssmallBusinessIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.smallBusinessIndicator, input_name='smallBusinessIndicator'), namespaceprefix_ , eol_))
        if self.currencyCode is not None:
            namespaceprefix_ = self.currencyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.currencyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrencyCode>%s</%scurrencyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.currencyCode), input_name='currencyCode')), namespaceprefix_ , eol_))
        if self.exchangeRate is not None:
            namespaceprefix_ = self.exchangeRate_nsprefix_ + ':' if (UseCapturedNS_ and self.exchangeRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexchangeRate>%s</%sexchangeRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.exchangeRate, input_name='exchangeRate'), namespaceprefix_ , eol_))
        if self.utilitySettlementIndicator is not None:
            namespaceprefix_ = self.utilitySettlementIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.utilitySettlementIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sutilitySettlementIndicator>%s</%sutilitySettlementIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.utilitySettlementIndicator, input_name='utilitySettlementIndicator'), namespaceprefix_ , eol_))
        if self.selfBillingIndicator is not None:
            namespaceprefix_ = self.selfBillingIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.selfBillingIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sselfBillingIndicator>%s</%sselfBillingIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.selfBillingIndicator, input_name='selfBillingIndicator'), namespaceprefix_ , eol_))
        if self.paymentMethod is not None:
            namespaceprefix_ = self.paymentMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.paymentMethod_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaymentMethod>%s</%spaymentMethod>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.paymentMethod), input_name='paymentMethod')), namespaceprefix_ , eol_))
        if self.paymentDate is not None:
            namespaceprefix_ = self.paymentDate_nsprefix_ + ':' if (UseCapturedNS_ and self.paymentDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaymentDate>%s</%spaymentDate>%s' % (namespaceprefix_ , self.gds_format_date(self.paymentDate, input_name='paymentDate'), namespaceprefix_ , eol_))
        if self.cashAccountingIndicator is not None:
            namespaceprefix_ = self.cashAccountingIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.cashAccountingIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scashAccountingIndicator>%s</%scashAccountingIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cashAccountingIndicator, input_name='cashAccountingIndicator'), namespaceprefix_ , eol_))
        if self.invoiceAppearance is not None:
            namespaceprefix_ = self.invoiceAppearance_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceAppearance_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceAppearance>%s</%sinvoiceAppearance>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceAppearance), input_name='invoiceAppearance')), namespaceprefix_ , eol_))
        if self.conventionalInvoiceInfo is not None:
            namespaceprefix_ = self.conventionalInvoiceInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.conventionalInvoiceInfo_nsprefix_) else ''
            self.conventionalInvoiceInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='conventionalInvoiceInfo', pretty_print=pretty_print)
        for additionalInvoiceData_ in self.additionalInvoiceData:
            namespaceprefix_ = self.additionalInvoiceData_nsprefix_ + ':' if (UseCapturedNS_ and self.additionalInvoiceData_nsprefix_) else ''
            additionalInvoiceData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='additionalInvoiceData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InvoiceDetailType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.invoiceCategory is not None:
            invoiceCategory_ = self.invoiceCategory
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceCategory').text = self.gds_format_string(invoiceCategory_)
        if self.invoiceDeliveryDate is not None:
            invoiceDeliveryDate_ = self.invoiceDeliveryDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceDeliveryDate').text = self.gds_format_date(invoiceDeliveryDate_)
        if self.invoiceDeliveryPeriodStart is not None:
            invoiceDeliveryPeriodStart_ = self.invoiceDeliveryPeriodStart
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceDeliveryPeriodStart').text = self.gds_format_date(invoiceDeliveryPeriodStart_)
        if self.invoiceDeliveryPeriodEnd is not None:
            invoiceDeliveryPeriodEnd_ = self.invoiceDeliveryPeriodEnd
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceDeliveryPeriodEnd').text = self.gds_format_date(invoiceDeliveryPeriodEnd_)
        if self.invoiceAccountingDeliveryDate is not None:
            invoiceAccountingDeliveryDate_ = self.invoiceAccountingDeliveryDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceAccountingDeliveryDate').text = self.gds_format_date(invoiceAccountingDeliveryDate_)
        if self.periodicalSettlement is not None:
            periodicalSettlement_ = self.periodicalSettlement
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}periodicalSettlement').text = self.gds_format_boolean(periodicalSettlement_)
        if self.smallBusinessIndicator is not None:
            smallBusinessIndicator_ = self.smallBusinessIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}smallBusinessIndicator').text = self.gds_format_boolean(smallBusinessIndicator_)
        if self.currencyCode is not None:
            currencyCode_ = self.currencyCode
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}currencyCode').text = self.gds_format_string(currencyCode_)
        if self.exchangeRate is not None:
            exchangeRate_ = self.exchangeRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}exchangeRate').text = self.gds_format_decimal(exchangeRate_)
        if self.utilitySettlementIndicator is not None:
            utilitySettlementIndicator_ = self.utilitySettlementIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}utilitySettlementIndicator').text = self.gds_format_boolean(utilitySettlementIndicator_)
        if self.selfBillingIndicator is not None:
            selfBillingIndicator_ = self.selfBillingIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}selfBillingIndicator').text = self.gds_format_boolean(selfBillingIndicator_)
        if self.paymentMethod is not None:
            paymentMethod_ = self.paymentMethod
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}paymentMethod').text = self.gds_format_string(paymentMethod_)
        if self.paymentDate is not None:
            paymentDate_ = self.paymentDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}paymentDate').text = self.gds_format_date(paymentDate_)
        if self.cashAccountingIndicator is not None:
            cashAccountingIndicator_ = self.cashAccountingIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}cashAccountingIndicator').text = self.gds_format_boolean(cashAccountingIndicator_)
        if self.invoiceAppearance is not None:
            invoiceAppearance_ = self.invoiceAppearance
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceAppearance').text = self.gds_format_string(invoiceAppearance_)
        if self.conventionalInvoiceInfo is not None:
            conventionalInvoiceInfo_ = self.conventionalInvoiceInfo
            conventionalInvoiceInfo_.to_etree(element, name_='conventionalInvoiceInfo', mapping_=mapping_, nsmap_=nsmap_)
        for additionalInvoiceData_ in self.additionalInvoiceData:
            additionalInvoiceData_.to_etree(element, name_='additionalInvoiceData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='InvoiceDetailType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceCategory is not None:
            showIndent(outfile, level)
            outfile.write('invoiceCategory=%s,\n' % self.gds_encode(quote_python(self.invoiceCategory)))
        if self.invoiceDeliveryDate is not None:
            showIndent(outfile, level)
            outfile.write('invoiceDeliveryDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.invoiceDeliveryDate, input_name='invoiceDeliveryDate'))
        if self.invoiceDeliveryPeriodStart is not None:
            showIndent(outfile, level)
            outfile.write('invoiceDeliveryPeriodStart=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.invoiceDeliveryPeriodStart, input_name='invoiceDeliveryPeriodStart'))
        if self.invoiceDeliveryPeriodEnd is not None:
            showIndent(outfile, level)
            outfile.write('invoiceDeliveryPeriodEnd=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.invoiceDeliveryPeriodEnd, input_name='invoiceDeliveryPeriodEnd'))
        if self.invoiceAccountingDeliveryDate is not None:
            showIndent(outfile, level)
            outfile.write('invoiceAccountingDeliveryDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.invoiceAccountingDeliveryDate, input_name='invoiceAccountingDeliveryDate'))
        if self.periodicalSettlement is not None:
            showIndent(outfile, level)
            outfile.write('periodicalSettlement=%s,\n' % self.periodicalSettlement)
        if self.smallBusinessIndicator is not None:
            showIndent(outfile, level)
            outfile.write('smallBusinessIndicator=%s,\n' % self.smallBusinessIndicator)
        if self.currencyCode is not None:
            showIndent(outfile, level)
            outfile.write('currencyCode=%s,\n' % self.gds_encode(quote_python(self.currencyCode)))
        if self.exchangeRate is not None:
            showIndent(outfile, level)
            outfile.write('exchangeRate=%f,\n' % self.exchangeRate)
        if self.utilitySettlementIndicator is not None:
            showIndent(outfile, level)
            outfile.write('utilitySettlementIndicator=%s,\n' % self.utilitySettlementIndicator)
        if self.selfBillingIndicator is not None:
            showIndent(outfile, level)
            outfile.write('selfBillingIndicator=%s,\n' % self.selfBillingIndicator)
        if self.paymentMethod is not None:
            showIndent(outfile, level)
            outfile.write('paymentMethod=%s,\n' % self.gds_encode(quote_python(self.paymentMethod)))
        if self.paymentDate is not None:
            showIndent(outfile, level)
            outfile.write('paymentDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.paymentDate, input_name='paymentDate'))
        if self.cashAccountingIndicator is not None:
            showIndent(outfile, level)
            outfile.write('cashAccountingIndicator=%s,\n' % self.cashAccountingIndicator)
        if self.invoiceAppearance is not None:
            showIndent(outfile, level)
            outfile.write('invoiceAppearance=%s,\n' % self.gds_encode(quote_python(self.invoiceAppearance)))
        if self.conventionalInvoiceInfo is not None:
            showIndent(outfile, level)
            outfile.write('conventionalInvoiceInfo=model_.ConventionalInvoiceInfoType(\n')
            self.conventionalInvoiceInfo.exportLiteral(outfile, level, name_='conventionalInvoiceInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('additionalInvoiceData=[\n')
        level += 1
        for additionalInvoiceData_ in self.additionalInvoiceData:
            showIndent(outfile, level)
            outfile.write('model_.AdditionalDataType(\n')
            additionalInvoiceData_.exportLiteral(outfile, level, name_='AdditionalDataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'invoiceCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceCategory')
            value_ = self.gds_validate_string(value_, node, 'invoiceCategory')
            self.invoiceCategory = value_
            self.invoiceCategory_nsprefix_ = child_.prefix
            # validate type InvoiceCategoryType
            self.validate_InvoiceCategoryType(self.invoiceCategory)
        elif nodeName_ == 'invoiceDeliveryDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.invoiceDeliveryDate = dval_
            self.invoiceDeliveryDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.invoiceDeliveryDate)
        elif nodeName_ == 'invoiceDeliveryPeriodStart':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.invoiceDeliveryPeriodStart = dval_
            self.invoiceDeliveryPeriodStart_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.invoiceDeliveryPeriodStart)
        elif nodeName_ == 'invoiceDeliveryPeriodEnd':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.invoiceDeliveryPeriodEnd = dval_
            self.invoiceDeliveryPeriodEnd_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.invoiceDeliveryPeriodEnd)
        elif nodeName_ == 'invoiceAccountingDeliveryDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.invoiceAccountingDeliveryDate = dval_
            self.invoiceAccountingDeliveryDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.invoiceAccountingDeliveryDate)
        elif nodeName_ == 'periodicalSettlement':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'periodicalSettlement')
            ival_ = self.gds_validate_boolean(ival_, node, 'periodicalSettlement')
            self.periodicalSettlement = ival_
            self.periodicalSettlement_nsprefix_ = child_.prefix
        elif nodeName_ == 'smallBusinessIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'smallBusinessIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'smallBusinessIndicator')
            self.smallBusinessIndicator = ival_
            self.smallBusinessIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'currencyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currencyCode')
            value_ = self.gds_validate_string(value_, node, 'currencyCode')
            self.currencyCode = value_
            self.currencyCode_nsprefix_ = child_.prefix
            # validate type CurrencyType
            self.validate_CurrencyType(self.currencyCode)
        elif nodeName_ == 'exchangeRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'exchangeRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'exchangeRate')
            self.exchangeRate = fval_
            self.exchangeRate_nsprefix_ = child_.prefix
            # validate type ExchangeRateType
            self.validate_ExchangeRateType(self.exchangeRate)
        elif nodeName_ == 'utilitySettlementIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'utilitySettlementIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'utilitySettlementIndicator')
            self.utilitySettlementIndicator = ival_
            self.utilitySettlementIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'selfBillingIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'selfBillingIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'selfBillingIndicator')
            self.selfBillingIndicator = ival_
            self.selfBillingIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'paymentMethod':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'paymentMethod')
            value_ = self.gds_validate_string(value_, node, 'paymentMethod')
            self.paymentMethod = value_
            self.paymentMethod_nsprefix_ = child_.prefix
            # validate type PaymentMethodType
            self.validate_PaymentMethodType(self.paymentMethod)
        elif nodeName_ == 'paymentDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.paymentDate = dval_
            self.paymentDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.paymentDate)
        elif nodeName_ == 'cashAccountingIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cashAccountingIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'cashAccountingIndicator')
            self.cashAccountingIndicator = ival_
            self.cashAccountingIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'invoiceAppearance':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceAppearance')
            value_ = self.gds_validate_string(value_, node, 'invoiceAppearance')
            self.invoiceAppearance = value_
            self.invoiceAppearance_nsprefix_ = child_.prefix
            # validate type InvoiceAppearanceType
            self.validate_InvoiceAppearanceType(self.invoiceAppearance)
        elif nodeName_ == 'conventionalInvoiceInfo':
            obj_ = ConventionalInvoiceInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.conventionalInvoiceInfo = obj_
            obj_.original_tagname_ = 'conventionalInvoiceInfo'
        elif nodeName_ == 'additionalInvoiceData':
            obj_ = AdditionalDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.additionalInvoiceData.append(obj_)
            obj_.original_tagname_ = 'additionalInvoiceData'
