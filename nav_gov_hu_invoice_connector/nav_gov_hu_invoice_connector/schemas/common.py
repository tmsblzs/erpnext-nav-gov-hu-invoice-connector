# generated/common.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0d3daac23ddc9471eb08d353bbabb02c4e781a2e
# Generated 2022-06-05 12:05:14.792084 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://schemas.nav.gov.hu/NTCA/1.0/common [xmlns:common]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.nav.gov.hu/NTCA/1.0/common', create_if_missing=True)
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


# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType100
class AtomicStringType100 (pyxb.binding.datatypes.string):

    """Atomi string típus 100 hosszraAtomic string type for 100 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType100')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 10, 1)
    _Documentation = 'Atomi string típus 100 hosszraAtomic string type for 100 length'
AtomicStringType100._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType100._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
AtomicStringType100._InitializeFacetMap(AtomicStringType100._CF_minLength,
   AtomicStringType100._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType100', AtomicStringType100)
_module_typeBindings.AtomicStringType100 = AtomicStringType100

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType1024
class AtomicStringType1024 (pyxb.binding.datatypes.string):

    """Atomi string típus 1024 hosszraAtomic string type for 1024 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType1024')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 20, 1)
    _Documentation = 'Atomi string típus 1024 hosszraAtomic string type for 1024 length'
