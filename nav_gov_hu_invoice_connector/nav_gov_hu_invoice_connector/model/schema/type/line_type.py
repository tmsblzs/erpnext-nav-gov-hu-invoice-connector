import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, raise_parse_error
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.additional_data_type import \
    AdditionalDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.advance_data_type import \
    AdvanceDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.aggregate_invoice_line_data_type import \
    AggregateInvoiceLineDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.conventional_invoice_info_type import \
    ConventionalInvoiceInfoType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.diesel_oil_purchase_type import \
    DieselOilPurchaseType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.discount_data_type import \
    DiscountDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.line_amounts_normal_type import \
    LineAmountsNormalType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.line_amounts_simplified_type import \
    LineAmountsSimplifiedType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.line_modification_reference_type import \
    LineModificationReferenceType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.new_transport_mean_type import \
    NewTransportMeanType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.product_codes_type import \
    ProductCodesType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.product_fee_clause_type import \
    ProductFeeClauseType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.product_fee_data_type import \
    ProductFeeDataType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.references_to_other_lines_type import \
    ReferencesToOtherLinesType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class LineType(GeneratedsSuper):
    """LineType -- A számla tételek (termék vagy szolgáltatás) adatait tartalmazó típus
    Field type including data of invoice items (product or service)
    lineNumber -- A tétel sorszáma
    Sequential number of the item
    lineModificationReference -- Módosításról történő adatszolgáltatás esetén a tételsor módosítás jellegének jelölése
    Marking the goal of modification of the line (in the case of data supply about changes/updates only)
    referencesToOtherLines -- Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükséges
    References to connected items if it is necessary according to VAT law
    advanceData -- Előleghez kapcsolódó adatok
    Advance related data
    productCodes -- Termékkódok
    Product codes
    lineExpressionIndicator -- Értéke true, ha a tétel mennyiségi egysége természetes mértékegységben kifejezhető
    The value is true if the unit of measure of the invoice item is expressible in natural unit
    lineNatureIndicator -- Adott tételsor termékértékesítés vagy szolgáltatás nyújtás jellegének jelzése
    Indication of the nature of the supply of goods or services on a given line
    lineDescription -- A termék vagy szolgáltatás megnevezése
    Name / description of the product or service
    quantity -- Mennyiség
    Quantity
    unitOfMeasure -- A számlán szereplő mennyiségi egység kanonikus kifejezése az interfész specifikáció szerint
    Canonical representation of the unit of measure of the invoice, according to the interface specification
    unitOfMeasureOwn -- A számlán szereplő mennyiségi egység literális kifejezése
    Literal unit of measure of the invoice
    unitPrice -- Egységár a számla pénznemében. Egyszerűsített számla esetén bruttó, egyéb esetben nettó egységár
    Unit price expressed in the currency of the invoice In the event of simplified invoices gross unit price,
        in other cases net unit price
    unitPriceHUF -- Egységár forintban
    Unit price expressed in HUF
    lineDiscountData -- A tételhez tartozó árengedmény adatok
    Discount data in relation to the item
    lineAmountsNormal -- Normál (nem egyszerűsített) számla esetén (beleértve a gyűjtőszámlát) kitöltendő tételérték adatok.
    Item value data to be completed in case of normal (not simplified, but including aggregated) invoice
    lineAmountsSimplified -- Egyszerűsített számla esetén kitöltendő tétel érték adatok
    Item value data to be completed in case of simplified invoice
    intermediatedService -- Értéke true ha a tétel közvetített szolgáltatás - Számviteli tv. 3. § (4) 1
    The value is true if the item is an intermediated service - paragraph (4) 1 of the Article 3 of Accounting Act
    aggregateInvoiceLineData -- Gyűjtőszámla adatok
    Aggregate invoice data
    newTransportMean -- Új közlekedési eszköz értékesítés ÁFA tv. 89 § ill. 169 § o)
    Supply of new means of transport - section 89 § and 169 (o) of the VAT law
    depositIndicator -- Értéke true, ha a tétel betétdíj jellegű
    The value is true if the item is bottle/container deposit
    obligatedForProductFee -- Értéke true ha a tételt termékdíj fizetési kötelezettség terheli
    The value is true if the item is liable to product fee
    GPCExcise -- Földgáz, villamos energia, szén jövedéki adója forintban - Jöt. 118. § (2)
    Excise duty on natural gas, electricity and coal in Hungarian forints – paragraph (2),
        Section 118 of the Act on Excise Duties
    dieselOilPurchase -- Gázolaj adózottan történő beszerzésének adatai – 45/2016 (XI. 29.) NGM rendelet 75. § (1) a)
    Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)
    netaDeclaration -- Értéke true, ha a Neta tv-ben meghatározott adókötelezettség az adóalanyát terheli.
        2011. évi CIII. tv. 3. § (2)
    Value is true, if the taxable person is liable for tax obligation determined in the Act on
        Public Health Product Tax (Neta tv.). Paragraph (2), Section 3 of the Act CIII of 2011
    productFeeClause -- A környezetvédelmi termékdíjról szóló 2011. évi LXXXV. tv. szerinti, tételre vonatkozó záradékok
    Clauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)
    lineProductFeeContent -- A tétel termékdíj tartalmára vonatkozó adatok
    Data on the content of the line's product charge
    conventionalLineInfo -- A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatok
    Other conventionally named data to assist in invoice processing
    additionalLineData -- A termék/szolgáltatás tételhez kapcsolódó, további adat
    Other data in relation to the product / service item

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineNumber=None, lineModificationReference=None, referencesToOtherLines=None, advanceData=None, productCodes=None, lineExpressionIndicator=None, lineNatureIndicator=None, lineDescription=None, quantity=None, unitOfMeasure=None, unitOfMeasureOwn=None, unitPrice=None, unitPriceHUF=None, lineDiscountData=None, lineAmountsNormal=None, lineAmountsSimplified=None, intermediatedService=None, aggregateInvoiceLineData=None, newTransportMean=None, depositIndicator=None, obligatedForProductFee=None, GPCExcise=None, dieselOilPurchase=None, netaDeclaration=None, productFeeClause=None, lineProductFeeContent=None, conventionalLineInfo=None, additionalLineData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNumber = lineNumber
        self.validate_LineNumberType(self.lineNumber)
        self.lineNumber_nsprefix_ = "base"
        self.lineModificationReference = lineModificationReference
        self.lineModificationReference_nsprefix_ = None
        self.referencesToOtherLines = referencesToOtherLines
        self.referencesToOtherLines_nsprefix_ = None
        self.advanceData = advanceData
        self.advanceData_nsprefix_ = None
        self.productCodes = productCodes
        self.productCodes_nsprefix_ = None
        self.lineExpressionIndicator = lineExpressionIndicator
        self.lineExpressionIndicator_nsprefix_ = "xs"
        self.lineNatureIndicator = lineNatureIndicator
        self.validate_LineNatureIndicatorType(self.lineNatureIndicator)
        self.lineNatureIndicator_nsprefix_ = None
        self.lineDescription = lineDescription
        self.validate_SimpleText512NotBlankType(self.lineDescription)
        self.lineDescription_nsprefix_ = "common"
        self.quantity = quantity
        self.validate_QuantityType(self.quantity)
        self.quantity_nsprefix_ = None
        self.unitOfMeasure = unitOfMeasure
        self.validate_UnitOfMeasureType(self.unitOfMeasure)
        self.unitOfMeasure_nsprefix_ = None
        self.unitOfMeasureOwn = unitOfMeasureOwn
        self.validate_SimpleText50NotBlankType(self.unitOfMeasureOwn)
        self.unitOfMeasureOwn_nsprefix_ = "common"
        self.unitPrice = unitPrice
        self.validate_QuantityType(self.unitPrice)
        self.unitPrice_nsprefix_ = None
        self.unitPriceHUF = unitPriceHUF
        self.validate_QuantityType(self.unitPriceHUF)
        self.unitPriceHUF_nsprefix_ = None
        self.lineDiscountData = lineDiscountData
        self.lineDiscountData_nsprefix_ = None
        self.lineAmountsNormal = lineAmountsNormal
        self.lineAmountsNormal_nsprefix_ = None
        self.lineAmountsSimplified = lineAmountsSimplified
        self.lineAmountsSimplified_nsprefix_ = None
        self.intermediatedService = intermediatedService
        self.intermediatedService_nsprefix_ = "xs"
        self.aggregateInvoiceLineData = aggregateInvoiceLineData
        self.aggregateInvoiceLineData_nsprefix_ = None
        self.newTransportMean = newTransportMean
        self.newTransportMean_nsprefix_ = None
        self.depositIndicator = depositIndicator
        self.depositIndicator_nsprefix_ = "xs"
        self.obligatedForProductFee = obligatedForProductFee
        self.obligatedForProductFee_nsprefix_ = "xs"
        self.GPCExcise = GPCExcise
        self.validate_MonetaryType(self.GPCExcise)
        self.GPCExcise_nsprefix_ = "base"
        self.dieselOilPurchase = dieselOilPurchase
        self.dieselOilPurchase_nsprefix_ = None
        self.netaDeclaration = netaDeclaration
        self.netaDeclaration_nsprefix_ = "xs"
        self.productFeeClause = productFeeClause
        self.productFeeClause_nsprefix_ = None
        if lineProductFeeContent is None:
            self.lineProductFeeContent = []
        else:
            self.lineProductFeeContent = lineProductFeeContent
        self.lineProductFeeContent_nsprefix_ = None
        self.conventionalLineInfo = conventionalLineInfo
        self.conventionalLineInfo_nsprefix_ = None
        if additionalLineData is None:
            self.additionalLineData = []
        else:
            self.additionalLineData = additionalLineData
        self.additionalLineData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineType.subclass:
            return LineType.subclass(*args_, **kwargs_)
        else:
            return LineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineNumber(self):
        return self.lineNumber
    def set_lineNumber(self, lineNumber):
        self.lineNumber = lineNumber
    def get_lineModificationReference(self):
        return self.lineModificationReference
    def set_lineModificationReference(self, lineModificationReference):
        self.lineModificationReference = lineModificationReference
    def get_referencesToOtherLines(self):
        return self.referencesToOtherLines
    def set_referencesToOtherLines(self, referencesToOtherLines):
        self.referencesToOtherLines = referencesToOtherLines
    def get_advanceData(self):
        return self.advanceData
    def set_advanceData(self, advanceData):
        self.advanceData = advanceData
    def get_productCodes(self):
        return self.productCodes
    def set_productCodes(self, productCodes):
        self.productCodes = productCodes
    def get_lineExpressionIndicator(self):
        return self.lineExpressionIndicator
    def set_lineExpressionIndicator(self, lineExpressionIndicator):
        self.lineExpressionIndicator = lineExpressionIndicator
    def get_lineNatureIndicator(self):
        return self.lineNatureIndicator
    def set_lineNatureIndicator(self, lineNatureIndicator):
        self.lineNatureIndicator = lineNatureIndicator
    def get_lineDescription(self):
        return self.lineDescription
    def set_lineDescription(self, lineDescription):
        self.lineDescription = lineDescription
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def get_unitOfMeasure(self):
        return self.unitOfMeasure
    def set_unitOfMeasure(self, unitOfMeasure):
        self.unitOfMeasure = unitOfMeasure
    def get_unitOfMeasureOwn(self):
        return self.unitOfMeasureOwn
    def set_unitOfMeasureOwn(self, unitOfMeasureOwn):
        self.unitOfMeasureOwn = unitOfMeasureOwn
    def get_unitPrice(self):
        return self.unitPrice
    def set_unitPrice(self, unitPrice):
        self.unitPrice = unitPrice
    def get_unitPriceHUF(self):
        return self.unitPriceHUF
    def set_unitPriceHUF(self, unitPriceHUF):
        self.unitPriceHUF = unitPriceHUF
    def get_lineDiscountData(self):
        return self.lineDiscountData
    def set_lineDiscountData(self, lineDiscountData):
        self.lineDiscountData = lineDiscountData
    def get_lineAmountsNormal(self):
        return self.lineAmountsNormal
    def set_lineAmountsNormal(self, lineAmountsNormal):
        self.lineAmountsNormal = lineAmountsNormal
    def get_lineAmountsSimplified(self):
        return self.lineAmountsSimplified
    def set_lineAmountsSimplified(self, lineAmountsSimplified):
        self.lineAmountsSimplified = lineAmountsSimplified
    def get_intermediatedService(self):
        return self.intermediatedService
    def set_intermediatedService(self, intermediatedService):
        self.intermediatedService = intermediatedService
    def get_aggregateInvoiceLineData(self):
        return self.aggregateInvoiceLineData
    def set_aggregateInvoiceLineData(self, aggregateInvoiceLineData):
        self.aggregateInvoiceLineData = aggregateInvoiceLineData
    def get_newTransportMean(self):
        return self.newTransportMean
    def set_newTransportMean(self, newTransportMean):
        self.newTransportMean = newTransportMean
    def get_depositIndicator(self):
        return self.depositIndicator
    def set_depositIndicator(self, depositIndicator):
        self.depositIndicator = depositIndicator
    def get_obligatedForProductFee(self):
        return self.obligatedForProductFee
    def set_obligatedForProductFee(self, obligatedForProductFee):
        self.obligatedForProductFee = obligatedForProductFee
    def get_GPCExcise(self):
        return self.GPCExcise
    def set_GPCExcise(self, GPCExcise):
        self.GPCExcise = GPCExcise
    def get_dieselOilPurchase(self):
        return self.dieselOilPurchase
    def set_dieselOilPurchase(self, dieselOilPurchase):
        self.dieselOilPurchase = dieselOilPurchase
    def get_netaDeclaration(self):
        return self.netaDeclaration
    def set_netaDeclaration(self, netaDeclaration):
        self.netaDeclaration = netaDeclaration
    def get_productFeeClause(self):
        return self.productFeeClause
    def set_productFeeClause(self, productFeeClause):
        self.productFeeClause = productFeeClause
    def get_lineProductFeeContent(self):
        return self.lineProductFeeContent
    def set_lineProductFeeContent(self, lineProductFeeContent):
        self.lineProductFeeContent = lineProductFeeContent
    def add_lineProductFeeContent(self, value):
        self.lineProductFeeContent.append(value)
    def insert_lineProductFeeContent_at(self, index, value):
        self.lineProductFeeContent.insert(index, value)
    def replace_lineProductFeeContent_at(self, index, value):
        self.lineProductFeeContent[index] = value
    def get_conventionalLineInfo(self):
        return self.conventionalLineInfo
    def set_conventionalLineInfo(self, conventionalLineInfo):
        self.conventionalLineInfo = conventionalLineInfo
    def get_additionalLineData(self):
        return self.additionalLineData
    def set_additionalLineData(self, additionalLineData):
        self.additionalLineData = additionalLineData
    def add_additionalLineData(self, value):
        self.additionalLineData.append(value)
    def insert_additionalLineData_at(self, index, value):
        self.additionalLineData.insert(index, value)
    def replace_additionalLineData_at(self, index, value):
        self.additionalLineData[index] = value
    def validate_LineNumberType(self, value):
        result = True
        # Validate type LineNumberType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_LineNatureIndicatorType(self, value):
        result = True
        # Validate type LineNatureIndicatorType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['PRODUCT', 'SERVICE', 'OTHER']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LineNatureIndicatorType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LineNatureIndicatorType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LineNatureIndicatorType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_UnitOfMeasureType(self, value):
        result = True
        # Validate type UnitOfMeasureType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['PIECE', 'KILOGRAM', 'TON', 'KWH', 'DAY', 'HOUR', 'MINUTE', 'MONTH', 'LITER', 'KILOMETER', 'CUBIC_METER', 'METER', 'LINEAR_METER', 'CARTON', 'PACK', 'OWN']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on UnitOfMeasureType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on UnitOfMeasureType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on UnitOfMeasureType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineNumber is not None or
            self.lineModificationReference is not None or
            self.referencesToOtherLines is not None or
            self.advanceData is not None or
            self.productCodes is not None or
            self.lineExpressionIndicator is not None or
            self.lineNatureIndicator is not None or
            self.lineDescription is not None or
            self.quantity is not None or
            self.unitOfMeasure is not None or
            self.unitOfMeasureOwn is not None or
            self.unitPrice is not None or
            self.unitPriceHUF is not None or
            self.lineDiscountData is not None or
            self.lineAmountsNormal is not None or
            self.lineAmountsSimplified is not None or
            self.intermediatedService is not None or
            self.aggregateInvoiceLineData is not None or
            self.newTransportMean is not None or
            self.depositIndicator is not None or
            self.obligatedForProductFee is not None or
            self.GPCExcise is not None or
            self.dieselOilPurchase is not None or
            self.netaDeclaration is not None or
            self.productFeeClause is not None or
            self.lineProductFeeContent or
            self.conventionalLineInfo is not None or
            self.additionalLineData
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='LineType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='LineType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNumber is not None:
            namespaceprefix_ = self.lineNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNumber>%s</%slineNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.lineNumber, input_name='lineNumber'), namespaceprefix_ , eol_))
        if self.lineModificationReference is not None:
            namespaceprefix_ = self.lineModificationReference_nsprefix_ + ':' if (UseCapturedNS_ and self.lineModificationReference_nsprefix_) else ''
            self.lineModificationReference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineModificationReference', pretty_print=pretty_print)
        if self.referencesToOtherLines is not None:
            namespaceprefix_ = self.referencesToOtherLines_nsprefix_ + ':' if (UseCapturedNS_ and self.referencesToOtherLines_nsprefix_) else ''
            self.referencesToOtherLines.export(outfile, level, namespaceprefix_, namespacedef_='', name_='referencesToOtherLines', pretty_print=pretty_print)
        if self.advanceData is not None:
            namespaceprefix_ = self.advanceData_nsprefix_ + ':' if (UseCapturedNS_ and self.advanceData_nsprefix_) else ''
            self.advanceData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='advanceData', pretty_print=pretty_print)
        if self.productCodes is not None:
            namespaceprefix_ = self.productCodes_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodes_nsprefix_) else ''
            self.productCodes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productCodes', pretty_print=pretty_print)
        if self.lineExpressionIndicator is not None:
            namespaceprefix_ = self.lineExpressionIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.lineExpressionIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineExpressionIndicator>%s</%slineExpressionIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.lineExpressionIndicator, input_name='lineExpressionIndicator'), namespaceprefix_ , eol_))
        if self.lineNatureIndicator is not None:
            namespaceprefix_ = self.lineNatureIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNatureIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNatureIndicator>%s</%slineNatureIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lineNatureIndicator), input_name='lineNatureIndicator')), namespaceprefix_ , eol_))
        if self.lineDescription is not None:
            namespaceprefix_ = self.lineDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.lineDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineDescription>%s</%slineDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lineDescription), input_name='lineDescription')), namespaceprefix_ , eol_))
        if self.quantity is not None:
            namespaceprefix_ = self.quantity_nsprefix_ + ':' if (UseCapturedNS_ and self.quantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squantity>%s</%squantity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.quantity, input_name='quantity'), namespaceprefix_ , eol_))
        if self.unitOfMeasure is not None:
            namespaceprefix_ = self.unitOfMeasure_nsprefix_ + ':' if (UseCapturedNS_ and self.unitOfMeasure_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitOfMeasure>%s</%sunitOfMeasure>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unitOfMeasure), input_name='unitOfMeasure')), namespaceprefix_ , eol_))
        if self.unitOfMeasureOwn is not None:
            namespaceprefix_ = self.unitOfMeasureOwn_nsprefix_ + ':' if (UseCapturedNS_ and self.unitOfMeasureOwn_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitOfMeasureOwn>%s</%sunitOfMeasureOwn>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unitOfMeasureOwn), input_name='unitOfMeasureOwn')), namespaceprefix_ , eol_))
        if self.unitPrice is not None:
            namespaceprefix_ = self.unitPrice_nsprefix_ + ':' if (UseCapturedNS_ and self.unitPrice_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitPrice>%s</%sunitPrice>%s' % (namespaceprefix_ , self.gds_format_decimal(self.unitPrice, input_name='unitPrice'), namespaceprefix_ , eol_))
        if self.unitPriceHUF is not None:
            namespaceprefix_ = self.unitPriceHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.unitPriceHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitPriceHUF>%s</%sunitPriceHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.unitPriceHUF, input_name='unitPriceHUF'), namespaceprefix_ , eol_))
        if self.lineDiscountData is not None:
            namespaceprefix_ = self.lineDiscountData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineDiscountData_nsprefix_) else ''
            self.lineDiscountData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineDiscountData', pretty_print=pretty_print)
        if self.lineAmountsNormal is not None:
            namespaceprefix_ = self.lineAmountsNormal_nsprefix_ + ':' if (UseCapturedNS_ and self.lineAmountsNormal_nsprefix_) else ''
            self.lineAmountsNormal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineAmountsNormal', pretty_print=pretty_print)
        if self.lineAmountsSimplified is not None:
            namespaceprefix_ = self.lineAmountsSimplified_nsprefix_ + ':' if (UseCapturedNS_ and self.lineAmountsSimplified_nsprefix_) else ''
            self.lineAmountsSimplified.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineAmountsSimplified', pretty_print=pretty_print)
        if self.intermediatedService is not None:
            namespaceprefix_ = self.intermediatedService_nsprefix_ + ':' if (UseCapturedNS_ and self.intermediatedService_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sintermediatedService>%s</%sintermediatedService>%s' % (namespaceprefix_ , self.gds_format_boolean(self.intermediatedService, input_name='intermediatedService'), namespaceprefix_ , eol_))
        if self.aggregateInvoiceLineData is not None:
            namespaceprefix_ = self.aggregateInvoiceLineData_nsprefix_ + ':' if (UseCapturedNS_ and self.aggregateInvoiceLineData_nsprefix_) else ''
            self.aggregateInvoiceLineData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='aggregateInvoiceLineData', pretty_print=pretty_print)
        if self.newTransportMean is not None:
            namespaceprefix_ = self.newTransportMean_nsprefix_ + ':' if (UseCapturedNS_ and self.newTransportMean_nsprefix_) else ''
            self.newTransportMean.export(outfile, level, namespaceprefix_, namespacedef_='', name_='newTransportMean', pretty_print=pretty_print)
        if self.depositIndicator is not None:
            namespaceprefix_ = self.depositIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.depositIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdepositIndicator>%s</%sdepositIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.depositIndicator, input_name='depositIndicator'), namespaceprefix_ , eol_))
        if self.obligatedForProductFee is not None:
            namespaceprefix_ = self.obligatedForProductFee_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedForProductFee_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sobligatedForProductFee>%s</%sobligatedForProductFee>%s' % (namespaceprefix_ , self.gds_format_boolean(self.obligatedForProductFee, input_name='obligatedForProductFee'), namespaceprefix_ , eol_))
        if self.GPCExcise is not None:
            namespaceprefix_ = self.GPCExcise_nsprefix_ + ':' if (UseCapturedNS_ and self.GPCExcise_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sGPCExcise>%s</%sGPCExcise>%s' % (namespaceprefix_ , self.gds_format_decimal(self.GPCExcise, input_name='GPCExcise'), namespaceprefix_ , eol_))
        if self.dieselOilPurchase is not None:
            namespaceprefix_ = self.dieselOilPurchase_nsprefix_ + ':' if (UseCapturedNS_ and self.dieselOilPurchase_nsprefix_) else ''
            self.dieselOilPurchase.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dieselOilPurchase', pretty_print=pretty_print)
        if self.netaDeclaration is not None:
            namespaceprefix_ = self.netaDeclaration_nsprefix_ + ':' if (UseCapturedNS_ and self.netaDeclaration_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snetaDeclaration>%s</%snetaDeclaration>%s' % (namespaceprefix_ , self.gds_format_boolean(self.netaDeclaration, input_name='netaDeclaration'), namespaceprefix_ , eol_))
        if self.productFeeClause is not None:
            namespaceprefix_ = self.productFeeClause_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeClause_nsprefix_) else ''
            self.productFeeClause.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeClause', pretty_print=pretty_print)
        for lineProductFeeContent_ in self.lineProductFeeContent:
            namespaceprefix_ = self.lineProductFeeContent_nsprefix_ + ':' if (UseCapturedNS_ and self.lineProductFeeContent_nsprefix_) else ''
            lineProductFeeContent_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineProductFeeContent', pretty_print=pretty_print)
        if self.conventionalLineInfo is not None:
            namespaceprefix_ = self.conventionalLineInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.conventionalLineInfo_nsprefix_) else ''
            self.conventionalLineInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='conventionalLineInfo', pretty_print=pretty_print)
        for additionalLineData_ in self.additionalLineData:
            namespaceprefix_ = self.additionalLineData_nsprefix_ + ':' if (UseCapturedNS_ and self.additionalLineData_nsprefix_) else ''
            additionalLineData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='additionalLineData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LineType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineNumber is not None:
            lineNumber_ = self.lineNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNumber').text = self.gds_format_integer(lineNumber_)
        if self.lineModificationReference is not None:
            lineModificationReference_ = self.lineModificationReference
            lineModificationReference_.to_etree(element, name_='lineModificationReference', mapping_=mapping_, nsmap_=nsmap_)
        if self.referencesToOtherLines is not None:
            referencesToOtherLines_ = self.referencesToOtherLines
            referencesToOtherLines_.to_etree(element, name_='referencesToOtherLines', mapping_=mapping_, nsmap_=nsmap_)
        if self.advanceData is not None:
            advanceData_ = self.advanceData
            advanceData_.to_etree(element, name_='advanceData', mapping_=mapping_, nsmap_=nsmap_)
        if self.productCodes is not None:
            productCodes_ = self.productCodes
            productCodes_.to_etree(element, name_='productCodes', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineExpressionIndicator is not None:
            lineExpressionIndicator_ = self.lineExpressionIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineExpressionIndicator').text = self.gds_format_boolean(lineExpressionIndicator_)
        if self.lineNatureIndicator is not None:
            lineNatureIndicator_ = self.lineNatureIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNatureIndicator').text = self.gds_format_string(lineNatureIndicator_)
        if self.lineDescription is not None:
            lineDescription_ = self.lineDescription
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineDescription').text = self.gds_format_string(lineDescription_)
        if self.quantity is not None:
            quantity_ = self.quantity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}quantity').text = self.gds_format_decimal(quantity_)
        if self.unitOfMeasure is not None:
            unitOfMeasure_ = self.unitOfMeasure
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitOfMeasure').text = self.gds_format_string(unitOfMeasure_)
        if self.unitOfMeasureOwn is not None:
            unitOfMeasureOwn_ = self.unitOfMeasureOwn
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitOfMeasureOwn').text = self.gds_format_string(unitOfMeasureOwn_)
        if self.unitPrice is not None:
            unitPrice_ = self.unitPrice
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitPrice').text = self.gds_format_decimal(unitPrice_)
        if self.unitPriceHUF is not None:
            unitPriceHUF_ = self.unitPriceHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitPriceHUF').text = self.gds_format_decimal(unitPriceHUF_)
        if self.lineDiscountData is not None:
            lineDiscountData_ = self.lineDiscountData
            lineDiscountData_.to_etree(element, name_='lineDiscountData', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineAmountsNormal is not None:
            lineAmountsNormal_ = self.lineAmountsNormal
            lineAmountsNormal_.to_etree(element, name_='lineAmountsNormal', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineAmountsSimplified is not None:
            lineAmountsSimplified_ = self.lineAmountsSimplified
            lineAmountsSimplified_.to_etree(element, name_='lineAmountsSimplified', mapping_=mapping_, nsmap_=nsmap_)
        if self.intermediatedService is not None:
            intermediatedService_ = self.intermediatedService
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}intermediatedService').text = self.gds_format_boolean(intermediatedService_)
        if self.aggregateInvoiceLineData is not None:
            aggregateInvoiceLineData_ = self.aggregateInvoiceLineData
            aggregateInvoiceLineData_.to_etree(element, name_='aggregateInvoiceLineData', mapping_=mapping_, nsmap_=nsmap_)
        if self.newTransportMean is not None:
            newTransportMean_ = self.newTransportMean
            newTransportMean_.to_etree(element, name_='newTransportMean', mapping_=mapping_, nsmap_=nsmap_)
        if self.depositIndicator is not None:
            depositIndicator_ = self.depositIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}depositIndicator').text = self.gds_format_boolean(depositIndicator_)
        if self.obligatedForProductFee is not None:
            obligatedForProductFee_ = self.obligatedForProductFee
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}obligatedForProductFee').text = self.gds_format_boolean(obligatedForProductFee_)
        if self.GPCExcise is not None:
            GPCExcise_ = self.GPCExcise
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}GPCExcise').text = self.gds_format_decimal(GPCExcise_)
        if self.dieselOilPurchase is not None:
            dieselOilPurchase_ = self.dieselOilPurchase
            dieselOilPurchase_.to_etree(element, name_='dieselOilPurchase', mapping_=mapping_, nsmap_=nsmap_)
        if self.netaDeclaration is not None:
            netaDeclaration_ = self.netaDeclaration
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}netaDeclaration').text = self.gds_format_boolean(netaDeclaration_)
        if self.productFeeClause is not None:
            productFeeClause_ = self.productFeeClause
            productFeeClause_.to_etree(element, name_='productFeeClause', mapping_=mapping_, nsmap_=nsmap_)
        for lineProductFeeContent_ in self.lineProductFeeContent:
            lineProductFeeContent_.to_etree(element, name_='lineProductFeeContent', mapping_=mapping_, nsmap_=nsmap_)
        if self.conventionalLineInfo is not None:
            conventionalLineInfo_ = self.conventionalLineInfo
            conventionalLineInfo_.to_etree(element, name_='conventionalLineInfo', mapping_=mapping_, nsmap_=nsmap_)
        for additionalLineData_ in self.additionalLineData:
            additionalLineData_.to_etree(element, name_='additionalLineData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNumber is not None:
            showIndent(outfile, level)
            outfile.write('lineNumber=%d,\n' % self.lineNumber)
        if self.lineModificationReference is not None:
            showIndent(outfile, level)
            outfile.write('lineModificationReference=model_.LineModificationReferenceType(\n')
            self.lineModificationReference.exportLiteral(outfile, level, name_='lineModificationReference')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.referencesToOtherLines is not None:
            showIndent(outfile, level)
            outfile.write('referencesToOtherLines=model_.ReferencesToOtherLinesType(\n')
            self.referencesToOtherLines.exportLiteral(outfile, level, name_='referencesToOtherLines')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.advanceData is not None:
            showIndent(outfile, level)
            outfile.write('advanceData=model_.AdvanceDataType(\n')
            self.advanceData.exportLiteral(outfile, level, name_='advanceData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.productCodes is not None:
            showIndent(outfile, level)
            outfile.write('productCodes=model_.ProductCodesType(\n')
            self.productCodes.exportLiteral(outfile, level, name_='productCodes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineExpressionIndicator is not None:
            showIndent(outfile, level)
            outfile.write('lineExpressionIndicator=%s,\n' % self.lineExpressionIndicator)
        if self.lineNatureIndicator is not None:
            showIndent(outfile, level)
            outfile.write('lineNatureIndicator=%s,\n' % self.gds_encode(quote_python(self.lineNatureIndicator)))
        if self.lineDescription is not None:
            showIndent(outfile, level)
            outfile.write('lineDescription=%s,\n' % self.gds_encode(quote_python(self.lineDescription)))
        if self.quantity is not None:
            showIndent(outfile, level)
            outfile.write('quantity=%f,\n' % self.quantity)
        if self.unitOfMeasure is not None:
            showIndent(outfile, level)
            outfile.write('unitOfMeasure=%s,\n' % self.gds_encode(quote_python(self.unitOfMeasure)))
        if self.unitOfMeasureOwn is not None:
            showIndent(outfile, level)
            outfile.write('unitOfMeasureOwn=%s,\n' % self.gds_encode(quote_python(self.unitOfMeasureOwn)))
        if self.unitPrice is not None:
            showIndent(outfile, level)
            outfile.write('unitPrice=%f,\n' % self.unitPrice)
        if self.unitPriceHUF is not None:
            showIndent(outfile, level)
            outfile.write('unitPriceHUF=%f,\n' % self.unitPriceHUF)
        if self.lineDiscountData is not None:
            showIndent(outfile, level)
            outfile.write('lineDiscountData=model_.DiscountDataType(\n')
            self.lineDiscountData.exportLiteral(outfile, level, name_='lineDiscountData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineAmountsNormal is not None:
            showIndent(outfile, level)
            outfile.write('lineAmountsNormal=model_.LineAmountsNormalType(\n')
            self.lineAmountsNormal.exportLiteral(outfile, level, name_='lineAmountsNormal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineAmountsSimplified is not None:
            showIndent(outfile, level)
            outfile.write('lineAmountsSimplified=model_.LineAmountsSimplifiedType(\n')
            self.lineAmountsSimplified.exportLiteral(outfile, level, name_='lineAmountsSimplified')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.intermediatedService is not None:
            showIndent(outfile, level)
            outfile.write('intermediatedService=%s,\n' % self.intermediatedService)
        if self.aggregateInvoiceLineData is not None:
            showIndent(outfile, level)
            outfile.write('aggregateInvoiceLineData=model_.AggregateInvoiceLineDataType(\n')
            self.aggregateInvoiceLineData.exportLiteral(outfile, level, name_='aggregateInvoiceLineData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.newTransportMean is not None:
            showIndent(outfile, level)
            outfile.write('newTransportMean=model_.NewTransportMeanType(\n')
            self.newTransportMean.exportLiteral(outfile, level, name_='newTransportMean')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.depositIndicator is not None:
            showIndent(outfile, level)
            outfile.write('depositIndicator=%s,\n' % self.depositIndicator)
        if self.obligatedForProductFee is not None:
            showIndent(outfile, level)
            outfile.write('obligatedForProductFee=%s,\n' % self.obligatedForProductFee)
        if self.GPCExcise is not None:
            showIndent(outfile, level)
            outfile.write('GPCExcise=%f,\n' % self.GPCExcise)
        if self.dieselOilPurchase is not None:
            showIndent(outfile, level)
            outfile.write('dieselOilPurchase=model_.DieselOilPurchaseType(\n')
            self.dieselOilPurchase.exportLiteral(outfile, level, name_='dieselOilPurchase')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.netaDeclaration is not None:
            showIndent(outfile, level)
            outfile.write('netaDeclaration=%s,\n' % self.netaDeclaration)
        if self.productFeeClause is not None:
            showIndent(outfile, level)
            outfile.write('productFeeClause=model_.ProductFeeClauseType(\n')
            self.productFeeClause.exportLiteral(outfile, level, name_='productFeeClause')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('lineProductFeeContent=[\n')
        level += 1
        for lineProductFeeContent_ in self.lineProductFeeContent:
            showIndent(outfile, level)
            outfile.write('model_.ProductFeeDataType(\n')
            lineProductFeeContent_.exportLiteral(outfile, level, name_='ProductFeeDataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.conventionalLineInfo is not None:
            showIndent(outfile, level)
            outfile.write('conventionalLineInfo=model_.ConventionalInvoiceInfoType(\n')
            self.conventionalLineInfo.exportLiteral(outfile, level, name_='conventionalLineInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('additionalLineData=[\n')
        level += 1
        for additionalLineData_ in self.additionalLineData:
            showIndent(outfile, level)
            outfile.write('model_.AdditionalDataType(\n')
            additionalLineData_.exportLiteral(outfile, level, name_='AdditionalDataType')
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
        if nodeName_ == 'lineNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'lineNumber')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'lineNumber')
            self.lineNumber = ival_
            self.lineNumber_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.lineNumber)
        elif nodeName_ == 'lineModificationReference':
            obj_ = LineModificationReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineModificationReference = obj_
            obj_.original_tagname_ = 'lineModificationReference'
        elif nodeName_ == 'referencesToOtherLines':
            obj_ = ReferencesToOtherLinesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.referencesToOtherLines = obj_
            obj_.original_tagname_ = 'referencesToOtherLines'
        elif nodeName_ == 'advanceData':
            obj_ = AdvanceDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.advanceData = obj_
            obj_.original_tagname_ = 'advanceData'
        elif nodeName_ == 'productCodes':
            obj_ = ProductCodesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productCodes = obj_
            obj_.original_tagname_ = 'productCodes'
        elif nodeName_ == 'lineExpressionIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'lineExpressionIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'lineExpressionIndicator')
            self.lineExpressionIndicator = ival_
            self.lineExpressionIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'lineNatureIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lineNatureIndicator')
            value_ = self.gds_validate_string(value_, node, 'lineNatureIndicator')
            self.lineNatureIndicator = value_
            self.lineNatureIndicator_nsprefix_ = child_.prefix
            # validate type LineNatureIndicatorType
            self.validate_LineNatureIndicatorType(self.lineNatureIndicator)
        elif nodeName_ == 'lineDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lineDescription')
            value_ = self.gds_validate_string(value_, node, 'lineDescription')
            self.lineDescription = value_
            self.lineDescription_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.lineDescription)
        elif nodeName_ == 'quantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'quantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'quantity')
            self.quantity = fval_
            self.quantity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.quantity)
        elif nodeName_ == 'unitOfMeasure':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unitOfMeasure')
            value_ = self.gds_validate_string(value_, node, 'unitOfMeasure')
            self.unitOfMeasure = value_
            self.unitOfMeasure_nsprefix_ = child_.prefix
            # validate type UnitOfMeasureType
            self.validate_UnitOfMeasureType(self.unitOfMeasure)
        elif nodeName_ == 'unitOfMeasureOwn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unitOfMeasureOwn')
            value_ = self.gds_validate_string(value_, node, 'unitOfMeasureOwn')
            self.unitOfMeasureOwn = value_
            self.unitOfMeasureOwn_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.unitOfMeasureOwn)
        elif nodeName_ == 'unitPrice' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'unitPrice')
            fval_ = self.gds_validate_decimal(fval_, node, 'unitPrice')
            self.unitPrice = fval_
            self.unitPrice_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.unitPrice)
        elif nodeName_ == 'unitPriceHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'unitPriceHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'unitPriceHUF')
            self.unitPriceHUF = fval_
            self.unitPriceHUF_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.unitPriceHUF)
        elif nodeName_ == 'lineDiscountData':
            obj_ = DiscountDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineDiscountData = obj_
            obj_.original_tagname_ = 'lineDiscountData'
        elif nodeName_ == 'lineAmountsNormal':
            obj_ = LineAmountsNormalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineAmountsNormal = obj_
            obj_.original_tagname_ = 'lineAmountsNormal'
        elif nodeName_ == 'lineAmountsSimplified':
            obj_ = LineAmountsSimplifiedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineAmountsSimplified = obj_
            obj_.original_tagname_ = 'lineAmountsSimplified'
        elif nodeName_ == 'intermediatedService':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'intermediatedService')
            ival_ = self.gds_validate_boolean(ival_, node, 'intermediatedService')
            self.intermediatedService = ival_
            self.intermediatedService_nsprefix_ = child_.prefix
        elif nodeName_ == 'aggregateInvoiceLineData':
            obj_ = AggregateInvoiceLineDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.aggregateInvoiceLineData = obj_
            obj_.original_tagname_ = 'aggregateInvoiceLineData'
        elif nodeName_ == 'newTransportMean':
            obj_ = NewTransportMeanType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.newTransportMean = obj_
            obj_.original_tagname_ = 'newTransportMean'
        elif nodeName_ == 'depositIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'depositIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'depositIndicator')
            self.depositIndicator = ival_
            self.depositIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'obligatedForProductFee':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'obligatedForProductFee')
            ival_ = self.gds_validate_boolean(ival_, node, 'obligatedForProductFee')
            self.obligatedForProductFee = ival_
            self.obligatedForProductFee_nsprefix_ = child_.prefix
        elif nodeName_ == 'GPCExcise' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'GPCExcise')
            fval_ = self.gds_validate_decimal(fval_, node, 'GPCExcise')
            self.GPCExcise = fval_
            self.GPCExcise_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.GPCExcise)
        elif nodeName_ == 'dieselOilPurchase':
            obj_ = DieselOilPurchaseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dieselOilPurchase = obj_
            obj_.original_tagname_ = 'dieselOilPurchase'
        elif nodeName_ == 'netaDeclaration':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'netaDeclaration')
            ival_ = self.gds_validate_boolean(ival_, node, 'netaDeclaration')
            self.netaDeclaration = ival_
            self.netaDeclaration_nsprefix_ = child_.prefix
        elif nodeName_ == 'productFeeClause':
            obj_ = ProductFeeClauseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeClause = obj_
            obj_.original_tagname_ = 'productFeeClause'
        elif nodeName_ == 'lineProductFeeContent':
            obj_ = ProductFeeDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineProductFeeContent.append(obj_)
            obj_.original_tagname_ = 'lineProductFeeContent'
        elif nodeName_ == 'conventionalLineInfo':
            obj_ = ConventionalInvoiceInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.conventionalLineInfo = obj_
            obj_.original_tagname_ = 'conventionalLineInfo'
        elif nodeName_ == 'additionalLineData':
            obj_ = AdditionalDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.additionalLineData.append(obj_)
            obj_.original_tagname_ = 'additionalLineData'
