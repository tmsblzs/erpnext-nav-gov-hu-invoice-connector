# generated/binding_2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4e5201a444a9834f7df8b550954bad6593de0403
# Generated 2022-06-05 12:05:14.793150 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://schemas.nav.gov.hu/OSA/3.0/data

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:fe4efb8c-e4b6-11ec-8491-000c29e8b4fc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import common as _ImportedBinding_common
import base as _ImportedBinding_base

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.nav.gov.hu/OSA/3.0/data', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_base = _ImportedBinding_base.Namespace
_Namespace_base.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}ExchangeRateType
class ExchangeRateType (pyxb.binding.datatypes.decimal):

    """Árfolyam adat típusExchange rate data type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExchangeRateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 57, 1)
    _Documentation = 'Árfolyam adat típusExchange rate data type'
ExchangeRateType._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.decimal, value=pyxb.binding.datatypes.anySimpleType('0'))
ExchangeRateType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14))
ExchangeRateType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(6))
ExchangeRateType._InitializeFacetMap(ExchangeRateType._CF_minExclusive,
   ExchangeRateType._CF_totalDigits,
   ExchangeRateType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'ExchangeRateType', ExchangeRateType)
_module_typeBindings.ExchangeRateType = ExchangeRateType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}CustomerVatStatusType
class CustomerVatStatusType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Vevő ÁFA szerinti státusz típusaCustomers status type by VAT"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerVatStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 11, 1)
    _Documentation = 'Vevő ÁFA szerinti státusz típusaCustomers status type by VAT'
CustomerVatStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CustomerVatStatusType, enum_prefix=None)
CustomerVatStatusType.DOMESTIC = CustomerVatStatusType._CF_enumeration.addEnumeration(unicode_value='DOMESTIC', tag='DOMESTIC')
CustomerVatStatusType.OTHER = CustomerVatStatusType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
CustomerVatStatusType.PRIVATE_PERSON = CustomerVatStatusType._CF_enumeration.addEnumeration(unicode_value='PRIVATE_PERSON', tag='PRIVATE_PERSON')
CustomerVatStatusType._InitializeFacetMap(CustomerVatStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CustomerVatStatusType', CustomerVatStatusType)
_module_typeBindings.CustomerVatStatusType = CustomerVatStatusType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}DataNameType
class DataNameType (_ImportedBinding_common.AtomicStringType255):

    """Az adatmező egyedi azonosító típusaUnique identification type of the data field"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 37, 1)
    _Documentation = 'Az adatmező egyedi azonosító típusaUnique identification type of the data field'
DataNameType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
DataNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
DataNameType._CF_pattern = pyxb.binding.facets.CF_pattern()
DataNameType._CF_pattern.addPattern(pattern='[A-Z][0-9]{5}[_][_A-Z0-9]{1,249}')
DataNameType._InitializeFacetMap(DataNameType._CF_minLength,
   DataNameType._CF_maxLength,
   DataNameType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DataNameType', DataNameType)
_module_typeBindings.DataNameType = DataNameType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}EkaerIdType
class EkaerIdType (_ImportedBinding_common.AtomicStringType15):

    """EKÁER szám azonosító típusEKÁER number identifier type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EkaerIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 48, 1)
    _Documentation = 'EKÁER szám azonosító típusEKÁER number identifier type'
EkaerIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
EkaerIdType._CF_pattern.addPattern(pattern='[E]{1}[0-9]{6}[0-9A-F]{8}')
EkaerIdType._InitializeFacetMap(EkaerIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'EkaerIdType', EkaerIdType)
_module_typeBindings.EkaerIdType = EkaerIdType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}LineNatureIndicatorType
class LineNatureIndicatorType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Adott tételsor termékértékesítés vagy szolgáltatás nyújtás jellegének jelzéseIndication of the nature of the supply of goods or services on a given line"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineNatureIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 68, 1)
    _Documentation = 'Adott tételsor termékértékesítés vagy szolgáltatás nyújtás jellegének jelzéseIndication of the nature of the supply of goods or services on a given line'
LineNatureIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LineNatureIndicatorType, enum_prefix=None)
LineNatureIndicatorType.PRODUCT = LineNatureIndicatorType._CF_enumeration.addEnumeration(unicode_value='PRODUCT', tag='PRODUCT')
LineNatureIndicatorType.SERVICE = LineNatureIndicatorType._CF_enumeration.addEnumeration(unicode_value='SERVICE', tag='SERVICE')
LineNatureIndicatorType.OTHER = LineNatureIndicatorType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
LineNatureIndicatorType._InitializeFacetMap(LineNatureIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LineNatureIndicatorType', LineNatureIndicatorType)
_module_typeBindings.LineNatureIndicatorType = LineNatureIndicatorType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}LineOperationType
class LineOperationType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """A számlatétel módosítás típusaInvoice line modification type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineOperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 94, 1)
    _Documentation = 'A számlatétel módosítás típusaInvoice line modification type'
LineOperationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LineOperationType, enum_prefix=None)
LineOperationType.CREATE = LineOperationType._CF_enumeration.addEnumeration(unicode_value='CREATE', tag='CREATE')
LineOperationType.MODIFY = LineOperationType._CF_enumeration.addEnumeration(unicode_value='MODIFY', tag='MODIFY')
LineOperationType._InitializeFacetMap(LineOperationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LineOperationType', LineOperationType)
_module_typeBindings.LineOperationType = LineOperationType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}MarginSchemeType
class MarginSchemeType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Különbözet szerinti szabályozás típusField type for inputting margin-scheme taxation"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MarginSchemeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 104, 1)
    _Documentation = 'Különbözet szerinti szabályozás típusField type for inputting margin-scheme taxation'
MarginSchemeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MarginSchemeType, enum_prefix=None)
MarginSchemeType.TRAVEL_AGENCY = MarginSchemeType._CF_enumeration.addEnumeration(unicode_value='TRAVEL_AGENCY', tag='TRAVEL_AGENCY')
MarginSchemeType.SECOND_HAND = MarginSchemeType._CF_enumeration.addEnumeration(unicode_value='SECOND_HAND', tag='SECOND_HAND')
MarginSchemeType.ARTWORK = MarginSchemeType._CF_enumeration.addEnumeration(unicode_value='ARTWORK', tag='ARTWORK')
MarginSchemeType.ANTIQUES = MarginSchemeType._CF_enumeration.addEnumeration(unicode_value='ANTIQUES', tag='ANTIQUES')
MarginSchemeType._InitializeFacetMap(MarginSchemeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MarginSchemeType', MarginSchemeType)
_module_typeBindings.MarginSchemeType = MarginSchemeType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}ProductCodeCategoryType
class ProductCodeCategoryType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """A termékkód fajtájának jelölésére szolgáló típusThe type used to mark the kind of product code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductCodeCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 136, 1)
    _Documentation = 'A termékkód fajtájának jelölésére szolgáló típusThe type used to mark the kind of product code'
ProductCodeCategoryType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
ProductCodeCategoryType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6))
ProductCodeCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProductCodeCategoryType, enum_prefix=None)
ProductCodeCategoryType.VTSZ = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='VTSZ', tag='VTSZ')
ProductCodeCategoryType.SZJ = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='SZJ', tag='SZJ')
ProductCodeCategoryType.KN = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
ProductCodeCategoryType.AHK = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='AHK', tag='AHK')
ProductCodeCategoryType.CSK = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='CSK', tag='CSK')
ProductCodeCategoryType.KT = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='KT', tag='KT')
ProductCodeCategoryType.EJ = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='EJ', tag='EJ')
ProductCodeCategoryType.TESZOR = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='TESZOR', tag='TESZOR')
ProductCodeCategoryType.OWN = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='OWN', tag='OWN')
ProductCodeCategoryType.OTHER = ProductCodeCategoryType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
ProductCodeCategoryType._InitializeFacetMap(ProductCodeCategoryType._CF_minLength,
   ProductCodeCategoryType._CF_maxLength,
   ProductCodeCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProductCodeCategoryType', ProductCodeCategoryType)
_module_typeBindings.ProductCodeCategoryType = ProductCodeCategoryType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}ProductCodeValueType
class ProductCodeValueType (_ImportedBinding_common.AtomicStringType32):

    """Termékkód típusField type for inputting product codes"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductCodeValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 206, 1)
    _Documentation = 'Termékkód típusField type for inputting product codes'
ProductCodeValueType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
ProductCodeValueType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
ProductCodeValueType._CF_pattern = pyxb.binding.facets.CF_pattern()
ProductCodeValueType._CF_pattern.addPattern(pattern='[A-Z0-9]{2,30}')
ProductCodeValueType._InitializeFacetMap(ProductCodeValueType._CF_minLength,
   ProductCodeValueType._CF_maxLength,
   ProductCodeValueType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ProductCodeValueType', ProductCodeValueType)
_module_typeBindings.ProductCodeValueType = ProductCodeValueType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}ProductFeeMeasuringUnitType
class ProductFeeMeasuringUnitType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Díjtétel egység típusUnit of the rate type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductFeeMeasuringUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 217, 1)
    _Documentation = 'Díjtétel egység típusUnit of the rate type'
ProductFeeMeasuringUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProductFeeMeasuringUnitType, enum_prefix=None)
ProductFeeMeasuringUnitType.DARAB = ProductFeeMeasuringUnitType._CF_enumeration.addEnumeration(unicode_value='DARAB', tag='DARAB')
ProductFeeMeasuringUnitType.KG = ProductFeeMeasuringUnitType._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
ProductFeeMeasuringUnitType._InitializeFacetMap(ProductFeeMeasuringUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProductFeeMeasuringUnitType', ProductFeeMeasuringUnitType)
_module_typeBindings.ProductFeeMeasuringUnitType = ProductFeeMeasuringUnitType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}ProductFeeOperationType
class ProductFeeOperationType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Termékdíj összesítés típusProduct fee summary type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductFeeOperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 237, 1)
    _Documentation = 'Termékdíj összesítés típusProduct fee summary type'
ProductFeeOperationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProductFeeOperationType, enum_prefix=None)
ProductFeeOperationType.REFUND = ProductFeeOperationType._CF_enumeration.addEnumeration(unicode_value='REFUND', tag='REFUND')
ProductFeeOperationType.DEPOSIT = ProductFeeOperationType._CF_enumeration.addEnumeration(unicode_value='DEPOSIT', tag='DEPOSIT')
ProductFeeOperationType._InitializeFacetMap(ProductFeeOperationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProductFeeOperationType', ProductFeeOperationType)
_module_typeBindings.ProductFeeOperationType = ProductFeeOperationType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}ProductStreamType
class ProductStreamType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Termékáram típusProduct stream"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductStreamType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 257, 1)
    _Documentation = 'Termékáram típusProduct stream'
ProductStreamType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProductStreamType, enum_prefix=None)
ProductStreamType.BATTERY = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='BATTERY', tag='BATTERY')
ProductStreamType.PACKAGING = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='PACKAGING', tag='PACKAGING')
ProductStreamType.OTHER_PETROL = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='OTHER_PETROL', tag='OTHER_PETROL')
ProductStreamType.ELECTRONIC = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='ELECTRONIC', tag='ELECTRONIC')
ProductStreamType.TIRE = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='TIRE', tag='TIRE')
ProductStreamType.COMMERCIAL = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='COMMERCIAL', tag='COMMERCIAL')
ProductStreamType.PLASTIC = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='PLASTIC', tag='PLASTIC')
ProductStreamType.OTHER_CHEMICAL = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='OTHER_CHEMICAL', tag='OTHER_CHEMICAL')
ProductStreamType.PAPER = ProductStreamType._CF_enumeration.addEnumeration(unicode_value='PAPER', tag='PAPER')
ProductStreamType._InitializeFacetMap(ProductStreamType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProductStreamType', ProductStreamType)
_module_typeBindings.ProductStreamType = ProductStreamType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}QuantityType
class QuantityType (_ImportedBinding_common.GenericDecimalType):

    """Mennyiségi érték típus. Maximum 22 számjegy, ami 10 tizedesjegyet tartalmazhatField type for quantity values. Maximum 22 digits that may include 10 decimal places"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuantityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 319, 1)
    _Documentation = 'Mennyiségi érték típus. Maximum 22 számjegy, ami 10 tizedesjegyet tartalmazhatField type for quantity values. Maximum 22 digits that may include 10 decimal places'
QuantityType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(22))
QuantityType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(10))
QuantityType._InitializeFacetMap(QuantityType._CF_totalDigits,
   QuantityType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'QuantityType', QuantityType)
_module_typeBindings.QuantityType = QuantityType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}RateType
class RateType (_ImportedBinding_common.GenericDecimalType):

    """Arány megadására szolgáló típus. 0 és 1 közötti szám, legfeljebb 4 tizedesjegy pontossággalRate type. A number between 0 and 1, may include maximum 4 decimal places"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 329, 1)
    _Documentation = 'Arány megadására szolgáló típus. 0 és 1 közötti szám, legfeljebb 4 tizedesjegy pontossággalRate type. A number between 0 and 1, may include maximum 4 decimal places'
RateType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=RateType, value=pyxb.binding.datatypes.decimal('0.0'))
RateType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=RateType, value=pyxb.binding.datatypes.decimal('1.0'))
RateType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5))
RateType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4))
RateType._InitializeFacetMap(RateType._CF_minInclusive,
   RateType._CF_maxInclusive,
   RateType._CF_totalDigits,
   RateType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'RateType', RateType)
_module_typeBindings.RateType = RateType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}TakeoverType
class TakeoverType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Az átvállalás adatait tartalmazó típusField type for data of takeover"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TakeoverType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 341, 1)
    _Documentation = 'Az átvállalás adatait tartalmazó típusField type for data of takeover'
TakeoverType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TakeoverType, enum_prefix=None)
TakeoverType.n01 = TakeoverType._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
TakeoverType.n02_aa = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_aa', tag='n02_aa')
TakeoverType.n02_ab = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_ab', tag='n02_ab')
TakeoverType.n02_b = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_b', tag='n02_b')
TakeoverType.n02_c = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_c', tag='n02_c')
TakeoverType.n02_d = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_d', tag='n02_d')
TakeoverType.n02_ea = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_ea', tag='n02_ea')
TakeoverType.n02_eb = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_eb', tag='n02_eb')
TakeoverType.n02_fa = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_fa', tag='n02_fa')
TakeoverType.n02_fb = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_fb', tag='n02_fb')
TakeoverType.n02_ga = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_ga', tag='n02_ga')
TakeoverType.n02_gb = TakeoverType._CF_enumeration.addEnumeration(unicode_value='02_gb', tag='n02_gb')
TakeoverType._InitializeFacetMap(TakeoverType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TakeoverType', TakeoverType)
_module_typeBindings.TakeoverType = TakeoverType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/data}UnitOfMeasureType
class UnitOfMeasureType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Mennyiség egység típusUnit of measure type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 371, 1)
    _Documentation = 'Mennyiség egység típusUnit of measure type'
UnitOfMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfMeasureType, enum_prefix=None)
UnitOfMeasureType.PIECE = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='PIECE', tag='PIECE')
UnitOfMeasureType.KILOGRAM = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOGRAM', tag='KILOGRAM')
UnitOfMeasureType.TON = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='TON', tag='TON')
UnitOfMeasureType.KWH = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='KWH', tag='KWH')
UnitOfMeasureType.DAY = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='DAY', tag='DAY')
UnitOfMeasureType.HOUR = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='HOUR', tag='HOUR')
UnitOfMeasureType.MINUTE = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='MINUTE', tag='MINUTE')
UnitOfMeasureType.MONTH = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='MONTH', tag='MONTH')
UnitOfMeasureType.LITER = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='LITER', tag='LITER')
UnitOfMeasureType.KILOMETER = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOMETER', tag='KILOMETER')
UnitOfMeasureType.CUBIC_METER = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='CUBIC_METER', tag='CUBIC_METER')
UnitOfMeasureType.METER = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='METER', tag='METER')
UnitOfMeasureType.LINEAR_METER = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='LINEAR_METER', tag='LINEAR_METER')
UnitOfMeasureType.CARTON = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='CARTON', tag='CARTON')
UnitOfMeasureType.PACK = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='PACK', tag='PACK')
UnitOfMeasureType.OWN = UnitOfMeasureType._CF_enumeration.addEnumeration(unicode_value='OWN', tag='OWN')
UnitOfMeasureType._InitializeFacetMap(UnitOfMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfMeasureType', UnitOfMeasureType)
_module_typeBindings.UnitOfMeasureType = UnitOfMeasureType

# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}AdditionalDataType with content type ELEMENT_ONLY
class AdditionalDataType (pyxb.binding.basis.complexTypeDefinition):
    """További adat leírására szolgáló típusType for additional data description"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 475, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}dataName uses Python identifier dataName
    __dataName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dataName'), 'dataName', '__httpschemas_nav_gov_huOSA3_0data_AdditionalDataType_httpschemas_nav_gov_huOSA3_0datadataName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 481, 3), )

    
    dataName = property(__dataName.value, __dataName.set, None, 'Az adatmező egyedi azonosítójaUnique identification of the data field')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}dataDescription uses Python identifier dataDescription
    __dataDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dataDescription'), 'dataDescription', '__httpschemas_nav_gov_huOSA3_0data_AdditionalDataType_httpschemas_nav_gov_huOSA3_0datadataDescription', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 487, 3), )

    
    dataDescription = property(__dataDescription.value, __dataDescription.set, None, 'Az adatmező tartalmának szöveges leírásaDescription of content of the data field')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}dataValue uses Python identifier dataValue
    __dataValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dataValue'), 'dataValue', '__httpschemas_nav_gov_huOSA3_0data_AdditionalDataType_httpschemas_nav_gov_huOSA3_0datadataValue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 493, 3), )

    
    dataValue = property(__dataValue.value, __dataValue.set, None, 'Az adat értékeValue of the data')

    _ElementMap.update({
        __dataName.name() : __dataName,
        __dataDescription.name() : __dataDescription,
        __dataValue.name() : __dataValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalDataType = AdditionalDataType
Namespace.addCategoryObject('typeBinding', 'AdditionalDataType', AdditionalDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}AdvanceDataType with content type ELEMENT_ONLY
class AdvanceDataType (pyxb.binding.basis.complexTypeDefinition):
    """Előleghez kapcsolódó adatokAdvance related data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdvanceDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 501, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}advanceIndicator uses Python identifier advanceIndicator
    __advanceIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'advanceIndicator'), 'advanceIndicator', '__httpschemas_nav_gov_huOSA3_0data_AdvanceDataType_httpschemas_nav_gov_huOSA3_0dataadvanceIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 507, 3), )

    
    advanceIndicator = property(__advanceIndicator.value, __advanceIndicator.set, None, 'Értéke true, ha a számla tétel előleg jellegűThe value is true if the invoice item is a kind of advance charge')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}advancePaymentData uses Python identifier advancePaymentData
    __advancePaymentData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'advancePaymentData'), 'advancePaymentData', '__httpschemas_nav_gov_huOSA3_0data_AdvanceDataType_httpschemas_nav_gov_huOSA3_0dataadvancePaymentData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 513, 3), )

    
    advancePaymentData = property(__advancePaymentData.value, __advancePaymentData.set, None, 'Előleg fizetéshez kapcsolódó adatokAdvance payment related data')

    _ElementMap.update({
        __advanceIndicator.name() : __advanceIndicator,
        __advancePaymentData.name() : __advancePaymentData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdvanceDataType = AdvanceDataType
Namespace.addCategoryObject('typeBinding', 'AdvanceDataType', AdvanceDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}AdvancePaymentDataType with content type ELEMENT_ONLY
class AdvancePaymentDataType (pyxb.binding.basis.complexTypeDefinition):
    """Előlegfizetéshez kapcsolódó adatokAdvance payment related data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdvancePaymentDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 521, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}advanceOriginalInvoice uses Python identifier advanceOriginalInvoice
    __advanceOriginalInvoice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'advanceOriginalInvoice'), 'advanceOriginalInvoice', '__httpschemas_nav_gov_huOSA3_0data_AdvancePaymentDataType_httpschemas_nav_gov_huOSA3_0dataadvanceOriginalInvoice', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 527, 3), )

    
    advanceOriginalInvoice = property(__advanceOriginalInvoice.value, __advanceOriginalInvoice.set, None, 'Az előlegszámlának a sorszáma, amelyben az előlegfizetés történtInvoice number containing the advance payment')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}advancePaymentDate uses Python identifier advancePaymentDate
    __advancePaymentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'advancePaymentDate'), 'advancePaymentDate', '__httpschemas_nav_gov_huOSA3_0data_AdvancePaymentDataType_httpschemas_nav_gov_huOSA3_0dataadvancePaymentDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 533, 3), )

    
    advancePaymentDate = property(__advancePaymentDate.value, __advancePaymentDate.set, None, 'Az előleg fizetésének dátumaPayment date of the advance')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}advanceExchangeRate uses Python identifier advanceExchangeRate
    __advanceExchangeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'advanceExchangeRate'), 'advanceExchangeRate', '__httpschemas_nav_gov_huOSA3_0data_AdvancePaymentDataType_httpschemas_nav_gov_huOSA3_0dataadvanceExchangeRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 539, 3), )

    
    advanceExchangeRate = property(__advanceExchangeRate.value, __advanceExchangeRate.set, None, 'Az előlegfizetés során alkalmazott árfolyamApplied exchange rate of the advance')

    _ElementMap.update({
        __advanceOriginalInvoice.name() : __advanceOriginalInvoice,
        __advancePaymentDate.name() : __advancePaymentDate,
        __advanceExchangeRate.name() : __advanceExchangeRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdvancePaymentDataType = AdvancePaymentDataType
Namespace.addCategoryObject('typeBinding', 'AdvancePaymentDataType', AdvancePaymentDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}AggregateInvoiceLineDataType with content type ELEMENT_ONLY
class AggregateInvoiceLineDataType (pyxb.binding.basis.complexTypeDefinition):
    """A gyűjtő számlára vonatkozó speciális adatokat tartalmazó típusField type including aggregate invoice special data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AggregateInvoiceLineDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 547, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineExchangeRate uses Python identifier lineExchangeRate
    __lineExchangeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineExchangeRate'), 'lineExchangeRate', '__httpschemas_nav_gov_huOSA3_0data_AggregateInvoiceLineDataType_httpschemas_nav_gov_huOSA3_0datalineExchangeRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 553, 3), )

    
    lineExchangeRate = property(__lineExchangeRate.value, __lineExchangeRate.set, None, 'A tételhez tartozó árfolyam, 1 (egy) egységre vonatkoztatva. Csak külföldi pénznemben kiállított gyűjtő számla esetén kitöltendőThe exchange rate applied to the item, pertaining to 1 (one) unit. This should be filled in only if an aggregate invoice in foreign currency is issued')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineDeliveryDate uses Python identifier lineDeliveryDate
    __lineDeliveryDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineDeliveryDate'), 'lineDeliveryDate', '__httpschemas_nav_gov_huOSA3_0data_AggregateInvoiceLineDataType_httpschemas_nav_gov_huOSA3_0datalineDeliveryDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 559, 3), )

    
    lineDeliveryDate = property(__lineDeliveryDate.value, __lineDeliveryDate.set, None, 'Gyűjtőszámla esetén az adott tétel teljesítési dátumaDelivery date of the given item in the case of an aggregate invoice')

    _ElementMap.update({
        __lineExchangeRate.name() : __lineExchangeRate,
        __lineDeliveryDate.name() : __lineDeliveryDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AggregateInvoiceLineDataType = AggregateInvoiceLineDataType
Namespace.addCategoryObject('typeBinding', 'AggregateInvoiceLineDataType', AggregateInvoiceLineDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}AircraftType with content type ELEMENT_ONLY
class AircraftType (pyxb.binding.basis.complexTypeDefinition):
    """Légi közlekedési eszközAircraft"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 567, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}takeOffWeight uses Python identifier takeOffWeight
    __takeOffWeight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'takeOffWeight'), 'takeOffWeight', '__httpschemas_nav_gov_huOSA3_0data_AircraftType_httpschemas_nav_gov_huOSA3_0datatakeOffWeight', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 573, 3), )

    
    takeOffWeight = property(__takeOffWeight.value, __takeOffWeight.set, None, 'Felszállási tömeg kilogrammbanTake-off weight in kilogram')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}airCargo uses Python identifier airCargo
    __airCargo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'airCargo'), 'airCargo', '__httpschemas_nav_gov_huOSA3_0data_AircraftType_httpschemas_nav_gov_huOSA3_0dataairCargo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 579, 3), )

    
    airCargo = property(__airCargo.value, __airCargo.set, None, 'Értéke true ha a jármű az ÁFA tv. 259.§ 25. c) szerinti kivétel alá tartozikThe value is true if the means of transport is exempt from VAT as per section 259 [25] (c)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}operationHours uses Python identifier operationHours
    __operationHours = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'operationHours'), 'operationHours', '__httpschemas_nav_gov_huOSA3_0data_AircraftType_httpschemas_nav_gov_huOSA3_0dataoperationHours', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 585, 3), )

    
    operationHours = property(__operationHours.value, __operationHours.set, None, 'Repült órák számaNumber of aviated hours')

    _ElementMap.update({
        __takeOffWeight.name() : __takeOffWeight,
        __airCargo.name() : __airCargo,
        __operationHours.name() : __operationHours
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AircraftType = AircraftType
Namespace.addCategoryObject('typeBinding', 'AircraftType', AircraftType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}BatchInvoiceType with content type ELEMENT_ONLY
class BatchInvoiceType (pyxb.binding.basis.complexTypeDefinition):
    """Kötegelt módosító okirat adataiData of a batch of modification documents"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BatchInvoiceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 593, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}batchIndex uses Python identifier batchIndex
    __batchIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), 'batchIndex', '__httpschemas_nav_gov_huOSA3_0data_BatchInvoiceType_httpschemas_nav_gov_huOSA3_0databatchIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 599, 3), )

    
    batchIndex = property(__batchIndex.value, __batchIndex.set, None, 'A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoice uses Python identifier invoice
    __invoice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoice'), 'invoice', '__httpschemas_nav_gov_huOSA3_0data_BatchInvoiceType_httpschemas_nav_gov_huOSA3_0datainvoice', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 605, 3), )

    
    invoice = property(__invoice.value, __invoice.set, None, 'Egy számla vagy módosító okirat adataiData of a single invoice or modification document')

    _ElementMap.update({
        __batchIndex.name() : __batchIndex,
        __invoice.name() : __invoice
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BatchInvoiceType = BatchInvoiceType
Namespace.addCategoryObject('typeBinding', 'BatchInvoiceType', BatchInvoiceType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ContractNumbersType with content type ELEMENT_ONLY
class ContractNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """SzerződésszámokContract numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContractNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 613, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}contractNumber uses Python identifier contractNumber
    __contractNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contractNumber'), 'contractNumber', '__httpschemas_nav_gov_huOSA3_0data_ContractNumbersType_httpschemas_nav_gov_huOSA3_0datacontractNumber', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 619, 3), )

    
    contractNumber = property(__contractNumber.value, __contractNumber.set, None, 'SzerződésszámContract number')

    _ElementMap.update({
        __contractNumber.name() : __contractNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ContractNumbersType = ContractNumbersType
Namespace.addCategoryObject('typeBinding', 'ContractNumbersType', ContractNumbersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ConventionalInvoiceInfoType with content type ELEMENT_ONLY
class ConventionalInvoiceInfoType (pyxb.binding.basis.complexTypeDefinition):
    """A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatokOther conventionally named data to assist in invoice processing"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConventionalInvoiceInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 627, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}orderNumbers uses Python identifier orderNumbers
    __orderNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderNumbers'), 'orderNumbers', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0dataorderNumbers', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 633, 3), )

    
    orderNumbers = property(__orderNumbers.value, __orderNumbers.set, None, 'Megrendelésszám(ok)Order numbers')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}deliveryNotes uses Python identifier deliveryNotes
    __deliveryNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deliveryNotes'), 'deliveryNotes', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datadeliveryNotes', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 639, 3), )

    
    deliveryNotes = property(__deliveryNotes.value, __deliveryNotes.set, None, 'Szállítólevél szám(ok)Delivery notes')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}shippingDates uses Python identifier shippingDates
    __shippingDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shippingDates'), 'shippingDates', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datashippingDates', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 645, 3), )

    
    shippingDates = property(__shippingDates.value, __shippingDates.set, None, 'Szállítási dátum(ok)Shipping dates')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}contractNumbers uses Python identifier contractNumbers
    __contractNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contractNumbers'), 'contractNumbers', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datacontractNumbers', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 651, 3), )

    
    contractNumbers = property(__contractNumbers.value, __contractNumbers.set, None, 'Szerződésszám(ok)Contract numbers')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}supplierCompanyCodes uses Python identifier supplierCompanyCodes
    __supplierCompanyCodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierCompanyCodes'), 'supplierCompanyCodes', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datasupplierCompanyCodes', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 657, 3), )

    
    supplierCompanyCodes = property(__supplierCompanyCodes.value, __supplierCompanyCodes.set, None, 'Az eladó vállalati kódja(i)Company codes of the supplier')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerCompanyCodes uses Python identifier customerCompanyCodes
    __customerCompanyCodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerCompanyCodes'), 'customerCompanyCodes', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datacustomerCompanyCodes', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 663, 3), )

    
    customerCompanyCodes = property(__customerCompanyCodes.value, __customerCompanyCodes.set, None, 'A vevő vállalati kódja(i)Company codes of the customer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}dealerCodes uses Python identifier dealerCodes
    __dealerCodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dealerCodes'), 'dealerCodes', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datadealerCodes', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 669, 3), )

    
    dealerCodes = property(__dealerCodes.value, __dealerCodes.set, None, 'Beszállító kód(ok)Dealer codes')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}costCenters uses Python identifier costCenters
    __costCenters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'costCenters'), 'costCenters', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datacostCenters', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 675, 3), )

    
    costCenters = property(__costCenters.value, __costCenters.set, None, 'Költséghely(ek)Cost centers')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}projectNumbers uses Python identifier projectNumbers
    __projectNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'projectNumbers'), 'projectNumbers', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0dataprojectNumbers', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 681, 3), )

    
    projectNumbers = property(__projectNumbers.value, __projectNumbers.set, None, 'Projektszám(ok)Project numbers')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}generalLedgerAccountNumbers uses Python identifier generalLedgerAccountNumbers
    __generalLedgerAccountNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generalLedgerAccountNumbers'), 'generalLedgerAccountNumbers', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datageneralLedgerAccountNumbers', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 687, 3), )

    
    generalLedgerAccountNumbers = property(__generalLedgerAccountNumbers.value, __generalLedgerAccountNumbers.set, None, 'Főkönyvi számlaszám(ok)General ledger account numbers')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}glnNumbersSupplier uses Python identifier glnNumbersSupplier
    __glnNumbersSupplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'glnNumbersSupplier'), 'glnNumbersSupplier', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0dataglnNumbersSupplier', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 693, 3), )

    
    glnNumbersSupplier = property(__glnNumbersSupplier.value, __glnNumbersSupplier.set, None, "Kiállítói globális helyazonosító szám(ok)Supplier's global location numbers")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}glnNumbersCustomer uses Python identifier glnNumbersCustomer
    __glnNumbersCustomer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'glnNumbersCustomer'), 'glnNumbersCustomer', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0dataglnNumbersCustomer', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 699, 3), )

    
    glnNumbersCustomer = property(__glnNumbersCustomer.value, __glnNumbersCustomer.set, None, "Vevői globális helyazonosító szám(ok)Customer's global location numbers")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}materialNumbers uses Python identifier materialNumbers
    __materialNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'materialNumbers'), 'materialNumbers', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0datamaterialNumbers', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 705, 3), )

    
    materialNumbers = property(__materialNumbers.value, __materialNumbers.set, None, 'Anyagszám(ok)Material numbers')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}itemNumbers uses Python identifier itemNumbers
    __itemNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemNumbers'), 'itemNumbers', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0dataitemNumbers', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 711, 3), )

    
    itemNumbers = property(__itemNumbers.value, __itemNumbers.set, None, 'Cikkszám(ok)Item number(s)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}ekaerIds uses Python identifier ekaerIds
    __ekaerIds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ekaerIds'), 'ekaerIds', '__httpschemas_nav_gov_huOSA3_0data_ConventionalInvoiceInfoType_httpschemas_nav_gov_huOSA3_0dataekaerIds', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 717, 3), )

    
    ekaerIds = property(__ekaerIds.value, __ekaerIds.set, None, 'EKÁER azonosító(k)EKAER ID-s')

    _ElementMap.update({
        __orderNumbers.name() : __orderNumbers,
        __deliveryNotes.name() : __deliveryNotes,
        __shippingDates.name() : __shippingDates,
        __contractNumbers.name() : __contractNumbers,
        __supplierCompanyCodes.name() : __supplierCompanyCodes,
        __customerCompanyCodes.name() : __customerCompanyCodes,
        __dealerCodes.name() : __dealerCodes,
        __costCenters.name() : __costCenters,
        __projectNumbers.name() : __projectNumbers,
        __generalLedgerAccountNumbers.name() : __generalLedgerAccountNumbers,
        __glnNumbersSupplier.name() : __glnNumbersSupplier,
        __glnNumbersCustomer.name() : __glnNumbersCustomer,
        __materialNumbers.name() : __materialNumbers,
        __itemNumbers.name() : __itemNumbers,
        __ekaerIds.name() : __ekaerIds
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConventionalInvoiceInfoType = ConventionalInvoiceInfoType
Namespace.addCategoryObject('typeBinding', 'ConventionalInvoiceInfoType', ConventionalInvoiceInfoType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}CostCentersType with content type ELEMENT_ONLY
class CostCentersType (pyxb.binding.basis.complexTypeDefinition):
    """KöltséghelyekCost centers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CostCentersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 725, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}costCenter uses Python identifier costCenter
    __costCenter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'costCenter'), 'costCenter', '__httpschemas_nav_gov_huOSA3_0data_CostCentersType_httpschemas_nav_gov_huOSA3_0datacostCenter', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 731, 3), )

    
    costCenter = property(__costCenter.value, __costCenter.set, None, 'KöltséghelyCost center')

    _ElementMap.update({
        __costCenter.name() : __costCenter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CostCentersType = CostCentersType
Namespace.addCategoryObject('typeBinding', 'CostCentersType', CostCentersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}CustomerCompanyCodesType with content type ELEMENT_ONLY
class CustomerCompanyCodesType (pyxb.binding.basis.complexTypeDefinition):
    """A vevő vállalati kódjaiCompany codes of the customer"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerCompanyCodesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 739, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerCompanyCode uses Python identifier customerCompanyCode
    __customerCompanyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerCompanyCode'), 'customerCompanyCode', '__httpschemas_nav_gov_huOSA3_0data_CustomerCompanyCodesType_httpschemas_nav_gov_huOSA3_0datacustomerCompanyCode', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 745, 3), )

    
    customerCompanyCode = property(__customerCompanyCode.value, __customerCompanyCode.set, None, 'A vevő vállalati kódjaCompany code of the customer')

    _ElementMap.update({
        __customerCompanyCode.name() : __customerCompanyCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomerCompanyCodesType = CustomerCompanyCodesType
Namespace.addCategoryObject('typeBinding', 'CustomerCompanyCodesType', CustomerCompanyCodesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}CustomerDeclarationType with content type ELEMENT_ONLY
class CustomerDeclarationType (pyxb.binding.basis.complexTypeDefinition):
    """Ha az eladó a vevő nyilatkozata alapján mentesül a termékdíj megfizetése alól, akkor az érintett termékáramShould the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerDeclarationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 753, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productStream uses Python identifier productStream
    __productStream = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productStream'), 'productStream', '__httpschemas_nav_gov_huOSA3_0data_CustomerDeclarationType_httpschemas_nav_gov_huOSA3_0dataproductStream', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 759, 3), )

    
    productStream = property(__productStream.value, __productStream.set, None, 'TermékáramProduct stream')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeWeight uses Python identifier productFeeWeight
    __productFeeWeight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeWeight'), 'productFeeWeight', '__httpschemas_nav_gov_huOSA3_0data_CustomerDeclarationType_httpschemas_nav_gov_huOSA3_0dataproductFeeWeight', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 765, 3), )

    
    productFeeWeight = property(__productFeeWeight.value, __productFeeWeight.set, None, 'Termékdíj köteles termék tömege kilogrammbanWeight of product fee obliged product in kilogram')

    _ElementMap.update({
        __productStream.name() : __productStream,
        __productFeeWeight.name() : __productFeeWeight
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomerDeclarationType = CustomerDeclarationType
Namespace.addCategoryObject('typeBinding', 'CustomerDeclarationType', CustomerDeclarationType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}CustomerInfoType with content type ELEMENT_ONLY
class CustomerInfoType (pyxb.binding.basis.complexTypeDefinition):
    """A vevő adataiCustomer data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 773, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerVatStatus uses Python identifier customerVatStatus
    __customerVatStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerVatStatus'), 'customerVatStatus', '__httpschemas_nav_gov_huOSA3_0data_CustomerInfoType_httpschemas_nav_gov_huOSA3_0datacustomerVatStatus', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 779, 3), )

    
    customerVatStatus = property(__customerVatStatus.value, __customerVatStatus.set, None, 'Vevő ÁFA szerinti státuszaCustomers status by VAT')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerVatData uses Python identifier customerVatData
    __customerVatData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerVatData'), 'customerVatData', '__httpschemas_nav_gov_huOSA3_0data_CustomerInfoType_httpschemas_nav_gov_huOSA3_0datacustomerVatData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 785, 3), )

    
    customerVatData = property(__customerVatData.value, __customerVatData.set, None, 'A vevő ÁFA alanyisági adataiVAT subjectivity data of the customer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerName uses Python identifier customerName
    __customerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerName'), 'customerName', '__httpschemas_nav_gov_huOSA3_0data_CustomerInfoType_httpschemas_nav_gov_huOSA3_0datacustomerName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 791, 3), )

    
    customerName = property(__customerName.value, __customerName.set, None, 'A vevő neveName of the customer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerAddress uses Python identifier customerAddress
    __customerAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerAddress'), 'customerAddress', '__httpschemas_nav_gov_huOSA3_0data_CustomerInfoType_httpschemas_nav_gov_huOSA3_0datacustomerAddress', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 797, 3), )

    
    customerAddress = property(__customerAddress.value, __customerAddress.set, None, 'A vevő címeAddress of the customer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerBankAccountNumber uses Python identifier customerBankAccountNumber
    __customerBankAccountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerBankAccountNumber'), 'customerBankAccountNumber', '__httpschemas_nav_gov_huOSA3_0data_CustomerInfoType_httpschemas_nav_gov_huOSA3_0datacustomerBankAccountNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 803, 3), )

    
    customerBankAccountNumber = property(__customerBankAccountNumber.value, __customerBankAccountNumber.set, None, 'Vevő bankszámlaszámaBank account number of the customer')

    _ElementMap.update({
        __customerVatStatus.name() : __customerVatStatus,
        __customerVatData.name() : __customerVatData,
        __customerName.name() : __customerName,
        __customerAddress.name() : __customerAddress,
        __customerBankAccountNumber.name() : __customerBankAccountNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomerInfoType = CustomerInfoType
Namespace.addCategoryObject('typeBinding', 'CustomerInfoType', CustomerInfoType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}CustomerVatDataType with content type ELEMENT_ONLY
class CustomerVatDataType (pyxb.binding.basis.complexTypeDefinition):
    """A vevő ÁFA alanyisági adataiVAT subjectivity data of the customer"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerVatDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 829, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerTaxNumber uses Python identifier customerTaxNumber
    __customerTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber'), 'customerTaxNumber', '__httpschemas_nav_gov_huOSA3_0data_CustomerVatDataType_httpschemas_nav_gov_huOSA3_0datacustomerTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 835, 3), )

    
    customerTaxNumber = property(__customerTaxNumber.value, __customerTaxNumber.set, None, 'Belföldi adószám, amely alatt a számlán szereplő termékbeszerzés vagy szolgáltatás igénybevétele történt. Lehet csoportazonosító szám isDomestic tax number or group identification number, under which the purchase of goods or services is done')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}communityVatNumber uses Python identifier communityVatNumber
    __communityVatNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'communityVatNumber'), 'communityVatNumber', '__httpschemas_nav_gov_huOSA3_0data_CustomerVatDataType_httpschemas_nav_gov_huOSA3_0datacommunityVatNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 841, 3), )

    
    communityVatNumber = property(__communityVatNumber.value, __communityVatNumber.set, None, 'Közösségi adószámCommunity tax number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}thirdStateTaxId uses Python identifier thirdStateTaxId
    __thirdStateTaxId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'thirdStateTaxId'), 'thirdStateTaxId', '__httpschemas_nav_gov_huOSA3_0data_CustomerVatDataType_httpschemas_nav_gov_huOSA3_0datathirdStateTaxId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 847, 3), )

    
    thirdStateTaxId = property(__thirdStateTaxId.value, __thirdStateTaxId.set, None, 'Harmadik országbeli adóazonosítóThird state tax identification number')

    _ElementMap.update({
        __customerTaxNumber.name() : __customerTaxNumber,
        __communityVatNumber.name() : __communityVatNumber,
        __thirdStateTaxId.name() : __thirdStateTaxId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomerVatDataType = CustomerVatDataType
Namespace.addCategoryObject('typeBinding', 'CustomerVatDataType', CustomerVatDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}DealerCodesType with content type ELEMENT_ONLY
class DealerCodesType (pyxb.binding.basis.complexTypeDefinition):
    """Beszállító kódokDealer codes"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DealerCodesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 855, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}dealerCode uses Python identifier dealerCode
    __dealerCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dealerCode'), 'dealerCode', '__httpschemas_nav_gov_huOSA3_0data_DealerCodesType_httpschemas_nav_gov_huOSA3_0datadealerCode', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 861, 3), )

    
    dealerCode = property(__dealerCode.value, __dealerCode.set, None, 'Beszállító kódDealer code')

    _ElementMap.update({
        __dealerCode.name() : __dealerCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DealerCodesType = DealerCodesType
Namespace.addCategoryObject('typeBinding', 'DealerCodesType', DealerCodesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}DeliveryNotesType with content type ELEMENT_ONLY
class DeliveryNotesType (pyxb.binding.basis.complexTypeDefinition):
    """Szállítólevél számokDelivery notes"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryNotesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 869, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}deliveryNote uses Python identifier deliveryNote
    __deliveryNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deliveryNote'), 'deliveryNote', '__httpschemas_nav_gov_huOSA3_0data_DeliveryNotesType_httpschemas_nav_gov_huOSA3_0datadeliveryNote', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 875, 3), )

    
    deliveryNote = property(__deliveryNote.value, __deliveryNote.set, None, 'Szállítólevél számDelivery note')

    _ElementMap.update({
        __deliveryNote.name() : __deliveryNote
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DeliveryNotesType = DeliveryNotesType
Namespace.addCategoryObject('typeBinding', 'DeliveryNotesType', DeliveryNotesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}DetailedReasonType with content type ELEMENT_ONLY
class DetailedReasonType (pyxb.binding.basis.complexTypeDefinition):
    """Mentesség, kivétel részletes indokolásaDetailed justification of exemption"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DetailedReasonType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 883, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}case uses Python identifier case
    __case = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'case'), 'case', '__httpschemas_nav_gov_huOSA3_0data_DetailedReasonType_httpschemas_nav_gov_huOSA3_0datacase', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 889, 3), )

    
    case = property(__case.value, __case.set, None, 'Az eset leírása kóddalCase notation with code')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}reason uses Python identifier reason
    __reason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reason'), 'reason', '__httpschemas_nav_gov_huOSA3_0data_DetailedReasonType_httpschemas_nav_gov_huOSA3_0datareason', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 895, 3), )

    
    reason = property(__reason.value, __reason.set, None, 'Az eset leírása szöveggelCase notation with text')

    _ElementMap.update({
        __case.name() : __case,
        __reason.name() : __reason
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DetailedReasonType = DetailedReasonType
Namespace.addCategoryObject('typeBinding', 'DetailedReasonType', DetailedReasonType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}DieselOilPurchaseType with content type ELEMENT_ONLY
class DieselOilPurchaseType (pyxb.binding.basis.complexTypeDefinition):
    """Gázolaj adózottan történő beszerzésének adatai – 45/2016 (XI. 29.) NGM rendelet 75. § (1) a)Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DieselOilPurchaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 903, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}purchaseLocation uses Python identifier purchaseLocation
    __purchaseLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'purchaseLocation'), 'purchaseLocation', '__httpschemas_nav_gov_huOSA3_0data_DieselOilPurchaseType_httpschemas_nav_gov_huOSA3_0datapurchaseLocation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 909, 3), )

    
    purchaseLocation = property(__purchaseLocation.value, __purchaseLocation.set, None, 'Gázolaj beszerzés helyePlace of purchase of the gas oil')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}purchaseDate uses Python identifier purchaseDate
    __purchaseDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'purchaseDate'), 'purchaseDate', '__httpschemas_nav_gov_huOSA3_0data_DieselOilPurchaseType_httpschemas_nav_gov_huOSA3_0datapurchaseDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 915, 3), )

    
    purchaseDate = property(__purchaseDate.value, __purchaseDate.set, None, 'Gázolaj beszerzés dátumaDate of purchase of gas oil')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vehicleRegistrationNumber uses Python identifier vehicleRegistrationNumber
    __vehicleRegistrationNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vehicleRegistrationNumber'), 'vehicleRegistrationNumber', '__httpschemas_nav_gov_huOSA3_0data_DieselOilPurchaseType_httpschemas_nav_gov_huOSA3_0datavehicleRegistrationNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 921, 3), )

    
    vehicleRegistrationNumber = property(__vehicleRegistrationNumber.value, __vehicleRegistrationNumber.set, None, 'Kereskedelmi jármű forgalmi rendszáma (csak betűk és számok)Registration number of vehicle (letters and numbers only)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}dieselOilQuantity uses Python identifier dieselOilQuantity
    __dieselOilQuantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dieselOilQuantity'), 'dieselOilQuantity', '__httpschemas_nav_gov_huOSA3_0data_DieselOilPurchaseType_httpschemas_nav_gov_huOSA3_0datadieselOilQuantity', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 927, 3), )

    
    dieselOilQuantity = property(__dieselOilQuantity.value, __dieselOilQuantity.set, None, 'Gépi bérmunka-szolgáltatás során felhasznált gázolaj mennyisége literben – Jöt. 117. § (2)Fordítandó helyett: Quantity of diesel oil used for contract work and machinery hire service in liter – Act LXVIII of 2016 on Excise Tax section 117 (2)')

    _ElementMap.update({
        __purchaseLocation.name() : __purchaseLocation,
        __purchaseDate.name() : __purchaseDate,
        __vehicleRegistrationNumber.name() : __vehicleRegistrationNumber,
        __dieselOilQuantity.name() : __dieselOilQuantity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DieselOilPurchaseType = DieselOilPurchaseType
Namespace.addCategoryObject('typeBinding', 'DieselOilPurchaseType', DieselOilPurchaseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}DiscountDataType with content type ELEMENT_ONLY
class DiscountDataType (pyxb.binding.basis.complexTypeDefinition):
    """Árengedmény adatokDiscount data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DiscountDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 935, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}discountDescription uses Python identifier discountDescription
    __discountDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discountDescription'), 'discountDescription', '__httpschemas_nav_gov_huOSA3_0data_DiscountDataType_httpschemas_nav_gov_huOSA3_0datadiscountDescription', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 941, 3), )

    
    discountDescription = property(__discountDescription.value, __discountDescription.set, None, 'Az árengedmény leírásaDescription of the discount')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}discountValue uses Python identifier discountValue
    __discountValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discountValue'), 'discountValue', '__httpschemas_nav_gov_huOSA3_0data_DiscountDataType_httpschemas_nav_gov_huOSA3_0datadiscountValue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 947, 3), )

    
    discountValue = property(__discountValue.value, __discountValue.set, None, 'Tételhez tartozó árengedmény összege a számla pénznemében, ha az egységár nem tartalmazzaTotal amount of discount per item expressed in the currency of the invoice if not included in the unit price')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}discountRate uses Python identifier discountRate
    __discountRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discountRate'), 'discountRate', '__httpschemas_nav_gov_huOSA3_0data_DiscountDataType_httpschemas_nav_gov_huOSA3_0datadiscountRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 953, 3), )

    
    discountRate = property(__discountRate.value, __discountRate.set, None, 'Tételhez tartozó árengedmény aránya, ha az egységár nem tartalmazzaRate of discount per item expressed in the currency of the invoice if not included in the unit price')

    _ElementMap.update({
        __discountDescription.name() : __discountDescription,
        __discountValue.name() : __discountValue,
        __discountRate.name() : __discountRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DiscountDataType = DiscountDataType
Namespace.addCategoryObject('typeBinding', 'DiscountDataType', DiscountDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}EkaerIdsType with content type ELEMENT_ONLY
class EkaerIdsType (pyxb.binding.basis.complexTypeDefinition):
    """EKÁER azonosító(k)EKAER ID-s"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EkaerIdsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 961, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}ekaerId uses Python identifier ekaerId
    __ekaerId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ekaerId'), 'ekaerId', '__httpschemas_nav_gov_huOSA3_0data_EkaerIdsType_httpschemas_nav_gov_huOSA3_0dataekaerId', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 967, 3), )

    
    ekaerId = property(__ekaerId.value, __ekaerId.set, None, 'EKÁER azonosítóEKAER numbers; EKAER stands for Electronic Trade and Transport Control System')

    _ElementMap.update({
        __ekaerId.name() : __ekaerId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EkaerIdsType = EkaerIdsType
Namespace.addCategoryObject('typeBinding', 'EkaerIdsType', EkaerIdsType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}FiscalRepresentativeType with content type ELEMENT_ONLY
class FiscalRepresentativeType (pyxb.binding.basis.complexTypeDefinition):
    """A pénzügyi képviselő adataiFiscal representative data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FiscalRepresentativeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 975, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeTaxNumber uses Python identifier fiscalRepresentativeTaxNumber
    __fiscalRepresentativeTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeTaxNumber'), 'fiscalRepresentativeTaxNumber', '__httpschemas_nav_gov_huOSA3_0data_FiscalRepresentativeType_httpschemas_nav_gov_huOSA3_0datafiscalRepresentativeTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 981, 3), )

    
    fiscalRepresentativeTaxNumber = property(__fiscalRepresentativeTaxNumber.value, __fiscalRepresentativeTaxNumber.set, None, 'A pénzügyi képviselő adószámaTax number of the fiscal representative')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeName uses Python identifier fiscalRepresentativeName
    __fiscalRepresentativeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeName'), 'fiscalRepresentativeName', '__httpschemas_nav_gov_huOSA3_0data_FiscalRepresentativeType_httpschemas_nav_gov_huOSA3_0datafiscalRepresentativeName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 987, 3), )

    
    fiscalRepresentativeName = property(__fiscalRepresentativeName.value, __fiscalRepresentativeName.set, None, 'A pénzügyi képviselő neveName of the fiscal representative')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeAddress uses Python identifier fiscalRepresentativeAddress
    __fiscalRepresentativeAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeAddress'), 'fiscalRepresentativeAddress', '__httpschemas_nav_gov_huOSA3_0data_FiscalRepresentativeType_httpschemas_nav_gov_huOSA3_0datafiscalRepresentativeAddress', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 993, 3), )

    
    fiscalRepresentativeAddress = property(__fiscalRepresentativeAddress.value, __fiscalRepresentativeAddress.set, None, 'Pénzügyi képviselő címeAddress of the fiscal representative')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeBankAccountNumber uses Python identifier fiscalRepresentativeBankAccountNumber
    __fiscalRepresentativeBankAccountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeBankAccountNumber'), 'fiscalRepresentativeBankAccountNumber', '__httpschemas_nav_gov_huOSA3_0data_FiscalRepresentativeType_httpschemas_nav_gov_huOSA3_0datafiscalRepresentativeBankAccountNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 999, 3), )

    
    fiscalRepresentativeBankAccountNumber = property(__fiscalRepresentativeBankAccountNumber.value, __fiscalRepresentativeBankAccountNumber.set, None, 'Pénzügyi képviselő által a számla kibocsátó (eladó) számára megnyitott bankszámla bankszámlaszámaBank account number opened by the fiscal representative for the issuer of the invoice (supplier)')

    _ElementMap.update({
        __fiscalRepresentativeTaxNumber.name() : __fiscalRepresentativeTaxNumber,
        __fiscalRepresentativeName.name() : __fiscalRepresentativeName,
        __fiscalRepresentativeAddress.name() : __fiscalRepresentativeAddress,
        __fiscalRepresentativeBankAccountNumber.name() : __fiscalRepresentativeBankAccountNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FiscalRepresentativeType = FiscalRepresentativeType
Namespace.addCategoryObject('typeBinding', 'FiscalRepresentativeType', FiscalRepresentativeType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}GeneralLedgerAccountNumbersType with content type ELEMENT_ONLY
class GeneralLedgerAccountNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """Főkönyvi számlaszámokGeneral ledger account numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneralLedgerAccountNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1007, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}generalLedgerAccountNumber uses Python identifier generalLedgerAccountNumber
    __generalLedgerAccountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generalLedgerAccountNumber'), 'generalLedgerAccountNumber', '__httpschemas_nav_gov_huOSA3_0data_GeneralLedgerAccountNumbersType_httpschemas_nav_gov_huOSA3_0datageneralLedgerAccountNumber', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1013, 3), )

    
    generalLedgerAccountNumber = property(__generalLedgerAccountNumber.value, __generalLedgerAccountNumber.set, None, 'Főkönyvi számlaszámGeneral ledger account number')

    _ElementMap.update({
        __generalLedgerAccountNumber.name() : __generalLedgerAccountNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GeneralLedgerAccountNumbersType = GeneralLedgerAccountNumbersType
Namespace.addCategoryObject('typeBinding', 'GeneralLedgerAccountNumbersType', GeneralLedgerAccountNumbersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}GlnNumbersType with content type ELEMENT_ONLY
class GlnNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """Globális helyazonosító számokGlobal location numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GlnNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1021, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}glnNumber uses Python identifier glnNumber
    __glnNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'glnNumber'), 'glnNumber', '__httpschemas_nav_gov_huOSA3_0data_GlnNumbersType_httpschemas_nav_gov_huOSA3_0dataglnNumber', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1027, 3), )

    
    glnNumber = property(__glnNumber.value, __glnNumber.set, None, 'Globális helyazonosító számGlobal location number')

    _ElementMap.update({
        __glnNumber.name() : __glnNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GlnNumbersType = GlnNumbersType
Namespace.addCategoryObject('typeBinding', 'GlnNumbersType', GlnNumbersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceDetailType with content type ELEMENT_ONLY
class InvoiceDetailType (pyxb.binding.basis.complexTypeDefinition):
    """Számla részletező adatokInvoice detail data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceDetailType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1035, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceCategory uses Python identifier invoiceCategory
    __invoiceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory'), 'invoiceCategory', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datainvoiceCategory', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1041, 3), )

    
    invoiceCategory = property(__invoiceCategory.value, __invoiceCategory.set, None, 'A számla típusa, módosító okirat esetén az eredeti számla típusaType of invoice. In case of modification document the type of original invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceDeliveryDate uses Python identifier invoiceDeliveryDate
    __invoiceDeliveryDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryDate'), 'invoiceDeliveryDate', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datainvoiceDeliveryDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1047, 3), )

    
    invoiceDeliveryDate = property(__invoiceDeliveryDate.value, __invoiceDeliveryDate.set, None, 'Teljesítés dátuma (ha nem szerepel a számlán, akkor azonos a számla keltével) - ÁFA tv. 169. § g)Delivery date (if this field does not exist on the invoice, the date of the invoice should be considered as such) - section 169 (g) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceDeliveryPeriodStart uses Python identifier invoiceDeliveryPeriodStart
    __invoiceDeliveryPeriodStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryPeriodStart'), 'invoiceDeliveryPeriodStart', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datainvoiceDeliveryPeriodStart', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1053, 3), )

    
    invoiceDeliveryPeriodStart = property(__invoiceDeliveryPeriodStart.value, __invoiceDeliveryPeriodStart.set, None, 'Amennyiben a számla egy időszakra vonatkozik, akkor az időszak első napjaThe first day of the delivery, if the invoice delivery is a period')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceDeliveryPeriodEnd uses Python identifier invoiceDeliveryPeriodEnd
    __invoiceDeliveryPeriodEnd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryPeriodEnd'), 'invoiceDeliveryPeriodEnd', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datainvoiceDeliveryPeriodEnd', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1059, 3), )

    
    invoiceDeliveryPeriodEnd = property(__invoiceDeliveryPeriodEnd.value, __invoiceDeliveryPeriodEnd.set, None, 'Amennyiben a számla egy időszakra vonatkozik, akkor az időszak utolsó napjaThe last day of the delivery, if the invoice delivery is a period')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceAccountingDeliveryDate uses Python identifier invoiceAccountingDeliveryDate
    __invoiceAccountingDeliveryDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceAccountingDeliveryDate'), 'invoiceAccountingDeliveryDate', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datainvoiceAccountingDeliveryDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1065, 3), )

    
    invoiceAccountingDeliveryDate = property(__invoiceAccountingDeliveryDate.value, __invoiceAccountingDeliveryDate.set, None, 'Számviteli teljesítés dátuma. Időszak esetén az időszak utolsó napjaDate of accounting accomplishment. In the event of a period, the last day of the period')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}periodicalSettlement uses Python identifier periodicalSettlement
    __periodicalSettlement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'periodicalSettlement'), 'periodicalSettlement', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0dataperiodicalSettlement', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1071, 3), )

    
    periodicalSettlement = property(__periodicalSettlement.value, __periodicalSettlement.set, None, 'Annak jelzése, ha a felek a termékértékesítés, szolgáltatás nyújtás során időszakonkénti elszámolásban vagy fizetésben állapodnak meg, vagy a termékértékesítés, szolgáltatás nyújtás ellenértékét meghatározott időpontra állapítják meg.Indicates where by agreement of the parties it gives rise to successive statements of account or successive payments relating to the supply of goods, or the supply of services, or if the consideration agreed upon for such goods and/or services applies to specific periods.')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}smallBusinessIndicator uses Python identifier smallBusinessIndicator
    __smallBusinessIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'smallBusinessIndicator'), 'smallBusinessIndicator', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datasmallBusinessIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1077, 3), )

    
    smallBusinessIndicator = property(__smallBusinessIndicator.value, __smallBusinessIndicator.set, None, 'Kisadózó jelzéseMarking of low tax-bracket enterprise')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}currencyCode uses Python identifier currencyCode
    __currencyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currencyCode'), 'currencyCode', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datacurrencyCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1083, 3), )

    
    currencyCode = property(__currencyCode.value, __currencyCode.set, None, 'A számla pénzneme az ISO 4217 szabvány szerintISO 4217 currency code on the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}exchangeRate uses Python identifier exchangeRate
    __exchangeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exchangeRate'), 'exchangeRate', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0dataexchangeRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1089, 3), )

    
    exchangeRate = property(__exchangeRate.value, __exchangeRate.set, None, 'HUF-tól különböző pénznem esetén az alkalmazott árfolyam: egy egység értéke HUF-banIn case any currency is used other than HUF, the applied exchange rate should be mentioned: 1 unit of the foreign currency expressed in HUF')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}utilitySettlementIndicator uses Python identifier utilitySettlementIndicator
    __utilitySettlementIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utilitySettlementIndicator'), 'utilitySettlementIndicator', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datautilitySettlementIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1095, 3), )

    
    utilitySettlementIndicator = property(__utilitySettlementIndicator.value, __utilitySettlementIndicator.set, None, 'Közmű elszámoló számla jelölése (2013.évi CLXXXVIII törvény szerinti elszámoló számla)Marking the fact of utility settlement invoice (invoice according to Act CLXXXVIII of 2013)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}selfBillingIndicator uses Python identifier selfBillingIndicator
    __selfBillingIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'selfBillingIndicator'), 'selfBillingIndicator', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0dataselfBillingIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1101, 3), )

    
    selfBillingIndicator = property(__selfBillingIndicator.value, __selfBillingIndicator.set, None, 'Önszámlázás jelölése (önszámlázás esetén true)Marking the fact of self-billing (in the case of self-billing the value is true)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}paymentMethod uses Python identifier paymentMethod
    __paymentMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), 'paymentMethod', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datapaymentMethod', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1107, 3), )

    
    paymentMethod = property(__paymentMethod.value, __paymentMethod.set, None, 'Fizetés módjaMethod of payment')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}paymentDate uses Python identifier paymentDate
    __paymentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentDate'), 'paymentDate', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datapaymentDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1113, 3), )

    
    paymentDate = property(__paymentDate.value, __paymentDate.set, None, 'Fizetési határidőDeadline for payment')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}cashAccountingIndicator uses Python identifier cashAccountingIndicator
    __cashAccountingIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cashAccountingIndicator'), 'cashAccountingIndicator', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datacashAccountingIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1119, 3), )

    
    cashAccountingIndicator = property(__cashAccountingIndicator.value, __cashAccountingIndicator.set, None, 'Pénzforgalmi elszámolás jelölése, ha az szerepel a számlán - ÁFA tv. 169. § h). Értéke true pénzforgalmi elszámolás eseténMarking the fact of cash accounting if this is indicated on the invoice - section 169 (h) of the VAT law. The value is true in case of cash accounting')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceAppearance uses Python identifier invoiceAppearance
    __invoiceAppearance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance'), 'invoiceAppearance', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0datainvoiceAppearance', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1125, 3), )

    
    invoiceAppearance = property(__invoiceAppearance.value, __invoiceAppearance.set, None, 'A számla vagy módosító okirat megjelenési formájaForm of appearance of the invoice or modification document')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}conventionalInvoiceInfo uses Python identifier conventionalInvoiceInfo
    __conventionalInvoiceInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conventionalInvoiceInfo'), 'conventionalInvoiceInfo', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0dataconventionalInvoiceInfo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1131, 3), )

    
    conventionalInvoiceInfo = property(__conventionalInvoiceInfo.value, __conventionalInvoiceInfo.set, None, 'A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatokOther conventionally named data to assist in invoice processing')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}additionalInvoiceData uses Python identifier additionalInvoiceData
    __additionalInvoiceData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalInvoiceData'), 'additionalInvoiceData', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDetailType_httpschemas_nav_gov_huOSA3_0dataadditionalInvoiceData', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1137, 3), )

    
    additionalInvoiceData = property(__additionalInvoiceData.value, __additionalInvoiceData.set, None, 'A számlára vonatkozó egyéb adatOther data in relation to the invoice')

    _ElementMap.update({
        __invoiceCategory.name() : __invoiceCategory,
        __invoiceDeliveryDate.name() : __invoiceDeliveryDate,
        __invoiceDeliveryPeriodStart.name() : __invoiceDeliveryPeriodStart,
        __invoiceDeliveryPeriodEnd.name() : __invoiceDeliveryPeriodEnd,
        __invoiceAccountingDeliveryDate.name() : __invoiceAccountingDeliveryDate,
        __periodicalSettlement.name() : __periodicalSettlement,
        __smallBusinessIndicator.name() : __smallBusinessIndicator,
        __currencyCode.name() : __currencyCode,
        __exchangeRate.name() : __exchangeRate,
        __utilitySettlementIndicator.name() : __utilitySettlementIndicator,
        __selfBillingIndicator.name() : __selfBillingIndicator,
        __paymentMethod.name() : __paymentMethod,
        __paymentDate.name() : __paymentDate,
        __cashAccountingIndicator.name() : __cashAccountingIndicator,
        __invoiceAppearance.name() : __invoiceAppearance,
        __conventionalInvoiceInfo.name() : __conventionalInvoiceInfo,
        __additionalInvoiceData.name() : __additionalInvoiceData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceDetailType = InvoiceDetailType
Namespace.addCategoryObject('typeBinding', 'InvoiceDetailType', InvoiceDetailType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceDataType with content type ELEMENT_ONLY
class InvoiceDataType (pyxb.binding.basis.complexTypeDefinition):
    """A számla adatszolgáltatás adataiInvoice exchange data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1145, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNumber uses Python identifier invoiceNumber
    __invoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), 'invoiceNumber', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDataType_httpschemas_nav_gov_huOSA3_0datainvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1151, 3), )

    
    invoiceNumber = property(__invoiceNumber.value, __invoiceNumber.set, None, 'Számla vagy módosító okirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pontSequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceIssueDate uses Python identifier invoiceIssueDate
    __invoiceIssueDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate'), 'invoiceIssueDate', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDataType_httpschemas_nav_gov_huOSA3_0datainvoiceIssueDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1157, 3), )

    
    invoiceIssueDate = property(__invoiceIssueDate.value, __invoiceIssueDate.set, None, 'Számla vagy módosító okirat kelte - ÁFA tv. 169. § a), ÁFA tv. 170. § (1) bek. a)Date of issue of the invoice or the modification document - section 169 (a) of the VAT law, section 170 (1) a) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}completenessIndicator uses Python identifier completenessIndicator
    __completenessIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'completenessIndicator'), 'completenessIndicator', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDataType_httpschemas_nav_gov_huOSA3_0datacompletenessIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1163, 3), )

    
    completenessIndicator = property(__completenessIndicator.value, __completenessIndicator.set, None, 'Jelöli, ha az adatszolgáltatás maga a számla (a számlán nem szerepel több adat)Indicates whether the data exchange is identical with the invoice (the invoice does not contain any more data)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceMain uses Python identifier invoiceMain
    __invoiceMain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceMain'), 'invoiceMain', '__httpschemas_nav_gov_huOSA3_0data_InvoiceDataType_httpschemas_nav_gov_huOSA3_0datainvoiceMain', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1169, 3), )

    
    invoiceMain = property(__invoiceMain.value, __invoiceMain.set, None, 'Számlaadatok leírására szolgáló közös típusA common type to describe invoice information')

    _ElementMap.update({
        __invoiceNumber.name() : __invoiceNumber,
        __invoiceIssueDate.name() : __invoiceIssueDate,
        __completenessIndicator.name() : __completenessIndicator,
        __invoiceMain.name() : __invoiceMain
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceDataType = InvoiceDataType
Namespace.addCategoryObject('typeBinding', 'InvoiceDataType', InvoiceDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceHeadType with content type ELEMENT_ONLY
class InvoiceHeadType (pyxb.binding.basis.complexTypeDefinition):
    """Számla fejléc adataiData in header of invoice"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceHeadType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1177, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}supplierInfo uses Python identifier supplierInfo
    __supplierInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierInfo'), 'supplierInfo', '__httpschemas_nav_gov_huOSA3_0data_InvoiceHeadType_httpschemas_nav_gov_huOSA3_0datasupplierInfo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1183, 3), )

    
    supplierInfo = property(__supplierInfo.value, __supplierInfo.set, None, 'Számla kibocsátó (eladó) adataiData related to the issuer of the invoice (supplier)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerInfo uses Python identifier customerInfo
    __customerInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerInfo'), 'customerInfo', '__httpschemas_nav_gov_huOSA3_0data_InvoiceHeadType_httpschemas_nav_gov_huOSA3_0datacustomerInfo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1189, 3), )

    
    customerInfo = property(__customerInfo.value, __customerInfo.set, None, 'Vevő adataiData related to the customer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeInfo uses Python identifier fiscalRepresentativeInfo
    __fiscalRepresentativeInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeInfo'), 'fiscalRepresentativeInfo', '__httpschemas_nav_gov_huOSA3_0data_InvoiceHeadType_httpschemas_nav_gov_huOSA3_0datafiscalRepresentativeInfo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1195, 3), )

    
    fiscalRepresentativeInfo = property(__fiscalRepresentativeInfo.value, __fiscalRepresentativeInfo.set, None, 'Pénzügyi képviselő adataiData related to the fiscal representative')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceDetail uses Python identifier invoiceDetail
    __invoiceDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDetail'), 'invoiceDetail', '__httpschemas_nav_gov_huOSA3_0data_InvoiceHeadType_httpschemas_nav_gov_huOSA3_0datainvoiceDetail', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1201, 3), )

    
    invoiceDetail = property(__invoiceDetail.value, __invoiceDetail.set, None, 'Számla részletező adatokInvoice detail adata')

    _ElementMap.update({
        __supplierInfo.name() : __supplierInfo,
        __customerInfo.name() : __customerInfo,
        __fiscalRepresentativeInfo.name() : __fiscalRepresentativeInfo,
        __invoiceDetail.name() : __invoiceDetail
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceHeadType = InvoiceHeadType
Namespace.addCategoryObject('typeBinding', 'InvoiceHeadType', InvoiceHeadType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceMainType with content type ELEMENT_ONLY
class InvoiceMainType (pyxb.binding.basis.complexTypeDefinition):
    """Számlaadatok leírására szolgáló közös típusA common type to describe invoice information"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceMainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1209, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoice uses Python identifier invoice
    __invoice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoice'), 'invoice', '__httpschemas_nav_gov_huOSA3_0data_InvoiceMainType_httpschemas_nav_gov_huOSA3_0datainvoice', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1215, 3), )

    
    invoice = property(__invoice.value, __invoice.set, None, 'Egy számla vagy módosító okirat adataiData of a single invoice or modification document')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}batchInvoice uses Python identifier batchInvoice
    __batchInvoice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batchInvoice'), 'batchInvoice', '__httpschemas_nav_gov_huOSA3_0data_InvoiceMainType_httpschemas_nav_gov_huOSA3_0databatchInvoice', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1221, 3), )

    
    batchInvoice = property(__batchInvoice.value, __batchInvoice.set, None, 'Kötegelt módosító okirat adataiData of a batch of modification documents')

    _ElementMap.update({
        __invoice.name() : __invoice,
        __batchInvoice.name() : __batchInvoice
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceMainType = InvoiceMainType
Namespace.addCategoryObject('typeBinding', 'InvoiceMainType', InvoiceMainType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceReferenceType with content type ELEMENT_ONLY
class InvoiceReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """A módosítás vagy érvénytelenítés hivatkozási adataiModification or cancellation reference data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1229, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}originalInvoiceNumber uses Python identifier originalInvoiceNumber
    __originalInvoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), 'originalInvoiceNumber', '__httpschemas_nav_gov_huOSA3_0data_InvoiceReferenceType_httpschemas_nav_gov_huOSA3_0dataoriginalInvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1235, 3), )

    
    originalInvoiceNumber = property(__originalInvoiceNumber.value, __originalInvoiceNumber.set, None, 'Az eredeti számla sorszáma, melyre a módosítás vonatkozik  - ÁFA tv. 170. § (1) c)Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}modifyWithoutMaster uses Python identifier modifyWithoutMaster
    __modifyWithoutMaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modifyWithoutMaster'), 'modifyWithoutMaster', '__httpschemas_nav_gov_huOSA3_0data_InvoiceReferenceType_httpschemas_nav_gov_huOSA3_0datamodifyWithoutMaster', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1241, 3), )

    
    modifyWithoutMaster = property(__modifyWithoutMaster.value, __modifyWithoutMaster.set, None, 'Annak jelzése, hogy a módosítás olyan alapszámlára hivatkozik, amelyről nem történt és nem is fog történni adatszolgáltatásIndicates whether the modification references to an original invoice which is not and will not be exchanged')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}modificationIndex uses Python identifier modificationIndex
    __modificationIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex'), 'modificationIndex', '__httpschemas_nav_gov_huOSA3_0data_InvoiceReferenceType_httpschemas_nav_gov_huOSA3_0datamodificationIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1247, 3), )

    
    modificationIndex = property(__modificationIndex.value, __modificationIndex.set, None, 'A számlára vonatkozó módosító okirat egyedi sorszámaThe unique sequence number referring to the original invoice')

    _ElementMap.update({
        __originalInvoiceNumber.name() : __originalInvoiceNumber,
        __modifyWithoutMaster.name() : __modifyWithoutMaster,
        __modificationIndex.name() : __modificationIndex
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceReferenceType = InvoiceReferenceType
Namespace.addCategoryObject('typeBinding', 'InvoiceReferenceType', InvoiceReferenceType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceType with content type ELEMENT_ONLY
class InvoiceType (pyxb.binding.basis.complexTypeDefinition):
    """Egy számla vagy módosító okirat adataiData of a single invoice or modification document"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1255, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceReference uses Python identifier invoiceReference
    __invoiceReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceReference'), 'invoiceReference', '__httpschemas_nav_gov_huOSA3_0data_InvoiceType_httpschemas_nav_gov_huOSA3_0datainvoiceReference', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1261, 3), )

    
    invoiceReference = property(__invoiceReference.value, __invoiceReference.set, None, 'A módosítás vagy érvénytelenítés adataiModification or cancellation data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceHead uses Python identifier invoiceHead
    __invoiceHead = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceHead'), 'invoiceHead', '__httpschemas_nav_gov_huOSA3_0data_InvoiceType_httpschemas_nav_gov_huOSA3_0datainvoiceHead', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1267, 3), )

    
    invoiceHead = property(__invoiceHead.value, __invoiceHead.set, None, 'A számla egészét jellemző adatokData concerning the whole invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceLines uses Python identifier invoiceLines
    __invoiceLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceLines'), 'invoiceLines', '__httpschemas_nav_gov_huOSA3_0data_InvoiceType_httpschemas_nav_gov_huOSA3_0datainvoiceLines', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1273, 3), )

    
    invoiceLines = property(__invoiceLines.value, __invoiceLines.set, None, 'A számlán szereplő tételek adataiProduct/service data appearing on the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeSummary uses Python identifier productFeeSummary
    __productFeeSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeSummary'), 'productFeeSummary', '__httpschemas_nav_gov_huOSA3_0data_InvoiceType_httpschemas_nav_gov_huOSA3_0dataproductFeeSummary', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1279, 3), )

    
    productFeeSummary = property(__productFeeSummary.value, __productFeeSummary.set, None, 'Termékdíjjal kapcsolatos összesítő adatokSummary data of product charges')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceSummary uses Python identifier invoiceSummary
    __invoiceSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceSummary'), 'invoiceSummary', '__httpschemas_nav_gov_huOSA3_0data_InvoiceType_httpschemas_nav_gov_huOSA3_0datainvoiceSummary', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1285, 3), )

    
    invoiceSummary = property(__invoiceSummary.value, __invoiceSummary.set, None, 'Az ÁFA törvény szerinti összesítő adatokSummary data according to VAT law')

    _ElementMap.update({
        __invoiceReference.name() : __invoiceReference,
        __invoiceHead.name() : __invoiceHead,
        __invoiceLines.name() : __invoiceLines,
        __productFeeSummary.name() : __productFeeSummary,
        __invoiceSummary.name() : __invoiceSummary
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceType = InvoiceType
Namespace.addCategoryObject('typeBinding', 'InvoiceType', InvoiceType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ItemNumbersType with content type ELEMENT_ONLY
class ItemNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """CikkszámokItem numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ItemNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1293, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}itemNumber uses Python identifier itemNumber
    __itemNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemNumber'), 'itemNumber', '__httpschemas_nav_gov_huOSA3_0data_ItemNumbersType_httpschemas_nav_gov_huOSA3_0dataitemNumber', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1299, 3), )

    
    itemNumber = property(__itemNumber.value, __itemNumber.set, None, 'CikkszámItem number')

    _ElementMap.update({
        __itemNumber.name() : __itemNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ItemNumbersType = ItemNumbersType
Namespace.addCategoryObject('typeBinding', 'ItemNumbersType', ItemNumbersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LineAmountsNormalType with content type ELEMENT_ONLY
class LineAmountsNormalType (pyxb.binding.basis.complexTypeDefinition):
    """Normál vagy gyűjtő számla esetén kitöltendő tétel érték adatokItem value data to be completed in case of normal or aggregate invoice"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineAmountsNormalType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1307, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineNetAmountData uses Python identifier lineNetAmountData
    __lineNetAmountData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmountData'), 'lineNetAmountData', '__httpschemas_nav_gov_huOSA3_0data_LineAmountsNormalType_httpschemas_nav_gov_huOSA3_0datalineNetAmountData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1313, 3), )

    
    lineNetAmountData = property(__lineNetAmountData.value, __lineNetAmountData.set, None, 'Tétel nettó adatokLine net data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineVatRate uses Python identifier lineVatRate
    __lineVatRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineVatRate'), 'lineVatRate', '__httpschemas_nav_gov_huOSA3_0data_LineAmountsNormalType_httpschemas_nav_gov_huOSA3_0datalineVatRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1319, 3), )

    
    lineVatRate = property(__lineVatRate.value, __lineVatRate.set, None, 'Adómérték vagy adómentesség jelöléseTax rate or tax exemption marking')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineVatData uses Python identifier lineVatData
    __lineVatData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineVatData'), 'lineVatData', '__httpschemas_nav_gov_huOSA3_0data_LineAmountsNormalType_httpschemas_nav_gov_huOSA3_0datalineVatData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1325, 3), )

    
    lineVatData = property(__lineVatData.value, __lineVatData.set, None, 'Tétel ÁFA adatokLine VAT data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountData uses Python identifier lineGrossAmountData
    __lineGrossAmountData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountData'), 'lineGrossAmountData', '__httpschemas_nav_gov_huOSA3_0data_LineAmountsNormalType_httpschemas_nav_gov_huOSA3_0datalineGrossAmountData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1331, 3), )

    
    lineGrossAmountData = property(__lineGrossAmountData.value, __lineGrossAmountData.set, None, 'Tétel bruttó adatokLine gross data')

    _ElementMap.update({
        __lineNetAmountData.name() : __lineNetAmountData,
        __lineVatRate.name() : __lineVatRate,
        __lineVatData.name() : __lineVatData,
        __lineGrossAmountData.name() : __lineGrossAmountData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LineAmountsNormalType = LineAmountsNormalType
Namespace.addCategoryObject('typeBinding', 'LineAmountsNormalType', LineAmountsNormalType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LineAmountsSimplifiedType with content type ELEMENT_ONLY
class LineAmountsSimplifiedType (pyxb.binding.basis.complexTypeDefinition):
    """Egyszerűsített számla esetén kitöltendő tétel érték adatokItem value data to be completed in case of simplified invoice"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineAmountsSimplifiedType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1339, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineVatRate uses Python identifier lineVatRate
    __lineVatRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineVatRate'), 'lineVatRate', '__httpschemas_nav_gov_huOSA3_0data_LineAmountsSimplifiedType_httpschemas_nav_gov_huOSA3_0datalineVatRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1345, 3), )

    
    lineVatRate = property(__lineVatRate.value, __lineVatRate.set, None, 'Adómérték vagy adómentesség jelöléseTax rate or tax exemption marking')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountSimplified uses Python identifier lineGrossAmountSimplified
    __lineGrossAmountSimplified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountSimplified'), 'lineGrossAmountSimplified', '__httpschemas_nav_gov_huOSA3_0data_LineAmountsSimplifiedType_httpschemas_nav_gov_huOSA3_0datalineGrossAmountSimplified', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1351, 3), )

    
    lineGrossAmountSimplified = property(__lineGrossAmountSimplified.value, __lineGrossAmountSimplified.set, None, 'Tétel bruttó értéke a számla pénznemébenGross amount of the item expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountSimplifiedHUF uses Python identifier lineGrossAmountSimplifiedHUF
    __lineGrossAmountSimplifiedHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountSimplifiedHUF'), 'lineGrossAmountSimplifiedHUF', '__httpschemas_nav_gov_huOSA3_0data_LineAmountsSimplifiedType_httpschemas_nav_gov_huOSA3_0datalineGrossAmountSimplifiedHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1357, 3), )

    
    lineGrossAmountSimplifiedHUF = property(__lineGrossAmountSimplifiedHUF.value, __lineGrossAmountSimplifiedHUF.set, None, 'Tétel bruttó értéke forintbanGross amount of the item expressed in HUF')

    _ElementMap.update({
        __lineVatRate.name() : __lineVatRate,
        __lineGrossAmountSimplified.name() : __lineGrossAmountSimplified,
        __lineGrossAmountSimplifiedHUF.name() : __lineGrossAmountSimplifiedHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LineAmountsSimplifiedType = LineAmountsSimplifiedType
Namespace.addCategoryObject('typeBinding', 'LineAmountsSimplifiedType', LineAmountsSimplifiedType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LineGrossAmountDataType with content type ELEMENT_ONLY
class LineGrossAmountDataType (pyxb.binding.basis.complexTypeDefinition):
    """Tétel bruttó adatokLine gross data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineGrossAmountDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1365, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountNormal uses Python identifier lineGrossAmountNormal
    __lineGrossAmountNormal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountNormal'), 'lineGrossAmountNormal', '__httpschemas_nav_gov_huOSA3_0data_LineGrossAmountDataType_httpschemas_nav_gov_huOSA3_0datalineGrossAmountNormal', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1371, 3), )

    
    lineGrossAmountNormal = property(__lineGrossAmountNormal.value, __lineGrossAmountNormal.set, None, 'Tétel bruttó értéke a számla pénznemében. ÁFA tartalmú különbözeti adózás esetén az ellenérték.Gross amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration expressed in the currency of the invoice.')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountNormalHUF uses Python identifier lineGrossAmountNormalHUF
    __lineGrossAmountNormalHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountNormalHUF'), 'lineGrossAmountNormalHUF', '__httpschemas_nav_gov_huOSA3_0data_LineGrossAmountDataType_httpschemas_nav_gov_huOSA3_0datalineGrossAmountNormalHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1377, 3), )

    
    lineGrossAmountNormalHUF = property(__lineGrossAmountNormalHUF.value, __lineGrossAmountNormalHUF.set, None, 'Tétel bruttó értéke forintbanGross amount of the item expressed in HUF')

    _ElementMap.update({
        __lineGrossAmountNormal.name() : __lineGrossAmountNormal,
        __lineGrossAmountNormalHUF.name() : __lineGrossAmountNormalHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LineGrossAmountDataType = LineGrossAmountDataType
Namespace.addCategoryObject('typeBinding', 'LineGrossAmountDataType', LineGrossAmountDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LineModificationReferenceType with content type ELEMENT_ONLY
class LineModificationReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Módosításról történő adatszolgáltatás esetén a tételsor módosítás jellegének jelöléseMarking the goal of modification of the line (in the case of data supply about changes/updates only)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineModificationReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1385, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineNumberReference uses Python identifier lineNumberReference
    __lineNumberReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNumberReference'), 'lineNumberReference', '__httpschemas_nav_gov_huOSA3_0data_LineModificationReferenceType_httpschemas_nav_gov_huOSA3_0datalineNumberReference', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1391, 3), )

    
    lineNumberReference = property(__lineNumberReference.value, __lineNumberReference.set, None, 'Az eredeti számla módosítással érintett tételének sorszáma (lineNumber). Új tétel létrehozása esetén az új tétel sorszáma, a meglévő tételsorok számozásának folytatásakéntLine number of the original invoice, which the modification occurs with. In case of create operation the tag shall contain the new line number, as a sequential increment of the the existing lines set')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineOperation uses Python identifier lineOperation
    __lineOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineOperation'), 'lineOperation', '__httpschemas_nav_gov_huOSA3_0data_LineModificationReferenceType_httpschemas_nav_gov_huOSA3_0datalineOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1397, 3), )

    
    lineOperation = property(__lineOperation.value, __lineOperation.set, None, 'A számlatétel módosításának jellegeLine modification type')

    _ElementMap.update({
        __lineNumberReference.name() : __lineNumberReference,
        __lineOperation.name() : __lineOperation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LineModificationReferenceType = LineModificationReferenceType
Namespace.addCategoryObject('typeBinding', 'LineModificationReferenceType', LineModificationReferenceType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LineNetAmountDataType with content type ELEMENT_ONLY
class LineNetAmountDataType (pyxb.binding.basis.complexTypeDefinition):
    """Tétel nettó adatokLine net data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineNetAmountDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1405, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineNetAmount uses Python identifier lineNetAmount
    __lineNetAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmount'), 'lineNetAmount', '__httpschemas_nav_gov_huOSA3_0data_LineNetAmountDataType_httpschemas_nav_gov_huOSA3_0datalineNetAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1411, 3), )

    
    lineNetAmount = property(__lineNetAmount.value, __lineNetAmount.set, None, 'Tétel nettó összege a számla pénznemében. ÁFA tartalmú különbözeti adózás esetén az ellenérték áfa összegével csökkentett értéke a számla pénznemében.Net amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration reduced with the amount of VAT, expressed in the currency of the invoice.')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineNetAmountHUF uses Python identifier lineNetAmountHUF
    __lineNetAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmountHUF'), 'lineNetAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_LineNetAmountDataType_httpschemas_nav_gov_huOSA3_0datalineNetAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1417, 3), )

    
    lineNetAmountHUF = property(__lineNetAmountHUF.value, __lineNetAmountHUF.set, None, 'Tétel nettó összege forintban. ÁFA tartalmú különbözeti adózás esetén az ellenérték áfa összegével csökkentett értéke forintban.Net amount of the item expressed in HUF. Net amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration reduced with the amount of VAT, expressed in HUF.')

    _ElementMap.update({
        __lineNetAmount.name() : __lineNetAmount,
        __lineNetAmountHUF.name() : __lineNetAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LineNetAmountDataType = LineNetAmountDataType
Namespace.addCategoryObject('typeBinding', 'LineNetAmountDataType', LineNetAmountDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LinesType with content type ELEMENT_ONLY
class LinesType (pyxb.binding.basis.complexTypeDefinition):
    """Termék/szolgáltatás tételekProduct / service items"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1425, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}mergedItemIndicator uses Python identifier mergedItemIndicator
    __mergedItemIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mergedItemIndicator'), 'mergedItemIndicator', '__httpschemas_nav_gov_huOSA3_0data_LinesType_httpschemas_nav_gov_huOSA3_0datamergedItemIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1431, 3), )

    
    mergedItemIndicator = property(__mergedItemIndicator.value, __mergedItemIndicator.set, None, 'Jelöli, ha az adatszolgáltatás méretcsökkentés miatt összevont soradatokat tartalmazIndicates whether the data exchange contains merged line data due to size reduction')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'line'), 'line', '__httpschemas_nav_gov_huOSA3_0data_LinesType_httpschemas_nav_gov_huOSA3_0dataline', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1437, 3), )

    
    line = property(__line.value, __line.set, None, 'Termék/szolgáltatás tételProduct / service item')

    _ElementMap.update({
        __mergedItemIndicator.name() : __mergedItemIndicator,
        __line.name() : __line
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LinesType = LinesType
Namespace.addCategoryObject('typeBinding', 'LinesType', LinesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LineType with content type ELEMENT_ONLY
class LineType (pyxb.binding.basis.complexTypeDefinition):
    """A számla tételek (termék vagy szolgáltatás) adatait tartalmazó típusField type including data of invoice items (product or service)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1445, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineNumber uses Python identifier lineNumber
    __lineNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNumber'), 'lineNumber', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1451, 3), )

    
    lineNumber = property(__lineNumber.value, __lineNumber.set, None, 'A tétel sorszámaSequential number of the item')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineModificationReference uses Python identifier lineModificationReference
    __lineModificationReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineModificationReference'), 'lineModificationReference', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineModificationReference', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1457, 3), )

    
    lineModificationReference = property(__lineModificationReference.value, __lineModificationReference.set, None, 'Módosításról történő adatszolgáltatás esetén a tételsor módosítás jellegének jelöléseMarking the goal of modification of the line (in the case of data supply about changes/updates only)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}referencesToOtherLines uses Python identifier referencesToOtherLines
    __referencesToOtherLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referencesToOtherLines'), 'referencesToOtherLines', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datareferencesToOtherLines', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1463, 3), )

    
    referencesToOtherLines = property(__referencesToOtherLines.value, __referencesToOtherLines.set, None, 'Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükségesReferences to connected items if it is necessary according to VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}advanceData uses Python identifier advanceData
    __advanceData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'advanceData'), 'advanceData', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataadvanceData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1469, 3), )

    
    advanceData = property(__advanceData.value, __advanceData.set, None, 'Előleghez kapcsolódó adatokAdvance related data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productCodes uses Python identifier productCodes
    __productCodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productCodes'), 'productCodes', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataproductCodes', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1475, 3), )

    
    productCodes = property(__productCodes.value, __productCodes.set, None, 'TermékkódokProduct codes')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineExpressionIndicator uses Python identifier lineExpressionIndicator
    __lineExpressionIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineExpressionIndicator'), 'lineExpressionIndicator', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineExpressionIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1481, 3), )

    
    lineExpressionIndicator = property(__lineExpressionIndicator.value, __lineExpressionIndicator.set, None, 'Értéke true, ha a tétel mennyiségi egysége természetes mértékegységben kifejezhetőThe value is true if the unit of measure of the invoice item is expressible in natural unit')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineNatureIndicator uses Python identifier lineNatureIndicator
    __lineNatureIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNatureIndicator'), 'lineNatureIndicator', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineNatureIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1487, 3), )

    
    lineNatureIndicator = property(__lineNatureIndicator.value, __lineNatureIndicator.set, None, 'Adott tételsor termékértékesítés vagy szolgáltatás nyújtás jellegének jelzéseIndication of the nature of the supply of goods or services on a given line')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineDescription uses Python identifier lineDescription
    __lineDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineDescription'), 'lineDescription', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineDescription', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1493, 3), )

    
    lineDescription = property(__lineDescription.value, __lineDescription.set, None, 'A termék vagy szolgáltatás megnevezéseName / description of the product or service')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quantity'), 'quantity', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataquantity', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1499, 3), )

    
    quantity = property(__quantity.value, __quantity.set, None, 'MennyiségQuantity')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}unitOfMeasure uses Python identifier unitOfMeasure
    __unitOfMeasure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unitOfMeasure'), 'unitOfMeasure', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataunitOfMeasure', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1505, 3), )

    
    unitOfMeasure = property(__unitOfMeasure.value, __unitOfMeasure.set, None, 'A számlán szereplő mennyiségi egység kanonikus kifejezése az interfész specifikáció szerintCanonical representation of the unit of measure of the invoice, according to the interface specification')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}unitOfMeasureOwn uses Python identifier unitOfMeasureOwn
    __unitOfMeasureOwn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unitOfMeasureOwn'), 'unitOfMeasureOwn', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataunitOfMeasureOwn', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1511, 3), )

    
    unitOfMeasureOwn = property(__unitOfMeasureOwn.value, __unitOfMeasureOwn.set, None, 'A számlán szereplő mennyiségi egység literális kifejezéseLiteral unit of measure of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}unitPrice uses Python identifier unitPrice
    __unitPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unitPrice'), 'unitPrice', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataunitPrice', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1517, 3), )

    
    unitPrice = property(__unitPrice.value, __unitPrice.set, None, 'Egységár a számla pénznemében. Egyszerűsített számla esetén bruttó, egyéb esetben nettó egységárUnit price expressed in the currency of the invoice In the event of simplified invoices gross unit price, in other cases net unit price')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}unitPriceHUF uses Python identifier unitPriceHUF
    __unitPriceHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unitPriceHUF'), 'unitPriceHUF', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataunitPriceHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1523, 3), )

    
    unitPriceHUF = property(__unitPriceHUF.value, __unitPriceHUF.set, None, 'Egységár forintbanUnit price expressed in HUF')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineDiscountData uses Python identifier lineDiscountData
    __lineDiscountData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineDiscountData'), 'lineDiscountData', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineDiscountData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1529, 3), )

    
    lineDiscountData = property(__lineDiscountData.value, __lineDiscountData.set, None, 'A tételhez tartozó árengedmény adatokDiscount data in relation to the item')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineAmountsNormal uses Python identifier lineAmountsNormal
    __lineAmountsNormal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineAmountsNormal'), 'lineAmountsNormal', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineAmountsNormal', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1536, 4), )

    
    lineAmountsNormal = property(__lineAmountsNormal.value, __lineAmountsNormal.set, None, 'Normál (nem egyszerűsített) számla esetén (beleértve a gyűjtőszámlát) kitöltendő tétel érték adatok.Item value data to be completed in case of normal (not simplified, but including aggregated) invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineAmountsSimplified uses Python identifier lineAmountsSimplified
    __lineAmountsSimplified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineAmountsSimplified'), 'lineAmountsSimplified', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineAmountsSimplified', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1542, 4), )

    
    lineAmountsSimplified = property(__lineAmountsSimplified.value, __lineAmountsSimplified.set, None, 'Egyszerűsített számla esetén kitöltendő tétel érték adatokItem value data to be completed in case of simplified invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}intermediatedService uses Python identifier intermediatedService
    __intermediatedService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'intermediatedService'), 'intermediatedService', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataintermediatedService', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1549, 3), )

    
    intermediatedService = property(__intermediatedService.value, __intermediatedService.set, None, 'Értéke true ha a tétel közvetített szolgáltatás - Számviteli tv. 3.§ (4) 1The value is true if the item is an intermediated service - paragraph (4) 1 of the Article 3 of Accounting Act')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}aggregateInvoiceLineData uses Python identifier aggregateInvoiceLineData
    __aggregateInvoiceLineData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aggregateInvoiceLineData'), 'aggregateInvoiceLineData', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataaggregateInvoiceLineData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1555, 3), )

    
    aggregateInvoiceLineData = property(__aggregateInvoiceLineData.value, __aggregateInvoiceLineData.set, None, 'Gyűjtő számla adatokAggregate invoice data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}newTransportMean uses Python identifier newTransportMean
    __newTransportMean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'newTransportMean'), 'newTransportMean', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datanewTransportMean', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1561, 3), )

    
    newTransportMean = property(__newTransportMean.value, __newTransportMean.set, None, 'Új közlekedési eszköz értékesítés ÁFA tv. 89 § ill. 169 § o)Supply of new means of transport - section 89 § and 169 (o) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}depositIndicator uses Python identifier depositIndicator
    __depositIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'depositIndicator'), 'depositIndicator', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datadepositIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1567, 3), )

    
    depositIndicator = property(__depositIndicator.value, __depositIndicator.set, None, 'Értéke true, ha a tétel betétdíj jellegűThe value is true if the item is bottle/container deposit')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}obligatedForProductFee uses Python identifier obligatedForProductFee
    __obligatedForProductFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'obligatedForProductFee'), 'obligatedForProductFee', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataobligatedForProductFee', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1573, 3), )

    
    obligatedForProductFee = property(__obligatedForProductFee.value, __obligatedForProductFee.set, None, 'Értéke true ha a tételt termékdíj fizetési kötelezettség terheliThe value is true if the item is liable to product fee')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}GPCExcise uses Python identifier GPCExcise
    __GPCExcise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GPCExcise'), 'GPCExcise', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataGPCExcise', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1579, 3), )

    
    GPCExcise = property(__GPCExcise.value, __GPCExcise.set, None, 'Földgáz, villamos energia, szén jövedéki adója forintban - Jöt. 118. § (2)Excise duty on natural gas, electricity and coal in Hungarian forints – paragraph (2), Section 118 of the Act on Excise Duties')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}dieselOilPurchase uses Python identifier dieselOilPurchase
    __dieselOilPurchase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dieselOilPurchase'), 'dieselOilPurchase', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datadieselOilPurchase', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1585, 3), )

    
    dieselOilPurchase = property(__dieselOilPurchase.value, __dieselOilPurchase.set, None, 'Gázolaj adózottan történő beszerzésének adatai – 45/2016 (XI. 29.) NGM rendelet 75. § (1) a)Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}netaDeclaration uses Python identifier netaDeclaration
    __netaDeclaration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'netaDeclaration'), 'netaDeclaration', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datanetaDeclaration', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1591, 3), )

    
    netaDeclaration = property(__netaDeclaration.value, __netaDeclaration.set, None, 'Értéke true, ha a Neta tv-ben meghatározott adókötelezettség az adó alanyát terheli. 2011. évi CIII. tv. 3.§(2)Value is true, if the taxable person is liable for tax obligation determined in the Act on Public Health Product Tax (Neta tv.). Paragraph (2), Section 3 of the Act CIII of 2011')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeClause uses Python identifier productFeeClause
    __productFeeClause = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeClause'), 'productFeeClause', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataproductFeeClause', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1597, 3), )

    
    productFeeClause = property(__productFeeClause.value, __productFeeClause.set, None, 'A környezetvédelmi termékdíjról szóló 2011. évi LXXXV. tv. szerinti, tételre vonatkozó záradékokClauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineProductFeeContent uses Python identifier lineProductFeeContent
    __lineProductFeeContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineProductFeeContent'), 'lineProductFeeContent', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0datalineProductFeeContent', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1603, 3), )

    
    lineProductFeeContent = property(__lineProductFeeContent.value, __lineProductFeeContent.set, None, "A tétel termékdíj tartalmára vonatkozó adatokData on the content of the line's product charge")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}conventionalLineInfo uses Python identifier conventionalLineInfo
    __conventionalLineInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conventionalLineInfo'), 'conventionalLineInfo', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataconventionalLineInfo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1609, 3), )

    
    conventionalLineInfo = property(__conventionalLineInfo.value, __conventionalLineInfo.set, None, 'A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatokOther conventionally named data to assist in invoice processing')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}additionalLineData uses Python identifier additionalLineData
    __additionalLineData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalLineData'), 'additionalLineData', '__httpschemas_nav_gov_huOSA3_0data_LineType_httpschemas_nav_gov_huOSA3_0dataadditionalLineData', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1615, 3), )

    
    additionalLineData = property(__additionalLineData.value, __additionalLineData.set, None, 'A termék/szolgáltatás tételhez kapcsolódó, további adatOther data in relation to the product / service item')

    _ElementMap.update({
        __lineNumber.name() : __lineNumber,
        __lineModificationReference.name() : __lineModificationReference,
        __referencesToOtherLines.name() : __referencesToOtherLines,
        __advanceData.name() : __advanceData,
        __productCodes.name() : __productCodes,
        __lineExpressionIndicator.name() : __lineExpressionIndicator,
        __lineNatureIndicator.name() : __lineNatureIndicator,
        __lineDescription.name() : __lineDescription,
        __quantity.name() : __quantity,
        __unitOfMeasure.name() : __unitOfMeasure,
        __unitOfMeasureOwn.name() : __unitOfMeasureOwn,
        __unitPrice.name() : __unitPrice,
        __unitPriceHUF.name() : __unitPriceHUF,
        __lineDiscountData.name() : __lineDiscountData,
        __lineAmountsNormal.name() : __lineAmountsNormal,
        __lineAmountsSimplified.name() : __lineAmountsSimplified,
        __intermediatedService.name() : __intermediatedService,
        __aggregateInvoiceLineData.name() : __aggregateInvoiceLineData,
        __newTransportMean.name() : __newTransportMean,
        __depositIndicator.name() : __depositIndicator,
        __obligatedForProductFee.name() : __obligatedForProductFee,
        __GPCExcise.name() : __GPCExcise,
        __dieselOilPurchase.name() : __dieselOilPurchase,
        __netaDeclaration.name() : __netaDeclaration,
        __productFeeClause.name() : __productFeeClause,
        __lineProductFeeContent.name() : __lineProductFeeContent,
        __conventionalLineInfo.name() : __conventionalLineInfo,
        __additionalLineData.name() : __additionalLineData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LineType = LineType
Namespace.addCategoryObject('typeBinding', 'LineType', LineType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}LineVatDataType with content type ELEMENT_ONLY
class LineVatDataType (pyxb.binding.basis.complexTypeDefinition):
    """Tétel ÁFA adatokLine VAT data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineVatDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1623, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineVatAmount uses Python identifier lineVatAmount
    __lineVatAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineVatAmount'), 'lineVatAmount', '__httpschemas_nav_gov_huOSA3_0data_LineVatDataType_httpschemas_nav_gov_huOSA3_0datalineVatAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1629, 3), )

    
    lineVatAmount = property(__lineVatAmount.value, __lineVatAmount.set, None, 'Tétel ÁFA összege a számla pénznemébenVAT amount of the item expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}lineVatAmountHUF uses Python identifier lineVatAmountHUF
    __lineVatAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineVatAmountHUF'), 'lineVatAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_LineVatDataType_httpschemas_nav_gov_huOSA3_0datalineVatAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1635, 3), )

    
    lineVatAmountHUF = property(__lineVatAmountHUF.value, __lineVatAmountHUF.set, None, 'Tétel ÁFA összege forintbanVAT amount of the item expressed in HUF')

    _ElementMap.update({
        __lineVatAmount.name() : __lineVatAmount,
        __lineVatAmountHUF.name() : __lineVatAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LineVatDataType = LineVatDataType
Namespace.addCategoryObject('typeBinding', 'LineVatDataType', LineVatDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}MaterialNumbersType with content type ELEMENT_ONLY
class MaterialNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """AnyagszámokMaterial numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1643, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}materialNumber uses Python identifier materialNumber
    __materialNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'materialNumber'), 'materialNumber', '__httpschemas_nav_gov_huOSA3_0data_MaterialNumbersType_httpschemas_nav_gov_huOSA3_0datamaterialNumber', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1649, 3), )

    
    materialNumber = property(__materialNumber.value, __materialNumber.set, None, 'AnyagszámMaterial number')

    _ElementMap.update({
        __materialNumber.name() : __materialNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MaterialNumbersType = MaterialNumbersType
Namespace.addCategoryObject('typeBinding', 'MaterialNumbersType', MaterialNumbersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}NewTransportMeanType with content type ELEMENT_ONLY
class NewTransportMeanType (pyxb.binding.basis.complexTypeDefinition):
    """Új közlekedési eszköz értékesítés ÁFA tv. 89 § ill. 169 § o)Supply of new means of transport - section 89 § and 169 (o) of the VAT law"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NewTransportMeanType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1657, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}brand uses Python identifier brand
    __brand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'brand'), 'brand', '__httpschemas_nav_gov_huOSA3_0data_NewTransportMeanType_httpschemas_nav_gov_huOSA3_0databrand', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1663, 3), )

    
    brand = property(__brand.value, __brand.set, None, 'Gyártmány/típusProduct / type')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}serialNum uses Python identifier serialNum
    __serialNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serialNum'), 'serialNum', '__httpschemas_nav_gov_huOSA3_0data_NewTransportMeanType_httpschemas_nav_gov_huOSA3_0dataserialNum', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1669, 3), )

    
    serialNum = property(__serialNum.value, __serialNum.set, None, 'Alvázszám/gyári szám/Gyártási számChassis number / serial number / product number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}engineNum uses Python identifier engineNum
    __engineNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'engineNum'), 'engineNum', '__httpschemas_nav_gov_huOSA3_0data_NewTransportMeanType_httpschemas_nav_gov_huOSA3_0dataengineNum', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1675, 3), )

    
    engineNum = property(__engineNum.value, __engineNum.set, None, 'MotorszámEngine number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}firstEntryIntoService uses Python identifier firstEntryIntoService
    __firstEntryIntoService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstEntryIntoService'), 'firstEntryIntoService', '__httpschemas_nav_gov_huOSA3_0data_NewTransportMeanType_httpschemas_nav_gov_huOSA3_0datafirstEntryIntoService', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1681, 3), )

    
    firstEntryIntoService = property(__firstEntryIntoService.value, __firstEntryIntoService.set, None, 'Első forgalomba helyezés időpontjaFirst entry into service')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vehicle uses Python identifier vehicle
    __vehicle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vehicle'), 'vehicle', '__httpschemas_nav_gov_huOSA3_0data_NewTransportMeanType_httpschemas_nav_gov_huOSA3_0datavehicle', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1688, 4), )

    
    vehicle = property(__vehicle.value, __vehicle.set, None, 'Szárazföldi közlekedési eszköz további adataiOther data in relation to motorised land vehicle')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vessel uses Python identifier vessel
    __vessel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vessel'), 'vessel', '__httpschemas_nav_gov_huOSA3_0data_NewTransportMeanType_httpschemas_nav_gov_huOSA3_0datavessel', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1694, 4), )

    
    vessel = property(__vessel.value, __vessel.set, None, 'Vízi jármű adataiData of vessel')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}aircraft uses Python identifier aircraft
    __aircraft = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aircraft'), 'aircraft', '__httpschemas_nav_gov_huOSA3_0data_NewTransportMeanType_httpschemas_nav_gov_huOSA3_0dataaircraft', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1700, 4), )

    
    aircraft = property(__aircraft.value, __aircraft.set, None, 'Légi közlekedési eszközAircraft')

    _ElementMap.update({
        __brand.name() : __brand,
        __serialNum.name() : __serialNum,
        __engineNum.name() : __engineNum,
        __firstEntryIntoService.name() : __firstEntryIntoService,
        __vehicle.name() : __vehicle,
        __vessel.name() : __vessel,
        __aircraft.name() : __aircraft
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NewTransportMeanType = NewTransportMeanType
Namespace.addCategoryObject('typeBinding', 'NewTransportMeanType', NewTransportMeanType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}OrderNumbersType with content type ELEMENT_ONLY
class OrderNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """MegrendelésszámokOrder numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1709, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}orderNumber uses Python identifier orderNumber
    __orderNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderNumber'), 'orderNumber', '__httpschemas_nav_gov_huOSA3_0data_OrderNumbersType_httpschemas_nav_gov_huOSA3_0dataorderNumber', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1715, 3), )

    
    orderNumber = property(__orderNumber.value, __orderNumber.set, None, 'MegrendelésszámOrder number')

    _ElementMap.update({
        __orderNumber.name() : __orderNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderNumbersType = OrderNumbersType
Namespace.addCategoryObject('typeBinding', 'OrderNumbersType', OrderNumbersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}PaymentEvidenceDocumentDataType with content type ELEMENT_ONLY
class PaymentEvidenceDocumentDataType (pyxb.binding.basis.complexTypeDefinition):
    """A termékdíj bevallását igazoló dokumentum adatai a 2011. évi LXXXV. tv. 13. § (3) szerint és a 25. § (3) szerintData of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentEvidenceDocumentDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1723, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}evidenceDocumentNo uses Python identifier evidenceDocumentNo
    __evidenceDocumentNo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'evidenceDocumentNo'), 'evidenceDocumentNo', '__httpschemas_nav_gov_huOSA3_0data_PaymentEvidenceDocumentDataType_httpschemas_nav_gov_huOSA3_0dataevidenceDocumentNo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1729, 3), )

    
    evidenceDocumentNo = property(__evidenceDocumentNo.value, __evidenceDocumentNo.set, None, 'Számla sorszáma vagy egyéb okirat azonosító számaSequential number of the invoice, or other document considered as such')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}evidenceDocumentDate uses Python identifier evidenceDocumentDate
    __evidenceDocumentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'evidenceDocumentDate'), 'evidenceDocumentDate', '__httpschemas_nav_gov_huOSA3_0data_PaymentEvidenceDocumentDataType_httpschemas_nav_gov_huOSA3_0dataevidenceDocumentDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1735, 3), )

    
    evidenceDocumentDate = property(__evidenceDocumentDate.value, __evidenceDocumentDate.set, None, 'Számla kelteDate of issue of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}obligatedName uses Python identifier obligatedName
    __obligatedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'obligatedName'), 'obligatedName', '__httpschemas_nav_gov_huOSA3_0data_PaymentEvidenceDocumentDataType_httpschemas_nav_gov_huOSA3_0dataobligatedName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1741, 3), )

    
    obligatedName = property(__obligatedName.value, __obligatedName.set, None, 'Kötelezett neveName of obligator')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}obligatedAddress uses Python identifier obligatedAddress
    __obligatedAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'obligatedAddress'), 'obligatedAddress', '__httpschemas_nav_gov_huOSA3_0data_PaymentEvidenceDocumentDataType_httpschemas_nav_gov_huOSA3_0dataobligatedAddress', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1747, 3), )

    
    obligatedAddress = property(__obligatedAddress.value, __obligatedAddress.set, None, 'Kötelezett címeAddress of obligator')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}obligatedTaxNumber uses Python identifier obligatedTaxNumber
    __obligatedTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'obligatedTaxNumber'), 'obligatedTaxNumber', '__httpschemas_nav_gov_huOSA3_0data_PaymentEvidenceDocumentDataType_httpschemas_nav_gov_huOSA3_0dataobligatedTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1753, 3), )

    
    obligatedTaxNumber = property(__obligatedTaxNumber.value, __obligatedTaxNumber.set, None, 'A kötelezett adószámaTax number of obligated')

    _ElementMap.update({
        __evidenceDocumentNo.name() : __evidenceDocumentNo,
        __evidenceDocumentDate.name() : __evidenceDocumentDate,
        __obligatedName.name() : __obligatedName,
        __obligatedAddress.name() : __obligatedAddress,
        __obligatedTaxNumber.name() : __obligatedTaxNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentEvidenceDocumentDataType = PaymentEvidenceDocumentDataType
Namespace.addCategoryObject('typeBinding', 'PaymentEvidenceDocumentDataType', PaymentEvidenceDocumentDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ProductCodesType with content type ELEMENT_ONLY
class ProductCodesType (pyxb.binding.basis.complexTypeDefinition):
    """TermékkódokProduct codes"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductCodesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1761, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productCode uses Python identifier productCode
    __productCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productCode'), 'productCode', '__httpschemas_nav_gov_huOSA3_0data_ProductCodesType_httpschemas_nav_gov_huOSA3_0dataproductCode', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1767, 3), )

    
    productCode = property(__productCode.value, __productCode.set, None, 'TermékkódProduct code')

    _ElementMap.update({
        __productCode.name() : __productCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductCodesType = ProductCodesType
Namespace.addCategoryObject('typeBinding', 'ProductCodesType', ProductCodesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ProductCodeType with content type ELEMENT_ONLY
class ProductCodeType (pyxb.binding.basis.complexTypeDefinition):
    """Különböző termék- vagy szolgáltatáskódokat tartalmazó típusField type including the different product and service codes"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1775, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productCodeCategory uses Python identifier productCodeCategory
    __productCodeCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productCodeCategory'), 'productCodeCategory', '__httpschemas_nav_gov_huOSA3_0data_ProductCodeType_httpschemas_nav_gov_huOSA3_0dataproductCodeCategory', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1781, 3), )

    
    productCodeCategory = property(__productCodeCategory.value, __productCodeCategory.set, None, 'A termékkód fajtájának (pl. VTSZ, CsK, stb.) jelöléseThe kind of product code (f. ex. VTSZ, CsK, etc.)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productCodeValue uses Python identifier productCodeValue
    __productCodeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productCodeValue'), 'productCodeValue', '__httpschemas_nav_gov_huOSA3_0data_ProductCodeType_httpschemas_nav_gov_huOSA3_0dataproductCodeValue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1788, 4), )

    
    productCodeValue = property(__productCodeValue.value, __productCodeValue.set, None, 'A termékkód értéke nem saját termékkód eseténThe value of (not own) product code')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productCodeOwnValue uses Python identifier productCodeOwnValue
    __productCodeOwnValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productCodeOwnValue'), 'productCodeOwnValue', '__httpschemas_nav_gov_huOSA3_0data_ProductCodeType_httpschemas_nav_gov_huOSA3_0dataproductCodeOwnValue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1794, 4), )

    
    productCodeOwnValue = property(__productCodeOwnValue.value, __productCodeOwnValue.set, None, 'Saját termékkód értékeOwn product code value')

    _ElementMap.update({
        __productCodeCategory.name() : __productCodeCategory,
        __productCodeValue.name() : __productCodeValue,
        __productCodeOwnValue.name() : __productCodeOwnValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductCodeType = ProductCodeType
Namespace.addCategoryObject('typeBinding', 'ProductCodeType', ProductCodeType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ProductFeeClauseType with content type ELEMENT_ONLY
class ProductFeeClauseType (pyxb.binding.basis.complexTypeDefinition):
    """A környezetvédelmi termékdíjról szóló 2011. évi LXXXV. tv. szerinti, tételre vonatkozó záradékokClauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductFeeClauseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1803, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeTakeoverData uses Python identifier productFeeTakeoverData
    __productFeeTakeoverData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeTakeoverData'), 'productFeeTakeoverData', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeClauseType_httpschemas_nav_gov_huOSA3_0dataproductFeeTakeoverData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1809, 3), )

    
    productFeeTakeoverData = property(__productFeeTakeoverData.value, __productFeeTakeoverData.set, None, 'A környezetvédelmi termékdíj kötelezettség átvállalásával kapcsolatos adatokData in connection with takeover of environmental protection product fee')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}customerDeclaration uses Python identifier customerDeclaration
    __customerDeclaration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerDeclaration'), 'customerDeclaration', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeClauseType_httpschemas_nav_gov_huOSA3_0datacustomerDeclaration', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1815, 3), )

    
    customerDeclaration = property(__customerDeclaration.value, __customerDeclaration.set, None, 'Ha az eladó a vevő nyilatkozata alapján mentesül a termékdíj megfizetése alól, akkor az érintett termékáramShould the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected')

    _ElementMap.update({
        __productFeeTakeoverData.name() : __productFeeTakeoverData,
        __customerDeclaration.name() : __customerDeclaration
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductFeeClauseType = ProductFeeClauseType
Namespace.addCategoryObject('typeBinding', 'ProductFeeClauseType', ProductFeeClauseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ProductFeeDataType with content type ELEMENT_ONLY
class ProductFeeDataType (pyxb.binding.basis.complexTypeDefinition):
    """Termékdíj adatokProduct charges data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductFeeDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1823, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeCode uses Python identifier productFeeCode
    __productFeeCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeCode'), 'productFeeCode', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeDataType_httpschemas_nav_gov_huOSA3_0dataproductFeeCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1829, 3), )

    
    productFeeCode = property(__productFeeCode.value, __productFeeCode.set, None, 'Termékdíj kód (Kt vagy Csk)Product charges code (Kt or Csk code)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeQuantity uses Python identifier productFeeQuantity
    __productFeeQuantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeQuantity'), 'productFeeQuantity', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeDataType_httpschemas_nav_gov_huOSA3_0dataproductFeeQuantity', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1835, 3), )

    
    productFeeQuantity = property(__productFeeQuantity.value, __productFeeQuantity.set, None, 'A termékdíjjal érintett termék mennyiségeQuantity of product, according to product charge')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeMeasuringUnit uses Python identifier productFeeMeasuringUnit
    __productFeeMeasuringUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeMeasuringUnit'), 'productFeeMeasuringUnit', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeDataType_httpschemas_nav_gov_huOSA3_0dataproductFeeMeasuringUnit', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1841, 3), )

    
    productFeeMeasuringUnit = property(__productFeeMeasuringUnit.value, __productFeeMeasuringUnit.set, None, 'A díjtétel egysége (kg vagy darab)Unit of the rate (kg or piece)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeRate uses Python identifier productFeeRate
    __productFeeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeRate'), 'productFeeRate', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeDataType_httpschemas_nav_gov_huOSA3_0dataproductFeeRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1847, 3), )

    
    productFeeRate = property(__productFeeRate.value, __productFeeRate.set, None, 'A termékdíj díjtétele (HUF/egység)Product fee rate (HUF/unit)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeAmount uses Python identifier productFeeAmount
    __productFeeAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeAmount'), 'productFeeAmount', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeDataType_httpschemas_nav_gov_huOSA3_0dataproductFeeAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1853, 3), )

    
    productFeeAmount = property(__productFeeAmount.value, __productFeeAmount.set, None, 'Termékdíj összege forintbanAmount in Hungarian forints of the product fee')

    _ElementMap.update({
        __productFeeCode.name() : __productFeeCode,
        __productFeeQuantity.name() : __productFeeQuantity,
        __productFeeMeasuringUnit.name() : __productFeeMeasuringUnit,
        __productFeeRate.name() : __productFeeRate,
        __productFeeAmount.name() : __productFeeAmount
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductFeeDataType = ProductFeeDataType
Namespace.addCategoryObject('typeBinding', 'ProductFeeDataType', ProductFeeDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ProductFeeSummaryType with content type ELEMENT_ONLY
class ProductFeeSummaryType (pyxb.binding.basis.complexTypeDefinition):
    """Termékdíj összegzés adatokSummary of product charges"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductFeeSummaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1861, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeOperation uses Python identifier productFeeOperation
    __productFeeOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeOperation'), 'productFeeOperation', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeSummaryType_httpschemas_nav_gov_huOSA3_0dataproductFeeOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1867, 3), )

    
    productFeeOperation = property(__productFeeOperation.value, __productFeeOperation.set, None, 'Annak jelzése, hogy a termékdíj összesítés visszaigénylésre (REFUND) vagy raktárba történő beszállításra (DEPOSIT) vonatkozikIndicating whether the the product fee summary concerns refund or deposit')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productFeeData uses Python identifier productFeeData
    __productFeeData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productFeeData'), 'productFeeData', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeSummaryType_httpschemas_nav_gov_huOSA3_0dataproductFeeData', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1873, 3), )

    
    productFeeData = property(__productFeeData.value, __productFeeData.set, None, 'Termékdíj adatokProduct charges data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}productChargeSum uses Python identifier productChargeSum
    __productChargeSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productChargeSum'), 'productChargeSum', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeSummaryType_httpschemas_nav_gov_huOSA3_0dataproductChargeSum', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1879, 3), )

    
    productChargeSum = property(__productChargeSum.value, __productChargeSum.set, None, 'Termékdíj összesenAggregate product charges')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}paymentEvidenceDocumentData uses Python identifier paymentEvidenceDocumentData
    __paymentEvidenceDocumentData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentEvidenceDocumentData'), 'paymentEvidenceDocumentData', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeSummaryType_httpschemas_nav_gov_huOSA3_0datapaymentEvidenceDocumentData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1885, 3), )

    
    paymentEvidenceDocumentData = property(__paymentEvidenceDocumentData.value, __paymentEvidenceDocumentData.set, None, 'A termékdíj bevallását igazoló dokumentum adatai a 2011. évi LXXXV. tv. 13. § (3) szerint és a 25. § (3) szerintData of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011')

    _ElementMap.update({
        __productFeeOperation.name() : __productFeeOperation,
        __productFeeData.name() : __productFeeData,
        __productChargeSum.name() : __productChargeSum,
        __paymentEvidenceDocumentData.name() : __paymentEvidenceDocumentData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductFeeSummaryType = ProductFeeSummaryType
Namespace.addCategoryObject('typeBinding', 'ProductFeeSummaryType', ProductFeeSummaryType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ProductFeeTakeoverDataType with content type ELEMENT_ONLY
class ProductFeeTakeoverDataType (pyxb.binding.basis.complexTypeDefinition):
    """A környezetvédelmi termékdíj kötelezettség átvállalásával kapcsolatos adatokData in connection with takeover of environmental protection product fee"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductFeeTakeoverDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1893, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}takeoverReason uses Python identifier takeoverReason
    __takeoverReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'takeoverReason'), 'takeoverReason', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeTakeoverDataType_httpschemas_nav_gov_huOSA3_0datatakeoverReason', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1899, 3), )

    
    takeoverReason = property(__takeoverReason.value, __takeoverReason.set, None, 'Az átvállalás iránya és jogszabályi alapjaDirection and legal base of takeover')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}takeoverAmount uses Python identifier takeoverAmount
    __takeoverAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'takeoverAmount'), 'takeoverAmount', '__httpschemas_nav_gov_huOSA3_0data_ProductFeeTakeoverDataType_httpschemas_nav_gov_huOSA3_0datatakeoverAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1905, 3), )

    
    takeoverAmount = property(__takeoverAmount.value, __takeoverAmount.set, None, 'Az átvállalt termékdíj összege forintban, ha a vevő vállalja át az eladó termékdíj-kötelezettségétAmount in Hungarian forints of the product fee taken over if the purchaser takes over the supplier’s product fee liability')

    _ElementMap.update({
        __takeoverReason.name() : __takeoverReason,
        __takeoverAmount.name() : __takeoverAmount
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductFeeTakeoverDataType = ProductFeeTakeoverDataType
Namespace.addCategoryObject('typeBinding', 'ProductFeeTakeoverDataType', ProductFeeTakeoverDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ProjectNumbersType with content type ELEMENT_ONLY
class ProjectNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """ProjektszámokProject numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1913, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}projectNumber uses Python identifier projectNumber
    __projectNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'projectNumber'), 'projectNumber', '__httpschemas_nav_gov_huOSA3_0data_ProjectNumbersType_httpschemas_nav_gov_huOSA3_0dataprojectNumber', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1919, 3), )

    
    projectNumber = property(__projectNumber.value, __projectNumber.set, None, 'ProjektszámProject number')

    _ElementMap.update({
        __projectNumber.name() : __projectNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProjectNumbersType = ProjectNumbersType
Namespace.addCategoryObject('typeBinding', 'ProjectNumbersType', ProjectNumbersType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ReferencesToOtherLinesType with content type ELEMENT_ONLY
class ReferencesToOtherLinesType (pyxb.binding.basis.complexTypeDefinition):
    """Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükségesReferences to connected items if it is necessary according to VAT law"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferencesToOtherLinesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1927, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}referenceToOtherLine uses Python identifier referenceToOtherLine
    __referenceToOtherLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referenceToOtherLine'), 'referenceToOtherLine', '__httpschemas_nav_gov_huOSA3_0data_ReferencesToOtherLinesType_httpschemas_nav_gov_huOSA3_0datareferenceToOtherLine', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1933, 3), )

    
    referenceToOtherLine = property(__referenceToOtherLine.value, __referenceToOtherLine.set, None, 'Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükségesReferences to connected items if it is necessary according to VAT law')

    _ElementMap.update({
        __referenceToOtherLine.name() : __referenceToOtherLine
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferencesToOtherLinesType = ReferencesToOtherLinesType
Namespace.addCategoryObject('typeBinding', 'ReferencesToOtherLinesType', ReferencesToOtherLinesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}ShippingDatesType with content type ELEMENT_ONLY
class ShippingDatesType (pyxb.binding.basis.complexTypeDefinition):
    """Szállítási dátumokShipping dates"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShippingDatesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1941, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}shippingDate uses Python identifier shippingDate
    __shippingDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shippingDate'), 'shippingDate', '__httpschemas_nav_gov_huOSA3_0data_ShippingDatesType_httpschemas_nav_gov_huOSA3_0datashippingDate', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1947, 3), )

    
    shippingDate = property(__shippingDate.value, __shippingDate.set, None, 'Szállítási dátumShipping date')

    _ElementMap.update({
        __shippingDate.name() : __shippingDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ShippingDatesType = ShippingDatesType
Namespace.addCategoryObject('typeBinding', 'ShippingDatesType', ShippingDatesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}SummaryByVatRateType with content type ELEMENT_ONLY
class SummaryByVatRateType (pyxb.binding.basis.complexTypeDefinition):
    """ÁFA mértékek szerinti összesítésSummary according to VAT rates"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SummaryByVatRateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1955, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRate uses Python identifier vatRate
    __vatRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRate'), 'vatRate', '__httpschemas_nav_gov_huOSA3_0data_SummaryByVatRateType_httpschemas_nav_gov_huOSA3_0datavatRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1961, 3), )

    
    vatRate = property(__vatRate.value, __vatRate.set, None, 'Adómérték vagy adómentesség jelöléseMarking the tax rate or the fact of tax exemption')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateNetData uses Python identifier vatRateNetData
    __vatRateNetData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetData'), 'vatRateNetData', '__httpschemas_nav_gov_huOSA3_0data_SummaryByVatRateType_httpschemas_nav_gov_huOSA3_0datavatRateNetData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1967, 3), )

    
    vatRateNetData = property(__vatRateNetData.value, __vatRateNetData.set, None, 'Adott adómértékhez tartozó nettó adatokNet data of given tax rate')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateVatData uses Python identifier vatRateVatData
    __vatRateVatData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatData'), 'vatRateVatData', '__httpschemas_nav_gov_huOSA3_0data_SummaryByVatRateType_httpschemas_nav_gov_huOSA3_0datavatRateVatData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1973, 3), )

    
    vatRateVatData = property(__vatRateVatData.value, __vatRateVatData.set, None, 'Adott adómértékhez tartozó ÁFA adatokVAT data of given tax rate')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateGrossData uses Python identifier vatRateGrossData
    __vatRateGrossData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossData'), 'vatRateGrossData', '__httpschemas_nav_gov_huOSA3_0data_SummaryByVatRateType_httpschemas_nav_gov_huOSA3_0datavatRateGrossData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1979, 3), )

    
    vatRateGrossData = property(__vatRateGrossData.value, __vatRateGrossData.set, None, 'Adott adómértékhez tartozó bruttó adatokGross data of given tax rate')

    _ElementMap.update({
        __vatRate.name() : __vatRate,
        __vatRateNetData.name() : __vatRateNetData,
        __vatRateVatData.name() : __vatRateVatData,
        __vatRateGrossData.name() : __vatRateGrossData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SummaryByVatRateType = SummaryByVatRateType
Namespace.addCategoryObject('typeBinding', 'SummaryByVatRateType', SummaryByVatRateType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}SummaryGrossDataType with content type ELEMENT_ONLY
class SummaryGrossDataType (pyxb.binding.basis.complexTypeDefinition):
    """A számla összesítő bruttó adataiGross data of the invoice summary"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SummaryGrossDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1987, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceGrossAmount uses Python identifier invoiceGrossAmount
    __invoiceGrossAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceGrossAmount'), 'invoiceGrossAmount', '__httpschemas_nav_gov_huOSA3_0data_SummaryGrossDataType_httpschemas_nav_gov_huOSA3_0datainvoiceGrossAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1993, 3), )

    
    invoiceGrossAmount = property(__invoiceGrossAmount.value, __invoiceGrossAmount.set, None, 'A számla bruttó összege a számla pénznemébenGross amount of the invoice expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceGrossAmountHUF uses Python identifier invoiceGrossAmountHUF
    __invoiceGrossAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceGrossAmountHUF'), 'invoiceGrossAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_SummaryGrossDataType_httpschemas_nav_gov_huOSA3_0datainvoiceGrossAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1999, 3), )

    
    invoiceGrossAmountHUF = property(__invoiceGrossAmountHUF.value, __invoiceGrossAmountHUF.set, None, 'A számla bruttó összege forintbanGross amount of the invoice expressed in HUF')

    _ElementMap.update({
        __invoiceGrossAmount.name() : __invoiceGrossAmount,
        __invoiceGrossAmountHUF.name() : __invoiceGrossAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SummaryGrossDataType = SummaryGrossDataType
Namespace.addCategoryObject('typeBinding', 'SummaryGrossDataType', SummaryGrossDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}SummaryNormalType with content type ELEMENT_ONLY
class SummaryNormalType (pyxb.binding.basis.complexTypeDefinition):
    """Számla összesítés (nem egyszerűsített számla esetén)Calculation of invoice totals (not simplified invoice)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SummaryNormalType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2007, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}summaryByVatRate uses Python identifier summaryByVatRate
    __summaryByVatRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'summaryByVatRate'), 'summaryByVatRate', '__httpschemas_nav_gov_huOSA3_0data_SummaryNormalType_httpschemas_nav_gov_huOSA3_0datasummaryByVatRate', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2013, 3), )

    
    summaryByVatRate = property(__summaryByVatRate.value, __summaryByVatRate.set, None, 'Összesítés ÁFA-mérték szerintCalculation of invoice totals per VAT rates')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNetAmount uses Python identifier invoiceNetAmount
    __invoiceNetAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount'), 'invoiceNetAmount', '__httpschemas_nav_gov_huOSA3_0data_SummaryNormalType_httpschemas_nav_gov_huOSA3_0datainvoiceNetAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2019, 3), )

    
    invoiceNetAmount = property(__invoiceNetAmount.value, __invoiceNetAmount.set, None, 'A számla nettó összege a számla pénznemébenNet amount of the invoice expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNetAmountHUF uses Python identifier invoiceNetAmountHUF
    __invoiceNetAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF'), 'invoiceNetAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_SummaryNormalType_httpschemas_nav_gov_huOSA3_0datainvoiceNetAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2025, 3), )

    
    invoiceNetAmountHUF = property(__invoiceNetAmountHUF.value, __invoiceNetAmountHUF.set, None, 'A számla nettó összege forintbanNet amount of the invoice expressed in HUF')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceVatAmount uses Python identifier invoiceVatAmount
    __invoiceVatAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount'), 'invoiceVatAmount', '__httpschemas_nav_gov_huOSA3_0data_SummaryNormalType_httpschemas_nav_gov_huOSA3_0datainvoiceVatAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2031, 3), )

    
    invoiceVatAmount = property(__invoiceVatAmount.value, __invoiceVatAmount.set, None, 'A számla ÁFA összege a számla pénznemébenVAT amount of the invoice expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}invoiceVatAmountHUF uses Python identifier invoiceVatAmountHUF
    __invoiceVatAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF'), 'invoiceVatAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_SummaryNormalType_httpschemas_nav_gov_huOSA3_0datainvoiceVatAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2037, 3), )

    
    invoiceVatAmountHUF = property(__invoiceVatAmountHUF.value, __invoiceVatAmountHUF.set, None, 'A számla ÁFA összege forintbanVAT amount of the invoice expressed in HUF')

    _ElementMap.update({
        __summaryByVatRate.name() : __summaryByVatRate,
        __invoiceNetAmount.name() : __invoiceNetAmount,
        __invoiceNetAmountHUF.name() : __invoiceNetAmountHUF,
        __invoiceVatAmount.name() : __invoiceVatAmount,
        __invoiceVatAmountHUF.name() : __invoiceVatAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SummaryNormalType = SummaryNormalType
Namespace.addCategoryObject('typeBinding', 'SummaryNormalType', SummaryNormalType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}SummarySimplifiedType with content type ELEMENT_ONLY
class SummarySimplifiedType (pyxb.binding.basis.complexTypeDefinition):
    """Egyszerűsített számla összesítésCalculation of simplified invoice totals"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SummarySimplifiedType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2045, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRate uses Python identifier vatRate
    __vatRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRate'), 'vatRate', '__httpschemas_nav_gov_huOSA3_0data_SummarySimplifiedType_httpschemas_nav_gov_huOSA3_0datavatRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2051, 3), )

    
    vatRate = property(__vatRate.value, __vatRate.set, None, 'Adómérték vagy adómentesség jelöléseMarking the tax rate or the fact of tax exemption')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatContentGrossAmount uses Python identifier vatContentGrossAmount
    __vatContentGrossAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatContentGrossAmount'), 'vatContentGrossAmount', '__httpschemas_nav_gov_huOSA3_0data_SummarySimplifiedType_httpschemas_nav_gov_huOSA3_0datavatContentGrossAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2057, 3), )

    
    vatContentGrossAmount = property(__vatContentGrossAmount.value, __vatContentGrossAmount.set, None, 'Az adott adótartalomhoz tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege a számla pénznemébenThe gross amount of the sale or service for the given tax amount in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatContentGrossAmountHUF uses Python identifier vatContentGrossAmountHUF
    __vatContentGrossAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatContentGrossAmountHUF'), 'vatContentGrossAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_SummarySimplifiedType_httpschemas_nav_gov_huOSA3_0datavatContentGrossAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2063, 3), )

    
    vatContentGrossAmountHUF = property(__vatContentGrossAmountHUF.value, __vatContentGrossAmountHUF.set, None, 'Az adott adótartalomhoz tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege forintbanThe gross amount of the sale or service for the given tax amount in HUF')

    _ElementMap.update({
        __vatRate.name() : __vatRate,
        __vatContentGrossAmount.name() : __vatContentGrossAmount,
        __vatContentGrossAmountHUF.name() : __vatContentGrossAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SummarySimplifiedType = SummarySimplifiedType
Namespace.addCategoryObject('typeBinding', 'SummarySimplifiedType', SummarySimplifiedType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}SummaryType with content type ELEMENT_ONLY
class SummaryType (pyxb.binding.basis.complexTypeDefinition):
    """Számla összesítés adataiData of calculation of invoice totals"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SummaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2071, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}summaryNormal uses Python identifier summaryNormal
    __summaryNormal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'summaryNormal'), 'summaryNormal', '__httpschemas_nav_gov_huOSA3_0data_SummaryType_httpschemas_nav_gov_huOSA3_0datasummaryNormal', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2078, 4), )

    
    summaryNormal = property(__summaryNormal.value, __summaryNormal.set, None, 'Számla összesítés (nem egyszerűsített számla esetén)Calculation of invoice totals (not simplified invoice)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}summarySimplified uses Python identifier summarySimplified
    __summarySimplified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'summarySimplified'), 'summarySimplified', '__httpschemas_nav_gov_huOSA3_0data_SummaryType_httpschemas_nav_gov_huOSA3_0datasummarySimplified', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2084, 4), )

    
    summarySimplified = property(__summarySimplified.value, __summarySimplified.set, None, 'Egyszerűsített számla összesítésCalculation of simplified invoice totals')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}summaryGrossData uses Python identifier summaryGrossData
    __summaryGrossData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'summaryGrossData'), 'summaryGrossData', '__httpschemas_nav_gov_huOSA3_0data_SummaryType_httpschemas_nav_gov_huOSA3_0datasummaryGrossData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2091, 3), )

    
    summaryGrossData = property(__summaryGrossData.value, __summaryGrossData.set, None, 'A számla összesítő bruttó adataiGross data of the invoice summary')

    _ElementMap.update({
        __summaryNormal.name() : __summaryNormal,
        __summarySimplified.name() : __summarySimplified,
        __summaryGrossData.name() : __summaryGrossData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SummaryType = SummaryType
Namespace.addCategoryObject('typeBinding', 'SummaryType', SummaryType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}SupplierCompanyCodesType with content type ELEMENT_ONLY
class SupplierCompanyCodesType (pyxb.binding.basis.complexTypeDefinition):
    """Az eladó vállalati kódjaiCompany codes of the supplier"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplierCompanyCodesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2099, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}supplierCompanyCode uses Python identifier supplierCompanyCode
    __supplierCompanyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierCompanyCode'), 'supplierCompanyCode', '__httpschemas_nav_gov_huOSA3_0data_SupplierCompanyCodesType_httpschemas_nav_gov_huOSA3_0datasupplierCompanyCode', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2105, 3), )

    
    supplierCompanyCode = property(__supplierCompanyCode.value, __supplierCompanyCode.set, None, 'Az eladó vállalati kódjaCompany code of the supplier')

    _ElementMap.update({
        __supplierCompanyCode.name() : __supplierCompanyCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SupplierCompanyCodesType = SupplierCompanyCodesType
Namespace.addCategoryObject('typeBinding', 'SupplierCompanyCodesType', SupplierCompanyCodesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}SupplierInfoType with content type ELEMENT_ONLY
class SupplierInfoType (pyxb.binding.basis.complexTypeDefinition):
    """A szállító (eladó) adataiInvoice supplier (seller) data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplierInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2113, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}supplierTaxNumber uses Python identifier supplierTaxNumber
    __supplierTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), 'supplierTaxNumber', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0datasupplierTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2119, 3), )

    
    supplierTaxNumber = property(__supplierTaxNumber.value, __supplierTaxNumber.set, None, 'Belföldi adószám vagy csoportazonosító számTax number or group identification number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}groupMemberTaxNumber uses Python identifier groupMemberTaxNumber
    __groupMemberTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber'), 'groupMemberTaxNumber', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0datagroupMemberTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2125, 3), )

    
    groupMemberTaxNumber = property(__groupMemberTaxNumber.value, __groupMemberTaxNumber.set, None, 'Csoport tag adószáma, ha a termékbeszerzés vagy szolgáltatás nyújtása csoportazonosító szám alatt történtTax number of group member, when the supply of goods or services is done under group identification number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}communityVatNumber uses Python identifier communityVatNumber
    __communityVatNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'communityVatNumber'), 'communityVatNumber', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0datacommunityVatNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2131, 3), )

    
    communityVatNumber = property(__communityVatNumber.value, __communityVatNumber.set, None, 'Közösségi adószámCommunity tax number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}supplierName uses Python identifier supplierName
    __supplierName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierName'), 'supplierName', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0datasupplierName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2137, 3), )

    
    supplierName = property(__supplierName.value, __supplierName.set, None, 'Az eladó (szállító) neveName of the seller (supplier)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}supplierAddress uses Python identifier supplierAddress
    __supplierAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierAddress'), 'supplierAddress', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0datasupplierAddress', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2143, 3), )

    
    supplierAddress = property(__supplierAddress.value, __supplierAddress.set, None, 'Az eladó (szállító) címeAddress of the seller (supplier)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}supplierBankAccountNumber uses Python identifier supplierBankAccountNumber
    __supplierBankAccountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierBankAccountNumber'), 'supplierBankAccountNumber', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0datasupplierBankAccountNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2149, 3), )

    
    supplierBankAccountNumber = property(__supplierBankAccountNumber.value, __supplierBankAccountNumber.set, None, 'Az eladó (szállító) bankszámlaszámaBank account number of the seller (supplier)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}individualExemption uses Python identifier individualExemption
    __individualExemption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'individualExemption'), 'individualExemption', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0dataindividualExemption', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2155, 3), )

    
    individualExemption = property(__individualExemption.value, __individualExemption.set, None, 'Értéke true, amennyiben az eladó (szállító) alanyi ÁFA mentesValue is true if the seller (supplier) is individually exempted from VAT')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}exciseLicenceNum uses Python identifier exciseLicenceNum
    __exciseLicenceNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exciseLicenceNum'), 'exciseLicenceNum', '__httpschemas_nav_gov_huOSA3_0data_SupplierInfoType_httpschemas_nav_gov_huOSA3_0dataexciseLicenceNum', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2161, 3), )

    
    exciseLicenceNum = property(__exciseLicenceNum.value, __exciseLicenceNum.set, None, 'Az eladó adóraktári engedélyének vagy jövedéki engedélyének száma (2016. évi LXVIII. tv.)Number of supplier’s tax warehouse license or excise license (Act LXVIII of 2016)')

    _ElementMap.update({
        __supplierTaxNumber.name() : __supplierTaxNumber,
        __groupMemberTaxNumber.name() : __groupMemberTaxNumber,
        __communityVatNumber.name() : __communityVatNumber,
        __supplierName.name() : __supplierName,
        __supplierAddress.name() : __supplierAddress,
        __supplierBankAccountNumber.name() : __supplierBankAccountNumber,
        __individualExemption.name() : __individualExemption,
        __exciseLicenceNum.name() : __exciseLicenceNum
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SupplierInfoType = SupplierInfoType
Namespace.addCategoryObject('typeBinding', 'SupplierInfoType', SupplierInfoType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}VatAmountMismatchType with content type ELEMENT_ONLY
class VatAmountMismatchType (pyxb.binding.basis.complexTypeDefinition):
    """Adóalap és felszámított adó eltérésének adataiData of mismatching tax base and levied tax"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VatAmountMismatchType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2169, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRate uses Python identifier vatRate
    __vatRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRate'), 'vatRate', '__httpschemas_nav_gov_huOSA3_0data_VatAmountMismatchType_httpschemas_nav_gov_huOSA3_0datavatRate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2175, 3), )

    
    vatRate = property(__vatRate.value, __vatRate.set, None, 'Adómérték, adótartalomVAT rate, VAT content')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}case uses Python identifier case
    __case = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'case'), 'case', '__httpschemas_nav_gov_huOSA3_0data_VatAmountMismatchType_httpschemas_nav_gov_huOSA3_0datacase', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2181, 3), )

    
    case = property(__case.value, __case.set, None, 'Az eset leírása kóddalCase notation with code')

    _ElementMap.update({
        __vatRate.name() : __vatRate,
        __case.name() : __case
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VatAmountMismatchType = VatAmountMismatchType
Namespace.addCategoryObject('typeBinding', 'VatAmountMismatchType', VatAmountMismatchType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}VatRateGrossDataType with content type ELEMENT_ONLY
class VatRateGrossDataType (pyxb.binding.basis.complexTypeDefinition):
    """Adott adómértékhez tartozó bruttó adatokGross data of given tax rate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VatRateGrossDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2189, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateGrossAmount uses Python identifier vatRateGrossAmount
    __vatRateGrossAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossAmount'), 'vatRateGrossAmount', '__httpschemas_nav_gov_huOSA3_0data_VatRateGrossDataType_httpschemas_nav_gov_huOSA3_0datavatRateGrossAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2195, 3), )

    
    vatRateGrossAmount = property(__vatRateGrossAmount.value, __vatRateGrossAmount.set, None, 'Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege a számla pénznemébenGross amount of sales or service delivery under a given tax rate expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateGrossAmountHUF uses Python identifier vatRateGrossAmountHUF
    __vatRateGrossAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossAmountHUF'), 'vatRateGrossAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_VatRateGrossDataType_httpschemas_nav_gov_huOSA3_0datavatRateGrossAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2201, 3), )

    
    vatRateGrossAmountHUF = property(__vatRateGrossAmountHUF.value, __vatRateGrossAmountHUF.set, None, 'Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege forintbanGross amount of sales or service delivery under a given tax rate expressed in HUF')

    _ElementMap.update({
        __vatRateGrossAmount.name() : __vatRateGrossAmount,
        __vatRateGrossAmountHUF.name() : __vatRateGrossAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VatRateGrossDataType = VatRateGrossDataType
Namespace.addCategoryObject('typeBinding', 'VatRateGrossDataType', VatRateGrossDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}VatRateNetDataType with content type ELEMENT_ONLY
class VatRateNetDataType (pyxb.binding.basis.complexTypeDefinition):
    """Adott adómértékhez tartozó nettó adatokNet data of given tax rate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VatRateNetDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2209, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateNetAmount uses Python identifier vatRateNetAmount
    __vatRateNetAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetAmount'), 'vatRateNetAmount', '__httpschemas_nav_gov_huOSA3_0data_VatRateNetDataType_httpschemas_nav_gov_huOSA3_0datavatRateNetAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2215, 3), )

    
    vatRateNetAmount = property(__vatRateNetAmount.value, __vatRateNetAmount.set, None, 'Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás nettó összege a számla pénznemébenNet amount of sales or service delivery under a given tax rate expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateNetAmountHUF uses Python identifier vatRateNetAmountHUF
    __vatRateNetAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetAmountHUF'), 'vatRateNetAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_VatRateNetDataType_httpschemas_nav_gov_huOSA3_0datavatRateNetAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2221, 3), )

    
    vatRateNetAmountHUF = property(__vatRateNetAmountHUF.value, __vatRateNetAmountHUF.set, None, 'Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás nettó összege forintbanNet amount of sales or service delivery under a given tax rate expressed in HUF')

    _ElementMap.update({
        __vatRateNetAmount.name() : __vatRateNetAmount,
        __vatRateNetAmountHUF.name() : __vatRateNetAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VatRateNetDataType = VatRateNetDataType
Namespace.addCategoryObject('typeBinding', 'VatRateNetDataType', VatRateNetDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}VatRateType with content type ELEMENT_ONLY
class VatRateType (pyxb.binding.basis.complexTypeDefinition):
    """Az adómérték vagy az adómentes értékesítés jelöléseMarking tax rate or tax exempt supply"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VatRateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2229, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatPercentage uses Python identifier vatPercentage
    __vatPercentage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatPercentage'), 'vatPercentage', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datavatPercentage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2235, 3), )

    
    vatPercentage = property(__vatPercentage.value, __vatPercentage.set, None, 'Az alkalmazott adó mértéke - ÁFA tv. 169. § j)Applied tax rate - section 169 (j) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatContent uses Python identifier vatContent
    __vatContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatContent'), 'vatContent', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datavatContent', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2241, 3), )

    
    vatContent = property(__vatContent.value, __vatContent.set, None, 'ÁFA tartalom egyszerűsített számla eseténVAT content in case of simplified invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatExemption uses Python identifier vatExemption
    __vatExemption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatExemption'), 'vatExemption', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datavatExemption', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2247, 3), )

    
    vatExemption = property(__vatExemption.value, __vatExemption.set, None, 'Az adómentesség jelölése - ÁFA tv. 169. § m)Marking tax exemption -  section 169 (m) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatOutOfScope uses Python identifier vatOutOfScope
    __vatOutOfScope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatOutOfScope'), 'vatOutOfScope', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datavatOutOfScope', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2253, 3), )

    
    vatOutOfScope = property(__vatOutOfScope.value, __vatOutOfScope.set, None, 'Az ÁFA törvény hatályán kívüliOut of scope of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatDomesticReverseCharge uses Python identifier vatDomesticReverseCharge
    __vatDomesticReverseCharge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatDomesticReverseCharge'), 'vatDomesticReverseCharge', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datavatDomesticReverseCharge', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2259, 3), )

    
    vatDomesticReverseCharge = property(__vatDomesticReverseCharge.value, __vatDomesticReverseCharge.set, None, 'A belföldi fordított adózás jelölése - ÁFA tv. 142. §Marking the national is reverse charge taxation - section 142 of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}marginSchemeIndicator uses Python identifier marginSchemeIndicator
    __marginSchemeIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'marginSchemeIndicator'), 'marginSchemeIndicator', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datamarginSchemeIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2265, 3), )

    
    marginSchemeIndicator = property(__marginSchemeIndicator.value, __marginSchemeIndicator.set, None, 'Különbözet szerinti szabályozás jelölése - ÁFA tv. 169. § p) q)Marking the margin-scheme taxation as per section 169 (p)(q)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatAmountMismatch uses Python identifier vatAmountMismatch
    __vatAmountMismatch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatAmountMismatch'), 'vatAmountMismatch', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datavatAmountMismatch', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2271, 3), )

    
    vatAmountMismatch = property(__vatAmountMismatch.value, __vatAmountMismatch.set, None, 'Adóalap és felszámított adó eltérésének eseteiDifferent cases of mismatching tax base and levied tax')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}noVatCharge uses Python identifier noVatCharge
    __noVatCharge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'noVatCharge'), 'noVatCharge', '__httpschemas_nav_gov_huOSA3_0data_VatRateType_httpschemas_nav_gov_huOSA3_0datanoVatCharge', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2277, 3), )

    
    noVatCharge = property(__noVatCharge.value, __noVatCharge.set, None, 'Nincs felszámított áfa a 17. § alapjánNo VAT charged under Section 17')

    _ElementMap.update({
        __vatPercentage.name() : __vatPercentage,
        __vatContent.name() : __vatContent,
        __vatExemption.name() : __vatExemption,
        __vatOutOfScope.name() : __vatOutOfScope,
        __vatDomesticReverseCharge.name() : __vatDomesticReverseCharge,
        __marginSchemeIndicator.name() : __marginSchemeIndicator,
        __vatAmountMismatch.name() : __vatAmountMismatch,
        __noVatCharge.name() : __noVatCharge
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VatRateType = VatRateType
Namespace.addCategoryObject('typeBinding', 'VatRateType', VatRateType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}VatRateVatDataType with content type ELEMENT_ONLY
class VatRateVatDataType (pyxb.binding.basis.complexTypeDefinition):
    """Adott adómértékhez tartozó ÁFA adatokVAT data of given tax rate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VatRateVatDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2285, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateVatAmount uses Python identifier vatRateVatAmount
    __vatRateVatAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatAmount'), 'vatRateVatAmount', '__httpschemas_nav_gov_huOSA3_0data_VatRateVatDataType_httpschemas_nav_gov_huOSA3_0datavatRateVatAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2291, 3), )

    
    vatRateVatAmount = property(__vatRateVatAmount.value, __vatRateVatAmount.set, None, 'Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás ÁFA összege a számla pénznemébenVAT amount of sales or service delivery under a given tax rate expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}vatRateVatAmountHUF uses Python identifier vatRateVatAmountHUF
    __vatRateVatAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatAmountHUF'), 'vatRateVatAmountHUF', '__httpschemas_nav_gov_huOSA3_0data_VatRateVatDataType_httpschemas_nav_gov_huOSA3_0datavatRateVatAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2297, 3), )

    
    vatRateVatAmountHUF = property(__vatRateVatAmountHUF.value, __vatRateVatAmountHUF.set, None, 'Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás ÁFA összege forintbanVAT amount of sales or service delivery under a given tax rate expressed in HUF')

    _ElementMap.update({
        __vatRateVatAmount.name() : __vatRateVatAmount,
        __vatRateVatAmountHUF.name() : __vatRateVatAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VatRateVatDataType = VatRateVatDataType
Namespace.addCategoryObject('typeBinding', 'VatRateVatDataType', VatRateVatDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}VehicleType with content type ELEMENT_ONLY
class VehicleType (pyxb.binding.basis.complexTypeDefinition):
    """Szárazföldi közlekedési eszköz további adataiOther data in relation to motorised land vehicle"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VehicleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2305, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}engineCapacity uses Python identifier engineCapacity
    __engineCapacity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'engineCapacity'), 'engineCapacity', '__httpschemas_nav_gov_huOSA3_0data_VehicleType_httpschemas_nav_gov_huOSA3_0dataengineCapacity', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2311, 3), )

    
    engineCapacity = property(__engineCapacity.value, __engineCapacity.set, None, 'Hengerűrtartalom köbcentiméterbenEngine capacity in cubic centimetre')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}enginePower uses Python identifier enginePower
    __enginePower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'enginePower'), 'enginePower', '__httpschemas_nav_gov_huOSA3_0data_VehicleType_httpschemas_nav_gov_huOSA3_0dataenginePower', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2317, 3), )

    
    enginePower = property(__enginePower.value, __enginePower.set, None, 'Teljesítmény kW-banEngine power in kW')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}kms uses Python identifier kms
    __kms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kms'), 'kms', '__httpschemas_nav_gov_huOSA3_0data_VehicleType_httpschemas_nav_gov_huOSA3_0datakms', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2323, 3), )

    
    kms = property(__kms.value, __kms.set, None, 'Futott kilométerek számaTravelled distance in km')

    _ElementMap.update({
        __engineCapacity.name() : __engineCapacity,
        __enginePower.name() : __enginePower,
        __kms.name() : __kms
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VehicleType = VehicleType
Namespace.addCategoryObject('typeBinding', 'VehicleType', VehicleType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}VesselType with content type ELEMENT_ONLY
class VesselType (pyxb.binding.basis.complexTypeDefinition):
    """Vízi jármű adataiData of vessel"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VesselType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2331, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'length'), 'length', '__httpschemas_nav_gov_huOSA3_0data_VesselType_httpschemas_nav_gov_huOSA3_0datalength', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2337, 3), )

    
    length = property(__length.value, __length.set, None, 'Hajó hossza méterbenLength of hull in metre')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}activityReferred uses Python identifier activityReferred
    __activityReferred = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityReferred'), 'activityReferred', '__httpschemas_nav_gov_huOSA3_0data_VesselType_httpschemas_nav_gov_huOSA3_0dataactivityReferred', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2343, 3), )

    
    activityReferred = property(__activityReferred.value, __activityReferred.set, None, 'Értéke true, ha a jármű az ÁFA tv. 259.§ 25. b) szerinti kivétel alá tartozikThe value is true if the means of transport is exempt from VAT as per section 259 [25] (b)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}sailedHours uses Python identifier sailedHours
    __sailedHours = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sailedHours'), 'sailedHours', '__httpschemas_nav_gov_huOSA3_0data_VesselType_httpschemas_nav_gov_huOSA3_0datasailedHours', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2349, 3), )

    
    sailedHours = property(__sailedHours.value, __sailedHours.set, None, 'Hajózott órák számaNumber of sailed hours')

    _ElementMap.update({
        __length.name() : __length,
        __activityReferred.name() : __activityReferred,
        __sailedHours.name() : __sailedHours
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VesselType = VesselType
Namespace.addCategoryObject('typeBinding', 'VesselType', VesselType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/data}CustomerTaxNumberType with content type ELEMENT_ONLY
class CustomerTaxNumberType (_ImportedBinding_base.TaxNumberType):
    """Adószám, amely alatt a számlán szereplő termékbeszerzés vagy szolgáltatás igénybevétele történt. Lehet csoportazonosító szám isTax number or group identification number, under which the purchase of goods or services is done"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerTaxNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 811, 1)
    _ElementMap = _ImportedBinding_base.TaxNumberType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_base.TaxNumberType._AttributeMap.copy()
    # Base type is _ImportedBinding_base.TaxNumberType
    
    # Element taxpayerId ({http://schemas.nav.gov.hu/OSA/3.0/base}taxpayerId) inherited from {http://schemas.nav.gov.hu/OSA/3.0/base}TaxNumberType
    
    # Element vatCode ({http://schemas.nav.gov.hu/OSA/3.0/base}vatCode) inherited from {http://schemas.nav.gov.hu/OSA/3.0/base}TaxNumberType
    
    # Element countyCode ({http://schemas.nav.gov.hu/OSA/3.0/base}countyCode) inherited from {http://schemas.nav.gov.hu/OSA/3.0/base}TaxNumberType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/data}groupMemberTaxNumber uses Python identifier groupMemberTaxNumber
    __groupMemberTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber'), 'groupMemberTaxNumber', '__httpschemas_nav_gov_huOSA3_0data_CustomerTaxNumberType_httpschemas_nav_gov_huOSA3_0datagroupMemberTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 819, 5), )

    
    groupMemberTaxNumber = property(__groupMemberTaxNumber.value, __groupMemberTaxNumber.set, None, 'Csoport tag adószáma, ha a termékbeszerzés vagy szolgáltatás igénybevétele csoportazonosító szám alatt történtTax number of group member, when the purchase of goods or services is done under group identification number')

    _ElementMap.update({
        __groupMemberTaxNumber.name() : __groupMemberTaxNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomerTaxNumberType = CustomerTaxNumberType
Namespace.addCategoryObject('typeBinding', 'CustomerTaxNumberType', CustomerTaxNumberType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (InvoiceDataType):
    """XML root element, számla vagy módosítás adatait leíró típus, amelyet BASE64 kódoltan tartalmaz az invoiceApi sémaleíró invoiceData elementjeXML root element, invoice or modification data type in BASE64 encoding, equivalent with the invoiceApi schema definition's invoiceData element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2362, 2)
    _ElementMap = InvoiceDataType._ElementMap.copy()
    _AttributeMap = InvoiceDataType._AttributeMap.copy()
    # Base type is InvoiceDataType
    
    # Element invoiceNumber ({http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNumber) inherited from {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceDataType
    
    # Element invoiceIssueDate ({http://schemas.nav.gov.hu/OSA/3.0/data}invoiceIssueDate) inherited from {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceDataType
    
    # Element completenessIndicator ({http://schemas.nav.gov.hu/OSA/3.0/data}completenessIndicator) inherited from {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceDataType
    
    # Element invoiceMain ({http://schemas.nav.gov.hu/OSA/3.0/data}invoiceMain) inherited from {http://schemas.nav.gov.hu/OSA/3.0/data}InvoiceDataType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


InvoiceData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InvoiceData'), CTD_ANON, documentation="XML root element, számla vagy módosítás adatait leíró típus, amelyet BASE64 kódoltan tartalmaz az invoiceApi sémaleíró invoiceData elementjeXML root element, invoice or modification data type in BASE64 encoding, equivalent with the invoiceApi schema definition's invoiceData element", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2357, 1))
Namespace.addCategoryObject('elementBinding', InvoiceData.name().localName(), InvoiceData)



AdditionalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dataName'), DataNameType, scope=AdditionalDataType, documentation='Az adatmező egyedi azonosítójaUnique identification of the data field', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 481, 3)))

AdditionalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dataDescription'), _ImportedBinding_common.SimpleText255NotBlankType, scope=AdditionalDataType, documentation='Az adatmező tartalmának szöveges leírásaDescription of content of the data field', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 487, 3)))

AdditionalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dataValue'), _ImportedBinding_common.SimpleText512NotBlankType, scope=AdditionalDataType, documentation='Az adat értékeValue of the data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 493, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AdditionalDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dataName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 481, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AdditionalDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dataDescription')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 487, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdditionalDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dataValue')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 493, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AdditionalDataType._Automaton = _BuildAutomaton()




AdvanceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'advanceIndicator'), pyxb.binding.datatypes.boolean, scope=AdvanceDataType, documentation='Értéke true, ha a számla tétel előleg jellegűThe value is true if the invoice item is a kind of advance charge', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 507, 3)))

AdvanceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'advancePaymentData'), AdvancePaymentDataType, scope=AdvanceDataType, documentation='Előleg fizetéshez kapcsolódó adatokAdvance payment related data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 513, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 513, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdvanceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'advanceIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 507, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdvanceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'advancePaymentData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 513, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AdvanceDataType._Automaton = _BuildAutomaton_()




AdvancePaymentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'advanceOriginalInvoice'), _ImportedBinding_common.SimpleText50NotBlankType, scope=AdvancePaymentDataType, documentation='Az előlegszámlának a sorszáma, amelyben az előlegfizetés történtInvoice number containing the advance payment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 527, 3)))

AdvancePaymentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'advancePaymentDate'), _ImportedBinding_base.InvoiceDateType, scope=AdvancePaymentDataType, documentation='Az előleg fizetésének dátumaPayment date of the advance', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 533, 3)))

AdvancePaymentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'advanceExchangeRate'), ExchangeRateType, scope=AdvancePaymentDataType, documentation='Az előlegfizetés során alkalmazott árfolyamApplied exchange rate of the advance', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 539, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AdvancePaymentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'advanceOriginalInvoice')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 527, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AdvancePaymentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'advancePaymentDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 533, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdvancePaymentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'advanceExchangeRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 539, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AdvancePaymentDataType._Automaton = _BuildAutomaton_2()




AggregateInvoiceLineDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineExchangeRate'), ExchangeRateType, scope=AggregateInvoiceLineDataType, documentation='A tételhez tartozó árfolyam, 1 (egy) egységre vonatkoztatva. Csak külföldi pénznemben kiállított gyűjtő számla esetén kitöltendőThe exchange rate applied to the item, pertaining to 1 (one) unit. This should be filled in only if an aggregate invoice in foreign currency is issued', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 553, 3)))

AggregateInvoiceLineDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineDeliveryDate'), _ImportedBinding_base.InvoiceDateType, scope=AggregateInvoiceLineDataType, documentation='Gyűjtőszámla esetén az adott tétel teljesítési dátumaDelivery date of the given item in the case of an aggregate invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 559, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 553, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AggregateInvoiceLineDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineExchangeRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 553, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AggregateInvoiceLineDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineDeliveryDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 559, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AggregateInvoiceLineDataType._Automaton = _BuildAutomaton_3()




AircraftType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'takeOffWeight'), QuantityType, scope=AircraftType, documentation='Felszállási tömeg kilogrammbanTake-off weight in kilogram', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 573, 3)))

AircraftType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'airCargo'), pyxb.binding.datatypes.boolean, scope=AircraftType, documentation='Értéke true ha a jármű az ÁFA tv. 259.§ 25. c) szerinti kivétel alá tartozikThe value is true if the means of transport is exempt from VAT as per section 259 [25] (c)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 579, 3)))

AircraftType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'operationHours'), QuantityType, scope=AircraftType, documentation='Repült órák számaNumber of aviated hours', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 585, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AircraftType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'takeOffWeight')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 573, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AircraftType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'airCargo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 579, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AircraftType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'operationHours')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 585, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AircraftType._Automaton = _BuildAutomaton_4()




BatchInvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=BatchInvoiceType, documentation='A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 599, 3)))

BatchInvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoice'), InvoiceType, scope=BatchInvoiceType, documentation='Egy számla vagy módosító okirat adataiData of a single invoice or modification document', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 605, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatchInvoiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batchIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 599, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BatchInvoiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoice')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 605, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BatchInvoiceType._Automaton = _BuildAutomaton_5()




ContractNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contractNumber'), _ImportedBinding_common.SimpleText100NotBlankType, scope=ContractNumbersType, documentation='SzerződésszámContract number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 619, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContractNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contractNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 619, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ContractNumbersType._Automaton = _BuildAutomaton_6()




ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderNumbers'), OrderNumbersType, scope=ConventionalInvoiceInfoType, documentation='Megrendelésszám(ok)Order numbers', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 633, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deliveryNotes'), DeliveryNotesType, scope=ConventionalInvoiceInfoType, documentation='Szállítólevél szám(ok)Delivery notes', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 639, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shippingDates'), ShippingDatesType, scope=ConventionalInvoiceInfoType, documentation='Szállítási dátum(ok)Shipping dates', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 645, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contractNumbers'), ContractNumbersType, scope=ConventionalInvoiceInfoType, documentation='Szerződésszám(ok)Contract numbers', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 651, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierCompanyCodes'), SupplierCompanyCodesType, scope=ConventionalInvoiceInfoType, documentation='Az eladó vállalati kódja(i)Company codes of the supplier', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 657, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerCompanyCodes'), CustomerCompanyCodesType, scope=ConventionalInvoiceInfoType, documentation='A vevő vállalati kódja(i)Company codes of the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 663, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dealerCodes'), DealerCodesType, scope=ConventionalInvoiceInfoType, documentation='Beszállító kód(ok)Dealer codes', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 669, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'costCenters'), CostCentersType, scope=ConventionalInvoiceInfoType, documentation='Költséghely(ek)Cost centers', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 675, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'projectNumbers'), ProjectNumbersType, scope=ConventionalInvoiceInfoType, documentation='Projektszám(ok)Project numbers', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 681, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generalLedgerAccountNumbers'), GeneralLedgerAccountNumbersType, scope=ConventionalInvoiceInfoType, documentation='Főkönyvi számlaszám(ok)General ledger account numbers', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 687, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'glnNumbersSupplier'), GlnNumbersType, scope=ConventionalInvoiceInfoType, documentation="Kiállítói globális helyazonosító szám(ok)Supplier's global location numbers", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 693, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'glnNumbersCustomer'), GlnNumbersType, scope=ConventionalInvoiceInfoType, documentation="Vevői globális helyazonosító szám(ok)Customer's global location numbers", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 699, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'materialNumbers'), MaterialNumbersType, scope=ConventionalInvoiceInfoType, documentation='Anyagszám(ok)Material numbers', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 705, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemNumbers'), ItemNumbersType, scope=ConventionalInvoiceInfoType, documentation='Cikkszám(ok)Item number(s)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 711, 3)))

ConventionalInvoiceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ekaerIds'), EkaerIdsType, scope=ConventionalInvoiceInfoType, documentation='EKÁER azonosító(k)EKAER ID-s', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 717, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 633, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 639, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 645, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 651, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 657, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 663, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 669, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 675, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 681, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 687, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 693, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 699, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 705, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 711, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 717, 3))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNumbers')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 633, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryNotes')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 639, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shippingDates')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 645, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contractNumbers')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 651, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierCompanyCodes')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 657, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerCompanyCodes')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 663, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dealerCodes')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 669, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'costCenters')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 675, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'projectNumbers')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 681, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generalLedgerAccountNumbers')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 687, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'glnNumbersSupplier')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 693, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'glnNumbersCustomer')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 699, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'materialNumbers')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 705, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemNumbers')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 711, 3))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(ConventionalInvoiceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ekaerIds')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 717, 3))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConventionalInvoiceInfoType._Automaton = _BuildAutomaton_7()




CostCentersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'costCenter'), _ImportedBinding_common.SimpleText100NotBlankType, scope=CostCentersType, documentation='KöltséghelyCost center', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 731, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CostCentersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'costCenter')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 731, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CostCentersType._Automaton = _BuildAutomaton_8()




CustomerCompanyCodesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerCompanyCode'), _ImportedBinding_common.SimpleText100NotBlankType, scope=CustomerCompanyCodesType, documentation='A vevő vállalati kódjaCompany code of the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 745, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerCompanyCodesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerCompanyCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 745, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CustomerCompanyCodesType._Automaton = _BuildAutomaton_9()




CustomerDeclarationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productStream'), ProductStreamType, scope=CustomerDeclarationType, documentation='TermékáramProduct stream', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 759, 3)))

CustomerDeclarationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeWeight'), QuantityType, scope=CustomerDeclarationType, documentation='Termékdíj köteles termék tömege kilogrammbanWeight of product fee obliged product in kilogram', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 765, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 765, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerDeclarationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productStream')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 759, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CustomerDeclarationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeWeight')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 765, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CustomerDeclarationType._Automaton = _BuildAutomaton_10()




CustomerInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerVatStatus'), CustomerVatStatusType, scope=CustomerInfoType, documentation='Vevő ÁFA szerinti státuszaCustomers status by VAT', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 779, 3)))

CustomerInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerVatData'), CustomerVatDataType, scope=CustomerInfoType, documentation='A vevő ÁFA alanyisági adataiVAT subjectivity data of the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 785, 3)))

CustomerInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerName'), _ImportedBinding_common.SimpleText512NotBlankType, scope=CustomerInfoType, documentation='A vevő neveName of the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 791, 3)))

CustomerInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerAddress'), _ImportedBinding_base.AddressType, scope=CustomerInfoType, documentation='A vevő címeAddress of the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 797, 3)))

CustomerInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerBankAccountNumber'), _ImportedBinding_common.BankAccountNumberType, scope=CustomerInfoType, documentation='Vevő bankszámlaszámaBank account number of the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 803, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 785, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 791, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 797, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 803, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerVatStatus')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 779, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CustomerInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerVatData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 785, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CustomerInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 791, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CustomerInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerAddress')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 797, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CustomerInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerBankAccountNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 803, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CustomerInfoType._Automaton = _BuildAutomaton_11()




CustomerVatDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber'), CustomerTaxNumberType, scope=CustomerVatDataType, documentation='Belföldi adószám, amely alatt a számlán szereplő termékbeszerzés vagy szolgáltatás igénybevétele történt. Lehet csoportazonosító szám isDomestic tax number or group identification number, under which the purchase of goods or services is done', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 835, 3)))

CustomerVatDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'communityVatNumber'), _ImportedBinding_common.CommunityVatNumberType, scope=CustomerVatDataType, documentation='Közösségi adószámCommunity tax number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 841, 3)))

CustomerVatDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thirdStateTaxId'), _ImportedBinding_common.SimpleText50NotBlankType, scope=CustomerVatDataType, documentation='Harmadik országbeli adóazonosítóThird state tax identification number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 847, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerVatDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 835, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerVatDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'communityVatNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 841, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerVatDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'thirdStateTaxId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 847, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CustomerVatDataType._Automaton = _BuildAutomaton_12()




DealerCodesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dealerCode'), _ImportedBinding_common.SimpleText100NotBlankType, scope=DealerCodesType, documentation='Beszállító kódDealer code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 861, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DealerCodesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dealerCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 861, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DealerCodesType._Automaton = _BuildAutomaton_13()




DeliveryNotesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deliveryNote'), _ImportedBinding_common.SimpleText100NotBlankType, scope=DeliveryNotesType, documentation='Szállítólevél számDelivery note', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 875, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeliveryNotesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryNote')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 875, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeliveryNotesType._Automaton = _BuildAutomaton_14()




DetailedReasonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'case'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedReasonType, documentation='Az eset leírása kóddalCase notation with code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 889, 3)))

DetailedReasonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reason'), _ImportedBinding_common.SimpleText200NotBlankType, scope=DetailedReasonType, documentation='Az eset leírása szöveggelCase notation with text', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 895, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DetailedReasonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'case')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 889, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DetailedReasonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reason')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 895, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DetailedReasonType._Automaton = _BuildAutomaton_15()




DieselOilPurchaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'purchaseLocation'), _ImportedBinding_base.SimpleAddressType, scope=DieselOilPurchaseType, documentation='Gázolaj beszerzés helyePlace of purchase of the gas oil', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 909, 3)))

DieselOilPurchaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'purchaseDate'), _ImportedBinding_base.InvoiceDateType, scope=DieselOilPurchaseType, documentation='Gázolaj beszerzés dátumaDate of purchase of gas oil', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 915, 3)))

DieselOilPurchaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vehicleRegistrationNumber'), _ImportedBinding_common.PlateNumberType, scope=DieselOilPurchaseType, documentation='Kereskedelmi jármű forgalmi rendszáma (csak betűk és számok)Registration number of vehicle (letters and numbers only)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 921, 3)))

DieselOilPurchaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dieselOilQuantity'), QuantityType, scope=DieselOilPurchaseType, documentation='Gépi bérmunka-szolgáltatás során felhasznált gázolaj mennyisége literben – Jöt. 117. § (2)Fordítandó helyett: Quantity of diesel oil used for contract work and machinery hire service in liter – Act LXVIII of 2016 on Excise Tax section 117 (2)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 927, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 927, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DieselOilPurchaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'purchaseLocation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 909, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DieselOilPurchaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'purchaseDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 915, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DieselOilPurchaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vehicleRegistrationNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 921, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DieselOilPurchaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dieselOilQuantity')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 927, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DieselOilPurchaseType._Automaton = _BuildAutomaton_16()




DiscountDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discountDescription'), _ImportedBinding_common.SimpleText255NotBlankType, scope=DiscountDataType, documentation='Az árengedmény leírásaDescription of the discount', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 941, 3)))

DiscountDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discountValue'), _ImportedBinding_base.MonetaryType, scope=DiscountDataType, documentation='Tételhez tartozó árengedmény összege a számla pénznemében, ha az egységár nem tartalmazzaTotal amount of discount per item expressed in the currency of the invoice if not included in the unit price', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 947, 3)))

DiscountDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discountRate'), RateType, scope=DiscountDataType, documentation='Tételhez tartozó árengedmény aránya, ha az egységár nem tartalmazzaRate of discount per item expressed in the currency of the invoice if not included in the unit price', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 953, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 941, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 947, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 953, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DiscountDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discountDescription')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 941, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DiscountDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discountValue')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 947, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DiscountDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discountRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 953, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DiscountDataType._Automaton = _BuildAutomaton_17()




EkaerIdsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ekaerId'), EkaerIdType, scope=EkaerIdsType, documentation='EKÁER azonosítóEKAER numbers; EKAER stands for Electronic Trade and Transport Control System', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 967, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EkaerIdsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ekaerId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 967, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EkaerIdsType._Automaton = _BuildAutomaton_18()




FiscalRepresentativeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeTaxNumber'), _ImportedBinding_base.TaxNumberType, scope=FiscalRepresentativeType, documentation='A pénzügyi képviselő adószámaTax number of the fiscal representative', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 981, 3)))

FiscalRepresentativeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeName'), _ImportedBinding_common.SimpleText512NotBlankType, scope=FiscalRepresentativeType, documentation='A pénzügyi képviselő neveName of the fiscal representative', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 987, 3)))

FiscalRepresentativeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeAddress'), _ImportedBinding_base.AddressType, scope=FiscalRepresentativeType, documentation='Pénzügyi képviselő címeAddress of the fiscal representative', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 993, 3)))

FiscalRepresentativeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeBankAccountNumber'), _ImportedBinding_common.BankAccountNumberType, scope=FiscalRepresentativeType, documentation='Pénzügyi képviselő által a számla kibocsátó (eladó) számára megnyitott bankszámla bankszámlaszámaBank account number opened by the fiscal representative for the issuer of the invoice (supplier)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 999, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 999, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FiscalRepresentativeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 981, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FiscalRepresentativeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 987, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FiscalRepresentativeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeAddress')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 993, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FiscalRepresentativeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeBankAccountNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 999, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FiscalRepresentativeType._Automaton = _BuildAutomaton_19()




GeneralLedgerAccountNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generalLedgerAccountNumber'), _ImportedBinding_common.SimpleText100NotBlankType, scope=GeneralLedgerAccountNumbersType, documentation='Főkönyvi számlaszámGeneral ledger account number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1013, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneralLedgerAccountNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generalLedgerAccountNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1013, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeneralLedgerAccountNumbersType._Automaton = _BuildAutomaton_20()




GlnNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'glnNumber'), _ImportedBinding_common.SimpleText100NotBlankType, scope=GlnNumbersType, documentation='Globális helyazonosító számGlobal location number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1027, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GlnNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'glnNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1027, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GlnNumbersType._Automaton = _BuildAutomaton_21()




InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory'), _ImportedBinding_base.InvoiceCategoryType, scope=InvoiceDetailType, documentation='A számla típusa, módosító okirat esetén az eredeti számla típusaType of invoice. In case of modification document the type of original invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1041, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryDate'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDetailType, documentation='Teljesítés dátuma (ha nem szerepel a számlán, akkor azonos a számla keltével) - ÁFA tv. 169. § g)Delivery date (if this field does not exist on the invoice, the date of the invoice should be considered as such) - section 169 (g) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1047, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryPeriodStart'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDetailType, documentation='Amennyiben a számla egy időszakra vonatkozik, akkor az időszak első napjaThe first day of the delivery, if the invoice delivery is a period', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1053, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryPeriodEnd'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDetailType, documentation='Amennyiben a számla egy időszakra vonatkozik, akkor az időszak utolsó napjaThe last day of the delivery, if the invoice delivery is a period', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1059, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceAccountingDeliveryDate'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDetailType, documentation='Számviteli teljesítés dátuma. Időszak esetén az időszak utolsó napjaDate of accounting accomplishment. In the event of a period, the last day of the period', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1065, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'periodicalSettlement'), pyxb.binding.datatypes.boolean, scope=InvoiceDetailType, documentation='Annak jelzése, ha a felek a termékértékesítés, szolgáltatás nyújtás során időszakonkénti elszámolásban vagy fizetésben állapodnak meg, vagy a termékértékesítés, szolgáltatás nyújtás ellenértékét meghatározott időpontra állapítják meg.Indicates where by agreement of the parties it gives rise to successive statements of account or successive payments relating to the supply of goods, or the supply of services, or if the consideration agreed upon for such goods and/or services applies to specific periods.', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1071, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'smallBusinessIndicator'), pyxb.binding.datatypes.boolean, scope=InvoiceDetailType, documentation='Kisadózó jelzéseMarking of low tax-bracket enterprise', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1077, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currencyCode'), _ImportedBinding_common.CurrencyType, scope=InvoiceDetailType, documentation='A számla pénzneme az ISO 4217 szabvány szerintISO 4217 currency code on the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1083, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exchangeRate'), ExchangeRateType, scope=InvoiceDetailType, documentation='HUF-tól különböző pénznem esetén az alkalmazott árfolyam: egy egység értéke HUF-banIn case any currency is used other than HUF, the applied exchange rate should be mentioned: 1 unit of the foreign currency expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1089, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utilitySettlementIndicator'), pyxb.binding.datatypes.boolean, scope=InvoiceDetailType, documentation='Közmű elszámoló számla jelölése (2013.évi CLXXXVIII törvény szerinti elszámoló számla)Marking the fact of utility settlement invoice (invoice according to Act CLXXXVIII of 2013)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1095, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'selfBillingIndicator'), pyxb.binding.datatypes.boolean, scope=InvoiceDetailType, documentation='Önszámlázás jelölése (önszámlázás esetén true)Marking the fact of self-billing (in the case of self-billing the value is true)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1101, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), _ImportedBinding_base.PaymentMethodType, scope=InvoiceDetailType, documentation='Fizetés módjaMethod of payment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1107, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentDate'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDetailType, documentation='Fizetési határidőDeadline for payment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1113, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cashAccountingIndicator'), pyxb.binding.datatypes.boolean, scope=InvoiceDetailType, documentation='Pénzforgalmi elszámolás jelölése, ha az szerepel a számlán - ÁFA tv. 169. § h). Értéke true pénzforgalmi elszámolás eseténMarking the fact of cash accounting if this is indicated on the invoice - section 169 (h) of the VAT law. The value is true in case of cash accounting', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1119, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance'), _ImportedBinding_base.InvoiceAppearanceType, scope=InvoiceDetailType, documentation='A számla vagy módosító okirat megjelenési formájaForm of appearance of the invoice or modification document', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1125, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conventionalInvoiceInfo'), ConventionalInvoiceInfoType, scope=InvoiceDetailType, documentation='A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatokOther conventionally named data to assist in invoice processing', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1131, 3)))

InvoiceDetailType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalInvoiceData'), AdditionalDataType, scope=InvoiceDetailType, documentation='A számlára vonatkozó egyéb adatOther data in relation to the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1137, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1053, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1059, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1065, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1071, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1077, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1095, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1101, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1107, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1113, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1119, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1131, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1137, 3))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1041, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1047, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryPeriodStart')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1053, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryPeriodEnd')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1059, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAccountingDeliveryDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1065, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'periodicalSettlement')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1071, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'smallBusinessIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1077, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currencyCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1083, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exchangeRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1089, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utilitySettlementIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1095, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selfBillingIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1101, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1107, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1113, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cashAccountingIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1119, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1125, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conventionalInvoiceInfo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1131, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceDetailType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalInvoiceData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1137, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceDetailType._Automaton = _BuildAutomaton_22()




InvoiceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceDataType, documentation='Számla vagy módosító okirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pontSequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1151, 3)))

InvoiceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDataType, documentation='Számla vagy módosító okirat kelte - ÁFA tv. 169. § a), ÁFA tv. 170. § (1) bek. a)Date of issue of the invoice or the modification document - section 169 (a) of the VAT law, section 170 (1) a) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1157, 3)))

InvoiceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'completenessIndicator'), pyxb.binding.datatypes.boolean, scope=InvoiceDataType, documentation='Jelöli, ha az adatszolgáltatás maga a számla (a számlán nem szerepel több adat)Indicates whether the data exchange is identical with the invoice (the invoice does not contain any more data)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1163, 3)))

InvoiceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceMain'), InvoiceMainType, scope=InvoiceDataType, documentation='Számlaadatok leírására szolgáló közös típusA common type to describe invoice information', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1169, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1151, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1157, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'completenessIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1163, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceMain')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1169, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceDataType._Automaton = _BuildAutomaton_23()




InvoiceHeadType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierInfo'), SupplierInfoType, scope=InvoiceHeadType, documentation='Számla kibocsátó (eladó) adataiData related to the issuer of the invoice (supplier)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1183, 3)))

InvoiceHeadType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerInfo'), CustomerInfoType, scope=InvoiceHeadType, documentation='Vevő adataiData related to the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1189, 3)))

InvoiceHeadType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeInfo'), FiscalRepresentativeType, scope=InvoiceHeadType, documentation='Pénzügyi képviselő adataiData related to the fiscal representative', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1195, 3)))

InvoiceHeadType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDetail'), InvoiceDetailType, scope=InvoiceHeadType, documentation='Számla részletező adatokInvoice detail adata', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1201, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1189, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1195, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceHeadType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierInfo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1183, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceHeadType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerInfo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1189, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceHeadType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fiscalRepresentativeInfo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1195, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceHeadType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDetail')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1201, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceHeadType._Automaton = _BuildAutomaton_24()




InvoiceMainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoice'), InvoiceType, scope=InvoiceMainType, documentation='Egy számla vagy módosító okirat adataiData of a single invoice or modification document', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1215, 3)))

InvoiceMainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batchInvoice'), BatchInvoiceType, scope=InvoiceMainType, documentation='Kötegelt módosító okirat adataiData of a batch of modification documents', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1221, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceMainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoice')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1215, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceMainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batchInvoice')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1221, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceMainType._Automaton = _BuildAutomaton_25()




InvoiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceReferenceType, documentation='Az eredeti számla sorszáma, melyre a módosítás vonatkozik  - ÁFA tv. 170. § (1) c)Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1235, 3)))

InvoiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modifyWithoutMaster'), pyxb.binding.datatypes.boolean, scope=InvoiceReferenceType, documentation='Annak jelzése, hogy a módosítás olyan alapszámlára hivatkozik, amelyről nem történt és nem is fog történni adatszolgáltatásIndicates whether the modification references to an original invoice which is not and will not be exchanged', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1241, 3)))

InvoiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=InvoiceReferenceType, documentation='A számlára vonatkozó módosító okirat egyedi sorszámaThe unique sequence number referring to the original invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1247, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1235, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modifyWithoutMaster')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1241, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1247, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceReferenceType._Automaton = _BuildAutomaton_26()




InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceReference'), InvoiceReferenceType, scope=InvoiceType, documentation='A módosítás vagy érvénytelenítés adataiModification or cancellation data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1261, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceHead'), InvoiceHeadType, scope=InvoiceType, documentation='A számla egészét jellemző adatokData concerning the whole invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1267, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceLines'), LinesType, scope=InvoiceType, documentation='A számlán szereplő tételek adataiProduct/service data appearing on the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1273, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeSummary'), ProductFeeSummaryType, scope=InvoiceType, documentation='Termékdíjjal kapcsolatos összesítő adatokSummary data of product charges', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1279, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceSummary'), SummaryType, scope=InvoiceType, documentation='Az ÁFA törvény szerinti összesítő adatokSummary data according to VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1285, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1261, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1273, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1279, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceReference')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1261, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceHead')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1267, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceLines')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1273, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeSummary')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1279, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceSummary')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1285, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceType._Automaton = _BuildAutomaton_27()




ItemNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemNumber'), _ImportedBinding_common.SimpleText100NotBlankType, scope=ItemNumbersType, documentation='CikkszámItem number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1299, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ItemNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1299, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ItemNumbersType._Automaton = _BuildAutomaton_28()




LineAmountsNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmountData'), LineNetAmountDataType, scope=LineAmountsNormalType, documentation='Tétel nettó adatokLine net data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1313, 3)))

LineAmountsNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineVatRate'), VatRateType, scope=LineAmountsNormalType, documentation='Adómérték vagy adómentesség jelöléseTax rate or tax exemption marking', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1319, 3)))

LineAmountsNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineVatData'), LineVatDataType, scope=LineAmountsNormalType, documentation='Tétel ÁFA adatokLine VAT data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1325, 3)))

LineAmountsNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountData'), LineGrossAmountDataType, scope=LineAmountsNormalType, documentation='Tétel bruttó adatokLine gross data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1331, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1325, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1331, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineAmountsNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmountData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1313, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineAmountsNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineVatRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1319, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LineAmountsNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineVatData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1325, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LineAmountsNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1331, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineAmountsNormalType._Automaton = _BuildAutomaton_29()




LineAmountsSimplifiedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineVatRate'), VatRateType, scope=LineAmountsSimplifiedType, documentation='Adómérték vagy adómentesség jelöléseTax rate or tax exemption marking', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1345, 3)))

LineAmountsSimplifiedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountSimplified'), _ImportedBinding_base.MonetaryType, scope=LineAmountsSimplifiedType, documentation='Tétel bruttó értéke a számla pénznemébenGross amount of the item expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1351, 3)))

LineAmountsSimplifiedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountSimplifiedHUF'), _ImportedBinding_base.MonetaryType, scope=LineAmountsSimplifiedType, documentation='Tétel bruttó értéke forintbanGross amount of the item expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1357, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineAmountsSimplifiedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineVatRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1345, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineAmountsSimplifiedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountSimplified')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1351, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineAmountsSimplifiedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountSimplifiedHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1357, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineAmountsSimplifiedType._Automaton = _BuildAutomaton_30()




LineGrossAmountDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountNormal'), _ImportedBinding_base.MonetaryType, scope=LineGrossAmountDataType, documentation='Tétel bruttó értéke a számla pénznemében. ÁFA tartalmú különbözeti adózás esetén az ellenérték.Gross amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration expressed in the currency of the invoice.', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1371, 3)))

LineGrossAmountDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountNormalHUF'), _ImportedBinding_base.MonetaryType, scope=LineGrossAmountDataType, documentation='Tétel bruttó értéke forintbanGross amount of the item expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1377, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineGrossAmountDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountNormal')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1371, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineGrossAmountDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineGrossAmountNormalHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1377, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineGrossAmountDataType._Automaton = _BuildAutomaton_31()




LineModificationReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNumberReference'), _ImportedBinding_base.LineNumberType, scope=LineModificationReferenceType, documentation='Az eredeti számla módosítással érintett tételének sorszáma (lineNumber). Új tétel létrehozása esetén az új tétel sorszáma, a meglévő tételsorok számozásának folytatásakéntLine number of the original invoice, which the modification occurs with. In case of create operation the tag shall contain the new line number, as a sequential increment of the the existing lines set', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1391, 3)))

LineModificationReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineOperation'), LineOperationType, scope=LineModificationReferenceType, documentation='A számlatétel módosításának jellegeLine modification type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1397, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineModificationReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNumberReference')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1391, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineModificationReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1397, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineModificationReferenceType._Automaton = _BuildAutomaton_32()




LineNetAmountDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmount'), _ImportedBinding_base.MonetaryType, scope=LineNetAmountDataType, documentation='Tétel nettó összege a számla pénznemében. ÁFA tartalmú különbözeti adózás esetén az ellenérték áfa összegével csökkentett értéke a számla pénznemében.Net amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration reduced with the amount of VAT, expressed in the currency of the invoice.', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1411, 3)))

LineNetAmountDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmountHUF'), _ImportedBinding_base.MonetaryType, scope=LineNetAmountDataType, documentation='Tétel nettó összege forintban. ÁFA tartalmú különbözeti adózás esetén az ellenérték áfa összegével csökkentett értéke forintban.Net amount of the item expressed in HUF. Net amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration reduced with the amount of VAT, expressed in HUF.', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1417, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineNetAmountDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1411, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineNetAmountDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNetAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1417, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineNetAmountDataType._Automaton = _BuildAutomaton_33()




LinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mergedItemIndicator'), pyxb.binding.datatypes.boolean, scope=LinesType, documentation='Jelöli, ha az adatszolgáltatás méretcsökkentés miatt összevont soradatokat tartalmazIndicates whether the data exchange contains merged line data due to size reduction', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1431, 3)))

LinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'line'), LineType, scope=LinesType, documentation='Termék/szolgáltatás tételProduct / service item', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1437, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mergedItemIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1431, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'line')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1437, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LinesType._Automaton = _BuildAutomaton_34()




LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNumber'), _ImportedBinding_base.LineNumberType, scope=LineType, documentation='A tétel sorszámaSequential number of the item', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1451, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineModificationReference'), LineModificationReferenceType, scope=LineType, documentation='Módosításról történő adatszolgáltatás esetén a tételsor módosítás jellegének jelöléseMarking the goal of modification of the line (in the case of data supply about changes/updates only)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1457, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referencesToOtherLines'), ReferencesToOtherLinesType, scope=LineType, documentation='Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükségesReferences to connected items if it is necessary according to VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1463, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'advanceData'), AdvanceDataType, scope=LineType, documentation='Előleghez kapcsolódó adatokAdvance related data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1469, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productCodes'), ProductCodesType, scope=LineType, documentation='TermékkódokProduct codes', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1475, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineExpressionIndicator'), pyxb.binding.datatypes.boolean, scope=LineType, documentation='Értéke true, ha a tétel mennyiségi egysége természetes mértékegységben kifejezhetőThe value is true if the unit of measure of the invoice item is expressible in natural unit', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1481, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNatureIndicator'), LineNatureIndicatorType, scope=LineType, documentation='Adott tételsor termékértékesítés vagy szolgáltatás nyújtás jellegének jelzéseIndication of the nature of the supply of goods or services on a given line', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1487, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineDescription'), _ImportedBinding_common.SimpleText512NotBlankType, scope=LineType, documentation='A termék vagy szolgáltatás megnevezéseName / description of the product or service', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1493, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quantity'), QuantityType, scope=LineType, documentation='MennyiségQuantity', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1499, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unitOfMeasure'), UnitOfMeasureType, scope=LineType, documentation='A számlán szereplő mennyiségi egység kanonikus kifejezése az interfész specifikáció szerintCanonical representation of the unit of measure of the invoice, according to the interface specification', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1505, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unitOfMeasureOwn'), _ImportedBinding_common.SimpleText50NotBlankType, scope=LineType, documentation='A számlán szereplő mennyiségi egység literális kifejezéseLiteral unit of measure of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1511, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unitPrice'), QuantityType, scope=LineType, documentation='Egységár a számla pénznemében. Egyszerűsített számla esetén bruttó, egyéb esetben nettó egységárUnit price expressed in the currency of the invoice In the event of simplified invoices gross unit price, in other cases net unit price', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1517, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unitPriceHUF'), QuantityType, scope=LineType, documentation='Egységár forintbanUnit price expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1523, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineDiscountData'), DiscountDataType, scope=LineType, documentation='A tételhez tartozó árengedmény adatokDiscount data in relation to the item', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1529, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineAmountsNormal'), LineAmountsNormalType, scope=LineType, documentation='Normál (nem egyszerűsített) számla esetén (beleértve a gyűjtőszámlát) kitöltendő tétel érték adatok.Item value data to be completed in case of normal (not simplified, but including aggregated) invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1536, 4)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineAmountsSimplified'), LineAmountsSimplifiedType, scope=LineType, documentation='Egyszerűsített számla esetén kitöltendő tétel érték adatokItem value data to be completed in case of simplified invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1542, 4)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intermediatedService'), pyxb.binding.datatypes.boolean, scope=LineType, documentation='Értéke true ha a tétel közvetített szolgáltatás - Számviteli tv. 3.§ (4) 1The value is true if the item is an intermediated service - paragraph (4) 1 of the Article 3 of Accounting Act', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1549, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aggregateInvoiceLineData'), AggregateInvoiceLineDataType, scope=LineType, documentation='Gyűjtő számla adatokAggregate invoice data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1555, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'newTransportMean'), NewTransportMeanType, scope=LineType, documentation='Új közlekedési eszköz értékesítés ÁFA tv. 89 § ill. 169 § o)Supply of new means of transport - section 89 § and 169 (o) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1561, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'depositIndicator'), pyxb.binding.datatypes.boolean, scope=LineType, documentation='Értéke true, ha a tétel betétdíj jellegűThe value is true if the item is bottle/container deposit', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1567, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'obligatedForProductFee'), pyxb.binding.datatypes.boolean, scope=LineType, documentation='Értéke true ha a tételt termékdíj fizetési kötelezettség terheliThe value is true if the item is liable to product fee', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1573, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GPCExcise'), _ImportedBinding_base.MonetaryType, scope=LineType, documentation='Földgáz, villamos energia, szén jövedéki adója forintban - Jöt. 118. § (2)Excise duty on natural gas, electricity and coal in Hungarian forints – paragraph (2), Section 118 of the Act on Excise Duties', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1579, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dieselOilPurchase'), DieselOilPurchaseType, scope=LineType, documentation='Gázolaj adózottan történő beszerzésének adatai – 45/2016 (XI. 29.) NGM rendelet 75. § (1) a)Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1585, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'netaDeclaration'), pyxb.binding.datatypes.boolean, scope=LineType, documentation='Értéke true, ha a Neta tv-ben meghatározott adókötelezettség az adó alanyát terheli. 2011. évi CIII. tv. 3.§(2)Value is true, if the taxable person is liable for tax obligation determined in the Act on Public Health Product Tax (Neta tv.). Paragraph (2), Section 3 of the Act CIII of 2011', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1591, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeClause'), ProductFeeClauseType, scope=LineType, documentation='A környezetvédelmi termékdíjról szóló 2011. évi LXXXV. tv. szerinti, tételre vonatkozó záradékokClauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1597, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineProductFeeContent'), ProductFeeDataType, scope=LineType, documentation="A tétel termékdíj tartalmára vonatkozó adatokData on the content of the line's product charge", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1603, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conventionalLineInfo'), ConventionalInvoiceInfoType, scope=LineType, documentation='A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatokOther conventionally named data to assist in invoice processing', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1609, 3)))

LineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalLineData'), AdditionalDataType, scope=LineType, documentation='A termék/szolgáltatás tételhez kapcsolódó, további adatOther data in relation to the product / service item', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1615, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1457, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1463, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1469, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1475, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1487, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1493, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1499, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1505, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1511, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1517, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1523, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1529, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1536, 4))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1542, 4))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1549, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1555, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1561, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1567, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1573, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1579, 3))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1585, 3))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1591, 3))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1597, 3))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1603, 3))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1609, 3))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1615, 3))
    counters.add(cc_25)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1451, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineModificationReference')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1457, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencesToOtherLines')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1463, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'advanceData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1469, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productCodes')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1475, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineExpressionIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1481, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNatureIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1487, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineDescription')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1493, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quantity')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1499, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unitOfMeasure')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1505, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unitOfMeasureOwn')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1511, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unitPrice')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1517, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unitPriceHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1523, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineDiscountData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1529, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineAmountsNormal')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1536, 4))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineAmountsSimplified')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1542, 4))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'intermediatedService')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1549, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aggregateInvoiceLineData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1555, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'newTransportMean')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1561, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'depositIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1567, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'obligatedForProductFee')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1573, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GPCExcise')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1579, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dieselOilPurchase')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1585, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'netaDeclaration')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1591, 3))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeClause')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1597, 3))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineProductFeeContent')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1603, 3))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conventionalLineInfo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1609, 3))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(LineType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalLineData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1615, 3))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    st_27._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineType._Automaton = _BuildAutomaton_35()




LineVatDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineVatAmount'), _ImportedBinding_base.MonetaryType, scope=LineVatDataType, documentation='Tétel ÁFA összege a számla pénznemébenVAT amount of the item expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1629, 3)))

LineVatDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineVatAmountHUF'), _ImportedBinding_base.MonetaryType, scope=LineVatDataType, documentation='Tétel ÁFA összege forintbanVAT amount of the item expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1635, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LineVatDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineVatAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1629, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineVatDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineVatAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1635, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineVatDataType._Automaton = _BuildAutomaton_36()




MaterialNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'materialNumber'), _ImportedBinding_common.SimpleText100NotBlankType, scope=MaterialNumbersType, documentation='AnyagszámMaterial number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1649, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MaterialNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'materialNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1649, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MaterialNumbersType._Automaton = _BuildAutomaton_37()




NewTransportMeanType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'brand'), _ImportedBinding_common.SimpleText50NotBlankType, scope=NewTransportMeanType, documentation='Gyártmány/típusProduct / type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1663, 3)))

NewTransportMeanType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serialNum'), _ImportedBinding_common.SimpleText255NotBlankType, scope=NewTransportMeanType, documentation='Alvázszám/gyári szám/Gyártási számChassis number / serial number / product number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1669, 3)))

NewTransportMeanType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'engineNum'), _ImportedBinding_common.SimpleText255NotBlankType, scope=NewTransportMeanType, documentation='MotorszámEngine number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1675, 3)))

NewTransportMeanType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstEntryIntoService'), _ImportedBinding_base.InvoiceDateType, scope=NewTransportMeanType, documentation='Első forgalomba helyezés időpontjaFirst entry into service', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1681, 3)))

NewTransportMeanType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vehicle'), VehicleType, scope=NewTransportMeanType, documentation='Szárazföldi közlekedési eszköz további adataiOther data in relation to motorised land vehicle', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1688, 4)))

NewTransportMeanType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vessel'), VesselType, scope=NewTransportMeanType, documentation='Vízi jármű adataiData of vessel', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1694, 4)))

NewTransportMeanType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aircraft'), AircraftType, scope=NewTransportMeanType, documentation='Légi közlekedési eszközAircraft', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1700, 4)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1663, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1669, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1675, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1681, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NewTransportMeanType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'brand')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1663, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NewTransportMeanType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serialNum')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1669, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NewTransportMeanType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'engineNum')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1675, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NewTransportMeanType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstEntryIntoService')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1681, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NewTransportMeanType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vehicle')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1688, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NewTransportMeanType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vessel')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1694, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NewTransportMeanType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aircraft')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1700, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NewTransportMeanType._Automaton = _BuildAutomaton_38()




OrderNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderNumber'), _ImportedBinding_common.SimpleText100NotBlankType, scope=OrderNumbersType, documentation='MegrendelésszámOrder number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1715, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1715, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderNumbersType._Automaton = _BuildAutomaton_39()




PaymentEvidenceDocumentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'evidenceDocumentNo'), _ImportedBinding_common.SimpleText50NotBlankType, scope=PaymentEvidenceDocumentDataType, documentation='Számla sorszáma vagy egyéb okirat azonosító számaSequential number of the invoice, or other document considered as such', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1729, 3)))

PaymentEvidenceDocumentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'evidenceDocumentDate'), _ImportedBinding_base.InvoiceDateType, scope=PaymentEvidenceDocumentDataType, documentation='Számla kelteDate of issue of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1735, 3)))

PaymentEvidenceDocumentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'obligatedName'), _ImportedBinding_common.SimpleText255NotBlankType, scope=PaymentEvidenceDocumentDataType, documentation='Kötelezett neveName of obligator', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1741, 3)))

PaymentEvidenceDocumentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'obligatedAddress'), _ImportedBinding_base.AddressType, scope=PaymentEvidenceDocumentDataType, documentation='Kötelezett címeAddress of obligator', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1747, 3)))

PaymentEvidenceDocumentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'obligatedTaxNumber'), _ImportedBinding_base.TaxNumberType, scope=PaymentEvidenceDocumentDataType, documentation='A kötelezett adószámaTax number of obligated', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1753, 3)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentEvidenceDocumentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'evidenceDocumentNo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1729, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentEvidenceDocumentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'evidenceDocumentDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1735, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentEvidenceDocumentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'obligatedName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1741, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentEvidenceDocumentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'obligatedAddress')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1747, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentEvidenceDocumentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'obligatedTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1753, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentEvidenceDocumentDataType._Automaton = _BuildAutomaton_40()




ProductCodesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productCode'), ProductCodeType, scope=ProductCodesType, documentation='TermékkódProduct code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1767, 3)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductCodesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1767, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductCodesType._Automaton = _BuildAutomaton_41()




ProductCodeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productCodeCategory'), ProductCodeCategoryType, scope=ProductCodeType, documentation='A termékkód fajtájának (pl. VTSZ, CsK, stb.) jelöléseThe kind of product code (f. ex. VTSZ, CsK, etc.)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1781, 3)))

ProductCodeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productCodeValue'), ProductCodeValueType, scope=ProductCodeType, documentation='A termékkód értéke nem saját termékkód eseténThe value of (not own) product code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1788, 4)))

ProductCodeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productCodeOwnValue'), _ImportedBinding_common.SimpleText255NotBlankType, scope=ProductCodeType, documentation='Saját termékkód értékeOwn product code value', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1794, 4)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProductCodeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productCodeCategory')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1781, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductCodeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productCodeValue')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1788, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductCodeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productCodeOwnValue')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1794, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductCodeType._Automaton = _BuildAutomaton_42()




ProductFeeClauseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeTakeoverData'), ProductFeeTakeoverDataType, scope=ProductFeeClauseType, documentation='A környezetvédelmi termékdíj kötelezettség átvállalásával kapcsolatos adatokData in connection with takeover of environmental protection product fee', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1809, 3)))

ProductFeeClauseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerDeclaration'), CustomerDeclarationType, scope=ProductFeeClauseType, documentation='Ha az eladó a vevő nyilatkozata alapján mentesül a termékdíj megfizetése alól, akkor az érintett termékáramShould the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1815, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductFeeClauseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeTakeoverData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1809, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductFeeClauseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerDeclaration')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1815, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductFeeClauseType._Automaton = _BuildAutomaton_43()




ProductFeeDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeCode'), ProductCodeType, scope=ProductFeeDataType, documentation='Termékdíj kód (Kt vagy Csk)Product charges code (Kt or Csk code)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1829, 3)))

ProductFeeDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeQuantity'), QuantityType, scope=ProductFeeDataType, documentation='A termékdíjjal érintett termék mennyiségeQuantity of product, according to product charge', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1835, 3)))

ProductFeeDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeMeasuringUnit'), ProductFeeMeasuringUnitType, scope=ProductFeeDataType, documentation='A díjtétel egysége (kg vagy darab)Unit of the rate (kg or piece)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1841, 3)))

ProductFeeDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeRate'), _ImportedBinding_base.MonetaryType, scope=ProductFeeDataType, documentation='A termékdíj díjtétele (HUF/egység)Product fee rate (HUF/unit)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1847, 3)))

ProductFeeDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeAmount'), _ImportedBinding_base.MonetaryType, scope=ProductFeeDataType, documentation='Termékdíj összege forintbanAmount in Hungarian forints of the product fee', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1853, 3)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProductFeeDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1829, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProductFeeDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeQuantity')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1835, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProductFeeDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeMeasuringUnit')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1841, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProductFeeDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1847, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductFeeDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1853, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductFeeDataType._Automaton = _BuildAutomaton_44()




ProductFeeSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeOperation'), ProductFeeOperationType, scope=ProductFeeSummaryType, documentation='Annak jelzése, hogy a termékdíj összesítés visszaigénylésre (REFUND) vagy raktárba történő beszállításra (DEPOSIT) vonatkozikIndicating whether the the product fee summary concerns refund or deposit', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1867, 3)))

ProductFeeSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productFeeData'), ProductFeeDataType, scope=ProductFeeSummaryType, documentation='Termékdíj adatokProduct charges data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1873, 3)))

ProductFeeSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productChargeSum'), _ImportedBinding_base.MonetaryType, scope=ProductFeeSummaryType, documentation='Termékdíj összesenAggregate product charges', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1879, 3)))

ProductFeeSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentEvidenceDocumentData'), PaymentEvidenceDocumentDataType, scope=ProductFeeSummaryType, documentation='A termékdíj bevallását igazoló dokumentum adatai a 2011. évi LXXXV. tv. 13. § (3) szerint és a 25. § (3) szerintData of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1885, 3)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1885, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProductFeeSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1867, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProductFeeSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productFeeData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1873, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductFeeSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productChargeSum')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1879, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProductFeeSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentEvidenceDocumentData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1885, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductFeeSummaryType._Automaton = _BuildAutomaton_45()




ProductFeeTakeoverDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'takeoverReason'), TakeoverType, scope=ProductFeeTakeoverDataType, documentation='Az átvállalás iránya és jogszabályi alapjaDirection and legal base of takeover', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1899, 3)))

ProductFeeTakeoverDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'takeoverAmount'), _ImportedBinding_base.MonetaryType, scope=ProductFeeTakeoverDataType, documentation='Az átvállalt termékdíj összege forintban, ha a vevő vállalja át az eladó termékdíj-kötelezettségétAmount in Hungarian forints of the product fee taken over if the purchaser takes over the supplier’s product fee liability', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1905, 3)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1905, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductFeeTakeoverDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'takeoverReason')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1899, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProductFeeTakeoverDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'takeoverAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1905, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductFeeTakeoverDataType._Automaton = _BuildAutomaton_46()




ProjectNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'projectNumber'), _ImportedBinding_common.SimpleText100NotBlankType, scope=ProjectNumbersType, documentation='ProjektszámProject number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1919, 3)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProjectNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'projectNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1919, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProjectNumbersType._Automaton = _BuildAutomaton_47()




ReferencesToOtherLinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referenceToOtherLine'), _ImportedBinding_base.LineNumberType, scope=ReferencesToOtherLinesType, documentation='Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükségesReferences to connected items if it is necessary according to VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1933, 3)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferencesToOtherLinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referenceToOtherLine')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1933, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferencesToOtherLinesType._Automaton = _BuildAutomaton_48()




ShippingDatesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shippingDate'), _ImportedBinding_common.SimpleText100NotBlankType, scope=ShippingDatesType, documentation='Szállítási dátumShipping date', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1947, 3)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShippingDatesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shippingDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1947, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ShippingDatesType._Automaton = _BuildAutomaton_49()




SummaryByVatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRate'), VatRateType, scope=SummaryByVatRateType, documentation='Adómérték vagy adómentesség jelöléseMarking the tax rate or the fact of tax exemption', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1961, 3)))

SummaryByVatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetData'), VatRateNetDataType, scope=SummaryByVatRateType, documentation='Adott adómértékhez tartozó nettó adatokNet data of given tax rate', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1967, 3)))

SummaryByVatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatData'), VatRateVatDataType, scope=SummaryByVatRateType, documentation='Adott adómértékhez tartozó ÁFA adatokVAT data of given tax rate', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1973, 3)))

SummaryByVatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossData'), VatRateGrossDataType, scope=SummaryByVatRateType, documentation='Adott adómértékhez tartozó bruttó adatokGross data of given tax rate', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1979, 3)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1979, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryByVatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1961, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryByVatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1967, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SummaryByVatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1973, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SummaryByVatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1979, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SummaryByVatRateType._Automaton = _BuildAutomaton_50()




SummaryGrossDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceGrossAmount'), _ImportedBinding_base.MonetaryType, scope=SummaryGrossDataType, documentation='A számla bruttó összege a számla pénznemébenGross amount of the invoice expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1993, 3)))

SummaryGrossDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceGrossAmountHUF'), _ImportedBinding_base.MonetaryType, scope=SummaryGrossDataType, documentation='A számla bruttó összege forintbanGross amount of the invoice expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1999, 3)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryGrossDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceGrossAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1993, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SummaryGrossDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceGrossAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1999, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SummaryGrossDataType._Automaton = _BuildAutomaton_51()




SummaryNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summaryByVatRate'), SummaryByVatRateType, scope=SummaryNormalType, documentation='Összesítés ÁFA-mérték szerintCalculation of invoice totals per VAT rates', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2013, 3)))

SummaryNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount'), _ImportedBinding_base.MonetaryType, scope=SummaryNormalType, documentation='A számla nettó összege a számla pénznemébenNet amount of the invoice expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2019, 3)))

SummaryNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF'), _ImportedBinding_base.MonetaryType, scope=SummaryNormalType, documentation='A számla nettó összege forintbanNet amount of the invoice expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2025, 3)))

SummaryNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount'), _ImportedBinding_base.MonetaryType, scope=SummaryNormalType, documentation='A számla ÁFA összege a számla pénznemébenVAT amount of the invoice expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2031, 3)))

SummaryNormalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF'), _ImportedBinding_base.MonetaryType, scope=SummaryNormalType, documentation='A számla ÁFA összege forintbanVAT amount of the invoice expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2037, 3)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'summaryByVatRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2013, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2019, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2025, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2031, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SummaryNormalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2037, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SummaryNormalType._Automaton = _BuildAutomaton_52()




SummarySimplifiedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRate'), VatRateType, scope=SummarySimplifiedType, documentation='Adómérték vagy adómentesség jelöléseMarking the tax rate or the fact of tax exemption', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2051, 3)))

SummarySimplifiedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatContentGrossAmount'), _ImportedBinding_base.MonetaryType, scope=SummarySimplifiedType, documentation='Az adott adótartalomhoz tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege a számla pénznemébenThe gross amount of the sale or service for the given tax amount in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2057, 3)))

SummarySimplifiedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatContentGrossAmountHUF'), _ImportedBinding_base.MonetaryType, scope=SummarySimplifiedType, documentation='Az adott adótartalomhoz tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege forintbanThe gross amount of the sale or service for the given tax amount in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2063, 3)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummarySimplifiedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2051, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummarySimplifiedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatContentGrossAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2057, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SummarySimplifiedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatContentGrossAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2063, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SummarySimplifiedType._Automaton = _BuildAutomaton_53()




SummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summaryNormal'), SummaryNormalType, scope=SummaryType, documentation='Számla összesítés (nem egyszerűsített számla esetén)Calculation of invoice totals (not simplified invoice)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2078, 4)))

SummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summarySimplified'), SummarySimplifiedType, scope=SummaryType, documentation='Egyszerűsített számla összesítésCalculation of simplified invoice totals', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2084, 4)))

SummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summaryGrossData'), SummaryGrossDataType, scope=SummaryType, documentation='A számla összesítő bruttó adataiGross data of the invoice summary', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2091, 3)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2091, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'summaryNormal')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2078, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'summarySimplified')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2084, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'summaryGrossData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2091, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SummaryType._Automaton = _BuildAutomaton_54()




SupplierCompanyCodesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierCompanyCode'), _ImportedBinding_common.SimpleText100NotBlankType, scope=SupplierCompanyCodesType, documentation='Az eladó vállalati kódjaCompany code of the supplier', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2105, 3)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SupplierCompanyCodesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierCompanyCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2105, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupplierCompanyCodesType._Automaton = _BuildAutomaton_55()




SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), _ImportedBinding_base.TaxNumberType, scope=SupplierInfoType, documentation='Belföldi adószám vagy csoportazonosító számTax number or group identification number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2119, 3)))

SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber'), _ImportedBinding_base.TaxNumberType, scope=SupplierInfoType, documentation='Csoport tag adószáma, ha a termékbeszerzés vagy szolgáltatás nyújtása csoportazonosító szám alatt történtTax number of group member, when the supply of goods or services is done under group identification number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2125, 3)))

SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'communityVatNumber'), _ImportedBinding_common.CommunityVatNumberType, scope=SupplierInfoType, documentation='Közösségi adószámCommunity tax number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2131, 3)))

SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierName'), _ImportedBinding_common.SimpleText512NotBlankType, scope=SupplierInfoType, documentation='Az eladó (szállító) neveName of the seller (supplier)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2137, 3)))

SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierAddress'), _ImportedBinding_base.AddressType, scope=SupplierInfoType, documentation='Az eladó (szállító) címeAddress of the seller (supplier)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2143, 3)))

SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierBankAccountNumber'), _ImportedBinding_common.BankAccountNumberType, scope=SupplierInfoType, documentation='Az eladó (szállító) bankszámlaszámaBank account number of the seller (supplier)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2149, 3)))

SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'individualExemption'), pyxb.binding.datatypes.boolean, scope=SupplierInfoType, documentation='Értéke true, amennyiben az eladó (szállító) alanyi ÁFA mentesValue is true if the seller (supplier) is individually exempted from VAT', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2155, 3)))

SupplierInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exciseLicenceNum'), _ImportedBinding_common.SimpleText50NotBlankType, scope=SupplierInfoType, documentation='Az eladó adóraktári engedélyének vagy jövedéki engedélyének száma (2016. évi LXVIII. tv.)Number of supplier’s tax warehouse license or excise license (Act LXVIII of 2016)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2161, 3)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2125, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2131, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2149, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2155, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2161, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2119, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2125, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'communityVatNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2131, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2137, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierAddress')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2143, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierBankAccountNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2149, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'individualExemption')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2155, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplierInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exciseLicenceNum')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2161, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupplierInfoType._Automaton = _BuildAutomaton_56()




VatAmountMismatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRate'), RateType, scope=VatAmountMismatchType, documentation='Adómérték, adótartalomVAT rate, VAT content', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2175, 3)))

VatAmountMismatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'case'), _ImportedBinding_common.SimpleText50NotBlankType, scope=VatAmountMismatchType, documentation='Az eset leírása kóddalCase notation with code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2181, 3)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VatAmountMismatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2175, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatAmountMismatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'case')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2181, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VatAmountMismatchType._Automaton = _BuildAutomaton_57()




VatRateGrossDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossAmount'), _ImportedBinding_base.MonetaryType, scope=VatRateGrossDataType, documentation='Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege a számla pénznemébenGross amount of sales or service delivery under a given tax rate expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2195, 3)))

VatRateGrossDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossAmountHUF'), _ImportedBinding_base.MonetaryType, scope=VatRateGrossDataType, documentation='Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege forintbanGross amount of sales or service delivery under a given tax rate expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2201, 3)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VatRateGrossDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2195, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateGrossDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateGrossAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2201, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VatRateGrossDataType._Automaton = _BuildAutomaton_58()




VatRateNetDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetAmount'), _ImportedBinding_base.MonetaryType, scope=VatRateNetDataType, documentation='Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás nettó összege a számla pénznemébenNet amount of sales or service delivery under a given tax rate expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2215, 3)))

VatRateNetDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetAmountHUF'), _ImportedBinding_base.MonetaryType, scope=VatRateNetDataType, documentation='Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás nettó összege forintbanNet amount of sales or service delivery under a given tax rate expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2221, 3)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VatRateNetDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2215, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateNetDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateNetAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2221, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VatRateNetDataType._Automaton = _BuildAutomaton_59()




VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatPercentage'), RateType, scope=VatRateType, documentation='Az alkalmazott adó mértéke - ÁFA tv. 169. § j)Applied tax rate - section 169 (j) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2235, 3)))

VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatContent'), RateType, scope=VatRateType, documentation='ÁFA tartalom egyszerűsített számla eseténVAT content in case of simplified invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2241, 3)))

VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatExemption'), DetailedReasonType, scope=VatRateType, documentation='Az adómentesség jelölése - ÁFA tv. 169. § m)Marking tax exemption -  section 169 (m) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2247, 3)))

VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatOutOfScope'), DetailedReasonType, scope=VatRateType, documentation='Az ÁFA törvény hatályán kívüliOut of scope of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2253, 3)))

VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatDomesticReverseCharge'), pyxb.binding.datatypes.boolean, scope=VatRateType, documentation='A belföldi fordított adózás jelölése - ÁFA tv. 142. §Marking the national is reverse charge taxation - section 142 of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2259, 3), fixed=True, unicode_default='true'))

VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'marginSchemeIndicator'), MarginSchemeType, scope=VatRateType, documentation='Különbözet szerinti szabályozás jelölése - ÁFA tv. 169. § p) q)Marking the margin-scheme taxation as per section 169 (p)(q)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2265, 3)))

VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatAmountMismatch'), VatAmountMismatchType, scope=VatRateType, documentation='Adóalap és felszámított adó eltérésének eseteiDifferent cases of mismatching tax base and levied tax', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2271, 3)))

VatRateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'noVatCharge'), pyxb.binding.datatypes.boolean, scope=VatRateType, documentation='Nincs felszámított áfa a 17. § alapjánNo VAT charged under Section 17', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2277, 3), fixed=True, unicode_default='true'))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatPercentage')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2235, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatContent')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2241, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatExemption')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2247, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatOutOfScope')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2253, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatDomesticReverseCharge')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2259, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'marginSchemeIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2265, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatAmountMismatch')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2271, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'noVatCharge')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2277, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VatRateType._Automaton = _BuildAutomaton_60()




VatRateVatDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatAmount'), _ImportedBinding_base.MonetaryType, scope=VatRateVatDataType, documentation='Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás ÁFA összege a számla pénznemébenVAT amount of sales or service delivery under a given tax rate expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2291, 3)))

VatRateVatDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatAmountHUF'), _ImportedBinding_base.MonetaryType, scope=VatRateVatDataType, documentation='Az adott adómértékhez tartozó értékesítés vagy szolgáltatásnyújtás ÁFA összege forintbanVAT amount of sales or service delivery under a given tax rate expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2297, 3)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VatRateVatDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2291, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VatRateVatDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatRateVatAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2297, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VatRateVatDataType._Automaton = _BuildAutomaton_61()




VehicleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'engineCapacity'), QuantityType, scope=VehicleType, documentation='Hengerűrtartalom köbcentiméterbenEngine capacity in cubic centimetre', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2311, 3)))

VehicleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'enginePower'), QuantityType, scope=VehicleType, documentation='Teljesítmény kW-banEngine power in kW', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2317, 3)))

VehicleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kms'), QuantityType, scope=VehicleType, documentation='Futott kilométerek számaTravelled distance in km', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2323, 3)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VehicleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'engineCapacity')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2311, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VehicleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'enginePower')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2317, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VehicleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kms')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2323, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VehicleType._Automaton = _BuildAutomaton_62()




VesselType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'length'), QuantityType, scope=VesselType, documentation='Hajó hossza méterbenLength of hull in metre', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2337, 3)))

VesselType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityReferred'), pyxb.binding.datatypes.boolean, scope=VesselType, documentation='Értéke true, ha a jármű az ÁFA tv. 259.§ 25. b) szerinti kivétel alá tartozikThe value is true if the means of transport is exempt from VAT as per section 259 [25] (b)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2343, 3)))

VesselType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sailedHours'), QuantityType, scope=VesselType, documentation='Hajózott órák számaNumber of sailed hours', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2349, 3)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VesselType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'length')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2337, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VesselType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityReferred')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2343, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VesselType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sailedHours')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 2349, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VesselType._Automaton = _BuildAutomaton_63()




CustomerTaxNumberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber'), _ImportedBinding_base.TaxNumberType, scope=CustomerTaxNumberType, documentation='Csoport tag adószáma, ha a termékbeszerzés vagy szolgáltatás igénybevétele csoportazonosító szám alatt történtTax number of group member, when the purchase of goods or services is done under group identification number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 819, 5)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 315, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 321, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 819, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerTaxNumberType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_base, 'taxpayerId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 309, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CustomerTaxNumberType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_base, 'vatCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 315, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CustomerTaxNumberType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_base, 'countyCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 321, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CustomerTaxNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 819, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CustomerTaxNumberType._Automaton = _BuildAutomaton_64()




def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1151, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1157, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'completenessIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1163, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceMain')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceData.xsd', 1169, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_65()