AtomicStringType1024._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType1024._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1024))
AtomicStringType1024._InitializeFacetMap(AtomicStringType1024._CF_minLength,
   AtomicStringType1024._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType1024', AtomicStringType1024)
_module_typeBindings.AtomicStringType1024 = AtomicStringType1024

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType128
class AtomicStringType128 (pyxb.binding.datatypes.string):

    """Atomi string típus 128 hosszraAtomic string type for 128 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType128')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 30, 1)
    _Documentation = 'Atomi string típus 128 hosszraAtomic string type for 128 length'
AtomicStringType128._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType128._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(128))
AtomicStringType128._InitializeFacetMap(AtomicStringType128._CF_minLength,
   AtomicStringType128._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType128', AtomicStringType128)
_module_typeBindings.AtomicStringType128 = AtomicStringType128

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType15
class AtomicStringType15 (pyxb.binding.datatypes.string):

    """Atomi string típus 15 hosszraAtomic string type for 15 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType15')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 40, 1)
    _Documentation = 'Atomi string típus 15 hosszraAtomic string type for 15 length'
AtomicStringType15._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType15._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
AtomicStringType15._InitializeFacetMap(AtomicStringType15._CF_minLength,
   AtomicStringType15._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType15', AtomicStringType15)
_module_typeBindings.AtomicStringType15 = AtomicStringType15

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType16
class AtomicStringType16 (pyxb.binding.datatypes.string):

    """Atomi string típus 16 hosszraAtomic string type for 16 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType16')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 50, 1)
    _Documentation = 'Atomi string típus 16 hosszraAtomic string type for 16 length'
AtomicStringType16._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
AtomicStringType16._InitializeFacetMap(AtomicStringType16._CF_minLength,
   AtomicStringType16._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType16', AtomicStringType16)
_module_typeBindings.AtomicStringType16 = AtomicStringType16

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType2
class AtomicStringType2 (pyxb.binding.datatypes.string):

    """Atomi string típus 2 hosszraAtomic string type for 2 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType2')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 60, 1)
    _Documentation = 'Atomi string típus 2 hosszraAtomic string type for 2 length'
AtomicStringType2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
AtomicStringType2._InitializeFacetMap(AtomicStringType2._CF_minLength,
   AtomicStringType2._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType2', AtomicStringType2)
_module_typeBindings.AtomicStringType2 = AtomicStringType2

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType200
class AtomicStringType200 (pyxb.binding.datatypes.string):

    """Atomi string típus 200 hosszraAtomic string type for 200 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType200')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 70, 1)
    _Documentation = 'Atomi string típus 200 hosszraAtomic string type for 200 length'
AtomicStringType200._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType200._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(200))
AtomicStringType200._InitializeFacetMap(AtomicStringType200._CF_minLength,
   AtomicStringType200._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType200', AtomicStringType200)
_module_typeBindings.AtomicStringType200 = AtomicStringType200

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType2048
class AtomicStringType2048 (pyxb.binding.datatypes.string):

    """Atomi string típus 2048 hosszraAtomic string type for 2048 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType2048')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 80, 1)
    _Documentation = 'Atomi string típus 2048 hosszraAtomic string type for 2048 length'
AtomicStringType2048._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType2048._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2048))
AtomicStringType2048._InitializeFacetMap(AtomicStringType2048._CF_minLength,
   AtomicStringType2048._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType2048', AtomicStringType2048)
_module_typeBindings.AtomicStringType2048 = AtomicStringType2048

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType255
class AtomicStringType255 (pyxb.binding.datatypes.string):

    """Atomi string típus 255 hosszraAtomic string type for 255 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType255')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 90, 1)
    _Documentation = 'Atomi string típus 255 hosszraAtomic string type for 255 length'
AtomicStringType255._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType255._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
AtomicStringType255._InitializeFacetMap(AtomicStringType255._CF_minLength,
   AtomicStringType255._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType255', AtomicStringType255)
_module_typeBindings.AtomicStringType255 = AtomicStringType255

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType256
class AtomicStringType256 (pyxb.binding.datatypes.string):

    """Atomi string típus 256 hosszraAtomic string type for 256 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType256')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 100, 1)
    _Documentation = 'Atomi string típus 256 hosszraAtomic string type for 256 length'
AtomicStringType256._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType256._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
AtomicStringType256._InitializeFacetMap(AtomicStringType256._CF_minLength,
   AtomicStringType256._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType256', AtomicStringType256)
_module_typeBindings.AtomicStringType256 = AtomicStringType256

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType32
class AtomicStringType32 (pyxb.binding.datatypes.string):

    """Atomi string típus 32 hosszraAtomic string type for 32 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType32')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 110, 1)
    _Documentation = 'Atomi string típus 32 hosszraAtomic string type for 32 length'
AtomicStringType32._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
AtomicStringType32._InitializeFacetMap(AtomicStringType32._CF_minLength,
   AtomicStringType32._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType32', AtomicStringType32)
_module_typeBindings.AtomicStringType32 = AtomicStringType32

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType4
class AtomicStringType4 (pyxb.binding.datatypes.string):

    """Atomi string típus 4 hosszraAtomic string type for 4 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType4')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 120, 1)
    _Documentation = 'Atomi string típus 4 hosszraAtomic string type for 4 length'
AtomicStringType4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
AtomicStringType4._InitializeFacetMap(AtomicStringType4._CF_minLength,
   AtomicStringType4._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType4', AtomicStringType4)
_module_typeBindings.AtomicStringType4 = AtomicStringType4

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType4000
class AtomicStringType4000 (pyxb.binding.datatypes.string):

    """Atomi string típus 4000 hosszraAtomic string type for 4000 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType4000')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 130, 1)
    _Documentation = 'Atomi string típus 4000 hosszraAtomic string type for 4000 length'
AtomicStringType4000._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType4000._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
AtomicStringType4000._InitializeFacetMap(AtomicStringType4000._CF_minLength,
   AtomicStringType4000._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType4000', AtomicStringType4000)
_module_typeBindings.AtomicStringType4000 = AtomicStringType4000

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType50
class AtomicStringType50 (pyxb.binding.datatypes.string):

    """Atomi string típus 50 hosszraAtomic string type for 50 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType50')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 140, 1)
    _Documentation = 'Atomi string típus 50 hosszraAtomic string type for 50 length'
AtomicStringType50._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType50._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
AtomicStringType50._InitializeFacetMap(AtomicStringType50._CF_minLength,
   AtomicStringType50._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType50', AtomicStringType50)
_module_typeBindings.AtomicStringType50 = AtomicStringType50

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType512
class AtomicStringType512 (pyxb.binding.datatypes.string):

    """Atomi string típus 512 hosszraAtomic string type for 512 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType512')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 150, 1)
    _Documentation = 'Atomi string típus 512 hosszraAtomic string type for 512 length'
AtomicStringType512._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType512._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(512))
AtomicStringType512._InitializeFacetMap(AtomicStringType512._CF_minLength,
   AtomicStringType512._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType512', AtomicStringType512)
_module_typeBindings.AtomicStringType512 = AtomicStringType512

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType64
class AtomicStringType64 (pyxb.binding.datatypes.string):

    """Atomi string típus 64 hosszraAtomic string type for 64 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType64')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 160, 1)
    _Documentation = 'Atomi string típus 64 hosszraAtomic string type for 64 length'
AtomicStringType64._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType64._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
AtomicStringType64._InitializeFacetMap(AtomicStringType64._CF_minLength,
   AtomicStringType64._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType64', AtomicStringType64)
_module_typeBindings.AtomicStringType64 = AtomicStringType64

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}AtomicStringType8
class AtomicStringType8 (pyxb.binding.datatypes.string):

    """Atomi string típus 8 hosszraAtomic string type for 8 length"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomicStringType8')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 170, 1)
    _Documentation = 'Atomi string típus 8 hosszraAtomic string type for 8 length'
AtomicStringType8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AtomicStringType8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
AtomicStringType8._InitializeFacetMap(AtomicStringType8._CF_minLength,
   AtomicStringType8._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AtomicStringType8', AtomicStringType8)
_module_typeBindings.AtomicStringType8 = AtomicStringType8

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}GenericDateType
class GenericDateType (pyxb.binding.datatypes.date):

    """Általános UTC dátumGeneric UTC date"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericDateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 180, 1)
    _Documentation = 'Általános UTC dátumGeneric UTC date'
GenericDateType._CF_pattern = pyxb.binding.facets.CF_pattern()
GenericDateType._CF_pattern.addPattern(pattern='\\d{4}-\\d{2}-\\d{2}Z')
GenericDateType._InitializeFacetMap(GenericDateType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'GenericDateType', GenericDateType)
_module_typeBindings.GenericDateType = GenericDateType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}GenericDecimalType
class GenericDecimalType (pyxb.binding.datatypes.decimal):

    """Általános lebegőpontos értékGeneric float point value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericDecimalType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 189, 1)
    _Documentation = 'Általános lebegőpontos értékGeneric float point value'
GenericDecimalType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'GenericDecimalType', GenericDecimalType)
_module_typeBindings.GenericDecimalType = GenericDecimalType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}GenericTimestampType
class GenericTimestampType (pyxb.binding.datatypes.dateTime):

    """Általános UTC időbélyegGeneric UTC timestamp"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericTimestampType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 196, 1)
    _Documentation = 'Általános UTC időbélyegGeneric UTC timestamp'
GenericTimestampType._CF_pattern = pyxb.binding.facets.CF_pattern()
GenericTimestampType._CF_pattern.addPattern(pattern='\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d{1,3})?Z')
GenericTimestampType._InitializeFacetMap(GenericTimestampType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'GenericTimestampType', GenericTimestampType)
_module_typeBindings.GenericTimestampType = GenericTimestampType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}RequestPageType
class RequestPageType (pyxb.binding.datatypes.int):

    """Lapozó paraméter típus kérések számáraPage parameter type for requests"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestPageType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 450, 1)
    _Documentation = 'Lapozó paraméter típus kérések számáraPage parameter type for requests'
RequestPageType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=RequestPageType, value=pyxb.binding.datatypes.int(1))
RequestPageType._InitializeFacetMap(RequestPageType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'RequestPageType', RequestPageType)
_module_typeBindings.RequestPageType = RequestPageType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}ResponsePageType
class ResponsePageType (pyxb.binding.datatypes.int):

    """Lapozó paraméter típus válaszok számáraPage parameter type for responses"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponsePageType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 459, 1)
    _Documentation = 'Lapozó paraméter típus válaszok számáraPage parameter type for responses'
ResponsePageType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ResponsePageType, value=pyxb.binding.datatypes.int(0))
ResponsePageType._InitializeFacetMap(ResponsePageType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'ResponsePageType', ResponsePageType)
_module_typeBindings.ResponsePageType = ResponsePageType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SHA256Type
class SHA256Type (AtomicStringType64):

    """SHA256 kód megadására szolgáló típusField type for holding an SHA256 code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SHA256Type')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 205, 1)
    _Documentation = 'SHA256 kód megadására szolgáló típusField type for holding an SHA256 code'
SHA256Type._CF_pattern = pyxb.binding.facets.CF_pattern()
SHA256Type._CF_pattern.addPattern(pattern='[0-9A-F]{64}')
SHA256Type._InitializeFacetMap(SHA256Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SHA256Type', SHA256Type)
_module_typeBindings.SHA256Type = SHA256Type

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SHA512Type
class SHA512Type (AtomicStringType128):

    """SHA512 kód megadására szolgáló típusField type for holding an SHA512 code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SHA512Type')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 214, 1)
    _Documentation = 'SHA512 kód megadására szolgáló típusField type for holding an SHA512 code'
SHA512Type._CF_pattern = pyxb.binding.facets.CF_pattern()
SHA512Type._CF_pattern.addPattern(pattern='[0-9A-F]{128}')
SHA512Type._InitializeFacetMap(SHA512Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SHA512Type', SHA512Type)
_module_typeBindings.SHA512Type = SHA512Type

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SimpleText100NotBlankType
class SimpleText100NotBlankType (AtomicStringType100):

    """Legfeljebb 100 karaktert tartalmazó szöveg típusString of maximum 100 characters"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleText100NotBlankType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 223, 1)
    _Documentation = 'Legfeljebb 100 karaktert tartalmazó szöveg típusString of maximum 100 characters'
SimpleText100NotBlankType._CF_pattern = pyxb.binding.facets.CF_pattern()
SimpleText100NotBlankType._CF_pattern.addPattern(pattern='.*[^\\s].*')
SimpleText100NotBlankType._InitializeFacetMap(SimpleText100NotBlankType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SimpleText100NotBlankType', SimpleText100NotBlankType)
_module_typeBindings.SimpleText100NotBlankType = SimpleText100NotBlankType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SimpleText1024NotBlankType
class SimpleText1024NotBlankType (AtomicStringType1024):

    """Legfeljebb 1024 karaktert tartalmazó szöveg típusString of maximum 1024 characters"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleText1024NotBlankType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 232, 1)
    _Documentation = 'Legfeljebb 1024 karaktert tartalmazó szöveg típusString of maximum 1024 characters'
SimpleText1024NotBlankType._CF_pattern = pyxb.binding.facets.CF_pattern()
SimpleText1024NotBlankType._CF_pattern.addPattern(pattern='.*[^\\s].*')
SimpleText1024NotBlankType._InitializeFacetMap(SimpleText1024NotBlankType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SimpleText1024NotBlankType', SimpleText1024NotBlankType)
_module_typeBindings.SimpleText1024NotBlankType = SimpleText1024NotBlankType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SimpleText15NotBlankType
class SimpleText15NotBlankType (AtomicStringType15):

    """Legfeljebb 15 karaktert tartalmazó szöveg típusString of maximum 15 characters"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleText15NotBlankType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 241, 1)
    _Documentation = 'Legfeljebb 15 karaktert tartalmazó szöveg típusString of maximum 15 characters'
SimpleText15NotBlankType._CF_pattern = pyxb.binding.facets.CF_pattern()
SimpleText15NotBlankType._CF_pattern.addPattern(pattern='.*[^\\s].*')
SimpleText15NotBlankType._InitializeFacetMap(SimpleText15NotBlankType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SimpleText15NotBlankType', SimpleText15NotBlankType)
_module_typeBindings.SimpleText15NotBlankType = SimpleText15NotBlankType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SimpleText200NotBlankType
class SimpleText200NotBlankType (AtomicStringType200):

    """Legfeljebb 200 karaktert tartalmazó szöveg típusString of maximum 200 characters"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleText200NotBlankType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 250, 1)
    _Documentation = 'Legfeljebb 200 karaktert tartalmazó szöveg típusString of maximum 200 characters'
SimpleText200NotBlankType._CF_pattern = pyxb.binding.facets.CF_pattern()
SimpleText200NotBlankType._CF_pattern.addPattern(pattern='.*[^\\s].*')
SimpleText200NotBlankType._InitializeFacetMap(SimpleText200NotBlankType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SimpleText200NotBlankType', SimpleText200NotBlankType)
_module_typeBindings.SimpleText200NotBlankType = SimpleText200NotBlankType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SimpleText255NotBlankType
class SimpleText255NotBlankType (AtomicStringType255):

    """Legfeljebb 255 karaktert tartalmazó szöveg típusString of maximum 255 characters"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleText255NotBlankType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 259, 1)
    _Documentation = 'Legfeljebb 255 karaktert tartalmazó szöveg típusString of maximum 255 characters'
SimpleText255NotBlankType._CF_pattern = pyxb.binding.facets.CF_pattern()
SimpleText255NotBlankType._CF_pattern.addPattern(pattern='.*[^\\s].*')
SimpleText255NotBlankType._InitializeFacetMap(SimpleText255NotBlankType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SimpleText255NotBlankType', SimpleText255NotBlankType)
_module_typeBindings.SimpleText255NotBlankType = SimpleText255NotBlankType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SimpleText50NotBlankType
class SimpleText50NotBlankType (AtomicStringType50):

    """Legfeljebb 50 karaktert tartalmazó szöveg típusString of maximum 50 characters"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleText50NotBlankType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 268, 1)
    _Documentation = 'Legfeljebb 50 karaktert tartalmazó szöveg típusString of maximum 50 characters'
SimpleText50NotBlankType._CF_pattern = pyxb.binding.facets.CF_pattern()
SimpleText50NotBlankType._CF_pattern.addPattern(pattern='.*[^\\s].*')
SimpleText50NotBlankType._InitializeFacetMap(SimpleText50NotBlankType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SimpleText50NotBlankType', SimpleText50NotBlankType)
_module_typeBindings.SimpleText50NotBlankType = SimpleText50NotBlankType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}SimpleText512NotBlankType
class SimpleText512NotBlankType (AtomicStringType512):

    """Legfeljebb 512 karaktert tartalmazó szöveg típusString of maximum 512 characters"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleText512NotBlankType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 277, 1)
    _Documentation = 'Legfeljebb 512 karaktert tartalmazó szöveg típusString of maximum 512 characters'
SimpleText512NotBlankType._CF_pattern = pyxb.binding.facets.CF_pattern()
SimpleText512NotBlankType._CF_pattern.addPattern(pattern='.*[^\\s].*')
SimpleText512NotBlankType._InitializeFacetMap(SimpleText512NotBlankType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SimpleText512NotBlankType', SimpleText512NotBlankType)
_module_typeBindings.SimpleText512NotBlankType = SimpleText512NotBlankType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}BankAccountNumberType
class BankAccountNumberType (AtomicStringType50):

    """Bankszámla megadására szolgáló típusType of bank account number"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BankAccountNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 287, 1)
    _Documentation = 'Bankszámla megadására szolgáló típusType of bank account number'
BankAccountNumberType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
BankAccountNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(34))
BankAccountNumberType._CF_pattern = pyxb.binding.facets.CF_pattern()
BankAccountNumberType._CF_pattern.addPattern(pattern='[0-9]{8}[-][0-9]{8}[-][0-9]{8}|[0-9]{8}[-][0-9]{8}|[A-Z]{2}[0-9]{2}[0-9A-Za-z]{11,30}')
BankAccountNumberType._InitializeFacetMap(BankAccountNumberType._CF_minLength,
   BankAccountNumberType._CF_maxLength,
   BankAccountNumberType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'BankAccountNumberType', BankAccountNumberType)
_module_typeBindings.BankAccountNumberType = BankAccountNumberType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}CommunityVatNumberType
class CommunityVatNumberType (AtomicStringType15):

    """Közösségi adószám típusCommunity VAT registration number"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommunityVatNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 298, 1)
    _Documentation = 'Közösségi adószám típusCommunity VAT registration number'
CommunityVatNumberType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
CommunityVatNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
CommunityVatNumberType._CF_pattern = pyxb.binding.facets.CF_pattern()
CommunityVatNumberType._CF_pattern.addPattern(pattern='[A-Z]{2}[0-9A-Z]{2,13}')
CommunityVatNumberType._InitializeFacetMap(CommunityVatNumberType._CF_minLength,
   CommunityVatNumberType._CF_maxLength,
   CommunityVatNumberType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CommunityVatNumberType', CommunityVatNumberType)
_module_typeBindings.CommunityVatNumberType = CommunityVatNumberType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}CountryCodeType
class CountryCodeType (AtomicStringType2):

    """Országkód típus ISO 3166 alpha-2 szabvány szerintCountry code type (ISO 3166 alpha-2)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 309, 1)
    _Documentation = 'Országkód típus ISO 3166 alpha-2 szabvány szerintCountry code type (ISO 3166 alpha-2)'
CountryCodeType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
CountryCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
CountryCodeType._CF_pattern.addPattern(pattern='[A-Z]{2}')
CountryCodeType._InitializeFacetMap(CountryCodeType._CF_length,
   CountryCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CountryCodeType', CountryCodeType)
_module_typeBindings.CountryCodeType = CountryCodeType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}CountyCodeType
class CountyCodeType (AtomicStringType2):

    """MegyekódCounty code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountyCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 319, 1)
    _Documentation = 'MegyekódCounty code'
CountyCodeType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
CountyCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
CountyCodeType._CF_pattern.addPattern(pattern='[0-9]{2}')
CountyCodeType._InitializeFacetMap(CountyCodeType._CF_length,
   CountyCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CountyCodeType', CountyCodeType)
_module_typeBindings.CountyCodeType = CountyCodeType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}CurrencyType
class CurrencyType (AtomicStringType4):

    """Pénznem típus (ISO 4217 szabvány szerinti 3 hosszú pénznem kód)Currency type (three digit ISO 4217 currency code)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 329, 1)
    _Documentation = 'Pénznem típus (ISO 4217 szabvány szerinti 3 hosszú pénznem kód)Currency type (three digit ISO 4217 currency code)'
CurrencyType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3))
CurrencyType._CF_pattern = pyxb.binding.facets.CF_pattern()
CurrencyType._CF_pattern.addPattern(pattern='[A-Z]{3}')
CurrencyType._InitializeFacetMap(CurrencyType._CF_length,
   CurrencyType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CurrencyType', CurrencyType)
_module_typeBindings.CurrencyType = CurrencyType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}PlateNumberType
class PlateNumberType (AtomicStringType32):

    """Kereskedelmi gépjármű forgalmi rendszáma (csak betűk és számok)Registration number of commercial motor vehicle (letters and numbers only)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlateNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 339, 1)
    _Documentation = 'Kereskedelmi gépjármű forgalmi rendszáma (csak betűk és számok)Registration number of commercial motor vehicle (letters and numbers only)'
PlateNumberType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
PlateNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
PlateNumberType._CF_pattern = pyxb.binding.facets.CF_pattern()
PlateNumberType._CF_pattern.addPattern(pattern='[A-Z0-9ÖŐÜŰ]{2,30}')
PlateNumberType._InitializeFacetMap(PlateNumberType._CF_minLength,
   PlateNumberType._CF_maxLength,
   PlateNumberType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'PlateNumberType', PlateNumberType)
_module_typeBindings.PlateNumberType = PlateNumberType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}PostalCodeType
class PostalCodeType (AtomicStringType15):

    """Irányítószám típusZIP code type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PostalCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 350, 1)
    _Documentation = 'Irányítószám típusZIP code type'
