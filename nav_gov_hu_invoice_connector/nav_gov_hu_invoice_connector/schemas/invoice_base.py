# generated/base.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a30801ed5a1daaaef9b1ec0b2b3dc6ff84952aca
# Generated 2022-06-05 12:05:14.792424 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://schemas.nav.gov.hu/OSA/3.0/base [xmlns:base]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.nav.gov.hu/OSA/3.0/base', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}InvoiceDateType
class InvoiceDateType (pyxb.binding.datatypes.date):

    """Dátum típus az Online Számla rendszerbenDate type in the Online Invoice system"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceDateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 68, 1)
    _Documentation = 'Dátum típus az Online Számla rendszerbenDate type in the Online Invoice system'
InvoiceDateType._CF_pattern = pyxb.binding.facets.CF_pattern()
InvoiceDateType._CF_pattern.addPattern(pattern='\\d{4}-\\d{2}-\\d{2}')
InvoiceDateType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=InvoiceDateType, value=pyxb.binding.datatypes.date('2010-01-01'))
InvoiceDateType._InitializeFacetMap(InvoiceDateType._CF_pattern,
   InvoiceDateType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'InvoiceDateType', InvoiceDateType)
_module_typeBindings.InvoiceDateType = InvoiceDateType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}InvoiceIndexType
class InvoiceIndexType (pyxb.binding.datatypes.int):

    """Sorszám típus az Online Számla rendszerbenIndex type in the Online Invoice system"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceIndexType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 78, 1)
    _Documentation = 'Sorszám típus az Online Számla rendszerbenIndex type in the Online Invoice system'
InvoiceIndexType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=InvoiceIndexType, value=pyxb.binding.datatypes.int(1))
InvoiceIndexType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=InvoiceIndexType, value=pyxb.binding.datatypes.int(100))
InvoiceIndexType._InitializeFacetMap(InvoiceIndexType._CF_minInclusive,
   InvoiceIndexType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'InvoiceIndexType', InvoiceIndexType)
_module_typeBindings.InvoiceIndexType = InvoiceIndexType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}InvoiceTimestampType
class InvoiceTimestampType (pyxb.binding.datatypes.dateTime):

    """Időbélyeg típus az Online Számla rendszerbenTimestamp type in the Online Invoice system"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceTimestampType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 88, 1)
    _Documentation = 'Időbélyeg típus az Online Számla rendszerbenTimestamp type in the Online Invoice system'
InvoiceTimestampType._CF_pattern = pyxb.binding.facets.CF_pattern()
InvoiceTimestampType._CF_pattern.addPattern(pattern='\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z')
InvoiceTimestampType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=InvoiceTimestampType, value=pyxb.binding.datatypes.dateTime('2010-01-01T00:00:00Z'))
InvoiceTimestampType._InitializeFacetMap(InvoiceTimestampType._CF_pattern,
   InvoiceTimestampType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'InvoiceTimestampType', InvoiceTimestampType)
_module_typeBindings.InvoiceTimestampType = InvoiceTimestampType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}InvoiceUnboundedIndexType
class InvoiceUnboundedIndexType (pyxb.binding.datatypes.int):

    """Sorszám típus kötegelt számlaművelethez az Online Számla rendszerbenIndex type for batch invoice operation in the Online Invoice system"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceUnboundedIndexType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 98, 1)
    _Documentation = 'Sorszám típus kötegelt számlaművelethez az Online Számla rendszerbenIndex type for batch invoice operation in the Online Invoice system'
