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


class InvoiceDigestType(GeneratedsSuper):
    """InvoiceDigestType -- Kivonatos lekérdezési eredmény
    Digest query result
    invoiceNumber -- Számla vagy módosító okirat sorszáma - ÁFA tv. 169.§ b) vagy 170.§ (1) bek. b) pont
            Sequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law
    batchIndex -- A módosító okirat sorszáma a kötegen belül
            Sequence number of the modification document within the batch
    invoiceOperation -- Számlaművelet típus
            Invoice operation type
    invoiceCategory -- A számla típusa
            Type of invoice
    invoiceIssueDate -- Számla vagy módosító okirat kiállításának dátuma
            Invoice or modification document issue date
    supplierTaxNumber -- A kibocsátó adószáma
            The supplier's tax number
    supplierGroupMemberTaxNumber -- A kibocsátó csoporttag száma
            The supplier's group tax number
    supplierName -- Az eladó (szállító) neve
            Name of the seller (supplier)
    customerTaxNumber -- A vevő adószáma
            The buyer's tax number
    customerGroupMemberTaxNumber -- A vevő csoporttag száma
            The buyer's group tax number
    customerName -- A vevő neve
            Name of the customer
    paymentMethod -- Fizetés módja
            Method of payment
    paymentDate -- Fizetési határidő
            Deadline for payment
    invoiceAppearance -- A számla megjelenési formája
            Form of appearance of the invoice
    source -- Az adatszolgáltatás forrása
            Data exchange source
    invoiceDeliveryDate -- Számla teljesítési dátuma
            Invoice delivery date
    currency -- A számla pénzneme
            Currency of the invoice
    invoiceNetAmount -- A számla nettó összege a számla pénznemében
            Invoice net amount expressed in the currency of the invoice
    invoiceNetAmountHUF -- A számla nettó összege forintban
            Invoice net amount expressed in HUF
    invoiceVatAmount -- A számla ÁFA összege a számla pénznemében
            Invoice VAT amount expressed in the currency of the invoice
    invoiceVatAmountHUF -- A számla ÁFA összege forintban
            Invoice VAT amount expressed in HUF
    transactionId -- Az adatszolgáltatás tranzakció azonosítója
            Transaction identifier of the data exchange
    index -- A számla sorszáma a kérésen belül
            Sequence number of the invoice within the request
    originalInvoiceNumber -- Az eredeti számla sorszáma, melyre a módosítás vonatkozik
            Sequence number of the original invoice, on which the modification occurs
    modificationIndex -- A számlára vonatkozó módosító okirat egyedi sorszáma
            The unique sequence number referring to the original invoice
    insDate -- A beszúrás időpontja UTC időben
            Insert date in UTC time
    completenessIndicator -- Jelöli, ha az adatszolgáltatás maga a számla (a számlán nem szerepel több adat)
            Indicates whether the data exchange is identical with the invoice (the invoice does not contain any more data)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, invoiceNumber=None, batchIndex=None, invoiceOperation=None, invoiceCategory=None,
                 invoiceIssueDate=None, supplierTaxNumber=None, supplierGroupMemberTaxNumber=None, supplierName=None,
                 customerTaxNumber=None, customerGroupMemberTaxNumber=None, customerName=None, paymentMethod=None,
                 paymentDate=None, invoiceAppearance=None, source=None, invoiceDeliveryDate=None, currency=None,
                 invoiceNetAmount=None, invoiceNetAmountHUF=None, invoiceVatAmount=None, invoiceVatAmountHUF=None,
                 transactionId=None, index=None, originalInvoiceNumber=None, modificationIndex=None, insDate=None,
                 completenessIndicator=None, gds_collector_=None, **kwargs_):
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
        self.invoiceCategory = invoiceCategory
        self.validate_InvoiceCategoryType(self.invoiceCategory)
        self.invoiceCategory_nsprefix_ = "base"
        if isinstance(invoiceIssueDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(invoiceIssueDate, '%Y-%m-%d').date()
        else:
            initvalue_ = invoiceIssueDate
        self.invoiceIssueDate = initvalue_
        self.invoiceIssueDate_nsprefix_ = "base"
        self.supplierTaxNumber = supplierTaxNumber
        self.validate_TaxpayerIdType(self.supplierTaxNumber)
        self.supplierTaxNumber_nsprefix_ = "common"
        self.supplierGroupMemberTaxNumber = supplierGroupMemberTaxNumber
        self.validate_TaxpayerIdType(self.supplierGroupMemberTaxNumber)
        self.supplierGroupMemberTaxNumber_nsprefix_ = "common"
        self.supplierName = supplierName
        self.validate_SimpleText512NotBlankType(self.supplierName)
        self.supplierName_nsprefix_ = "common"
        self.customerTaxNumber = customerTaxNumber
        self.validate_TaxpayerIdType(self.customerTaxNumber)
        self.customerTaxNumber_nsprefix_ = "common"
        self.customerGroupMemberTaxNumber = customerGroupMemberTaxNumber
        self.validate_TaxpayerIdType(self.customerGroupMemberTaxNumber)
        self.customerGroupMemberTaxNumber_nsprefix_ = "common"
        self.customerName = customerName
        self.validate_SimpleText512NotBlankType(self.customerName)
        self.customerName_nsprefix_ = "common"
        self.paymentMethod = paymentMethod
        self.validate_PaymentMethodType(self.paymentMethod)
        self.paymentMethod_nsprefix_ = "base"
        if isinstance(paymentDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(paymentDate, '%Y-%m-%d').date()
        else:
            initvalue_ = paymentDate
        self.paymentDate = initvalue_
        self.paymentDate_nsprefix_ = "base"
        self.invoiceAppearance = invoiceAppearance
        self.validate_InvoiceAppearanceType(self.invoiceAppearance)
        self.invoiceAppearance_nsprefix_ = "base"
        self.source = source
        self.validate_SourceType(self.source)
        self.source_nsprefix_ = None
        if isinstance(invoiceDeliveryDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(invoiceDeliveryDate, '%Y-%m-%d').date()
        else:
            initvalue_ = invoiceDeliveryDate
        self.invoiceDeliveryDate = initvalue_
        self.invoiceDeliveryDate_nsprefix_ = "base"
        self.currency = currency
        self.validate_CurrencyType(self.currency)
        self.currency_nsprefix_ = "common"
        self.invoiceNetAmount = invoiceNetAmount
        self.validate_MonetaryType(self.invoiceNetAmount)
        self.invoiceNetAmount_nsprefix_ = "base"
        self.invoiceNetAmountHUF = invoiceNetAmountHUF
        self.validate_MonetaryType(self.invoiceNetAmountHUF)
        self.invoiceNetAmountHUF_nsprefix_ = "base"
        self.invoiceVatAmount = invoiceVatAmount
        self.validate_MonetaryType(self.invoiceVatAmount)
        self.invoiceVatAmount_nsprefix_ = "base"
        self.invoiceVatAmountHUF = invoiceVatAmountHUF
        self.validate_MonetaryType(self.invoiceVatAmountHUF)
        self.invoiceVatAmountHUF_nsprefix_ = "base"
        self.transactionId = transactionId
        self.validate_EntityIdType(self.transactionId)
        self.transactionId_nsprefix_ = "common"
        self.index = index
        self.validate_InvoiceIndexType(self.index)
        self.index_nsprefix_ = "base"
        self.originalInvoiceNumber = originalInvoiceNumber
        self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
        self.originalInvoiceNumber_nsprefix_ = "common"
        self.modificationIndex = modificationIndex
        self.validate_InvoiceUnboundedIndexType(self.modificationIndex)
        self.modificationIndex_nsprefix_ = "base"
        if isinstance(insDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(insDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = insDate
        self.insDate = initvalue_
        self.insDate_nsprefix_ = "base"
        self.completenessIndicator = completenessIndicator
        self.completenessIndicator_nsprefix_ = "xs"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceDigestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceDigestType.subclass:
            return InvoiceDigestType.subclass(*args_, **kwargs_)
        else:
            return InvoiceDigestType(*args_, **kwargs_)

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

    def get_invoiceCategory(self):
        return self.invoiceCategory

    def set_invoiceCategory(self, invoiceCategory):
        self.invoiceCategory = invoiceCategory

    def get_invoiceIssueDate(self):
        return self.invoiceIssueDate

    def set_invoiceIssueDate(self, invoiceIssueDate):
        self.invoiceIssueDate = invoiceIssueDate

    def get_supplierTaxNumber(self):
        return self.supplierTaxNumber

    def set_supplierTaxNumber(self, supplierTaxNumber):
        self.supplierTaxNumber = supplierTaxNumber

    def get_supplierGroupMemberTaxNumber(self):
        return self.supplierGroupMemberTaxNumber

    def set_supplierGroupMemberTaxNumber(self, supplierGroupMemberTaxNumber):
        self.supplierGroupMemberTaxNumber = supplierGroupMemberTaxNumber

    def get_supplierName(self):
        return self.supplierName

    def set_supplierName(self, supplierName):
        self.supplierName = supplierName

    def get_customerTaxNumber(self):
        return self.customerTaxNumber

    def set_customerTaxNumber(self, customerTaxNumber):
        self.customerTaxNumber = customerTaxNumber

    def get_customerGroupMemberTaxNumber(self):
        return self.customerGroupMemberTaxNumber

    def set_customerGroupMemberTaxNumber(self, customerGroupMemberTaxNumber):
        self.customerGroupMemberTaxNumber = customerGroupMemberTaxNumber

    def get_customerName(self):
        return self.customerName

    def set_customerName(self, customerName):
        self.customerName = customerName

    def get_paymentMethod(self):
        return self.paymentMethod

    def set_paymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod

    def get_paymentDate(self):
        return self.paymentDate

    def set_paymentDate(self, paymentDate):
        self.paymentDate = paymentDate

    def get_invoiceAppearance(self):
        return self.invoiceAppearance

    def set_invoiceAppearance(self, invoiceAppearance):
        self.invoiceAppearance = invoiceAppearance

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source

    def get_invoiceDeliveryDate(self):
        return self.invoiceDeliveryDate

    def set_invoiceDeliveryDate(self, invoiceDeliveryDate):
        self.invoiceDeliveryDate = invoiceDeliveryDate

    def get_currency(self):
        return self.currency

    def set_currency(self, currency):
        self.currency = currency

    def get_invoiceNetAmount(self):
        return self.invoiceNetAmount

    def set_invoiceNetAmount(self, invoiceNetAmount):
        self.invoiceNetAmount = invoiceNetAmount

    def get_invoiceNetAmountHUF(self):
        return self.invoiceNetAmountHUF

    def set_invoiceNetAmountHUF(self, invoiceNetAmountHUF):
        self.invoiceNetAmountHUF = invoiceNetAmountHUF

    def get_invoiceVatAmount(self):
        return self.invoiceVatAmount

    def set_invoiceVatAmount(self, invoiceVatAmount):
        self.invoiceVatAmount = invoiceVatAmount

    def get_invoiceVatAmountHUF(self):
        return self.invoiceVatAmountHUF

    def set_invoiceVatAmountHUF(self, invoiceVatAmountHUF):
        self.invoiceVatAmountHUF = invoiceVatAmountHUF

    def get_transactionId(self):
        return self.transactionId

    def set_transactionId(self, transactionId):
        self.transactionId = transactionId

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_originalInvoiceNumber(self):
        return self.originalInvoiceNumber

    def set_originalInvoiceNumber(self, originalInvoiceNumber):
        self.originalInvoiceNumber = originalInvoiceNumber

    def get_modificationIndex(self):
        return self.modificationIndex

    def set_modificationIndex(self, modificationIndex):
        self.modificationIndex = modificationIndex

    def get_insDate(self):
        return self.insDate

    def set_insDate(self, insDate):
        self.insDate = insDate

    def get_completenessIndicator(self):
        return self.completenessIndicator

    def set_completenessIndicator(self, completenessIndicator):
        self.completenessIndicator = completenessIndicator

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

    def validate_InvoiceCategoryType(self, value):
        result = True
        # Validate type InvoiceCategoryType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['NORMAL', 'SIMPLIFIED', 'AGGREGATE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on InvoiceCategoryType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on InvoiceCategoryType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on InvoiceCategoryType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_InvoiceDateType_patterns_,))
                result = False
        return result

    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]

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

    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def validate_PaymentMethodType(self, value):
        result = True
        # Validate type PaymentMethodType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['TRANSFER', 'CASH', 'CARD', 'VOUCHER', 'OTHER']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on PaymentMethodType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PaymentMethodType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PaymentMethodType' % {
                        "value": value, "lineno": lineno})
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
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on InvoiceAppearanceType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on InvoiceAppearanceType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on InvoiceAppearanceType' % {
                        "value": value, "lineno": lineno})
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
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on SourceType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SourceType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SourceType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_CurrencyType(self, value):
        result = True
        # Validate type CurrencyType, a restriction on AtomicStringType4.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on CurrencyType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CurrencyType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CurrencyType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CurrencyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_CurrencyType_patterns_,))
                result = False
        return result

    validate_CurrencyType_patterns_ = [['^([A-Z]{3})$']]

    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_EntityIdType(self, value):
        result = True
        # Validate type EntityIdType, a restriction on AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EntityIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_EntityIdType_patterns_,))
                result = False
        return result

    validate_EntityIdType_patterns_ = [['^([+a-zA-Z0-9_]{1,30})$']]

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

    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
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

    def _hasContent(self):
        if (
                self.invoiceNumber is not None or
                self.batchIndex is not None or
                self.invoiceOperation is not None or
                self.invoiceCategory is not None or
                self.invoiceIssueDate is not None or
                self.supplierTaxNumber is not None or
                self.supplierGroupMemberTaxNumber is not None or
                self.supplierName is not None or
                self.customerTaxNumber is not None or
                self.customerGroupMemberTaxNumber is not None or
                self.customerName is not None or
                self.paymentMethod is not None or
                self.paymentDate is not None or
                self.invoiceAppearance is not None or
                self.source is not None or
                self.invoiceDeliveryDate is not None or
                self.currency is not None or
                self.invoiceNetAmount is not None or
                self.invoiceNetAmountHUF is not None or
                self.invoiceVatAmount is not None or
                self.invoiceVatAmountHUF is not None or
                self.transactionId is not None or
                self.index is not None or
                self.originalInvoiceNumber is not None or
                self.modificationIndex is not None or
                self.insDate is not None or
                self.completenessIndicator is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ',
               name_='InvoiceDigestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceDigestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceDigestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceDigestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceDigestType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceDigestType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ',
                        name_='InvoiceDigestType', fromsubclass_=False, pretty_print=True):
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
        if self.invoiceCategory is not None:
            namespaceprefix_ = self.invoiceCategory_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceCategory>%s</%sinvoiceCategory>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.invoiceCategory), input_name='invoiceCategory')),
                                                                           namespaceprefix_, eol_))
        if self.invoiceIssueDate is not None:
            namespaceprefix_ = self.invoiceIssueDate_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceIssueDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceIssueDate>%s</%sinvoiceIssueDate>%s' % (
            namespaceprefix_, self.gds_format_date(self.invoiceIssueDate, input_name='invoiceIssueDate'),
            namespaceprefix_, eol_))
        if self.supplierTaxNumber is not None:
            namespaceprefix_ = self.supplierTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.supplierTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierTaxNumber>%s</%ssupplierTaxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.supplierTaxNumber), input_name='supplierTaxNumber')),
                                                                               namespaceprefix_, eol_))
        if self.supplierGroupMemberTaxNumber is not None:
            namespaceprefix_ = self.supplierGroupMemberTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.supplierGroupMemberTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierGroupMemberTaxNumber>%s</%ssupplierGroupMemberTaxNumber>%s' % (namespaceprefix_,
                                                                                                     self.gds_encode(
                                                                                                         self.gds_format_string(
                                                                                                             quote_xml(
                                                                                                                 self.supplierGroupMemberTaxNumber),
                                                                                                             input_name='supplierGroupMemberTaxNumber')),
                                                                                                     namespaceprefix_,
                                                                                                     eol_))
        if self.supplierName is not None:
            namespaceprefix_ = self.supplierName_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.supplierName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierName>%s</%ssupplierName>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.supplierName), input_name='supplierName')), namespaceprefix_,
                                                                     eol_))
        if self.customerTaxNumber is not None:
            namespaceprefix_ = self.customerTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.customerTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerTaxNumber>%s</%scustomerTaxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.customerTaxNumber), input_name='customerTaxNumber')),
                                                                               namespaceprefix_, eol_))
        if self.customerGroupMemberTaxNumber is not None:
            namespaceprefix_ = self.customerGroupMemberTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.customerGroupMemberTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerGroupMemberTaxNumber>%s</%scustomerGroupMemberTaxNumber>%s' % (namespaceprefix_,
                                                                                                     self.gds_encode(
                                                                                                         self.gds_format_string(
                                                                                                             quote_xml(
                                                                                                                 self.customerGroupMemberTaxNumber),
                                                                                                             input_name='customerGroupMemberTaxNumber')),
                                                                                                     namespaceprefix_,
                                                                                                     eol_))
        if self.customerName is not None:
            namespaceprefix_ = self.customerName_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.customerName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerName>%s</%scustomerName>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.customerName), input_name='customerName')), namespaceprefix_,
                                                                     eol_))
        if self.paymentMethod is not None:
            namespaceprefix_ = self.paymentMethod_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.paymentMethod_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaymentMethod>%s</%spaymentMethod>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.paymentMethod), input_name='paymentMethod')), namespaceprefix_,
                                                                       eol_))
        if self.paymentDate is not None:
            namespaceprefix_ = self.paymentDate_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.paymentDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaymentDate>%s</%spaymentDate>%s' % (
            namespaceprefix_, self.gds_format_date(self.paymentDate, input_name='paymentDate'), namespaceprefix_, eol_))
        if self.invoiceAppearance is not None:
            namespaceprefix_ = self.invoiceAppearance_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceAppearance_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceAppearance>%s</%sinvoiceAppearance>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.invoiceAppearance), input_name='invoiceAppearance')),
                                                                               namespaceprefix_, eol_))
        if self.source is not None:
            namespaceprefix_ = self.source_nsprefix_ + ':' if (UseCapturedNS_ and self.source_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssource>%s</%ssource>%s' % (
            namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.source), input_name='source')),
            namespaceprefix_, eol_))
        if self.invoiceDeliveryDate is not None:
            namespaceprefix_ = self.invoiceDeliveryDate_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceDeliveryDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceDeliveryDate>%s</%sinvoiceDeliveryDate>%s' % (
            namespaceprefix_, self.gds_format_date(self.invoiceDeliveryDate, input_name='invoiceDeliveryDate'),
            namespaceprefix_, eol_))
        if self.currency is not None:
            namespaceprefix_ = self.currency_nsprefix_ + ':' if (UseCapturedNS_ and self.currency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrency>%s</%scurrency>%s' % (
            namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.currency), input_name='currency')),
            namespaceprefix_, eol_))
        if self.invoiceNetAmount is not None:
            namespaceprefix_ = self.invoiceNetAmount_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceNetAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNetAmount>%s</%sinvoiceNetAmount>%s' % (
            namespaceprefix_, self.gds_format_decimal(self.invoiceNetAmount, input_name='invoiceNetAmount'),
            namespaceprefix_, eol_))
        if self.invoiceNetAmountHUF is not None:
            namespaceprefix_ = self.invoiceNetAmountHUF_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceNetAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNetAmountHUF>%s</%sinvoiceNetAmountHUF>%s' % (
            namespaceprefix_, self.gds_format_decimal(self.invoiceNetAmountHUF, input_name='invoiceNetAmountHUF'),
            namespaceprefix_, eol_))
        if self.invoiceVatAmount is not None:
            namespaceprefix_ = self.invoiceVatAmount_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceVatAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceVatAmount>%s</%sinvoiceVatAmount>%s' % (
            namespaceprefix_, self.gds_format_decimal(self.invoiceVatAmount, input_name='invoiceVatAmount'),
            namespaceprefix_, eol_))
        if self.invoiceVatAmountHUF is not None:
            namespaceprefix_ = self.invoiceVatAmountHUF_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceVatAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceVatAmountHUF>%s</%sinvoiceVatAmountHUF>%s' % (
            namespaceprefix_, self.gds_format_decimal(self.invoiceVatAmountHUF, input_name='invoiceVatAmountHUF'),
            namespaceprefix_, eol_))
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.transactionId), input_name='transactionId')), namespaceprefix_,
                                                                       eol_))
        if self.index is not None:
            namespaceprefix_ = self.index_nsprefix_ + ':' if (UseCapturedNS_ and self.index_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindex>%s</%sindex>%s' % (
            namespaceprefix_, self.gds_format_integer(self.index, input_name='index'), namespaceprefix_, eol_))
        if self.originalInvoiceNumber is not None:
            namespaceprefix_ = self.originalInvoiceNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.originalInvoiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalInvoiceNumber>%s</%soriginalInvoiceNumber>%s' % (namespaceprefix_,
                                                                                       self.gds_encode(
                                                                                           self.gds_format_string(
                                                                                               quote_xml(
                                                                                                   self.originalInvoiceNumber),
                                                                                               input_name='originalInvoiceNumber')),
                                                                                       namespaceprefix_, eol_))
        if self.modificationIndex is not None:
            namespaceprefix_ = self.modificationIndex_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.modificationIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smodificationIndex>%s</%smodificationIndex>%s' % (
            namespaceprefix_, self.gds_format_integer(self.modificationIndex, input_name='modificationIndex'),
            namespaceprefix_, eol_))
        if self.insDate is not None:
            namespaceprefix_ = self.insDate_nsprefix_ + ':' if (UseCapturedNS_ and self.insDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinsDate>%s</%sinsDate>%s' % (
            namespaceprefix_, self.gds_format_datetime(self.insDate, input_name='insDate'), namespaceprefix_, eol_))
        if self.completenessIndicator is not None:
            namespaceprefix_ = self.completenessIndicator_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.completenessIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompletenessIndicator>%s</%scompletenessIndicator>%s' % (
            namespaceprefix_, self.gds_format_boolean(self.completenessIndicator, input_name='completenessIndicator'),
            namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='InvoiceDigestType', mapping_=None, nsmap_=None):
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
        if self.invoiceCategory is not None:
            invoiceCategory_ = self.invoiceCategory
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceCategory').text = self.gds_format_string(
                invoiceCategory_)
        if self.invoiceIssueDate is not None:
            invoiceIssueDate_ = self.invoiceIssueDate
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceIssueDate').text = self.gds_format_date(
                invoiceIssueDate_)
        if self.supplierTaxNumber is not None:
            supplierTaxNumber_ = self.supplierTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}supplierTaxNumber').text = self.gds_format_string(
                supplierTaxNumber_)
        if self.supplierGroupMemberTaxNumber is not None:
            supplierGroupMemberTaxNumber_ = self.supplierGroupMemberTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}supplierGroupMemberTaxNumber').text = self.gds_format_string(
                supplierGroupMemberTaxNumber_)
        if self.supplierName is not None:
            supplierName_ = self.supplierName
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}supplierName').text = self.gds_format_string(
                supplierName_)
        if self.customerTaxNumber is not None:
            customerTaxNumber_ = self.customerTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}customerTaxNumber').text = self.gds_format_string(
                customerTaxNumber_)
        if self.customerGroupMemberTaxNumber is not None:
            customerGroupMemberTaxNumber_ = self.customerGroupMemberTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}customerGroupMemberTaxNumber').text = self.gds_format_string(
                customerGroupMemberTaxNumber_)
        if self.customerName is not None:
            customerName_ = self.customerName
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}customerName').text = self.gds_format_string(
                customerName_)
        if self.paymentMethod is not None:
            paymentMethod_ = self.paymentMethod
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}paymentMethod').text = self.gds_format_string(
                paymentMethod_)
        if self.paymentDate is not None:
            paymentDate_ = self.paymentDate
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}paymentDate').text = self.gds_format_date(
                paymentDate_)
        if self.invoiceAppearance is not None:
            invoiceAppearance_ = self.invoiceAppearance
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceAppearance').text = self.gds_format_string(
                invoiceAppearance_)
        if self.source is not None:
            source_ = self.source
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}source').text = self.gds_format_string(
                source_)
        if self.invoiceDeliveryDate is not None:
            invoiceDeliveryDate_ = self.invoiceDeliveryDate
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDeliveryDate').text = self.gds_format_date(
                invoiceDeliveryDate_)
        if self.currency is not None:
            currency_ = self.currency
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}currency').text = self.gds_format_string(
                currency_)
        if self.invoiceNetAmount is not None:
            invoiceNetAmount_ = self.invoiceNetAmount
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNetAmount').text = self.gds_format_decimal(
                invoiceNetAmount_)
        if self.invoiceNetAmountHUF is not None:
            invoiceNetAmountHUF_ = self.invoiceNetAmountHUF
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNetAmountHUF').text = self.gds_format_decimal(
                invoiceNetAmountHUF_)
        if self.invoiceVatAmount is not None:
            invoiceVatAmount_ = self.invoiceVatAmount
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceVatAmount').text = self.gds_format_decimal(
                invoiceVatAmount_)
        if self.invoiceVatAmountHUF is not None:
            invoiceVatAmountHUF_ = self.invoiceVatAmountHUF
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceVatAmountHUF').text = self.gds_format_decimal(
                invoiceVatAmountHUF_)
        if self.transactionId is not None:
            transactionId_ = self.transactionId
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}transactionId').text = self.gds_format_string(
                transactionId_)
        if self.index is not None:
            index_ = self.index
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}index').text = self.gds_format_integer(
                index_)
        if self.originalInvoiceNumber is not None:
            originalInvoiceNumber_ = self.originalInvoiceNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber').text = self.gds_format_string(
                originalInvoiceNumber_)
        if self.modificationIndex is not None:
            modificationIndex_ = self.modificationIndex
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}modificationIndex').text = self.gds_format_integer(
                modificationIndex_)
        if self.insDate is not None:
            insDate_ = self.insDate
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}insDate').text = self.gds_format_datetime(
                insDate_)
        if self.completenessIndicator is not None:
            completenessIndicator_ = self.completenessIndicator
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}completenessIndicator').text = self.gds_format_boolean(
                completenessIndicator_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceDigestType'):
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
        if self.invoiceCategory is not None:
            showIndent(outfile, level)
            outfile.write('invoiceCategory=%s,\n' % self.gds_encode(quote_python(self.invoiceCategory)))
        if self.invoiceIssueDate is not None:
            showIndent(outfile, level)
            outfile.write('invoiceIssueDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(
                self.invoiceIssueDate, input_name='invoiceIssueDate'))
        if self.supplierTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('supplierTaxNumber=%s,\n' % self.gds_encode(quote_python(self.supplierTaxNumber)))
        if self.supplierGroupMemberTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write(
                'supplierGroupMemberTaxNumber=%s,\n' % self.gds_encode(quote_python(self.supplierGroupMemberTaxNumber)))
        if self.supplierName is not None:
            showIndent(outfile, level)
            outfile.write('supplierName=%s,\n' % self.gds_encode(quote_python(self.supplierName)))
        if self.customerTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('customerTaxNumber=%s,\n' % self.gds_encode(quote_python(self.customerTaxNumber)))
        if self.customerGroupMemberTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write(
                'customerGroupMemberTaxNumber=%s,\n' % self.gds_encode(quote_python(self.customerGroupMemberTaxNumber)))
        if self.customerName is not None:
            showIndent(outfile, level)
            outfile.write('customerName=%s,\n' % self.gds_encode(quote_python(self.customerName)))
        if self.paymentMethod is not None:
            showIndent(outfile, level)
            outfile.write('paymentMethod=%s,\n' % self.gds_encode(quote_python(self.paymentMethod)))
        if self.paymentDate is not None:
            showIndent(outfile, level)
            outfile.write(
                'paymentDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.paymentDate,
                                                                                                    input_name='paymentDate'))
        if self.invoiceAppearance is not None:
            showIndent(outfile, level)
            outfile.write('invoiceAppearance=%s,\n' % self.gds_encode(quote_python(self.invoiceAppearance)))
        if self.source is not None:
            showIndent(outfile, level)
            outfile.write('source=%s,\n' % self.gds_encode(quote_python(self.source)))
        if self.invoiceDeliveryDate is not None:
            showIndent(outfile, level)
            outfile.write('invoiceDeliveryDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(
                self.invoiceDeliveryDate, input_name='invoiceDeliveryDate'))
        if self.currency is not None:
            showIndent(outfile, level)
            outfile.write('currency=%s,\n' % self.gds_encode(quote_python(self.currency)))
        if self.invoiceNetAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNetAmount=%f,\n' % self.invoiceNetAmount)
        if self.invoiceNetAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNetAmountHUF=%f,\n' % self.invoiceNetAmountHUF)
        if self.invoiceVatAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceVatAmount=%f,\n' % self.invoiceVatAmount)
        if self.invoiceVatAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceVatAmountHUF=%f,\n' % self.invoiceVatAmountHUF)
        if self.transactionId is not None:
            showIndent(outfile, level)
            outfile.write('transactionId=%s,\n' % self.gds_encode(quote_python(self.transactionId)))
        if self.index is not None:
            showIndent(outfile, level)
            outfile.write('index=%d,\n' % self.index)
        if self.originalInvoiceNumber is not None:
            showIndent(outfile, level)
            outfile.write('originalInvoiceNumber=%s,\n' % self.gds_encode(quote_python(self.originalInvoiceNumber)))
        if self.modificationIndex is not None:
            showIndent(outfile, level)
            outfile.write('modificationIndex=%d,\n' % self.modificationIndex)
        if self.insDate is not None:
            showIndent(outfile, level)
            outfile.write(
                'insDate=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.insDate,
                                                                                                        input_name='insDate'))
        if self.completenessIndicator is not None:
            showIndent(outfile, level)
            outfile.write('completenessIndicator=%s,\n' % self.completenessIndicator)

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
        elif nodeName_ == 'invoiceCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceCategory')
            value_ = self.gds_validate_string(value_, node, 'invoiceCategory')
            self.invoiceCategory = value_
            self.invoiceCategory_nsprefix_ = child_.prefix
            # validate type InvoiceCategoryType
            self.validate_InvoiceCategoryType(self.invoiceCategory)
        elif nodeName_ == 'invoiceIssueDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.invoiceIssueDate = dval_
            self.invoiceIssueDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.invoiceIssueDate)
        elif nodeName_ == 'supplierTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'supplierTaxNumber')
            self.supplierTaxNumber = value_
            self.supplierTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.supplierTaxNumber)
        elif nodeName_ == 'supplierGroupMemberTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierGroupMemberTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'supplierGroupMemberTaxNumber')
            self.supplierGroupMemberTaxNumber = value_
            self.supplierGroupMemberTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.supplierGroupMemberTaxNumber)
        elif nodeName_ == 'supplierName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierName')
            value_ = self.gds_validate_string(value_, node, 'supplierName')
            self.supplierName = value_
            self.supplierName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.supplierName)
        elif nodeName_ == 'customerTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'customerTaxNumber')
            self.customerTaxNumber = value_
            self.customerTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.customerTaxNumber)
        elif nodeName_ == 'customerGroupMemberTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerGroupMemberTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'customerGroupMemberTaxNumber')
            self.customerGroupMemberTaxNumber = value_
            self.customerGroupMemberTaxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.customerGroupMemberTaxNumber)
        elif nodeName_ == 'customerName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerName')
            value_ = self.gds_validate_string(value_, node, 'customerName')
            self.customerName = value_
            self.customerName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.customerName)
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
        elif nodeName_ == 'invoiceDeliveryDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.invoiceDeliveryDate = dval_
            self.invoiceDeliveryDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.invoiceDeliveryDate)
        elif nodeName_ == 'currency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currency')
            value_ = self.gds_validate_string(value_, node, 'currency')
            self.currency = value_
            self.currency_nsprefix_ = child_.prefix
            # validate type CurrencyType
            self.validate_CurrencyType(self.currency)
        elif nodeName_ == 'invoiceNetAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceNetAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceNetAmount')
            self.invoiceNetAmount = fval_
            self.invoiceNetAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceNetAmount)
        elif nodeName_ == 'invoiceNetAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceNetAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceNetAmountHUF')
            self.invoiceNetAmountHUF = fval_
            self.invoiceNetAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceNetAmountHUF)
        elif nodeName_ == 'invoiceVatAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceVatAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceVatAmount')
            self.invoiceVatAmount = fval_
            self.invoiceVatAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceVatAmount)
        elif nodeName_ == 'invoiceVatAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceVatAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceVatAmountHUF')
            self.invoiceVatAmountHUF = fval_
            self.invoiceVatAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceVatAmountHUF)
        elif nodeName_ == 'transactionId':
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
        elif nodeName_ == 'originalInvoiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalInvoiceNumber')
            value_ = self.gds_validate_string(value_, node, 'originalInvoiceNumber')
            self.originalInvoiceNumber = value_
            self.originalInvoiceNumber_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
        elif nodeName_ == 'modificationIndex' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'modificationIndex')
            ival_ = self.gds_validate_integer(ival_, node, 'modificationIndex')
            self.modificationIndex = ival_
            self.modificationIndex_nsprefix_ = child_.prefix
            # validate type InvoiceUnboundedIndexType
            self.validate_InvoiceUnboundedIndexType(self.modificationIndex)
        elif nodeName_ == 'insDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.insDate = dval_
            self.insDate_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.insDate)
        elif nodeName_ == 'completenessIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'completenessIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'completenessIndicator')
            self.completenessIndicator = ival_
            self.completenessIndicator_nsprefix_ = child_.prefix