PostalCodeType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
PostalCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
PostalCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
PostalCodeType._CF_pattern.addPattern(pattern='[A-Z0-9][A-Z0-9\\s\\-]{1,8}[A-Z0-9]')
PostalCodeType._InitializeFacetMap(PostalCodeType._CF_minLength,
   PostalCodeType._CF_maxLength,
   PostalCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'PostalCodeType', PostalCodeType)
_module_typeBindings.PostalCodeType = PostalCodeType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}TaxpayerIdType
class TaxpayerIdType (AtomicStringType8):

    """Az adószám nyolc jegyű törzsszám részeThe 8-digit core number section of the tax number"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxpayerIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 361, 1)
    _Documentation = 'Az adószám nyolc jegyű törzsszám részeThe 8-digit core number section of the tax number'
TaxpayerIdType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(8))
TaxpayerIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
TaxpayerIdType._CF_pattern.addPattern(pattern='[0-9]{8}')
TaxpayerIdType._InitializeFacetMap(TaxpayerIdType._CF_length,
   TaxpayerIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TaxpayerIdType', TaxpayerIdType)
_module_typeBindings.TaxpayerIdType = TaxpayerIdType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}VatCodeType
class VatCodeType (AtomicStringType2):

    """ÁFA kódVAT code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VatCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 371, 1)
    _Documentation = 'ÁFA kódVAT code'