InvoiceUnboundedIndexType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=InvoiceUnboundedIndexType, value=pyxb.binding.datatypes.int(1))
InvoiceUnboundedIndexType._InitializeFacetMap(InvoiceUnboundedIndexType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'InvoiceUnboundedIndexType', InvoiceUnboundedIndexType)
_module_typeBindings.InvoiceUnboundedIndexType = InvoiceUnboundedIndexType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}LineNumberType
class LineNumberType (pyxb.binding.datatypes.nonNegativeInteger):

    """Tételszám típusLine number type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 107, 1)
    _Documentation = 'Tételszám típusLine number type'
LineNumberType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=LineNumberType, value=pyxb.binding.datatypes.nonNegativeInteger(1))
LineNumberType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(20))
LineNumberType._InitializeFacetMap(LineNumberType._CF_minInclusive,
   LineNumberType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'LineNumberType', LineNumberType)
_module_typeBindings.LineNumberType = LineNumberType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}InvoiceAppearanceType
class InvoiceAppearanceType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Számla megjelenési formája típusForm of appearance of the invoice type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceAppearanceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 10, 1)
    _Documentation = 'Számla megjelenési formája típusForm of appearance of the invoice type'
InvoiceAppearanceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InvoiceAppearanceType, enum_prefix=None)
InvoiceAppearanceType.PAPER = InvoiceAppearanceType._CF_enumeration.addEnumeration(unicode_value='PAPER', tag='PAPER')
InvoiceAppearanceType.ELECTRONIC = InvoiceAppearanceType._CF_enumeration.addEnumeration(unicode_value='ELECTRONIC', tag='ELECTRONIC')
InvoiceAppearanceType.EDI = InvoiceAppearanceType._CF_enumeration.addEnumeration(unicode_value='EDI', tag='EDI')
InvoiceAppearanceType.UNKNOWN = InvoiceAppearanceType._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
InvoiceAppearanceType._InitializeFacetMap(InvoiceAppearanceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InvoiceAppearanceType', InvoiceAppearanceType)
_module_typeBindings.InvoiceAppearanceType = InvoiceAppearanceType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}InvoiceCategoryType
class InvoiceCategoryType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """A számla típusaType of invoice"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 42, 1)
    _Documentation = 'A számla típusaType of invoice'
InvoiceCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InvoiceCategoryType, enum_prefix=None)
InvoiceCategoryType.NORMAL = InvoiceCategoryType._CF_enumeration.addEnumeration(unicode_value='NORMAL', tag='NORMAL')
InvoiceCategoryType.SIMPLIFIED = InvoiceCategoryType._CF_enumeration.addEnumeration(unicode_value='SIMPLIFIED', tag='SIMPLIFIED')
InvoiceCategoryType.AGGREGATE = InvoiceCategoryType._CF_enumeration.addEnumeration(unicode_value='AGGREGATE', tag='AGGREGATE')
InvoiceCategoryType._InitializeFacetMap(InvoiceCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InvoiceCategoryType', InvoiceCategoryType)
_module_typeBindings.InvoiceCategoryType = InvoiceCategoryType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}MonetaryType
class MonetaryType (_ImportedBinding_common.GenericDecimalType):

    """Pénzérték típus. Maximum 18 számjegy, ami 2 tizedesjegyet tartalmazhatField type for money value input. Maximum 18 digits that may include 2 decimal places"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonetaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 117, 1)
    _Documentation = 'Pénzérték típus. Maximum 18 számjegy, ami 2 tizedesjegyet tartalmazhatField type for money value input. Maximum 18 digits that may include 2 decimal places'
MonetaryType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
MonetaryType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
MonetaryType._InitializeFacetMap(MonetaryType._CF_totalDigits,
   MonetaryType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'MonetaryType', MonetaryType)
_module_typeBindings.MonetaryType = MonetaryType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/base}PaymentMethodType
class PaymentMethodType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Fizetés módjaMethod of payment"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentMethodType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 127, 1)
    _Documentation = 'Fizetés módjaMethod of payment'
PaymentMethodType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PaymentMethodType, enum_prefix=None)
PaymentMethodType.TRANSFER = PaymentMethodType._CF_enumeration.addEnumeration(unicode_value='TRANSFER', tag='TRANSFER')
PaymentMethodType.CASH = PaymentMethodType._CF_enumeration.addEnumeration(unicode_value='CASH', tag='CASH')
PaymentMethodType.CARD = PaymentMethodType._CF_enumeration.addEnumeration(unicode_value='CARD', tag='CARD')
PaymentMethodType.VOUCHER = PaymentMethodType._CF_enumeration.addEnumeration(unicode_value='VOUCHER', tag='VOUCHER')
PaymentMethodType.OTHER = PaymentMethodType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
PaymentMethodType._InitializeFacetMap(PaymentMethodType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PaymentMethodType', PaymentMethodType)
_module_typeBindings.PaymentMethodType = PaymentMethodType

# Complex type {http://schemas.nav.gov.hu/OSA/3.0/base}AddressType with content type ELEMENT_ONLY
class AddressType (pyxb.binding.basis.complexTypeDefinition):
    """Cím típus, amely vagy egyszerű, vagy részletes címet tartalmazFormat of address that includes either a simple or a detailed address"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 165, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}simpleAddress uses Python identifier simpleAddress
    __simpleAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'simpleAddress'), 'simpleAddress', '__httpschemas_nav_gov_huOSA3_0base_AddressType_httpschemas_nav_gov_huOSA3_0basesimpleAddress', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 171, 3), )

    
    simpleAddress = property(__simpleAddress.value, __simpleAddress.set, None, 'Egyszerű címSimple address')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}detailedAddress uses Python identifier detailedAddress
    __detailedAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'detailedAddress'), 'detailedAddress', '__httpschemas_nav_gov_huOSA3_0base_AddressType_httpschemas_nav_gov_huOSA3_0basedetailedAddress', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 177, 3), )

    
    detailedAddress = property(__detailedAddress.value, __detailedAddress.set, None, 'Részletes címDetailed address')

    _ElementMap.update({
        __simpleAddress.name() : __simpleAddress,
        __detailedAddress.name() : __detailedAddress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AddressType = AddressType
Namespace.addCategoryObject('typeBinding', 'AddressType', AddressType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/base}DetailedAddressType with content type ELEMENT_ONLY
class DetailedAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Részletes címadatokDetailed address data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DetailedAddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 185, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basecountryCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 191, 3), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, 'Az országkód ISO 3166 alpha-2 szabvány szerintISO 3166 alpha-2 country code')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'region'), 'region', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0baseregion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 197, 3), )

    
    region = property(__region.value, __region.set, None, 'Tartomány kódja (amennyiben értelmezhető az adott országban) az ISO 3166-2 alpha 2 szabvány szerintISO 3166 alpha-2 province code (if appropriate in a given country)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basepostalCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 203, 3), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, 'Irányítószám (amennyiben nem értelmezhető, 0000 értékkel kell kitölteni)ZIP code (If can not be interpreted, need to be filled "0000")')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basecity', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 209, 3), )

    
    city = property(__city.value, __city.set, None, 'TelepülésSettlement')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}streetName uses Python identifier streetName
    __streetName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetName'), 'streetName', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basestreetName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 215, 3), )

    
    streetName = property(__streetName.value, __streetName.set, None, 'Közterület neveName of public place')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}publicPlaceCategory uses Python identifier publicPlaceCategory
    __publicPlaceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'publicPlaceCategory'), 'publicPlaceCategory', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basepublicPlaceCategory', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 221, 3), )

    
    publicPlaceCategory = property(__publicPlaceCategory.value, __publicPlaceCategory.set, None, 'Közterület jellegeCategory of public place')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'number'), 'number', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basenumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 227, 3), )

    
    number = property(__number.value, __number.set, None, 'HázszámHouse number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}building uses Python identifier building
    __building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building'), 'building', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basebuilding', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 233, 3), )

    
    building = property(__building.value, __building.set, None, 'ÉpületBuilding')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}staircase uses Python identifier staircase
    __staircase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'staircase'), 'staircase', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basestaircase', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 239, 3), )

    
    staircase = property(__staircase.value, __staircase.set, None, 'LépcsőházStaircase')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}floor uses Python identifier floor
    __floor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'floor'), 'floor', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basefloor', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 245, 3), )

    
    floor = property(__floor.value, __floor.set, None, 'EmeletFloor')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}door uses Python identifier door
    __door = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'door'), 'door', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0basedoor', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 251, 3), )

    
    door = property(__door.value, __door.set, None, 'AjtóDoor number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}lotNumber uses Python identifier lotNumber
    __lotNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lotNumber'), 'lotNumber', '__httpschemas_nav_gov_huOSA3_0base_DetailedAddressType_httpschemas_nav_gov_huOSA3_0baselotNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 257, 3), )

    
    lotNumber = property(__lotNumber.value, __lotNumber.set, None, 'Helyrajzi számLot number')

    _ElementMap.update({
        __countryCode.name() : __countryCode,
        __region.name() : __region,
        __postalCode.name() : __postalCode,
        __city.name() : __city,
        __streetName.name() : __streetName,
        __publicPlaceCategory.name() : __publicPlaceCategory,
        __number.name() : __number,
        __building.name() : __building,
        __staircase.name() : __staircase,
        __floor.name() : __floor,
        __door.name() : __door,
        __lotNumber.name() : __lotNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DetailedAddressType = DetailedAddressType
Namespace.addCategoryObject('typeBinding', 'DetailedAddressType', DetailedAddressType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/base}SimpleAddressType with content type ELEMENT_ONLY
class SimpleAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Egyszerű címtípusSimple address type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleAddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 265, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httpschemas_nav_gov_huOSA3_0base_SimpleAddressType_httpschemas_nav_gov_huOSA3_0basecountryCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 271, 3), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, 'Az országkód az ISO 3166 alpha-2 szabvány szerintISO 3166 alpha-2 country code')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'region'), 'region', '__httpschemas_nav_gov_huOSA3_0base_SimpleAddressType_httpschemas_nav_gov_huOSA3_0baseregion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 277, 3), )

    
    region = property(__region.value, __region.set, None, 'Tartomány kódja (amennyiben értelmezhető az adott országban) az ISO 3166-2 alpha 2 szabvány szerintISO 3166 alpha-2 province code (if appropriate in a given country)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httpschemas_nav_gov_huOSA3_0base_SimpleAddressType_httpschemas_nav_gov_huOSA3_0basepostalCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 283, 3), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, 'Irányítószám (amennyiben nem értelmezhető, 0000 értékkel kell kitölteni)ZIP code (If can not be interpreted, need to be filled "0000")')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpschemas_nav_gov_huOSA3_0base_SimpleAddressType_httpschemas_nav_gov_huOSA3_0basecity', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 289, 3), )

    
    city = property(__city.value, __city.set, None, 'TelepülésSettlement')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}additionalAddressDetail uses Python identifier additionalAddressDetail
    __additionalAddressDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalAddressDetail'), 'additionalAddressDetail', '__httpschemas_nav_gov_huOSA3_0base_SimpleAddressType_httpschemas_nav_gov_huOSA3_0baseadditionalAddressDetail', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 295, 3), )

    
    additionalAddressDetail = property(__additionalAddressDetail.value, __additionalAddressDetail.set, None, 'További címadatok (pl. közterület neve és jellege, házszám, emelet, ajtó, helyrajzi szám, stb.)Further address data (name and type of public place, house number, floor, door, lot number, etc.)')

    _ElementMap.update({
        __countryCode.name() : __countryCode,
        __region.name() : __region,
        __postalCode.name() : __postalCode,
        __city.name() : __city,
        __additionalAddressDetail.name() : __additionalAddressDetail
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimpleAddressType = SimpleAddressType
Namespace.addCategoryObject('typeBinding', 'SimpleAddressType', SimpleAddressType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/base}TaxNumberType with content type ELEMENT_ONLY
class TaxNumberType (pyxb.binding.basis.complexTypeDefinition):
    """Adószám típusTax number type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 303, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}taxpayerId uses Python identifier taxpayerId
    __taxpayerId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerId'), 'taxpayerId', '__httpschemas_nav_gov_huOSA3_0base_TaxNumberType_httpschemas_nav_gov_huOSA3_0basetaxpayerId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 309, 3), )

    
    taxpayerId = property(__taxpayerId.value, __taxpayerId.set, None, 'Az adóalany adó törzsszáma. Csoportos adóalany esetén csoportazonosító számCore tax number of the taxable person. In case of group taxation arrangement the group identification number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}vatCode uses Python identifier vatCode
    __vatCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatCode'), 'vatCode', '__httpschemas_nav_gov_huOSA3_0base_TaxNumberType_httpschemas_nav_gov_huOSA3_0basevatCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 315, 3), )

    
    vatCode = property(__vatCode.value, __vatCode.set, None, 'ÁFA kód az adóalanyiság típusának jelzésére. Egy számjegyVAT code to indicate taxation type of the taxpayer. One digit')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/base}countyCode uses Python identifier countyCode
    __countyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countyCode'), 'countyCode', '__httpschemas_nav_gov_huOSA3_0base_TaxNumberType_httpschemas_nav_gov_huOSA3_0basecountyCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 321, 3), )

    
    countyCode = property(__countyCode.value, __countyCode.set, None, 'Megyekód, két számjegyCounty code, two digits')

    _ElementMap.update({
        __taxpayerId.name() : __taxpayerId,
        __vatCode.name() : __vatCode,
        __countyCode.name() : __countyCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxNumberType = TaxNumberType
Namespace.addCategoryObject('typeBinding', 'TaxNumberType', TaxNumberType)




AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'simpleAddress'), SimpleAddressType, scope=AddressType, documentation='Egyszerű címSimple address', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 171, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'detailedAddress'), DetailedAddressType, scope=AddressType, documentation='Részletes címDetailed address', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 177, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'simpleAddress')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 171, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'detailedAddress')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 177, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddressType._Automaton = _BuildAutomaton()




DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), _ImportedBinding_common.CountryCodeType, scope=DetailedAddressType, documentation='Az országkód ISO 3166 alpha-2 szabvány szerintISO 3166 alpha-2 country code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 191, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'region'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='Tartomány kódja (amennyiben értelmezhető az adott országban) az ISO 3166-2 alpha 2 szabvány szerintISO 3166 alpha-2 province code (if appropriate in a given country)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 197, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), _ImportedBinding_common.PostalCodeType, scope=DetailedAddressType, documentation='Irányítószám (amennyiben nem értelmezhető, 0000 értékkel kell kitölteni)ZIP code (If can not be interpreted, need to be filled "0000")', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 203, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), _ImportedBinding_common.SimpleText255NotBlankType, scope=DetailedAddressType, documentation='TelepülésSettlement', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 209, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetName'), _ImportedBinding_common.SimpleText255NotBlankType, scope=DetailedAddressType, documentation='Közterület neveName of public place', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 215, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publicPlaceCategory'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='Közterület jellegeCategory of public place', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 221, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='HázszámHouse number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 227, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='ÉpületBuilding', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 233, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'staircase'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='LépcsőházStaircase', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 239, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'floor'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='EmeletFloor', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 245, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'door'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='AjtóDoor number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 251, 3)))

DetailedAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lotNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=DetailedAddressType, documentation='Helyrajzi számLot number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 257, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 197, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 227, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 233, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 239, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 245, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 251, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 257, 3))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 197, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 203, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 209, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 215, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'publicPlaceCategory')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 221, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'number')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 227, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 233, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'staircase')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 239, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'floor')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 245, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'door')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 251, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DetailedAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lotNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 257, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    transitions.append(fac.Transition(st_5, [
         ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DetailedAddressType._Automaton = _BuildAutomaton_()




SimpleAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), _ImportedBinding_common.CountryCodeType, scope=SimpleAddressType, documentation='Az országkód az ISO 3166 alpha-2 szabvány szerintISO 3166 alpha-2 country code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 271, 3)))

SimpleAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'region'), _ImportedBinding_common.SimpleText50NotBlankType, scope=SimpleAddressType, documentation='Tartomány kódja (amennyiben értelmezhető az adott országban) az ISO 3166-2 alpha 2 szabvány szerintISO 3166 alpha-2 province code (if appropriate in a given country)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 277, 3)))

SimpleAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), _ImportedBinding_common.PostalCodeType, scope=SimpleAddressType, documentation='Irányítószám (amennyiben nem értelmezhető, 0000 értékkel kell kitölteni)ZIP code (If can not be interpreted, need to be filled "0000")', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 283, 3)))

SimpleAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), _ImportedBinding_common.SimpleText255NotBlankType, scope=SimpleAddressType, documentation='TelepülésSettlement', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 289, 3)))

SimpleAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalAddressDetail'), _ImportedBinding_common.SimpleText255NotBlankType, scope=SimpleAddressType, documentation='További címadatok (pl. közterület neve és jellege, házszám, emelet, ajtó, helyrajzi szám, stb.)Further address data (name and type of public place, house number, floor, door, lot number, etc.)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 295, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 277, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 271, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 277, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 283, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 289, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalAddressDetail')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 295, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
SimpleAddressType._Automaton = _BuildAutomaton_2()




TaxNumberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerId'), _ImportedBinding_common.TaxpayerIdType, scope=TaxNumberType, documentation='Az adóalany adó törzsszáma. Csoportos adóalany esetén csoportazonosító számCore tax number of the taxable person. In case of group taxation arrangement the group identification number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 309, 3)))

TaxNumberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatCode'), _ImportedBinding_common.VatCodeType, scope=TaxNumberType, documentation='ÁFA kód az adóalanyiság típusának jelzésére. Egy számjegyVAT code to indicate taxation type of the taxpayer. One digit', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 315, 3)))

TaxNumberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countyCode'), _ImportedBinding_common.CountyCodeType, scope=TaxNumberType, documentation='Megyekód, két számjegyCounty code, two digits', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 321, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 315, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 321, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 309, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 315, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countyCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceBase.xsd', 321, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxNumberType._Automaton = _BuildAutomaton_3()