VatCodeType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
VatCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
VatCodeType._CF_pattern.addPattern(pattern='[1-5]{1}')
VatCodeType._InitializeFacetMap(VatCodeType._CF_length,
   VatCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VatCodeType', VatCodeType)
_module_typeBindings.VatCodeType = VatCodeType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}BusinessResultCodeType
class BusinessResultCodeType (AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Üzleti eredmény kód típusBusiness result code type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BusinessResultCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 382, 1)
    _Documentation = 'Üzleti eredmény kód típusBusiness result code type'
BusinessResultCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BusinessResultCodeType, enum_prefix=None)
BusinessResultCodeType.ERROR = BusinessResultCodeType._CF_enumeration.addEnumeration(unicode_value='ERROR', tag='ERROR')
BusinessResultCodeType.WARN = BusinessResultCodeType._CF_enumeration.addEnumeration(unicode_value='WARN', tag='WARN')
BusinessResultCodeType.INFO = BusinessResultCodeType._CF_enumeration.addEnumeration(unicode_value='INFO', tag='INFO')
BusinessResultCodeType._InitializeFacetMap(BusinessResultCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BusinessResultCodeType', BusinessResultCodeType)
_module_typeBindings.BusinessResultCodeType = BusinessResultCodeType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}EntityIdType
class EntityIdType (AtomicStringType32):

    """Generált azonosító típusGenerated ID type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EntityIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 408, 1)
    _Documentation = 'Generált azonosító típusGenerated ID type'
EntityIdType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
EntityIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
EntityIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
EntityIdType._CF_pattern.addPattern(pattern='[+a-zA-Z0-9_]{1,30}')
EntityIdType._InitializeFacetMap(EntityIdType._CF_minLength,
   EntityIdType._CF_maxLength,
   EntityIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'EntityIdType', EntityIdType)
_module_typeBindings.EntityIdType = EntityIdType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}FunctionCodeType
class FunctionCodeType (AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Funkciókód típusFunction code type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FunctionCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 419, 1)
    _Documentation = 'Funkciókód típusFunction code type'
FunctionCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FunctionCodeType, enum_prefix=None)
FunctionCodeType.OK = FunctionCodeType._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
FunctionCodeType.ERROR = FunctionCodeType._CF_enumeration.addEnumeration(unicode_value='ERROR', tag='ERROR')
FunctionCodeType._InitializeFacetMap(FunctionCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FunctionCodeType', FunctionCodeType)
_module_typeBindings.FunctionCodeType = FunctionCodeType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}LoginType
class LoginType (AtomicStringType15):

    """Felhasználónév típusLogin type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LoginType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 439, 1)
    _Documentation = 'Felhasználónév típusLogin type'
LoginType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(6))
LoginType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
LoginType._CF_pattern = pyxb.binding.facets.CF_pattern()
LoginType._CF_pattern.addPattern(pattern='[a-zA-Z0-9]{6,15}')
LoginType._InitializeFacetMap(LoginType._CF_minLength,
   LoginType._CF_maxLength,
   LoginType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LoginType', LoginType)
_module_typeBindings.LoginType = LoginType

# Atomic simple type: {http://schemas.nav.gov.hu/NTCA/1.0/common}TechnicalResultCodeType
class TechnicalResultCodeType (AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Technikai eredmény kód típusTechnical result code type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TechnicalResultCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 468, 1)
    _Documentation = 'Technikai eredmény kód típusTechnical result code type'
TechnicalResultCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TechnicalResultCodeType, enum_prefix=None)
TechnicalResultCodeType.CRITICAL = TechnicalResultCodeType._CF_enumeration.addEnumeration(unicode_value='CRITICAL', tag='CRITICAL')
TechnicalResultCodeType.ERROR = TechnicalResultCodeType._CF_enumeration.addEnumeration(unicode_value='ERROR', tag='ERROR')
TechnicalResultCodeType._InitializeFacetMap(TechnicalResultCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TechnicalResultCodeType', TechnicalResultCodeType)
_module_typeBindings.TechnicalResultCodeType = TechnicalResultCodeType

# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicHeaderType with content type ELEMENT_ONLY
class BasicHeaderType (pyxb.binding.basis.complexTypeDefinition):
    """A kérés tranzakcionális adataiTransactional data of the request"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicHeaderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 488, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}requestId uses Python identifier requestId
    __requestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requestId'), 'requestId', '__httpschemas_nav_gov_huNTCA1_0common_BasicHeaderType_httpschemas_nav_gov_huNTCA1_0commonrequestId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 494, 3), )

    
    requestId = property(__requestId.value, __requestId.set, None, 'A kérés/válasz azonosítója, minden üzenetváltásnál - adószámonként - egyediIdentifier of the request/response, unique with the taxnumber in every data exchange transaction')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpschemas_nav_gov_huNTCA1_0common_BasicHeaderType_httpschemas_nav_gov_huNTCA1_0commontimestamp', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 500, 3), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, 'A kérés/válasz keletkezésének UTC idejeUTC time of the request/response')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}requestVersion uses Python identifier requestVersion
    __requestVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requestVersion'), 'requestVersion', '__httpschemas_nav_gov_huNTCA1_0common_BasicHeaderType_httpschemas_nav_gov_huNTCA1_0commonrequestVersion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 506, 3), )

    
    requestVersion = property(__requestVersion.value, __requestVersion.set, None, 'A kérés/válasz verziószáma, hogy a hívó melyik interfész verzió szerint küld adatot és várja a választRequest version number, indicating which datastructure the client sends data in, and in which the response is expected')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}headerVersion uses Python identifier headerVersion
    __headerVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'headerVersion'), 'headerVersion', '__httpschemas_nav_gov_huNTCA1_0common_BasicHeaderType_httpschemas_nav_gov_huNTCA1_0commonheaderVersion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 512, 3), )

    
    headerVersion = property(__headerVersion.value, __headerVersion.set, None, 'A header verziószámaHeader version number')

    _ElementMap.update({
        __requestId.name() : __requestId,
        __timestamp.name() : __timestamp,
        __requestVersion.name() : __requestVersion,
        __headerVersion.name() : __headerVersion
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicHeaderType = BasicHeaderType
Namespace.addCategoryObject('typeBinding', 'BasicHeaderType', BasicHeaderType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType with content type ELEMENT_ONLY
class BasicRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Alap kérés adatokBasic request data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 520, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'header'), 'header', '__httpschemas_nav_gov_huNTCA1_0common_BasicRequestType_httpschemas_nav_gov_huNTCA1_0commonheader', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3), )

    
    header = property(__header.value, __header.set, None, 'A kérés tranzakcionális adataiTransactional data of the request')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'user'), 'user', '__httpschemas_nav_gov_huNTCA1_0common_BasicRequestType_httpschemas_nav_gov_huNTCA1_0commonuser', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3), )

    
    user = property(__user.value, __user.set, None, 'A kérés authentikációs adataiAuthentication data of the request')

    _ElementMap.update({
        __header.name() : __header,
        __user.name() : __user
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicRequestType = BasicRequestType
Namespace.addCategoryObject('typeBinding', 'BasicRequestType', BasicRequestType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType with content type ELEMENT_ONLY
class BasicResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Alap válasz adatokBasic response data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 540, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'header'), 'header', '__httpschemas_nav_gov_huNTCA1_0common_BasicResponseType_httpschemas_nav_gov_huNTCA1_0commonheader', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3), )

    
    header = property(__header.value, __header.set, None, 'A válasz tranzakcionális adataiTransactional data of the response')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httpschemas_nav_gov_huNTCA1_0common_BasicResponseType_httpschemas_nav_gov_huNTCA1_0commonresult', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3), )

    
    result = property(__result.value, __result.set, None, 'Alap válaszeredmény adatokBasic result data')

    _ElementMap.update({
        __header.name() : __header,
        __result.name() : __result
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicResponseType = BasicResponseType
Namespace.addCategoryObject('typeBinding', 'BasicResponseType', BasicResponseType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResultType with content type ELEMENT_ONLY
class BasicResultType (pyxb.binding.basis.complexTypeDefinition):
    """Alap válaszeredmény adatokBasic result data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 560, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}funcCode uses Python identifier funcCode
    __funcCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'funcCode'), 'funcCode', '__httpschemas_nav_gov_huNTCA1_0common_BasicResultType_httpschemas_nav_gov_huNTCA1_0commonfuncCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 566, 3), )

    
    funcCode = property(__funcCode.value, __funcCode.set, None, 'Feldolgozási eredményProcessing result')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}errorCode uses Python identifier errorCode
    __errorCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorCode'), 'errorCode', '__httpschemas_nav_gov_huNTCA1_0common_BasicResultType_httpschemas_nav_gov_huNTCA1_0commonerrorCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 572, 3), )

    
    errorCode = property(__errorCode.value, __errorCode.set, None, 'A feldolgozási hibakódProcessing error code')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'message'), 'message', '__httpschemas_nav_gov_huNTCA1_0common_BasicResultType_httpschemas_nav_gov_huNTCA1_0commonmessage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 578, 3), )

    
    message = property(__message.value, __message.set, None, 'Feldolgozási üzenetProcessing message')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}notifications uses Python identifier notifications
    __notifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notifications'), 'notifications', '__httpschemas_nav_gov_huNTCA1_0common_BasicResultType_httpschemas_nav_gov_huNTCA1_0commonnotifications', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 584, 3), )

    
    notifications = property(__notifications.value, __notifications.set, None, 'Egyéb értesítésekMiscellaneous notifications')

    _ElementMap.update({
        __funcCode.name() : __funcCode,
        __errorCode.name() : __errorCode,
        __message.name() : __message,
        __notifications.name() : __notifications
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicResultType = BasicResultType
Namespace.addCategoryObject('typeBinding', 'BasicResultType', BasicResultType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}NotificationsType with content type ELEMENT_ONLY
class NotificationsType (pyxb.binding.basis.complexTypeDefinition):
    """Egyéb értesítésekMiscellaneous notifications"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NotificationsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 612, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}notification uses Python identifier notification
    __notification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notification'), 'notification', '__httpschemas_nav_gov_huNTCA1_0common_NotificationsType_httpschemas_nav_gov_huNTCA1_0commonnotification', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 618, 3), )

    
    notification = property(__notification.value, __notification.set, None, 'ÉrtesítésNotification')

    _ElementMap.update({
        __notification.name() : __notification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NotificationsType = NotificationsType
Namespace.addCategoryObject('typeBinding', 'NotificationsType', NotificationsType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}NotificationType with content type ELEMENT_ONLY
class NotificationType (pyxb.binding.basis.complexTypeDefinition):
    """ÉrtesítésNotification"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NotificationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 626, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}notificationCode uses Python identifier notificationCode
    __notificationCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notificationCode'), 'notificationCode', '__httpschemas_nav_gov_huNTCA1_0common_NotificationType_httpschemas_nav_gov_huNTCA1_0commonnotificationCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 632, 3), )

    
    notificationCode = property(__notificationCode.value, __notificationCode.set, None, 'Értesítés kódNotification code')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}notificationText uses Python identifier notificationText
    __notificationText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notificationText'), 'notificationText', '__httpschemas_nav_gov_huNTCA1_0common_NotificationType_httpschemas_nav_gov_huNTCA1_0commonnotificationText', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 638, 3), )

    
    notificationText = property(__notificationText.value, __notificationText.set, None, 'Értesítés szövegNotification text')

    _ElementMap.update({
        __notificationCode.name() : __notificationCode,
        __notificationText.name() : __notificationText
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NotificationType = NotificationType
Namespace.addCategoryObject('typeBinding', 'NotificationType', NotificationType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}TechnicalValidationResultType with content type ELEMENT_ONLY
class TechnicalValidationResultType (pyxb.binding.basis.complexTypeDefinition):
    """Technikai validációs választípusTechnical validation response type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TechnicalValidationResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 646, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}validationResultCode uses Python identifier validationResultCode
    __validationResultCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validationResultCode'), 'validationResultCode', '__httpschemas_nav_gov_huNTCA1_0common_TechnicalValidationResultType_httpschemas_nav_gov_huNTCA1_0commonvalidationResultCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 652, 3), )

    
    validationResultCode = property(__validationResultCode.value, __validationResultCode.set, None, 'Validációs eredményValidation result')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}validationErrorCode uses Python identifier validationErrorCode
    __validationErrorCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validationErrorCode'), 'validationErrorCode', '__httpschemas_nav_gov_huNTCA1_0common_TechnicalValidationResultType_httpschemas_nav_gov_huNTCA1_0commonvalidationErrorCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 658, 3), )

    
    validationErrorCode = property(__validationErrorCode.value, __validationErrorCode.set, None, 'Validációs hibakódValidation error code')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'message'), 'message', '__httpschemas_nav_gov_huNTCA1_0common_TechnicalValidationResultType_httpschemas_nav_gov_huNTCA1_0commonmessage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 664, 3), )

    
    message = property(__message.value, __message.set, None, 'Feldolgozási üzenetProcessing message')

    _ElementMap.update({
        __validationResultCode.name() : __validationResultCode,
        __validationErrorCode.name() : __validationErrorCode,
        __message.name() : __message
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TechnicalValidationResultType = TechnicalValidationResultType
Namespace.addCategoryObject('typeBinding', 'TechnicalValidationResultType', TechnicalValidationResultType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}UserHeaderType with content type ELEMENT_ONLY
class UserHeaderType (pyxb.binding.basis.complexTypeDefinition):
    """A kérés authentikációs adataiAuthentication data of the request"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UserHeaderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 672, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}login uses Python identifier login
    __login = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'login'), 'login', '__httpschemas_nav_gov_huNTCA1_0common_UserHeaderType_httpschemas_nav_gov_huNTCA1_0commonlogin', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 678, 3), )

    
    login = property(__login.value, __login.set, None, 'A technikai felhasználó login neveLogin name of the technical user')

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}passwordHash uses Python identifier passwordHash
    __passwordHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passwordHash'), 'passwordHash', '__httpschemas_nav_gov_huNTCA1_0common_UserHeaderType_httpschemas_nav_gov_huNTCA1_0commonpasswordHash', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 684, 3), )

    
    passwordHash = property(__passwordHash.value, __passwordHash.set, None, "A technikai felhasználó jelszavának hash értékeHash value of the technical user's password")

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}taxNumber uses Python identifier taxNumber
    __taxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), 'taxNumber', '__httpschemas_nav_gov_huNTCA1_0common_UserHeaderType_httpschemas_nav_gov_huNTCA1_0commontaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 690, 3), )

    
    taxNumber = property(__taxNumber.value, __taxNumber.set, None, "A rendszerben regisztrált adózó adószáma, aki nevében a technikai felhasználó tevékenykedikThe taxpayer's tax number, whose name the technical user operates in")

    
    # Element {http://schemas.nav.gov.hu/NTCA/1.0/common}requestSignature uses Python identifier requestSignature
    __requestSignature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requestSignature'), 'requestSignature', '__httpschemas_nav_gov_huNTCA1_0common_UserHeaderType_httpschemas_nav_gov_huNTCA1_0commonrequestSignature', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 696, 3), )

    
    requestSignature = property(__requestSignature.value, __requestSignature.set, None, "A kérés aláírásának hash értékeHash value of the request's signature")

    _ElementMap.update({
        __login.name() : __login,
        __passwordHash.name() : __passwordHash,
        __taxNumber.name() : __taxNumber,
        __requestSignature.name() : __requestSignature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UserHeaderType = UserHeaderType
Namespace.addCategoryObject('typeBinding', 'UserHeaderType', UserHeaderType)


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}GeneralErrorHeaderResponseType with content type ELEMENT_ONLY
class GeneralErrorHeaderResponseType (BasicResponseType):
    """Általános hibatípus minden REST operációraGeneric fault type for every REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneralErrorHeaderResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 603, 1)
    _ElementMap = BasicResponseType._ElementMap.copy()
    _AttributeMap = BasicResponseType._AttributeMap.copy()
    # Base type is BasicResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GeneralErrorHeaderResponseType = GeneralErrorHeaderResponseType
Namespace.addCategoryObject('typeBinding', 'GeneralErrorHeaderResponseType', GeneralErrorHeaderResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (BasicResultType):
    """Az összes REST operációra vonatkozó kivétel válasz generikus elementjeGeneral exception response of every REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 721, 2)
    _ElementMap = BasicResultType._ElementMap.copy()
    _AttributeMap = BasicResultType._AttributeMap.copy()
    # Base type is BasicResultType
    
    # Element funcCode ({http://schemas.nav.gov.hu/NTCA/1.0/common}funcCode) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResultType
    
    # Element errorCode ({http://schemas.nav.gov.hu/NTCA/1.0/common}errorCode) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResultType
    
    # Element message ({http://schemas.nav.gov.hu/NTCA/1.0/common}message) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResultType
    
    # Element notifications ({http://schemas.nav.gov.hu/NTCA/1.0/common}notifications) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResultType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://schemas.nav.gov.hu/NTCA/1.0/common}CryptoType with content type SIMPLE
class CryptoType (pyxb.binding.basis.complexTypeDefinition):
    """Kriptográfiai metódust leíró típusDenoting type of cryptographic method"""
    _TypeDefinition = SimpleText512NotBlankType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CryptoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 592, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is SimpleText512NotBlankType
    
    # Attribute cryptoType uses Python identifier cryptoType
    __cryptoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cryptoType'), 'cryptoType', '__httpschemas_nav_gov_huNTCA1_0common_CryptoType_cryptoType', _module_typeBindings.SimpleText50NotBlankType, required=True)
    __cryptoType._DeclarationLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 599, 4)
    __cryptoType._UseLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 599, 4)
    
    cryptoType = property(__cryptoType.value, __cryptoType.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __cryptoType.name() : __cryptoType
    })
_module_typeBindings.CryptoType = CryptoType
Namespace.addCategoryObject('typeBinding', 'CryptoType', CryptoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (GeneralErrorHeaderResponseType):
    """Az összes REST operációra vonatkozó hibaválasz generikus elementjeGeneral error response of every REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 710, 2)
    _ElementMap = GeneralErrorHeaderResponseType._ElementMap.copy()
    _AttributeMap = GeneralErrorHeaderResponseType._AttributeMap.copy()
    # Base type is GeneralErrorHeaderResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


GeneralExceptionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneralExceptionResponse'), CTD_ANON, documentation='Az összes REST operációra vonatkozó kivétel válasz generikus elementjeGeneral exception response of every REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 716, 1))
Namespace.addCategoryObject('elementBinding', GeneralExceptionResponse.name().localName(), GeneralExceptionResponse)

GeneralErrorHeaderResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneralErrorHeaderResponse'), CTD_ANON_, documentation='Az összes REST operációra vonatkozó hibaválasz generikus elementjeGeneral error response of every REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 705, 1))
Namespace.addCategoryObject('elementBinding', GeneralErrorHeaderResponse.name().localName(), GeneralErrorHeaderResponse)



BasicHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requestId'), EntityIdType, scope=BasicHeaderType, documentation='A kérés/válasz azonosítója, minden üzenetváltásnál - adószámonként - egyediIdentifier of the request/response, unique with the taxnumber in every data exchange transaction', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 494, 3)))

BasicHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), GenericTimestampType, scope=BasicHeaderType, documentation='A kérés/válasz keletkezésének UTC idejeUTC time of the request/response', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 500, 3)))

BasicHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requestVersion'), AtomicStringType15, scope=BasicHeaderType, documentation='A kérés/válasz verziószáma, hogy a hívó melyik interfész verzió szerint küld adatot és várja a választRequest version number, indicating which datastructure the client sends data in, and in which the response is expected', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 506, 3)))

BasicHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'headerVersion'), AtomicStringType15, scope=BasicHeaderType, documentation='A header verziószámaHeader version number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 512, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 512, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requestId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 494, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 500, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BasicHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requestVersion')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 506, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BasicHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'headerVersion')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 512, 3))
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
BasicHeaderType._Automaton = _BuildAutomaton()




BasicRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'header'), BasicHeaderType, scope=BasicRequestType, documentation='A kérés tranzakcionális adataiTransactional data of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3)))

BasicRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'user'), UserHeaderType, scope=BasicRequestType, documentation='A kérés authentikációs adataiAuthentication data of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BasicRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BasicRequestType._Automaton = _BuildAutomaton_()




BasicResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'header'), BasicHeaderType, scope=BasicResponseType, documentation='A válasz tranzakcionális adataiTransactional data of the response', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3)))

BasicResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), BasicResultType, scope=BasicResponseType, documentation='Alap válaszeredmény adatokBasic result data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BasicResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BasicResponseType._Automaton = _BuildAutomaton_2()




BasicResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'funcCode'), FunctionCodeType, scope=BasicResultType, documentation='Feldolgozási eredményProcessing result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 566, 3)))

BasicResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorCode'), SimpleText50NotBlankType, scope=BasicResultType, documentation='A feldolgozási hibakódProcessing error code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 572, 3)))

BasicResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'message'), SimpleText1024NotBlankType, scope=BasicResultType, documentation='Feldolgozási üzenetProcessing message', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 578, 3)))

BasicResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notifications'), NotificationsType, scope=BasicResultType, documentation='Egyéb értesítésekMiscellaneous notifications', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 584, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 572, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 578, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 584, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BasicResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'funcCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 566, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BasicResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 572, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BasicResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'message')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 578, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BasicResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notifications')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 584, 3))
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
BasicResultType._Automaton = _BuildAutomaton_3()




NotificationsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notification'), NotificationType, scope=NotificationsType, documentation='ÉrtesítésNotification', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 618, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NotificationsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notification')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 618, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NotificationsType._Automaton = _BuildAutomaton_4()




NotificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notificationCode'), SimpleText100NotBlankType, scope=NotificationType, documentation='Értesítés kódNotification code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 632, 3)))

NotificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notificationText'), SimpleText1024NotBlankType, scope=NotificationType, documentation='Értesítés szövegNotification text', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 638, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NotificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notificationCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 632, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NotificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notificationText')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 638, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NotificationType._Automaton = _BuildAutomaton_5()




TechnicalValidationResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validationResultCode'), TechnicalResultCodeType, scope=TechnicalValidationResultType, documentation='Validációs eredményValidation result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 652, 3)))

TechnicalValidationResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validationErrorCode'), SimpleText100NotBlankType, scope=TechnicalValidationResultType, documentation='Validációs hibakódValidation error code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 658, 3)))

TechnicalValidationResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'message'), SimpleText1024NotBlankType, scope=TechnicalValidationResultType, documentation='Feldolgozási üzenetProcessing message', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 664, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 658, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 664, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TechnicalValidationResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validationResultCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 652, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TechnicalValidationResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validationErrorCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 658, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TechnicalValidationResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'message')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 664, 3))
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
TechnicalValidationResultType._Automaton = _BuildAutomaton_6()




UserHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'login'), LoginType, scope=UserHeaderType, documentation='A technikai felhasználó login neveLogin name of the technical user', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 678, 3)))

UserHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passwordHash'), CryptoType, scope=UserHeaderType, documentation="A technikai felhasználó jelszavának hash értékeHash value of the technical user's password", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 684, 3)))

UserHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), TaxpayerIdType, scope=UserHeaderType, documentation="A rendszerben regisztrált adózó adószáma, aki nevében a technikai felhasználó tevékenykedikThe taxpayer's tax number, whose name the technical user operates in", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 690, 3)))

UserHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requestSignature'), CryptoType, scope=UserHeaderType, documentation="A kérés aláírásának hash értékeHash value of the request's signature", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 696, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UserHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'login')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 678, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UserHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passwordHash')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 684, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UserHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 690, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UserHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requestSignature')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 696, 3))
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
UserHeaderType._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeneralErrorHeaderResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneralErrorHeaderResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeneralErrorHeaderResponseType._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 572, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 578, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 584, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'funcCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 566, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 572, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'message')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 578, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notifications')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 584, 3))
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
CTD_ANON._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_10()

