# generated/binding_.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2471684dbc2b6e2920b2522240f044a8f010c589
# Generated 2022-06-05 12:05:14.793021 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://schemas.nav.gov.hu/OSA/3.0/api

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
import common as _ImportedBinding_common
import pyxb.binding.datatypes
import base as _ImportedBinding_base

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.nav.gov.hu/OSA/3.0/api', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_common = _ImportedBinding_common.Namespace
_Namespace_common.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}AnnulmentVerificationStatusType
class AnnulmentVerificationStatusType (_ImportedBinding_common.AtomicStringType32, pyxb.binding.basis.enumeration_mixin):

    """Technikai érvénytelenítő kérések jóváhagyási státuszaVerification status of technical annulment requests"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnnulmentVerificationStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 11, 1)
    _Documentation = 'Technikai érvénytelenítő kérések jóváhagyási státuszaVerification status of technical annulment requests'
AnnulmentVerificationStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AnnulmentVerificationStatusType, enum_prefix=None)
AnnulmentVerificationStatusType.NOT_VERIFIABLE = AnnulmentVerificationStatusType._CF_enumeration.addEnumeration(unicode_value='NOT_VERIFIABLE', tag='NOT_VERIFIABLE')
AnnulmentVerificationStatusType.VERIFICATION_PENDING = AnnulmentVerificationStatusType._CF_enumeration.addEnumeration(unicode_value='VERIFICATION_PENDING', tag='VERIFICATION_PENDING')
AnnulmentVerificationStatusType.VERIFICATION_DONE = AnnulmentVerificationStatusType._CF_enumeration.addEnumeration(unicode_value='VERIFICATION_DONE', tag='VERIFICATION_DONE')
AnnulmentVerificationStatusType.VERIFICATION_REJECTED = AnnulmentVerificationStatusType._CF_enumeration.addEnumeration(unicode_value='VERIFICATION_REJECTED', tag='VERIFICATION_REJECTED')
AnnulmentVerificationStatusType._InitializeFacetMap(AnnulmentVerificationStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AnnulmentVerificationStatusType', AnnulmentVerificationStatusType)
_module_typeBindings.AnnulmentVerificationStatusType = AnnulmentVerificationStatusType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}IncorporationType
class IncorporationType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Gazdasági típusIncorporation type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IncorporationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 43, 1)
    _Documentation = 'Gazdasági típusIncorporation type'
IncorporationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IncorporationType, enum_prefix=None)
IncorporationType.ORGANIZATION = IncorporationType._CF_enumeration.addEnumeration(unicode_value='ORGANIZATION', tag='ORGANIZATION')
IncorporationType.SELF_EMPLOYED = IncorporationType._CF_enumeration.addEnumeration(unicode_value='SELF_EMPLOYED', tag='SELF_EMPLOYED')
IncorporationType.TAXABLE_PERSON = IncorporationType._CF_enumeration.addEnumeration(unicode_value='TAXABLE_PERSON', tag='TAXABLE_PERSON')
IncorporationType._InitializeFacetMap(IncorporationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IncorporationType', IncorporationType)
_module_typeBindings.IncorporationType = IncorporationType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceDirectionType
class InvoiceDirectionType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceDirectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 69, 1)
    _Documentation = 'Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter'
InvoiceDirectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InvoiceDirectionType, enum_prefix=None)
InvoiceDirectionType.INBOUND = InvoiceDirectionType._CF_enumeration.addEnumeration(unicode_value='INBOUND', tag='INBOUND')
InvoiceDirectionType.OUTBOUND = InvoiceDirectionType._CF_enumeration.addEnumeration(unicode_value='OUTBOUND', tag='OUTBOUND')
InvoiceDirectionType._InitializeFacetMap(InvoiceDirectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InvoiceDirectionType', InvoiceDirectionType)
_module_typeBindings.InvoiceDirectionType = InvoiceDirectionType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceStatusType
class InvoiceStatusType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """A számla feldolgozási státuszaProcessing status of the invoice"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 89, 1)
    _Documentation = 'A számla feldolgozási státuszaProcessing status of the invoice'
InvoiceStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InvoiceStatusType, enum_prefix=None)
InvoiceStatusType.RECEIVED = InvoiceStatusType._CF_enumeration.addEnumeration(unicode_value='RECEIVED', tag='RECEIVED')
InvoiceStatusType.PROCESSING = InvoiceStatusType._CF_enumeration.addEnumeration(unicode_value='PROCESSING', tag='PROCESSING')
InvoiceStatusType.SAVED = InvoiceStatusType._CF_enumeration.addEnumeration(unicode_value='SAVED', tag='SAVED')
InvoiceStatusType.DONE = InvoiceStatusType._CF_enumeration.addEnumeration(unicode_value='DONE', tag='DONE')
InvoiceStatusType.ABORTED = InvoiceStatusType._CF_enumeration.addEnumeration(unicode_value='ABORTED', tag='ABORTED')
InvoiceStatusType._InitializeFacetMap(InvoiceStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InvoiceStatusType', InvoiceStatusType)
_module_typeBindings.InvoiceStatusType = InvoiceStatusType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}ManageAnnulmentOperationType
class ManageAnnulmentOperationType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Technikai érvénytelenítés műveleti típusTechnical annulment operation type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManageAnnulmentOperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 127, 1)
    _Documentation = 'Technikai érvénytelenítés műveleti típusTechnical annulment operation type'
ManageAnnulmentOperationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ManageAnnulmentOperationType, enum_prefix=None)
ManageAnnulmentOperationType.ANNUL = ManageAnnulmentOperationType._CF_enumeration.addEnumeration(unicode_value='ANNUL', tag='ANNUL')
ManageAnnulmentOperationType._InitializeFacetMap(ManageAnnulmentOperationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ManageAnnulmentOperationType', ManageAnnulmentOperationType)
_module_typeBindings.ManageAnnulmentOperationType = ManageAnnulmentOperationType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}ManageInvoiceOperationType
class ManageInvoiceOperationType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Számlaművelet típusInvoice operation type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManageInvoiceOperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 141, 1)
    _Documentation = 'Számlaművelet típusInvoice operation type'
ManageInvoiceOperationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ManageInvoiceOperationType, enum_prefix=None)
ManageInvoiceOperationType.CREATE = ManageInvoiceOperationType._CF_enumeration.addEnumeration(unicode_value='CREATE', tag='CREATE')
ManageInvoiceOperationType.MODIFY = ManageInvoiceOperationType._CF_enumeration.addEnumeration(unicode_value='MODIFY', tag='MODIFY')
ManageInvoiceOperationType.STORNO = ManageInvoiceOperationType._CF_enumeration.addEnumeration(unicode_value='STORNO', tag='STORNO')
ManageInvoiceOperationType._InitializeFacetMap(ManageInvoiceOperationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ManageInvoiceOperationType', ManageInvoiceOperationType)
_module_typeBindings.ManageInvoiceOperationType = ManageInvoiceOperationType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}OriginalRequestVersionType
class OriginalRequestVersionType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """A lekérdezett számla requestVersion értékeRequest version value of the queried invoice"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OriginalRequestVersionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 167, 1)
    _Documentation = 'A lekérdezett számla requestVersion értékeRequest version value of the queried invoice'
OriginalRequestVersionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OriginalRequestVersionType, enum_prefix=None)
OriginalRequestVersionType.n1_0 = OriginalRequestVersionType._CF_enumeration.addEnumeration(unicode_value='1.0', tag='n1_0')
OriginalRequestVersionType.n1_1 = OriginalRequestVersionType._CF_enumeration.addEnumeration(unicode_value='1.1', tag='n1_1')
OriginalRequestVersionType.n2_0 = OriginalRequestVersionType._CF_enumeration.addEnumeration(unicode_value='2.0', tag='n2_0')
OriginalRequestVersionType.n3_0 = OriginalRequestVersionType._CF_enumeration.addEnumeration(unicode_value='3.0', tag='n3_0')
OriginalRequestVersionType._InitializeFacetMap(OriginalRequestVersionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OriginalRequestVersionType', OriginalRequestVersionType)
_module_typeBindings.OriginalRequestVersionType = OriginalRequestVersionType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}QueryOperatorType
class QueryOperatorType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Relációs művelet típusRelational operator type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 188, 1)
    _Documentation = 'Relációs művelet típusRelational operator type'
QueryOperatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=QueryOperatorType, enum_prefix=None)
QueryOperatorType.EQ = QueryOperatorType._CF_enumeration.addEnumeration(unicode_value='EQ', tag='EQ')
QueryOperatorType.GT = QueryOperatorType._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
QueryOperatorType.GTE = QueryOperatorType._CF_enumeration.addEnumeration(unicode_value='GTE', tag='GTE')
QueryOperatorType.LT = QueryOperatorType._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
QueryOperatorType.LTE = QueryOperatorType._CF_enumeration.addEnumeration(unicode_value='LTE', tag='LTE')
QueryOperatorType._InitializeFacetMap(QueryOperatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'QueryOperatorType', QueryOperatorType)
_module_typeBindings.QueryOperatorType = QueryOperatorType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}RequestStatusType
class RequestStatusType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """A kérés feldolgozási státuszaProcessing status of the request"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 226, 1)
    _Documentation = 'A kérés feldolgozási státuszaProcessing status of the request'
RequestStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RequestStatusType, enum_prefix=None)
RequestStatusType.RECEIVED = RequestStatusType._CF_enumeration.addEnumeration(unicode_value='RECEIVED', tag='RECEIVED')
RequestStatusType.PROCESSING = RequestStatusType._CF_enumeration.addEnumeration(unicode_value='PROCESSING', tag='PROCESSING')
RequestStatusType.SAVED = RequestStatusType._CF_enumeration.addEnumeration(unicode_value='SAVED', tag='SAVED')
RequestStatusType.FINISHED = RequestStatusType._CF_enumeration.addEnumeration(unicode_value='FINISHED', tag='FINISHED')
RequestStatusType.NOTIFIED = RequestStatusType._CF_enumeration.addEnumeration(unicode_value='NOTIFIED', tag='NOTIFIED')
RequestStatusType._InitializeFacetMap(RequestStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RequestStatusType', RequestStatusType)
_module_typeBindings.RequestStatusType = RequestStatusType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}SoftwareIdType
class SoftwareIdType (_ImportedBinding_common.AtomicStringType32):

    """A számlázóprogram azonosítójaBilling software ID"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 264, 1)
    _Documentation = 'A számlázóprogram azonosítójaBilling software ID'
SoftwareIdType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(18))
SoftwareIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
SoftwareIdType._CF_pattern.addPattern(pattern='[0-9A-Z\\-]{18}')
SoftwareIdType._InitializeFacetMap(SoftwareIdType._CF_length,
   SoftwareIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SoftwareIdType', SoftwareIdType)
_module_typeBindings.SoftwareIdType = SoftwareIdType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}SoftwareOperationType
class SoftwareOperationType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """A számlázóprogram működési típusa (lokális program vagy online számlázó szolgáltatás)Billing operation type (local program or online billing service)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareOperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 274, 1)
    _Documentation = 'A számlázóprogram működési típusa (lokális program vagy online számlázó szolgáltatás)Billing operation type (local program or online billing service)'
SoftwareOperationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoftwareOperationType, enum_prefix=None)
SoftwareOperationType.LOCAL_SOFTWARE = SoftwareOperationType._CF_enumeration.addEnumeration(unicode_value='LOCAL_SOFTWARE', tag='LOCAL_SOFTWARE')
SoftwareOperationType.ONLINE_SERVICE = SoftwareOperationType._CF_enumeration.addEnumeration(unicode_value='ONLINE_SERVICE', tag='ONLINE_SERVICE')
SoftwareOperationType._InitializeFacetMap(SoftwareOperationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SoftwareOperationType', SoftwareOperationType)
_module_typeBindings.SoftwareOperationType = SoftwareOperationType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}SourceType
class SourceType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Az adatszolgáltatás forrásaData exchange source"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 294, 1)
    _Documentation = 'Az adatszolgáltatás forrásaData exchange source'
SourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SourceType, enum_prefix=None)
SourceType.WEB = SourceType._CF_enumeration.addEnumeration(unicode_value='WEB', tag='WEB')
SourceType.XML = SourceType._CF_enumeration.addEnumeration(unicode_value='XML', tag='XML')
SourceType.MGM = SourceType._CF_enumeration.addEnumeration(unicode_value='MGM', tag='MGM')
SourceType.OPG = SourceType._CF_enumeration.addEnumeration(unicode_value='OPG', tag='OPG')
SourceType.OSZ = SourceType._CF_enumeration.addEnumeration(unicode_value='OSZ', tag='OSZ')
SourceType._InitializeFacetMap(SourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SourceType', SourceType)
_module_typeBindings.SourceType = SourceType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}TaxpayerAddressTypeType
class TaxpayerAddressTypeType (_ImportedBinding_common.AtomicStringType8, pyxb.binding.basis.enumeration_mixin):

    """Adózói cím típusTaxpayer address type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxpayerAddressTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 332, 1)
    _Documentation = 'Adózói cím típusTaxpayer address type'
TaxpayerAddressTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TaxpayerAddressTypeType, enum_prefix=None)
TaxpayerAddressTypeType.HQ = TaxpayerAddressTypeType._CF_enumeration.addEnumeration(unicode_value='HQ', tag='HQ')
TaxpayerAddressTypeType.SITE = TaxpayerAddressTypeType._CF_enumeration.addEnumeration(unicode_value='SITE', tag='SITE')
TaxpayerAddressTypeType.BRANCH = TaxpayerAddressTypeType._CF_enumeration.addEnumeration(unicode_value='BRANCH', tag='BRANCH')
TaxpayerAddressTypeType._InitializeFacetMap(TaxpayerAddressTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TaxpayerAddressTypeType', TaxpayerAddressTypeType)
_module_typeBindings.TaxpayerAddressTypeType = TaxpayerAddressTypeType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/api}QueryNameType
class QueryNameType (_ImportedBinding_common.SimpleText512NotBlankType):

    """Név kereső paraméter típusName query parameter type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 179, 1)
    _Documentation = 'Név kereső paraméter típusName query parameter type'
QueryNameType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
QueryNameType._InitializeFacetMap(QueryNameType._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'QueryNameType', QueryNameType)
_module_typeBindings.QueryNameType = QueryNameType

# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}AdditionalQueryParamsType with content type ELEMENT_ONLY
class AdditionalQueryParamsType (pyxb.binding.basis.complexTypeDefinition):
    """A számla lekérdezés kiegészítő paramétereiAdditional params of the invoice query"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalQueryParamsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 358, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxNumber uses Python identifier taxNumber
    __taxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), 'taxNumber', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apitaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 364, 3), )

    
    taxNumber = property(__taxNumber.value, __taxNumber.set, None, 'A számla kiállítójának vagy vevőjének adószáma (a keresési feltétel az invoiceDirection tag értékétől függ)Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}groupMemberTaxNumber uses Python identifier groupMemberTaxNumber
    __groupMemberTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber'), 'groupMemberTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apigroupMemberTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 370, 3), )

    
    groupMemberTaxNumber = property(__groupMemberTaxNumber.value, __groupMemberTaxNumber.set, None, 'A számla kiállítójának vagy vevőjének csoport tag adószáma (a keresési feltétel az invoiceDirection tag értékétől függ)Tax number of group member of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiname', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 376, 3), )

    
    name = property(__name.value, __name.set, None, 'A számla kiállítójának vagy vevőjének keresőparamétere szó eleji egyezőségre (a keresési feltétel az invoiceDirection tag értékétől függ)Query param of the supplier or the customer of the invoice for leading match pattern (the search criteria depends on the value of the invoiceDirection tag)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceCategory uses Python identifier invoiceCategory
    __invoiceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory'), 'invoiceCategory', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceCategory', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 382, 3), )

    
    invoiceCategory = property(__invoiceCategory.value, __invoiceCategory.set, None, 'A számla típusaType of invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}paymentMethod uses Python identifier paymentMethod
    __paymentMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), 'paymentMethod', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apipaymentMethod', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 388, 3), )

    
    paymentMethod = property(__paymentMethod.value, __paymentMethod.set, None, 'Fizetés módjaMethod of payment')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceAppearance uses Python identifier invoiceAppearance
    __invoiceAppearance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance'), 'invoiceAppearance', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceAppearance', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 394, 3), )

    
    invoiceAppearance = property(__invoiceAppearance.value, __invoiceAppearance.set, None, 'A számla megjelenési formájaForm of appearance of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apisource', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 400, 3), )

    
    source = property(__source.value, __source.set, None, 'Az adatszolgáltatás forrásaData exchange source')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__httpschemas_nav_gov_huOSA3_0api_AdditionalQueryParamsType_httpschemas_nav_gov_huOSA3_0apicurrency', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 406, 3), )

    
    currency = property(__currency.value, __currency.set, None, 'A számla pénznemeCurrency of the invoice')

    _ElementMap.update({
        __taxNumber.name() : __taxNumber,
        __groupMemberTaxNumber.name() : __groupMemberTaxNumber,
        __name.name() : __name,
        __invoiceCategory.name() : __invoiceCategory,
        __paymentMethod.name() : __paymentMethod,
        __invoiceAppearance.name() : __invoiceAppearance,
        __source.name() : __source,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalQueryParamsType = AdditionalQueryParamsType
Namespace.addCategoryObject('typeBinding', 'AdditionalQueryParamsType', AdditionalQueryParamsType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}AnnulmentDataType with content type ELEMENT_ONLY
class AnnulmentDataType (pyxb.binding.basis.complexTypeDefinition):
    """Technikai érvénytelenítés státusz adataiStatus data of technical annulment"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnnulmentDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 414, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}annulmentVerificationStatus uses Python identifier annulmentVerificationStatus
    __annulmentVerificationStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentVerificationStatus'), 'annulmentVerificationStatus', '__httpschemas_nav_gov_huOSA3_0api_AnnulmentDataType_httpschemas_nav_gov_huOSA3_0apiannulmentVerificationStatus', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 420, 3), )

    
    annulmentVerificationStatus = property(__annulmentVerificationStatus.value, __annulmentVerificationStatus.set, None, 'Technikai érvénytelenítő kérések jóváhagyási státuszaVerification status of technical annulment requests')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}annulmentDecisionDate uses Python identifier annulmentDecisionDate
    __annulmentDecisionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentDecisionDate'), 'annulmentDecisionDate', '__httpschemas_nav_gov_huOSA3_0api_AnnulmentDataType_httpschemas_nav_gov_huOSA3_0apiannulmentDecisionDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 426, 3), )

    
    annulmentDecisionDate = property(__annulmentDecisionDate.value, __annulmentDecisionDate.set, None, 'A technikai érvénytelenítés jóváhagyásának vagy elutasításának időpontja UTC időbenDate of verification or rejection of the technical annulment in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}annulmentDecisionUser uses Python identifier annulmentDecisionUser
    __annulmentDecisionUser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentDecisionUser'), 'annulmentDecisionUser', '__httpschemas_nav_gov_huOSA3_0api_AnnulmentDataType_httpschemas_nav_gov_huOSA3_0apiannulmentDecisionUser', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 432, 3), )

    
    annulmentDecisionUser = property(__annulmentDecisionUser.value, __annulmentDecisionUser.set, None, "A technikai érvénytelenítést jóváhagyó vagy elutasító felhasználó neveLogin name of the user deciding over the technical annulment's verification or rejection")

    _ElementMap.update({
        __annulmentVerificationStatus.name() : __annulmentVerificationStatus,
        __annulmentDecisionDate.name() : __annulmentDecisionDate,
        __annulmentDecisionUser.name() : __annulmentDecisionUser
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AnnulmentDataType = AnnulmentDataType
Namespace.addCategoryObject('typeBinding', 'AnnulmentDataType', AnnulmentDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}AnnulmentOperationListType with content type ELEMENT_ONLY
class AnnulmentOperationListType (pyxb.binding.basis.complexTypeDefinition):
    """A kéréshez tartozó kötegelt technikai érvénytelenítésekBatch technical annulment operations of the request"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnnulmentOperationListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 440, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}annulmentOperation uses Python identifier annulmentOperation
    __annulmentOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperation'), 'annulmentOperation', '__httpschemas_nav_gov_huOSA3_0api_AnnulmentOperationListType_httpschemas_nav_gov_huOSA3_0apiannulmentOperation', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 446, 3), )

    
    annulmentOperation = property(__annulmentOperation.value, __annulmentOperation.set, None, 'A kéréshez tartozó technikai érvénytelenítő műveletTechnical annulment operation of the request')

    _ElementMap.update({
        __annulmentOperation.name() : __annulmentOperation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AnnulmentOperationListType = AnnulmentOperationListType
Namespace.addCategoryObject('typeBinding', 'AnnulmentOperationListType', AnnulmentOperationListType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}AnnulmentOperationType with content type ELEMENT_ONLY
class AnnulmentOperationType (pyxb.binding.basis.complexTypeDefinition):
    """A kéréshez tartozó technikai érvénytelenítő műveletTechnical annulment operation of the request"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnnulmentOperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 454, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpschemas_nav_gov_huOSA3_0api_AnnulmentOperationType_httpschemas_nav_gov_huOSA3_0apiindex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 460, 3), )

    
    index = property(__index.value, __index.set, None, 'A technikai érvénytelenítés sorszáma a kérésen belülSequence number of the technical annulment within the request')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}annulmentOperation uses Python identifier annulmentOperation
    __annulmentOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperation'), 'annulmentOperation', '__httpschemas_nav_gov_huOSA3_0api_AnnulmentOperationType_httpschemas_nav_gov_huOSA3_0apiannulmentOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 466, 3), )

    
    annulmentOperation = property(__annulmentOperation.value, __annulmentOperation.set, None, 'A kért technikai érvénytelenítés művelet típusaType of the desired technical annulment operation')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceAnnulment uses Python identifier invoiceAnnulment
    __invoiceAnnulment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceAnnulment'), 'invoiceAnnulment', '__httpschemas_nav_gov_huOSA3_0api_AnnulmentOperationType_httpschemas_nav_gov_huOSA3_0apiinvoiceAnnulment', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 472, 3), )

    
    invoiceAnnulment = property(__invoiceAnnulment.value, __invoiceAnnulment.set, None, 'Technikai érvénytelenítés adatok BASE64-ben kódolt tartalmaTechnical annulment data in BASE64 encoded form')

    _ElementMap.update({
        __index.name() : __index,
        __annulmentOperation.name() : __annulmentOperation,
        __invoiceAnnulment.name() : __invoiceAnnulment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AnnulmentOperationType = AnnulmentOperationType
Namespace.addCategoryObject('typeBinding', 'AnnulmentOperationType', AnnulmentOperationType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}AuditDataType with content type ELEMENT_ONLY
class AuditDataType (pyxb.binding.basis.complexTypeDefinition):
    """A számla audit adataiInvoice audit data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AuditDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 480, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insdate uses Python identifier insdate
    __insdate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insdate'), 'insdate', '__httpschemas_nav_gov_huOSA3_0api_AuditDataType_httpschemas_nav_gov_huOSA3_0apiinsdate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 486, 3), )

    
    insdate = property(__insdate.value, __insdate.set, None, 'A beszúrás időpontja UTC időbenInsert date in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insCusUser uses Python identifier insCusUser
    __insCusUser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insCusUser'), 'insCusUser', '__httpschemas_nav_gov_huOSA3_0api_AuditDataType_httpschemas_nav_gov_huOSA3_0apiinsCusUser', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 492, 3), )

    
    insCusUser = property(__insCusUser.value, __insCusUser.set, None, 'A beszúrást végző technikai felhasználóInserting technical user name')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpschemas_nav_gov_huOSA3_0api_AuditDataType_httpschemas_nav_gov_huOSA3_0apisource', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 498, 3), )

    
    source = property(__source.value, __source.set, None, 'Az adatszolgáltatás forrásaData exchange source')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httpschemas_nav_gov_huOSA3_0api_AuditDataType_httpschemas_nav_gov_huOSA3_0apitransactionId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 504, 3), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, 'A számla tranzakció azonosítója, ha az gépi interfészen került beküldésreTransaction ID of the invoice if it was exchanged via M2M interface')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpschemas_nav_gov_huOSA3_0api_AuditDataType_httpschemas_nav_gov_huOSA3_0apiindex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 510, 3), )

    
    index = property(__index.value, __index.set, None, 'A számla sorszáma a kérésen belülSequence number of the invoice within the request')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex uses Python identifier batchIndex
    __batchIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), 'batchIndex', '__httpschemas_nav_gov_huOSA3_0api_AuditDataType_httpschemas_nav_gov_huOSA3_0apibatchIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 516, 3), )

    
    batchIndex = property(__batchIndex.value, __batchIndex.set, None, 'A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion uses Python identifier originalRequestVersion
    __originalRequestVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), 'originalRequestVersion', '__httpschemas_nav_gov_huOSA3_0api_AuditDataType_httpschemas_nav_gov_huOSA3_0apioriginalRequestVersion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 522, 3), )

    
    originalRequestVersion = property(__originalRequestVersion.value, __originalRequestVersion.set, None, 'Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange')

    _ElementMap.update({
        __insdate.name() : __insdate,
        __insCusUser.name() : __insCusUser,
        __source.name() : __source,
        __transactionId.name() : __transactionId,
        __index.name() : __index,
        __batchIndex.name() : __batchIndex,
        __originalRequestVersion.name() : __originalRequestVersion
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AuditDataType = AuditDataType
Namespace.addCategoryObject('typeBinding', 'AuditDataType', AuditDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}BusinessValidationResultType with content type ELEMENT_ONLY
class BusinessValidationResultType (pyxb.binding.basis.complexTypeDefinition):
    """Üzleti validációs választípusBusiness validation response type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BusinessValidationResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 566, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}validationResultCode uses Python identifier validationResultCode
    __validationResultCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validationResultCode'), 'validationResultCode', '__httpschemas_nav_gov_huOSA3_0api_BusinessValidationResultType_httpschemas_nav_gov_huOSA3_0apivalidationResultCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 572, 3), )

    
    validationResultCode = property(__validationResultCode.value, __validationResultCode.set, None, 'Validációs eredményValidation result')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}validationErrorCode uses Python identifier validationErrorCode
    __validationErrorCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validationErrorCode'), 'validationErrorCode', '__httpschemas_nav_gov_huOSA3_0api_BusinessValidationResultType_httpschemas_nav_gov_huOSA3_0apivalidationErrorCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 578, 3), )

    
    validationErrorCode = property(__validationErrorCode.value, __validationErrorCode.set, None, 'Validációs hibakódValidation error code')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'message'), 'message', '__httpschemas_nav_gov_huOSA3_0api_BusinessValidationResultType_httpschemas_nav_gov_huOSA3_0apimessage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 584, 3), )

    
    message = property(__message.value, __message.set, None, 'Feldolgozási üzenetProcessing message')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}pointer uses Python identifier pointer
    __pointer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pointer'), 'pointer', '__httpschemas_nav_gov_huOSA3_0api_BusinessValidationResultType_httpschemas_nav_gov_huOSA3_0apipointer', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 590, 3), )

    
    pointer = property(__pointer.value, __pointer.set, None, 'Feldolgozási kurzor adatokProcessing cursor data')

    _ElementMap.update({
        __validationResultCode.name() : __validationResultCode,
        __validationErrorCode.name() : __validationErrorCode,
        __message.name() : __message,
        __pointer.name() : __pointer
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BusinessValidationResultType = BusinessValidationResultType
Namespace.addCategoryObject('typeBinding', 'BusinessValidationResultType', BusinessValidationResultType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}DateIntervalParamType with content type ELEMENT_ONLY
class DateIntervalParamType (pyxb.binding.basis.complexTypeDefinition):
    """Dátumos számla kereső paraméterDate query params of invoice"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateIntervalParamType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 598, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}dateFrom uses Python identifier dateFrom
    __dateFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateFrom'), 'dateFrom', '__httpschemas_nav_gov_huOSA3_0api_DateIntervalParamType_httpschemas_nav_gov_huOSA3_0apidateFrom', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 604, 3), )

    
    dateFrom = property(__dateFrom.value, __dateFrom.set, None, 'Dátum intervallum nagyobb vagy egyenlő paramétereDate interval greater or equals parameter')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}dateTo uses Python identifier dateTo
    __dateTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateTo'), 'dateTo', '__httpschemas_nav_gov_huOSA3_0api_DateIntervalParamType_httpschemas_nav_gov_huOSA3_0apidateTo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 610, 3), )

    
    dateTo = property(__dateTo.value, __dateTo.set, None, 'Dátum intervallum kisebb vagy egyenlő paramétereDate interval less or equals parameter')

    _ElementMap.update({
        __dateFrom.name() : __dateFrom,
        __dateTo.name() : __dateTo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateIntervalParamType = DateIntervalParamType
Namespace.addCategoryObject('typeBinding', 'DateIntervalParamType', DateIntervalParamType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}DateTimeIntervalParamType with content type ELEMENT_ONLY
class DateTimeIntervalParamType (pyxb.binding.basis.complexTypeDefinition):
    """Időpontos számla kereső paraméterDatestamp query params of invoice"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateTimeIntervalParamType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 618, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}dateTimeFrom uses Python identifier dateTimeFrom
    __dateTimeFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateTimeFrom'), 'dateTimeFrom', '__httpschemas_nav_gov_huOSA3_0api_DateTimeIntervalParamType_httpschemas_nav_gov_huOSA3_0apidateTimeFrom', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 624, 3), )

    
    dateTimeFrom = property(__dateTimeFrom.value, __dateTimeFrom.set, None, 'Időpontos intervallum nagyobb vagy egyenlő paramétere UTC idő szerintDatetime interval greater or equals parameter')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}dateTimeTo uses Python identifier dateTimeTo
    __dateTimeTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateTimeTo'), 'dateTimeTo', '__httpschemas_nav_gov_huOSA3_0api_DateTimeIntervalParamType_httpschemas_nav_gov_huOSA3_0apidateTimeTo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 630, 3), )

    
    dateTimeTo = property(__dateTimeTo.value, __dateTimeTo.set, None, 'Időpontos intervallum kisebb vagy egyenlő paramétere UTC idő szerintDatetime interval less or equals parameter')

    _ElementMap.update({
        __dateTimeFrom.name() : __dateTimeFrom,
        __dateTimeTo.name() : __dateTimeTo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateTimeIntervalParamType = DateTimeIntervalParamType
Namespace.addCategoryObject('typeBinding', 'DateTimeIntervalParamType', DateTimeIntervalParamType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceChainDigestResultType with content type ELEMENT_ONLY
class InvoiceChainDigestResultType (pyxb.binding.basis.complexTypeDefinition):
    """Számlalánc kivonat lekérdezés eredményeiInvoice chain digest query result"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceChainDigestResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 662, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}currentPage uses Python identifier currentPage
    __currentPage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentPage'), 'currentPage', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestResultType_httpschemas_nav_gov_huOSA3_0apicurrentPage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 668, 3), )

    
    currentPage = property(__currentPage.value, __currentPage.set, None, 'A jelenleg lekérdezett lapszámThe currently queried page count')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}availablePage uses Python identifier availablePage
    __availablePage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'availablePage'), 'availablePage', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestResultType_httpschemas_nav_gov_huOSA3_0apiavailablePage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 674, 3), )

    
    availablePage = property(__availablePage.value, __availablePage.set, None, 'A lekérdezés eredménye szerint elérhető utolsó lapszámThe highest available page count matching the query')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceChainElement uses Python identifier invoiceChainElement
    __invoiceChainElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainElement'), 'invoiceChainElement', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestResultType_httpschemas_nav_gov_huOSA3_0apiinvoiceChainElement', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 680, 3), )

    
    invoiceChainElement = property(__invoiceChainElement.value, __invoiceChainElement.set, None, 'Számlalánc elemInvoice chain element')

    _ElementMap.update({
        __currentPage.name() : __currentPage,
        __availablePage.name() : __availablePage,
        __invoiceChainElement.name() : __invoiceChainElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceChainDigestResultType = InvoiceChainDigestResultType
Namespace.addCategoryObject('typeBinding', 'InvoiceChainDigestResultType', InvoiceChainDigestResultType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceChainDigestType with content type ELEMENT_ONLY
class InvoiceChainDigestType (pyxb.binding.basis.complexTypeDefinition):
    """Számlalánc kivonat adatokInvoice chain digest data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceChainDigestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 688, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumber uses Python identifier invoiceNumber
    __invoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), 'invoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 694, 3), )

    
    invoiceNumber = property(__invoiceNumber.value, __invoiceNumber.set, None, 'Számla vagy módosító okirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pontSequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex uses Python identifier batchIndex
    __batchIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), 'batchIndex', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestType_httpschemas_nav_gov_huOSA3_0apibatchIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 700, 3), )

    
    batchIndex = property(__batchIndex.value, __batchIndex.set, None, 'A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation uses Python identifier invoiceOperation
    __invoiceOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), 'invoiceOperation', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 706, 3), )

    
    invoiceOperation = property(__invoiceOperation.value, __invoiceOperation.set, None, 'Számlaművelet típusInvoice operation type')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}supplierTaxNumber uses Python identifier supplierTaxNumber
    __supplierTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), 'supplierTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestType_httpschemas_nav_gov_huOSA3_0apisupplierTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 712, 3), )

    
    supplierTaxNumber = property(__supplierTaxNumber.value, __supplierTaxNumber.set, None, "A kibocsátó adószámaThe supplier's tax number")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}customerTaxNumber uses Python identifier customerTaxNumber
    __customerTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber'), 'customerTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestType_httpschemas_nav_gov_huOSA3_0apicustomerTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 718, 3), )

    
    customerTaxNumber = property(__customerTaxNumber.value, __customerTaxNumber.set, None, "A vevő adószámaThe buyer's tax number")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insDate uses Python identifier insDate
    __insDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insDate'), 'insDate', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestType_httpschemas_nav_gov_huOSA3_0apiinsDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 724, 3), )

    
    insDate = property(__insDate.value, __insDate.set, None, 'A beszúrás időpontja UTC időbenInsert date in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion uses Python identifier originalRequestVersion
    __originalRequestVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), 'originalRequestVersion', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainDigestType_httpschemas_nav_gov_huOSA3_0apioriginalRequestVersion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 730, 3), )

    
    originalRequestVersion = property(__originalRequestVersion.value, __originalRequestVersion.set, None, 'Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange')

    _ElementMap.update({
        __invoiceNumber.name() : __invoiceNumber,
        __batchIndex.name() : __batchIndex,
        __invoiceOperation.name() : __invoiceOperation,
        __supplierTaxNumber.name() : __supplierTaxNumber,
        __customerTaxNumber.name() : __customerTaxNumber,
        __insDate.name() : __insDate,
        __originalRequestVersion.name() : __originalRequestVersion
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceChainDigestType = InvoiceChainDigestType
Namespace.addCategoryObject('typeBinding', 'InvoiceChainDigestType', InvoiceChainDigestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceChainElementType with content type ELEMENT_ONLY
class InvoiceChainElementType (pyxb.binding.basis.complexTypeDefinition):
    """Számlalánc elemInvoice chain element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceChainElementType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 738, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceChainDigest uses Python identifier invoiceChainDigest
    __invoiceChainDigest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainDigest'), 'invoiceChainDigest', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainElementType_httpschemas_nav_gov_huOSA3_0apiinvoiceChainDigest', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 744, 3), )

    
    invoiceChainDigest = property(__invoiceChainDigest.value, __invoiceChainDigest.set, None, 'Számlalánc kivonat adatokInvoice chain digest data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceLines uses Python identifier invoiceLines
    __invoiceLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceLines'), 'invoiceLines', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainElementType_httpschemas_nav_gov_huOSA3_0apiinvoiceLines', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 750, 3), )

    
    invoiceLines = property(__invoiceLines.value, __invoiceLines.set, None, 'A számlán vagy módosító okiraton szereplő tételek kivonatos adataiProduct/service digest data appearing on the invoice or the modification document')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceReferenceData uses Python identifier invoiceReferenceData
    __invoiceReferenceData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceReferenceData'), 'invoiceReferenceData', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainElementType_httpschemas_nav_gov_huOSA3_0apiinvoiceReferenceData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 756, 3), )

    
    invoiceReferenceData = property(__invoiceReferenceData.value, __invoiceReferenceData.set, None, 'A módosítás vagy érvénytelenítés adataiModification or cancellation data')

    _ElementMap.update({
        __invoiceChainDigest.name() : __invoiceChainDigest,
        __invoiceLines.name() : __invoiceLines,
        __invoiceReferenceData.name() : __invoiceReferenceData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceChainElementType = InvoiceChainElementType
Namespace.addCategoryObject('typeBinding', 'InvoiceChainElementType', InvoiceChainElementType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceChainQueryType with content type ELEMENT_ONLY
class InvoiceChainQueryType (pyxb.binding.basis.complexTypeDefinition):
    """Számlalánc kivonat lekérdezés számlaszám paramétereInvoice number param of the invoice chain digest query"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceChainQueryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 764, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumber uses Python identifier invoiceNumber
    __invoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), 'invoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainQueryType_httpschemas_nav_gov_huOSA3_0apiinvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 770, 3), )

    
    invoiceNumber = property(__invoiceNumber.value, __invoiceNumber.set, None, 'Számla vagy módosító okirat sorszámaSequential number of the original or modification invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDirection uses Python identifier invoiceDirection
    __invoiceDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection'), 'invoiceDirection', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainQueryType_httpschemas_nav_gov_huOSA3_0apiinvoiceDirection', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 776, 3), )

    
    invoiceDirection = property(__invoiceDirection.value, __invoiceDirection.set, None, 'Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxNumber uses Python identifier taxNumber
    __taxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), 'taxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceChainQueryType_httpschemas_nav_gov_huOSA3_0apitaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 782, 3), )

    
    taxNumber = property(__taxNumber.value, __taxNumber.set, None, 'A számla kiállítójának vagy vevőjének adószáma (a keresési feltétel az invoiceDirection tag értékétől függ)Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)')

    _ElementMap.update({
        __invoiceNumber.name() : __invoiceNumber,
        __invoiceDirection.name() : __invoiceDirection,
        __taxNumber.name() : __taxNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceChainQueryType = InvoiceChainQueryType
Namespace.addCategoryObject('typeBinding', 'InvoiceChainQueryType', InvoiceChainQueryType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceDataResultType with content type ELEMENT_ONLY
class InvoiceDataResultType (pyxb.binding.basis.complexTypeDefinition):
    """Számlaszámra történő lekérdezés eredményeInvoice number based query result"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceDataResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 790, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceData uses Python identifier invoiceData
    __invoiceData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceData'), 'invoiceData', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDataResultType_httpschemas_nav_gov_huOSA3_0apiinvoiceData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 796, 3), )

    
    invoiceData = property(__invoiceData.value, __invoiceData.set, None, 'Számla adatok BASE64-ben kódolt tartalmaInvoice data in BASE64 encoded form')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}auditData uses Python identifier auditData
    __auditData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'auditData'), 'auditData', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDataResultType_httpschemas_nav_gov_huOSA3_0apiauditData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 802, 3), )

    
    auditData = property(__auditData.value, __auditData.set, None, 'A számla audit adataiInvoice audit data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}compressedContentIndicator uses Python identifier compressedContentIndicator
    __compressedContentIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'compressedContentIndicator'), 'compressedContentIndicator', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDataResultType_httpschemas_nav_gov_huOSA3_0apicompressedContentIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 808, 3), )

    
    compressedContentIndicator = property(__compressedContentIndicator.value, __compressedContentIndicator.set, None, 'Jelöli, ha az invoice tartalmát a BASE64 dekódolást követően még ki kell tömöríteni az olvasáshozIndicates if the content of the invoice needs to be decompressed to be read following the BASE64 decoding')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}electronicInvoiceHash uses Python identifier electronicInvoiceHash
    __electronicInvoiceHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electronicInvoiceHash'), 'electronicInvoiceHash', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDataResultType_httpschemas_nav_gov_huOSA3_0apielectronicInvoiceHash', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 814, 3), )

    
    electronicInvoiceHash = property(__electronicInvoiceHash.value, __electronicInvoiceHash.set, None, 'Elektronikus számla vagy módosító okirat állomány hash lenyomataElectronic invoice or modification document file hash value')

    _ElementMap.update({
        __invoiceData.name() : __invoiceData,
        __auditData.name() : __auditData,
        __compressedContentIndicator.name() : __compressedContentIndicator,
        __electronicInvoiceHash.name() : __electronicInvoiceHash
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceDataResultType = InvoiceDataResultType
Namespace.addCategoryObject('typeBinding', 'InvoiceDataResultType', InvoiceDataResultType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceDigestResultType with content type ELEMENT_ONLY
class InvoiceDigestResultType (pyxb.binding.basis.complexTypeDefinition):
    """Számla lekérdezési eredményekInvoice query results"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceDigestResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 822, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}currentPage uses Python identifier currentPage
    __currentPage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentPage'), 'currentPage', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestResultType_httpschemas_nav_gov_huOSA3_0apicurrentPage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 828, 3), )

    
    currentPage = property(__currentPage.value, __currentPage.set, None, 'A jelenleg lekérdezett lapszámThe currently queried page count')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}availablePage uses Python identifier availablePage
    __availablePage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'availablePage'), 'availablePage', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestResultType_httpschemas_nav_gov_huOSA3_0apiavailablePage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 834, 3), )

    
    availablePage = property(__availablePage.value, __availablePage.set, None, 'A lekérdezés eredménye szerint elérhető utolsó lapszámThe highest available page count matching the query')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDigest uses Python identifier invoiceDigest
    __invoiceDigest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDigest'), 'invoiceDigest', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestResultType_httpschemas_nav_gov_huOSA3_0apiinvoiceDigest', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 840, 3), )

    
    invoiceDigest = property(__invoiceDigest.value, __invoiceDigest.set, None, 'Számla kivonat lekérdezési eredményInvoice digest query result')

    _ElementMap.update({
        __currentPage.name() : __currentPage,
        __availablePage.name() : __availablePage,
        __invoiceDigest.name() : __invoiceDigest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceDigestResultType = InvoiceDigestResultType
Namespace.addCategoryObject('typeBinding', 'InvoiceDigestResultType', InvoiceDigestResultType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceDigestType with content type ELEMENT_ONLY
class InvoiceDigestType (pyxb.binding.basis.complexTypeDefinition):
    """Kivonatos lekérdezési eredményDigest query result"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceDigestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 848, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumber uses Python identifier invoiceNumber
    __invoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), 'invoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 854, 3), )

    
    invoiceNumber = property(__invoiceNumber.value, __invoiceNumber.set, None, 'Számla vagy módosító okirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pontSequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex uses Python identifier batchIndex
    __batchIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), 'batchIndex', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apibatchIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 860, 3), )

    
    batchIndex = property(__batchIndex.value, __batchIndex.set, None, 'A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation uses Python identifier invoiceOperation
    __invoiceOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), 'invoiceOperation', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 866, 3), )

    
    invoiceOperation = property(__invoiceOperation.value, __invoiceOperation.set, None, 'Számlaművelet típusInvoice operation type')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceCategory uses Python identifier invoiceCategory
    __invoiceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory'), 'invoiceCategory', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceCategory', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 872, 3), )

    
    invoiceCategory = property(__invoiceCategory.value, __invoiceCategory.set, None, 'A számla típusaType of invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceIssueDate uses Python identifier invoiceIssueDate
    __invoiceIssueDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate'), 'invoiceIssueDate', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceIssueDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 878, 3), )

    
    invoiceIssueDate = property(__invoiceIssueDate.value, __invoiceIssueDate.set, None, 'Számla vagy módosító okirat kiállításának dátumaInvoice or modification document issue date')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}supplierTaxNumber uses Python identifier supplierTaxNumber
    __supplierTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), 'supplierTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apisupplierTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 884, 3), )

    
    supplierTaxNumber = property(__supplierTaxNumber.value, __supplierTaxNumber.set, None, "A kibocsátó adószámaThe supplier's tax number")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}supplierGroupMemberTaxNumber uses Python identifier supplierGroupMemberTaxNumber
    __supplierGroupMemberTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierGroupMemberTaxNumber'), 'supplierGroupMemberTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apisupplierGroupMemberTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 890, 3), )

    
    supplierGroupMemberTaxNumber = property(__supplierGroupMemberTaxNumber.value, __supplierGroupMemberTaxNumber.set, None, "A kibocsátó csoporttag számaThe supplier's group tax number")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}supplierName uses Python identifier supplierName
    __supplierName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierName'), 'supplierName', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apisupplierName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 896, 3), )

    
    supplierName = property(__supplierName.value, __supplierName.set, None, 'Az eladó (szállító) neveName of the seller (supplier)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}customerTaxNumber uses Python identifier customerTaxNumber
    __customerTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber'), 'customerTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apicustomerTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 902, 3), )

    
    customerTaxNumber = property(__customerTaxNumber.value, __customerTaxNumber.set, None, "A vevő adószámaThe buyer's tax number")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}customerGroupMemberTaxNumber uses Python identifier customerGroupMemberTaxNumber
    __customerGroupMemberTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerGroupMemberTaxNumber'), 'customerGroupMemberTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apicustomerGroupMemberTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 908, 3), )

    
    customerGroupMemberTaxNumber = property(__customerGroupMemberTaxNumber.value, __customerGroupMemberTaxNumber.set, None, "A vevő csoporttag számaThe buyer's group tax number")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}customerName uses Python identifier customerName
    __customerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerName'), 'customerName', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apicustomerName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 914, 3), )

    
    customerName = property(__customerName.value, __customerName.set, None, 'A vevő neveName of the customer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}paymentMethod uses Python identifier paymentMethod
    __paymentMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), 'paymentMethod', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apipaymentMethod', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 920, 3), )

    
    paymentMethod = property(__paymentMethod.value, __paymentMethod.set, None, 'Fizetés módjaMethod of payment')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}paymentDate uses Python identifier paymentDate
    __paymentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentDate'), 'paymentDate', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apipaymentDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 926, 3), )

    
    paymentDate = property(__paymentDate.value, __paymentDate.set, None, 'Fizetési határidőDeadline for payment')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceAppearance uses Python identifier invoiceAppearance
    __invoiceAppearance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance'), 'invoiceAppearance', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceAppearance', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 932, 3), )

    
    invoiceAppearance = property(__invoiceAppearance.value, __invoiceAppearance.set, None, 'A számla megjelenési formájaForm of appearance of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apisource', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 938, 3), )

    
    source = property(__source.value, __source.set, None, 'Az adatszolgáltatás forrásaData exchange source')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDeliveryDate uses Python identifier invoiceDeliveryDate
    __invoiceDeliveryDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryDate'), 'invoiceDeliveryDate', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceDeliveryDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 944, 3), )

    
    invoiceDeliveryDate = property(__invoiceDeliveryDate.value, __invoiceDeliveryDate.set, None, 'Számla teljesítési dátumaInvoice delivery date')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apicurrency', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 950, 3), )

    
    currency = property(__currency.value, __currency.set, None, 'A számla pénznemeCurrency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNetAmount uses Python identifier invoiceNetAmount
    __invoiceNetAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount'), 'invoiceNetAmount', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceNetAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 956, 3), )

    
    invoiceNetAmount = property(__invoiceNetAmount.value, __invoiceNetAmount.set, None, 'A számla nettó összege a számla pénznemébenInvoice net amount expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNetAmountHUF uses Python identifier invoiceNetAmountHUF
    __invoiceNetAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF'), 'invoiceNetAmountHUF', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceNetAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 962, 3), )

    
    invoiceNetAmountHUF = property(__invoiceNetAmountHUF.value, __invoiceNetAmountHUF.set, None, 'A számla nettó összege forintbanInvoice net amount expressed in HUF')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceVatAmount uses Python identifier invoiceVatAmount
    __invoiceVatAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount'), 'invoiceVatAmount', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceVatAmount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 968, 3), )

    
    invoiceVatAmount = property(__invoiceVatAmount.value, __invoiceVatAmount.set, None, 'A számla ÁFA összege a számla pénznemébenInvoice VAT amount expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceVatAmountHUF uses Python identifier invoiceVatAmountHUF
    __invoiceVatAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF'), 'invoiceVatAmountHUF', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinvoiceVatAmountHUF', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 974, 3), )

    
    invoiceVatAmountHUF = property(__invoiceVatAmountHUF.value, __invoiceVatAmountHUF.set, None, 'A számla ÁFA összege forintbanInvoice VAT amount expressed in HUF')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apitransactionId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 980, 3), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, 'Az adatszolgáltatás tranzakció azonosítójaTransaction identifier of the data exchange')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiindex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 986, 3), )

    
    index = property(__index.value, __index.set, None, 'A számla sorszáma a kérésen belülSequence number of the invoice within the request')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber uses Python identifier originalInvoiceNumber
    __originalInvoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), 'originalInvoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apioriginalInvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 992, 3), )

    
    originalInvoiceNumber = property(__originalInvoiceNumber.value, __originalInvoiceNumber.set, None, 'Az eredeti számla sorszáma, melyre a módosítás vonatkozikSequence number of the original invoice, on which the modification occurs')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}modificationIndex uses Python identifier modificationIndex
    __modificationIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex'), 'modificationIndex', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apimodificationIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 998, 3), )

    
    modificationIndex = property(__modificationIndex.value, __modificationIndex.set, None, 'A számlára vonatkozó módosító okirat egyedi sorszámaThe unique sequence number referring to the original invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insDate uses Python identifier insDate
    __insDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insDate'), 'insDate', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apiinsDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1004, 3), )

    
    insDate = property(__insDate.value, __insDate.set, None, 'A beszúrás időpontja UTC időbenInsert date in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}completenessIndicator uses Python identifier completenessIndicator
    __completenessIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'completenessIndicator'), 'completenessIndicator', '__httpschemas_nav_gov_huOSA3_0api_InvoiceDigestType_httpschemas_nav_gov_huOSA3_0apicompletenessIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1010, 3), )

    
    completenessIndicator = property(__completenessIndicator.value, __completenessIndicator.set, None, 'Jelöli, ha az adatszolgáltatás maga a számla (a számlán nem szerepel több adat)Indicates whether the data exchange is identical with the invoice (the invoice does not contain any more data)')

    _ElementMap.update({
        __invoiceNumber.name() : __invoiceNumber,
        __batchIndex.name() : __batchIndex,
        __invoiceOperation.name() : __invoiceOperation,
        __invoiceCategory.name() : __invoiceCategory,
        __invoiceIssueDate.name() : __invoiceIssueDate,
        __supplierTaxNumber.name() : __supplierTaxNumber,
        __supplierGroupMemberTaxNumber.name() : __supplierGroupMemberTaxNumber,
        __supplierName.name() : __supplierName,
        __customerTaxNumber.name() : __customerTaxNumber,
        __customerGroupMemberTaxNumber.name() : __customerGroupMemberTaxNumber,
        __customerName.name() : __customerName,
        __paymentMethod.name() : __paymentMethod,
        __paymentDate.name() : __paymentDate,
        __invoiceAppearance.name() : __invoiceAppearance,
        __source.name() : __source,
        __invoiceDeliveryDate.name() : __invoiceDeliveryDate,
        __currency.name() : __currency,
        __invoiceNetAmount.name() : __invoiceNetAmount,
        __invoiceNetAmountHUF.name() : __invoiceNetAmountHUF,
        __invoiceVatAmount.name() : __invoiceVatAmount,
        __invoiceVatAmountHUF.name() : __invoiceVatAmountHUF,
        __transactionId.name() : __transactionId,
        __index.name() : __index,
        __originalInvoiceNumber.name() : __originalInvoiceNumber,
        __modificationIndex.name() : __modificationIndex,
        __insDate.name() : __insDate,
        __completenessIndicator.name() : __completenessIndicator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceDigestType = InvoiceDigestType
Namespace.addCategoryObject('typeBinding', 'InvoiceDigestType', InvoiceDigestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceLinesType with content type ELEMENT_ONLY
class InvoiceLinesType (pyxb.binding.basis.complexTypeDefinition):
    """A számlán vagy módosító okiraton szereplő tételek kivonatos adataiProduct/service digest data appearing on the invoice or the modification document"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceLinesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1018, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}maxLineNumber uses Python identifier maxLineNumber
    __maxLineNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxLineNumber'), 'maxLineNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceLinesType_httpschemas_nav_gov_huOSA3_0apimaxLineNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1024, 3), )

    
    maxLineNumber = property(__maxLineNumber.value, __maxLineNumber.set, None, 'A sorok száma közül a legmagasabb, amit a számla tartalmazThe highest line number value the invoice contains')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}newCreatedLines uses Python identifier newCreatedLines
    __newCreatedLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'newCreatedLines'), 'newCreatedLines', '__httpschemas_nav_gov_huOSA3_0api_InvoiceLinesType_httpschemas_nav_gov_huOSA3_0apinewCreatedLines', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1030, 3), )

    
    newCreatedLines = property(__newCreatedLines.value, __newCreatedLines.set, None, 'A módosító okirat által újként létrehozott számlasorokNew invoice lines created by the modification document')

    _ElementMap.update({
        __maxLineNumber.name() : __maxLineNumber,
        __newCreatedLines.name() : __newCreatedLines
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceLinesType = InvoiceLinesType
Namespace.addCategoryObject('typeBinding', 'InvoiceLinesType', InvoiceLinesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceNumberQueryType with content type ELEMENT_ONLY
class InvoiceNumberQueryType (pyxb.binding.basis.complexTypeDefinition):
    """Számla lekérdezés számlaszám paramétereInvoice number param of the Invoice query"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceNumberQueryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1038, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumber uses Python identifier invoiceNumber
    __invoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), 'invoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceNumberQueryType_httpschemas_nav_gov_huOSA3_0apiinvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1044, 3), )

    
    invoiceNumber = property(__invoiceNumber.value, __invoiceNumber.set, None, 'Számla vagy módosító okirat sorszámaSequential number of the original or modification invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDirection uses Python identifier invoiceDirection
    __invoiceDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection'), 'invoiceDirection', '__httpschemas_nav_gov_huOSA3_0api_InvoiceNumberQueryType_httpschemas_nav_gov_huOSA3_0apiinvoiceDirection', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1050, 3), )

    
    invoiceDirection = property(__invoiceDirection.value, __invoiceDirection.set, None, 'Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex uses Python identifier batchIndex
    __batchIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), 'batchIndex', '__httpschemas_nav_gov_huOSA3_0api_InvoiceNumberQueryType_httpschemas_nav_gov_huOSA3_0apibatchIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1056, 3), )

    
    batchIndex = property(__batchIndex.value, __batchIndex.set, None, 'A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}supplierTaxNumber uses Python identifier supplierTaxNumber
    __supplierTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), 'supplierTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceNumberQueryType_httpschemas_nav_gov_huOSA3_0apisupplierTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1062, 3), )

    
    supplierTaxNumber = property(__supplierTaxNumber.value, __supplierTaxNumber.set, None, "Vevő oldali lekérdezés esetén a számla kiállítójának adószáma, ha több érvényes számla is megtalálható azonos sorszámmalThe supplier's tax number in case of querying as customer, if the query result found more than one valid invoices with the same invoice number")

    _ElementMap.update({
        __invoiceNumber.name() : __invoiceNumber,
        __invoiceDirection.name() : __invoiceDirection,
        __batchIndex.name() : __batchIndex,
        __supplierTaxNumber.name() : __supplierTaxNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceNumberQueryType = InvoiceNumberQueryType
Namespace.addCategoryObject('typeBinding', 'InvoiceNumberQueryType', InvoiceNumberQueryType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceOperationListType with content type ELEMENT_ONLY
class InvoiceOperationListType (pyxb.binding.basis.complexTypeDefinition):
    """A kéréshez tartozó kötegelt számlaműveletekBatch invoice operations of the request"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceOperationListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1070, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}compressedContent uses Python identifier compressedContent
    __compressedContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'compressedContent'), 'compressedContent', '__httpschemas_nav_gov_huOSA3_0api_InvoiceOperationListType_httpschemas_nav_gov_huOSA3_0apicompressedContent', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1076, 3), )

    
    compressedContent = property(__compressedContent.value, __compressedContent.set, None, 'Tömörített tartalom jelzése a feldolgozási folyamat számáraCompressed content indicator for the processing flow')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation uses Python identifier invoiceOperation
    __invoiceOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), 'invoiceOperation', '__httpschemas_nav_gov_huOSA3_0api_InvoiceOperationListType_httpschemas_nav_gov_huOSA3_0apiinvoiceOperation', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1082, 3), )

    
    invoiceOperation = property(__invoiceOperation.value, __invoiceOperation.set, None, 'A kéréshez tartozó számlaműveletInvoice operation of the request')

    _ElementMap.update({
        __compressedContent.name() : __compressedContent,
        __invoiceOperation.name() : __invoiceOperation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceOperationListType = InvoiceOperationListType
Namespace.addCategoryObject('typeBinding', 'InvoiceOperationListType', InvoiceOperationListType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceOperationType with content type ELEMENT_ONLY
class InvoiceOperationType (pyxb.binding.basis.complexTypeDefinition):
    """A kéréshez tartozó számlaműveletInvoice operation of the request"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceOperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1090, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpschemas_nav_gov_huOSA3_0api_InvoiceOperationType_httpschemas_nav_gov_huOSA3_0apiindex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1096, 3), )

    
    index = property(__index.value, __index.set, None, 'A számla sorszáma a kérésen belülSequence number of the invoice within the request')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation uses Python identifier invoiceOperation
    __invoiceOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), 'invoiceOperation', '__httpschemas_nav_gov_huOSA3_0api_InvoiceOperationType_httpschemas_nav_gov_huOSA3_0apiinvoiceOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1102, 3), )

    
    invoiceOperation = property(__invoiceOperation.value, __invoiceOperation.set, None, 'A kért számla művelet típusaType of the desired invoice operation')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceData uses Python identifier invoiceData
    __invoiceData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceData'), 'invoiceData', '__httpschemas_nav_gov_huOSA3_0api_InvoiceOperationType_httpschemas_nav_gov_huOSA3_0apiinvoiceData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1108, 3), )

    
    invoiceData = property(__invoiceData.value, __invoiceData.set, None, 'Számla adatok BASE64-ben kódolt tartalmaInvoice data in BASE64 encoded form')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}electronicInvoiceHash uses Python identifier electronicInvoiceHash
    __electronicInvoiceHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electronicInvoiceHash'), 'electronicInvoiceHash', '__httpschemas_nav_gov_huOSA3_0api_InvoiceOperationType_httpschemas_nav_gov_huOSA3_0apielectronicInvoiceHash', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1114, 3), )

    
    electronicInvoiceHash = property(__electronicInvoiceHash.value, __electronicInvoiceHash.set, None, 'Elektronikus számla vagy módosító okirat állomány hash lenyomataElectronic invoice or modification document file hash value')

    _ElementMap.update({
        __index.name() : __index,
        __invoiceOperation.name() : __invoiceOperation,
        __invoiceData.name() : __invoiceData,
        __electronicInvoiceHash.name() : __electronicInvoiceHash
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceOperationType = InvoiceOperationType
Namespace.addCategoryObject('typeBinding', 'InvoiceOperationType', InvoiceOperationType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceQueryParamsType with content type ELEMENT_ONLY
class InvoiceQueryParamsType (pyxb.binding.basis.complexTypeDefinition):
    """Számla lekérdezési paraméterekInvoice query parameters"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceQueryParamsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1122, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}mandatoryQueryParams uses Python identifier mandatoryQueryParams
    __mandatoryQueryParams = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mandatoryQueryParams'), 'mandatoryQueryParams', '__httpschemas_nav_gov_huOSA3_0api_InvoiceQueryParamsType_httpschemas_nav_gov_huOSA3_0apimandatoryQueryParams', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1128, 3), )

    
    mandatoryQueryParams = property(__mandatoryQueryParams.value, __mandatoryQueryParams.set, None, 'A számla lekérdezés kötelező paramétereiMandatory params of the invoice query')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}additionalQueryParams uses Python identifier additionalQueryParams
    __additionalQueryParams = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalQueryParams'), 'additionalQueryParams', '__httpschemas_nav_gov_huOSA3_0api_InvoiceQueryParamsType_httpschemas_nav_gov_huOSA3_0apiadditionalQueryParams', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1134, 3), )

    
    additionalQueryParams = property(__additionalQueryParams.value, __additionalQueryParams.set, None, 'A számla lekérdezés kiegészítő paramétereiAdditional params of the invoice query')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}relationalQueryParams uses Python identifier relationalQueryParams
    __relationalQueryParams = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relationalQueryParams'), 'relationalQueryParams', '__httpschemas_nav_gov_huOSA3_0api_InvoiceQueryParamsType_httpschemas_nav_gov_huOSA3_0apirelationalQueryParams', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1140, 3), )

    
    relationalQueryParams = property(__relationalQueryParams.value, __relationalQueryParams.set, None, 'A számla lekérdezés relációs paramétereiRelational params of the invoice query')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionQueryParams uses Python identifier transactionQueryParams
    __transactionQueryParams = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionQueryParams'), 'transactionQueryParams', '__httpschemas_nav_gov_huOSA3_0api_InvoiceQueryParamsType_httpschemas_nav_gov_huOSA3_0apitransactionQueryParams', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1146, 3), )

    
    transactionQueryParams = property(__transactionQueryParams.value, __transactionQueryParams.set, None, 'A számla lekérdezés tranzakciós paramétereiTransactional params of the invoice query')

    _ElementMap.update({
        __mandatoryQueryParams.name() : __mandatoryQueryParams,
        __additionalQueryParams.name() : __additionalQueryParams,
        __relationalQueryParams.name() : __relationalQueryParams,
        __transactionQueryParams.name() : __transactionQueryParams
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceQueryParamsType = InvoiceQueryParamsType
Namespace.addCategoryObject('typeBinding', 'InvoiceQueryParamsType', InvoiceQueryParamsType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}InvoiceReferenceDataType with content type ELEMENT_ONLY
class InvoiceReferenceDataType (pyxb.binding.basis.complexTypeDefinition):
    """A módosítás vagy érvénytelenítés adataiModification or cancellation data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceReferenceDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1154, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber uses Python identifier originalInvoiceNumber
    __originalInvoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), 'originalInvoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_InvoiceReferenceDataType_httpschemas_nav_gov_huOSA3_0apioriginalInvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1160, 3), )

    
    originalInvoiceNumber = property(__originalInvoiceNumber.value, __originalInvoiceNumber.set, None, 'Az eredeti számla sorszáma, melyre a módosítás vonatkozik  - ÁFA tv. 170. § (1) c)Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}modifyWithoutMaster uses Python identifier modifyWithoutMaster
    __modifyWithoutMaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modifyWithoutMaster'), 'modifyWithoutMaster', '__httpschemas_nav_gov_huOSA3_0api_InvoiceReferenceDataType_httpschemas_nav_gov_huOSA3_0apimodifyWithoutMaster', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1166, 3), )

    
    modifyWithoutMaster = property(__modifyWithoutMaster.value, __modifyWithoutMaster.set, None, 'Annak jelzése, hogy a módosítás olyan alapszámlára hivatkozik, amelyről nem történt és nem is fog történni adatszolgáltatásIndicates whether the modification references to an original invoice which is not and will not be exchanged')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}modificationTimestamp uses Python identifier modificationTimestamp
    __modificationTimestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modificationTimestamp'), 'modificationTimestamp', '__httpschemas_nav_gov_huOSA3_0api_InvoiceReferenceDataType_httpschemas_nav_gov_huOSA3_0apimodificationTimestamp', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1173, 4), )

    
    modificationTimestamp = property(__modificationTimestamp.value, __modificationTimestamp.set, None, 'A módosító okirat készítésének időbélyege a forrásrendszerben UTC időbenCreation date timestamp of the modification document in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}modificationIndex uses Python identifier modificationIndex
    __modificationIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex'), 'modificationIndex', '__httpschemas_nav_gov_huOSA3_0api_InvoiceReferenceDataType_httpschemas_nav_gov_huOSA3_0apimodificationIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1179, 4), )

    
    modificationIndex = property(__modificationIndex.value, __modificationIndex.set, None, 'A számlára vonatkozó módosító okirat egyedi sorszámaThe unique sequence number referring to the original invoice')

    _ElementMap.update({
        __originalInvoiceNumber.name() : __originalInvoiceNumber,
        __modifyWithoutMaster.name() : __modifyWithoutMaster,
        __modificationTimestamp.name() : __modificationTimestamp,
        __modificationIndex.name() : __modificationIndex
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceReferenceDataType = InvoiceReferenceDataType
Namespace.addCategoryObject('typeBinding', 'InvoiceReferenceDataType', InvoiceReferenceDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}MandatoryQueryParamsType with content type ELEMENT_ONLY
class MandatoryQueryParamsType (pyxb.binding.basis.complexTypeDefinition):
    """A számla lekérdezés kötelező paramétereiMandatory params of the invoice query"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MandatoryQueryParamsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1236, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceIssueDate uses Python identifier invoiceIssueDate
    __invoiceIssueDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate'), 'invoiceIssueDate', '__httpschemas_nav_gov_huOSA3_0api_MandatoryQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceIssueDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1242, 3), )

    
    invoiceIssueDate = property(__invoiceIssueDate.value, __invoiceIssueDate.set, None, 'Számla kiállításának dátumtartományaDate range of the invoice issue date')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insDate uses Python identifier insDate
    __insDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insDate'), 'insDate', '__httpschemas_nav_gov_huOSA3_0api_MandatoryQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinsDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1248, 3), )

    
    insDate = property(__insDate.value, __insDate.set, None, 'Számla adatszolgáltatás feldolgozásának időpont tartománya UTC idő szerintDatetime range of processing data exchange in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber uses Python identifier originalInvoiceNumber
    __originalInvoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), 'originalInvoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_MandatoryQueryParamsType_httpschemas_nav_gov_huOSA3_0apioriginalInvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1254, 3), )

    
    originalInvoiceNumber = property(__originalInvoiceNumber.value, __originalInvoiceNumber.set, None, 'Az eredeti számla sorszáma, melyre a módosítás vonatkozikSequence number of the original invoice, on which the modification occurs')

    _ElementMap.update({
        __invoiceIssueDate.name() : __invoiceIssueDate,
        __insDate.name() : __insDate,
        __originalInvoiceNumber.name() : __originalInvoiceNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MandatoryQueryParamsType = MandatoryQueryParamsType
Namespace.addCategoryObject('typeBinding', 'MandatoryQueryParamsType', MandatoryQueryParamsType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}NewCreatedLinesType with content type ELEMENT_ONLY
class NewCreatedLinesType (pyxb.binding.basis.complexTypeDefinition):
    """A módosító okirat által újként létrehozott számlasorokNew invoice lines created by the modification document"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NewCreatedLinesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1262, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}lineNumberIntervalStart uses Python identifier lineNumberIntervalStart
    __lineNumberIntervalStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNumberIntervalStart'), 'lineNumberIntervalStart', '__httpschemas_nav_gov_huOSA3_0api_NewCreatedLinesType_httpschemas_nav_gov_huOSA3_0apilineNumberIntervalStart', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1268, 3), )

    
    lineNumberIntervalStart = property(__lineNumberIntervalStart.value, __lineNumberIntervalStart.set, None, 'Számla sor intervallum kezdeteInvoice line interval start')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}lineNumberIntervalEnd uses Python identifier lineNumberIntervalEnd
    __lineNumberIntervalEnd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineNumberIntervalEnd'), 'lineNumberIntervalEnd', '__httpschemas_nav_gov_huOSA3_0api_NewCreatedLinesType_httpschemas_nav_gov_huOSA3_0apilineNumberIntervalEnd', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1274, 3), )

    
    lineNumberIntervalEnd = property(__lineNumberIntervalEnd.value, __lineNumberIntervalEnd.set, None, 'Számla sor intervallum vége (inkluzív)Invoice line interval end (inclusive)')

    _ElementMap.update({
        __lineNumberIntervalStart.name() : __lineNumberIntervalStart,
        __lineNumberIntervalEnd.name() : __lineNumberIntervalEnd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NewCreatedLinesType = NewCreatedLinesType
Namespace.addCategoryObject('typeBinding', 'NewCreatedLinesType', NewCreatedLinesType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}PointerType with content type ELEMENT_ONLY
class PointerType (pyxb.binding.basis.complexTypeDefinition):
    """Feldolgozási kurzor adatokProcessing cursor data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointerType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1282, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}tag uses Python identifier tag
    __tag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tag'), 'tag', '__httpschemas_nav_gov_huOSA3_0api_PointerType_httpschemas_nav_gov_huOSA3_0apitag', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1288, 3), )

    
    tag = property(__tag.value, __tag.set, None, 'Tag hivatkozásTag reference')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpschemas_nav_gov_huOSA3_0api_PointerType_httpschemas_nav_gov_huOSA3_0apivalue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1294, 3), )

    
    value_ = property(__value.value, __value.set, None, 'Érték hivatkozásValue reference')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'line'), 'line', '__httpschemas_nav_gov_huOSA3_0api_PointerType_httpschemas_nav_gov_huOSA3_0apiline', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1300, 3), )

    
    line = property(__line.value, __line.set, None, 'SorhivatkozásLine reference')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber uses Python identifier originalInvoiceNumber
    __originalInvoiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), 'originalInvoiceNumber', '__httpschemas_nav_gov_huOSA3_0api_PointerType_httpschemas_nav_gov_huOSA3_0apioriginalInvoiceNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1306, 3), )

    
    originalInvoiceNumber = property(__originalInvoiceNumber.value, __originalInvoiceNumber.set, None, 'Kötegelt számla művelet esetén az eredeti számla sorszáma, melyre a módosítás vonatkozikIn case of a batch operation, the sequence number of the original invoice, on which the modification occurs')

    _ElementMap.update({
        __tag.name() : __tag,
        __value.name() : __value,
        __line.name() : __line,
        __originalInvoiceNumber.name() : __originalInvoiceNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PointerType = PointerType
Namespace.addCategoryObject('typeBinding', 'PointerType', PointerType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}ProcessingResultListType with content type ELEMENT_ONLY
class ProcessingResultListType (pyxb.binding.basis.complexTypeDefinition):
    """A kéréshez tartozó feldolgozási eredményekProcessing results of the request"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessingResultListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1314, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}processingResult uses Python identifier processingResult
    __processingResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processingResult'), 'processingResult', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultListType_httpschemas_nav_gov_huOSA3_0apiprocessingResult', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1320, 3), )

    
    processingResult = property(__processingResult.value, __processingResult.set, None, 'Számla feldolgozási eredményInvoice processing result')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion uses Python identifier originalRequestVersion
    __originalRequestVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), 'originalRequestVersion', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultListType_httpschemas_nav_gov_huOSA3_0apioriginalRequestVersion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1326, 3), )

    
    originalRequestVersion = property(__originalRequestVersion.value, __originalRequestVersion.set, None, 'Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}annulmentData uses Python identifier annulmentData
    __annulmentData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentData'), 'annulmentData', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultListType_httpschemas_nav_gov_huOSA3_0apiannulmentData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1332, 3), )

    
    annulmentData = property(__annulmentData.value, __annulmentData.set, None, 'Technikai érvénytelenítés státusz adataiStatus data of technical annulment')

    _ElementMap.update({
        __processingResult.name() : __processingResult,
        __originalRequestVersion.name() : __originalRequestVersion,
        __annulmentData.name() : __annulmentData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProcessingResultListType = ProcessingResultListType
Namespace.addCategoryObject('typeBinding', 'ProcessingResultListType', ProcessingResultListType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}ProcessingResultType with content type ELEMENT_ONLY
class ProcessingResultType (pyxb.binding.basis.complexTypeDefinition):
    """Számla feldolgozási eredményInvoice processing result"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessingResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1340, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultType_httpschemas_nav_gov_huOSA3_0apiindex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1346, 3), )

    
    index = property(__index.value, __index.set, None, 'A számla sorszáma a kérésen belülSequence number of the invoice within the request')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex uses Python identifier batchIndex
    __batchIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), 'batchIndex', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultType_httpschemas_nav_gov_huOSA3_0apibatchIndex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1352, 3), )

    
    batchIndex = property(__batchIndex.value, __batchIndex.set, None, 'A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceStatus uses Python identifier invoiceStatus
    __invoiceStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceStatus'), 'invoiceStatus', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultType_httpschemas_nav_gov_huOSA3_0apiinvoiceStatus', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1358, 3), )

    
    invoiceStatus = property(__invoiceStatus.value, __invoiceStatus.set, None, 'A számla feldolgozási státuszaProcessing status of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}technicalValidationMessages uses Python identifier technicalValidationMessages
    __technicalValidationMessages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'technicalValidationMessages'), 'technicalValidationMessages', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultType_httpschemas_nav_gov_huOSA3_0apitechnicalValidationMessages', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1364, 3), )

    
    technicalValidationMessages = property(__technicalValidationMessages.value, __technicalValidationMessages.set, None, 'Technikai validációs üzenetekTechnical validation messages')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}businessValidationMessages uses Python identifier businessValidationMessages
    __businessValidationMessages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'businessValidationMessages'), 'businessValidationMessages', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultType_httpschemas_nav_gov_huOSA3_0apibusinessValidationMessages', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1370, 3), )

    
    businessValidationMessages = property(__businessValidationMessages.value, __businessValidationMessages.set, None, 'Üzleti validációs üzenetekBusiness validation messages')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}compressedContentIndicator uses Python identifier compressedContentIndicator
    __compressedContentIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'compressedContentIndicator'), 'compressedContentIndicator', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultType_httpschemas_nav_gov_huOSA3_0apicompressedContentIndicator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1376, 3), )

    
    compressedContentIndicator = property(__compressedContentIndicator.value, __compressedContentIndicator.set, None, 'Jelöli, ha az originalRequest tartalmát a BASE64 dekódolást követően még ki kell tömöríteni az olvasáshozIndicates if the content of the originalRequest needs to be decompressed to be read following the BASE64 decoding')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalRequest uses Python identifier originalRequest
    __originalRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalRequest'), 'originalRequest', '__httpschemas_nav_gov_huOSA3_0api_ProcessingResultType_httpschemas_nav_gov_huOSA3_0apioriginalRequest', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1382, 3), )

    
    originalRequest = property(__originalRequest.value, __originalRequest.set, None, 'Számla adatok BASE64-ben kódolt tartalmaInvoice data in BASE64 encoded form')

    _ElementMap.update({
        __index.name() : __index,
        __batchIndex.name() : __batchIndex,
        __invoiceStatus.name() : __invoiceStatus,
        __technicalValidationMessages.name() : __technicalValidationMessages,
        __businessValidationMessages.name() : __businessValidationMessages,
        __compressedContentIndicator.name() : __compressedContentIndicator,
        __originalRequest.name() : __originalRequest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProcessingResultType = ProcessingResultType
Namespace.addCategoryObject('typeBinding', 'ProcessingResultType', ProcessingResultType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}RelationalQueryParamsType with content type ELEMENT_ONLY
class RelationalQueryParamsType (pyxb.binding.basis.complexTypeDefinition):
    """A számla lekérdezés relációs paramétereiRelational params of the invoice query"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelationalQueryParamsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1672, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDelivery uses Python identifier invoiceDelivery
    __invoiceDelivery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDelivery'), 'invoiceDelivery', '__httpschemas_nav_gov_huOSA3_0api_RelationalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceDelivery', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1678, 3), )

    
    invoiceDelivery = property(__invoiceDelivery.value, __invoiceDelivery.set, None, 'Számla teljesítési dátumának kereső paramétereQuery parameter of the invoice delivery date')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}paymentDate uses Python identifier paymentDate
    __paymentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentDate'), 'paymentDate', '__httpschemas_nav_gov_huOSA3_0api_RelationalQueryParamsType_httpschemas_nav_gov_huOSA3_0apipaymentDate', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1684, 3), )

    
    paymentDate = property(__paymentDate.value, __paymentDate.set, None, 'A számla fizetési határidejének kereső paramétereQuery parameter of the invoice payment date')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNetAmount uses Python identifier invoiceNetAmount
    __invoiceNetAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount'), 'invoiceNetAmount', '__httpschemas_nav_gov_huOSA3_0api_RelationalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceNetAmount', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1690, 3), )

    
    invoiceNetAmount = property(__invoiceNetAmount.value, __invoiceNetAmount.set, None, 'A számla nettó összeg kereső paramétere a számla pénznemébenQuery parameter of the invoice net amount expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNetAmountHUF uses Python identifier invoiceNetAmountHUF
    __invoiceNetAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF'), 'invoiceNetAmountHUF', '__httpschemas_nav_gov_huOSA3_0api_RelationalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceNetAmountHUF', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1696, 3), )

    
    invoiceNetAmountHUF = property(__invoiceNetAmountHUF.value, __invoiceNetAmountHUF.set, None, 'A számla nettó összegének kereső paramétere forintbanQuery parameter of the invoice net amount expressed in HUF')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceVatAmount uses Python identifier invoiceVatAmount
    __invoiceVatAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount'), 'invoiceVatAmount', '__httpschemas_nav_gov_huOSA3_0api_RelationalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceVatAmount', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1702, 3), )

    
    invoiceVatAmount = property(__invoiceVatAmount.value, __invoiceVatAmount.set, None, 'A számla ÁFA összegének kereső paramétere a számla pénznemébenQuery parameter of the invoice VAT amount expressed in the currency of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceVatAmountHUF uses Python identifier invoiceVatAmountHUF
    __invoiceVatAmountHUF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF'), 'invoiceVatAmountHUF', '__httpschemas_nav_gov_huOSA3_0api_RelationalQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceVatAmountHUF', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1708, 3), )

    
    invoiceVatAmountHUF = property(__invoiceVatAmountHUF.value, __invoiceVatAmountHUF.set, None, 'A számla ÁFA összegének kereső paramétere forintbanQuery parameter of the invoice VAT amount expressed in HUF')

    _ElementMap.update({
        __invoiceDelivery.name() : __invoiceDelivery,
        __paymentDate.name() : __paymentDate,
        __invoiceNetAmount.name() : __invoiceNetAmount,
        __invoiceNetAmountHUF.name() : __invoiceNetAmountHUF,
        __invoiceVatAmount.name() : __invoiceVatAmount,
        __invoiceVatAmountHUF.name() : __invoiceVatAmountHUF
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RelationalQueryParamsType = RelationalQueryParamsType
Namespace.addCategoryObject('typeBinding', 'RelationalQueryParamsType', RelationalQueryParamsType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}RelationQueryDateType with content type ELEMENT_ONLY
class RelationQueryDateType (pyxb.binding.basis.complexTypeDefinition):
    """Kereső paraméter dátum értékekhezQuery parameter for date values"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelationQueryDateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1716, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}queryOperator uses Python identifier queryOperator
    __queryOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'queryOperator'), 'queryOperator', '__httpschemas_nav_gov_huOSA3_0api_RelationQueryDateType_httpschemas_nav_gov_huOSA3_0apiqueryOperator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1722, 3), )

    
    queryOperator = property(__queryOperator.value, __queryOperator.set, None, 'Kereső operátorQuery operator')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}queryValue uses Python identifier queryValue
    __queryValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'queryValue'), 'queryValue', '__httpschemas_nav_gov_huOSA3_0api_RelationQueryDateType_httpschemas_nav_gov_huOSA3_0apiqueryValue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1728, 3), )

    
    queryValue = property(__queryValue.value, __queryValue.set, None, 'Kereső értékQuery value')

    _ElementMap.update({
        __queryOperator.name() : __queryOperator,
        __queryValue.name() : __queryValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RelationQueryDateType = RelationQueryDateType
Namespace.addCategoryObject('typeBinding', 'RelationQueryDateType', RelationQueryDateType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}RelationQueryMonetaryType with content type ELEMENT_ONLY
class RelationQueryMonetaryType (pyxb.binding.basis.complexTypeDefinition):
    """Kereső paraméter monetáris értékekhezQuery parameter for monetary values"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelationQueryMonetaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1736, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}queryOperator uses Python identifier queryOperator
    __queryOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'queryOperator'), 'queryOperator', '__httpschemas_nav_gov_huOSA3_0api_RelationQueryMonetaryType_httpschemas_nav_gov_huOSA3_0apiqueryOperator', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1742, 3), )

    
    queryOperator = property(__queryOperator.value, __queryOperator.set, None, 'Kereső operátorQuery operator')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}queryValue uses Python identifier queryValue
    __queryValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'queryValue'), 'queryValue', '__httpschemas_nav_gov_huOSA3_0api_RelationQueryMonetaryType_httpschemas_nav_gov_huOSA3_0apiqueryValue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1748, 3), )

    
    queryValue = property(__queryValue.value, __queryValue.set, None, 'Kereső értékQuery value')

    _ElementMap.update({
        __queryOperator.name() : __queryOperator,
        __queryValue.name() : __queryValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RelationQueryMonetaryType = RelationQueryMonetaryType
Namespace.addCategoryObject('typeBinding', 'RelationQueryMonetaryType', RelationQueryMonetaryType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}SoftwareType with content type ELEMENT_ONLY
class SoftwareType (pyxb.binding.basis.complexTypeDefinition):
    """A számlázóprogram adataiBilling software data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1756, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareId uses Python identifier softwareId
    __softwareId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareId'), 'softwareId', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1762, 3), )

    
    softwareId = property(__softwareId.value, __softwareId.set, None, 'A számlázóprogram azonosítójaBilling software ID')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareName uses Python identifier softwareName
    __softwareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareName'), 'softwareName', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1768, 3), )

    
    softwareName = property(__softwareName.value, __softwareName.set, None, 'A számlázóprogram neveBilling software name')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareOperation uses Python identifier softwareOperation
    __softwareOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareOperation'), 'softwareOperation', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1774, 3), )

    
    softwareOperation = property(__softwareOperation.value, __softwareOperation.set, None, 'A számlázóprogram működési típusa (lokális program vagy online számlázó szolgáltatás)Billing software operation type (local program or online billing service)')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareMainVersion uses Python identifier softwareMainVersion
    __softwareMainVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareMainVersion'), 'softwareMainVersion', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareMainVersion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1780, 3), )

    
    softwareMainVersion = property(__softwareMainVersion.value, __softwareMainVersion.set, None, 'A számlázóprogram főverziójaBilling software main version')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevName uses Python identifier softwareDevName
    __softwareDevName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareDevName'), 'softwareDevName', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareDevName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1786, 3), )

    
    softwareDevName = property(__softwareDevName.value, __softwareDevName.set, None, "A számlázóprogram fejlesztőjének neveName of the billing software's developer")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevContact uses Python identifier softwareDevContact
    __softwareDevContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareDevContact'), 'softwareDevContact', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareDevContact', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1792, 3), )

    
    softwareDevContact = property(__softwareDevContact.value, __softwareDevContact.set, None, "A számlázóprogram fejlesztőjének elektronikus elérhetőségeElectronic contact of the billing software's developer")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevCountryCode uses Python identifier softwareDevCountryCode
    __softwareDevCountryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareDevCountryCode'), 'softwareDevCountryCode', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareDevCountryCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1798, 3), )

    
    softwareDevCountryCode = property(__softwareDevCountryCode.value, __softwareDevCountryCode.set, None, "A számlázóprogram fejlesztőjének ISO-3166 alpha2 országkódjaISO-3166 alpha2 country code of the billing software's developer")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevTaxNumber uses Python identifier softwareDevTaxNumber
    __softwareDevTaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareDevTaxNumber'), 'softwareDevTaxNumber', '__httpschemas_nav_gov_huOSA3_0api_SoftwareType_httpschemas_nav_gov_huOSA3_0apisoftwareDevTaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1804, 3), )

    
    softwareDevTaxNumber = property(__softwareDevTaxNumber.value, __softwareDevTaxNumber.set, None, "A számlázóprogram fejlesztőjének adószámaTax number of the billing software's developer")

    _ElementMap.update({
        __softwareId.name() : __softwareId,
        __softwareName.name() : __softwareName,
        __softwareOperation.name() : __softwareOperation,
        __softwareMainVersion.name() : __softwareMainVersion,
        __softwareDevName.name() : __softwareDevName,
        __softwareDevContact.name() : __softwareDevContact,
        __softwareDevCountryCode.name() : __softwareDevCountryCode,
        __softwareDevTaxNumber.name() : __softwareDevTaxNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SoftwareType = SoftwareType
Namespace.addCategoryObject('typeBinding', 'SoftwareType', SoftwareType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TaxpayerAddressItemType with content type ELEMENT_ONLY
class TaxpayerAddressItemType (pyxb.binding.basis.complexTypeDefinition):
    """Adózói címsor adatTaxpayer address item"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxpayerAddressItemType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1812, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerAddressType uses Python identifier taxpayerAddressType
    __taxpayerAddressType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressType'), 'taxpayerAddressType', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerAddressItemType_httpschemas_nav_gov_huOSA3_0apitaxpayerAddressType', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1818, 3), )

    
    taxpayerAddressType = property(__taxpayerAddressType.value, __taxpayerAddressType.set, None, 'Adózói cím típusTaxpayer address type')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerAddress uses Python identifier taxpayerAddress
    __taxpayerAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddress'), 'taxpayerAddress', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerAddressItemType_httpschemas_nav_gov_huOSA3_0apitaxpayerAddress', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1824, 3), )

    
    taxpayerAddress = property(__taxpayerAddress.value, __taxpayerAddress.set, None, 'Az adózó címadataiAddress data of the taxpayer')

    _ElementMap.update({
        __taxpayerAddressType.name() : __taxpayerAddressType,
        __taxpayerAddress.name() : __taxpayerAddress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxpayerAddressItemType = TaxpayerAddressItemType
Namespace.addCategoryObject('typeBinding', 'TaxpayerAddressItemType', TaxpayerAddressItemType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TaxpayerAddressListType with content type ELEMENT_ONLY
class TaxpayerAddressListType (pyxb.binding.basis.complexTypeDefinition):
    """Adózói cím lista típusTaxpayer address list type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxpayerAddressListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1832, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerAddressItem uses Python identifier taxpayerAddressItem
    __taxpayerAddressItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressItem'), 'taxpayerAddressItem', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerAddressListType_httpschemas_nav_gov_huOSA3_0apitaxpayerAddressItem', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1838, 3), )

    
    taxpayerAddressItem = property(__taxpayerAddressItem.value, __taxpayerAddressItem.set, None, 'Adózói címsor adatTaxpayer address item')

    _ElementMap.update({
        __taxpayerAddressItem.name() : __taxpayerAddressItem
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxpayerAddressListType = TaxpayerAddressListType
Namespace.addCategoryObject('typeBinding', 'TaxpayerAddressListType', TaxpayerAddressListType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TaxpayerDataType with content type ELEMENT_ONLY
class TaxpayerDataType (pyxb.binding.basis.complexTypeDefinition):
    """Az adózó lekérdezés válasz adataiResponse data of the taxpayer query"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxpayerDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1846, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerName uses Python identifier taxpayerName
    __taxpayerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerName'), 'taxpayerName', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerDataType_httpschemas_nav_gov_huOSA3_0apitaxpayerName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1852, 3), )

    
    taxpayerName = property(__taxpayerName.value, __taxpayerName.set, None, 'Az adózó neveName of the taxpayer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerShortName uses Python identifier taxpayerShortName
    __taxpayerShortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerShortName'), 'taxpayerShortName', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerDataType_httpschemas_nav_gov_huOSA3_0apitaxpayerShortName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1858, 3), )

    
    taxpayerShortName = property(__taxpayerShortName.value, __taxpayerShortName.set, None, 'Az adózó rövidített neveShortened name of the taxpayer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxNumberDetail uses Python identifier taxNumberDetail
    __taxNumberDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxNumberDetail'), 'taxNumberDetail', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerDataType_httpschemas_nav_gov_huOSA3_0apitaxNumberDetail', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1864, 3), )

    
    taxNumberDetail = property(__taxNumberDetail.value, __taxNumberDetail.set, None, 'Az adószám részletes adataiDetailed data of the tax number')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}incorporation uses Python identifier incorporation
    __incorporation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'incorporation'), 'incorporation', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerDataType_httpschemas_nav_gov_huOSA3_0apiincorporation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1870, 3), )

    
    incorporation = property(__incorporation.value, __incorporation.set, None, 'Gazdasági típusIncorporation type')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}vatGroupMembership uses Python identifier vatGroupMembership
    __vatGroupMembership = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vatGroupMembership'), 'vatGroupMembership', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerDataType_httpschemas_nav_gov_huOSA3_0apivatGroupMembership', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1876, 3), )

    
    vatGroupMembership = property(__vatGroupMembership.value, __vatGroupMembership.set, None, 'Az adózó ÁFA csoport tagságaVAT group membership of the taxpayer')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerAddressList uses Python identifier taxpayerAddressList
    __taxpayerAddressList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressList'), 'taxpayerAddressList', '__httpschemas_nav_gov_huOSA3_0api_TaxpayerDataType_httpschemas_nav_gov_huOSA3_0apitaxpayerAddressList', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1882, 3), )

    
    taxpayerAddressList = property(__taxpayerAddressList.value, __taxpayerAddressList.set, None, 'Adózói cím lista típusTaxpayer address list type')

    _ElementMap.update({
        __taxpayerName.name() : __taxpayerName,
        __taxpayerShortName.name() : __taxpayerShortName,
        __taxNumberDetail.name() : __taxNumberDetail,
        __incorporation.name() : __incorporation,
        __vatGroupMembership.name() : __vatGroupMembership,
        __taxpayerAddressList.name() : __taxpayerAddressList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxpayerDataType = TaxpayerDataType
Namespace.addCategoryObject('typeBinding', 'TaxpayerDataType', TaxpayerDataType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TransactionListResultType with content type ELEMENT_ONLY
class TransactionListResultType (pyxb.binding.basis.complexTypeDefinition):
    """Tranzakció lekérdezési eredményeiTransaction query results"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionListResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1920, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}currentPage uses Python identifier currentPage
    __currentPage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentPage'), 'currentPage', '__httpschemas_nav_gov_huOSA3_0api_TransactionListResultType_httpschemas_nav_gov_huOSA3_0apicurrentPage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1926, 3), )

    
    currentPage = property(__currentPage.value, __currentPage.set, None, 'A jelenleg lekérdezett lapszámThe currently queried page count')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}availablePage uses Python identifier availablePage
    __availablePage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'availablePage'), 'availablePage', '__httpschemas_nav_gov_huOSA3_0api_TransactionListResultType_httpschemas_nav_gov_huOSA3_0apiavailablePage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1932, 3), )

    
    availablePage = property(__availablePage.value, __availablePage.set, None, 'A lekérdezés eredménye szerint elérhető utolsó lapszámThe highest available page count matching the query')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transaction uses Python identifier transaction
    __transaction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transaction'), 'transaction', '__httpschemas_nav_gov_huOSA3_0api_TransactionListResultType_httpschemas_nav_gov_huOSA3_0apitransaction', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1938, 3), )

    
    transaction = property(__transaction.value, __transaction.set, None, 'Tranzakció lekérdezési eredményTransaction query result')

    _ElementMap.update({
        __currentPage.name() : __currentPage,
        __availablePage.name() : __availablePage,
        __transaction.name() : __transaction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TransactionListResultType = TransactionListResultType
Namespace.addCategoryObject('typeBinding', 'TransactionListResultType', TransactionListResultType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TransactionQueryParamsType with content type ELEMENT_ONLY
class TransactionQueryParamsType (pyxb.binding.basis.complexTypeDefinition):
    """A számla lekérdezés tranzakciós paramétereiTransactional params of the invoice query"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionQueryParamsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1946, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httpschemas_nav_gov_huOSA3_0api_TransactionQueryParamsType_httpschemas_nav_gov_huOSA3_0apitransactionId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1952, 3), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, 'Az adatszolgáltatás tranzakció azonosítójaTransaction identifier of the data exchange')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpschemas_nav_gov_huOSA3_0api_TransactionQueryParamsType_httpschemas_nav_gov_huOSA3_0apiindex', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1958, 3), )

    
    index = property(__index.value, __index.set, None, 'A számla sorszáma a kérésen belülSequence number of the invoice within the request')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperation uses Python identifier invoiceOperation
    __invoiceOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), 'invoiceOperation', '__httpschemas_nav_gov_huOSA3_0api_TransactionQueryParamsType_httpschemas_nav_gov_huOSA3_0apiinvoiceOperation', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1964, 3), )

    
    invoiceOperation = property(__invoiceOperation.value, __invoiceOperation.set, None, 'Számlaművelet típusInvoice operation type')

    _ElementMap.update({
        __transactionId.name() : __transactionId,
        __index.name() : __index,
        __invoiceOperation.name() : __invoiceOperation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TransactionQueryParamsType = TransactionQueryParamsType
Namespace.addCategoryObject('typeBinding', 'TransactionQueryParamsType', TransactionQueryParamsType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TransactionType with content type ELEMENT_ONLY
class TransactionType (pyxb.binding.basis.complexTypeDefinition):
    """Tranzakció lekérdezési eredményTransaction query result"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1990, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insDate uses Python identifier insDate
    __insDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insDate'), 'insDate', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apiinsDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1996, 3), )

    
    insDate = property(__insDate.value, __insDate.set, None, 'A beszúrás időpontja UTC időbenInsert date in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insCusUser uses Python identifier insCusUser
    __insCusUser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insCusUser'), 'insCusUser', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apiinsCusUser', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2002, 3), )

    
    insCusUser = property(__insCusUser.value, __insCusUser.set, None, 'A beszúrást végző felhasználóInserting user name')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apisource', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2008, 3), )

    
    source = property(__source.value, __source.set, None, 'Az adatszolgáltatás forrásaData exchange source')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apitransactionId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2014, 3), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, 'A számla tranzakció azonosítójaTransaction ID of the invoice')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}requestStatus uses Python identifier requestStatus
    __requestStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requestStatus'), 'requestStatus', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apirequestStatus', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2020, 3), )

    
    requestStatus = property(__requestStatus.value, __requestStatus.set, None, 'A kérés feldolgozási státuszaProcessing status of the request')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}technicalAnnulment uses Python identifier technicalAnnulment
    __technicalAnnulment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'technicalAnnulment'), 'technicalAnnulment', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apitechnicalAnnulment', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2026, 3), )

    
    technicalAnnulment = property(__technicalAnnulment.value, __technicalAnnulment.set, None, 'Jelöli ha a tranzakció technikai érvénytelenítést tartalmazIndicates whether the transaction contains technical annulment')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion uses Python identifier originalRequestVersion
    __originalRequestVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), 'originalRequestVersion', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apioriginalRequestVersion', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2032, 3), )

    
    originalRequestVersion = property(__originalRequestVersion.value, __originalRequestVersion.set, None, 'Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}itemCount uses Python identifier itemCount
    __itemCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemCount'), 'itemCount', '__httpschemas_nav_gov_huOSA3_0api_TransactionType_httpschemas_nav_gov_huOSA3_0apiitemCount', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2038, 3), )

    
    itemCount = property(__itemCount.value, __itemCount.set, None, 'Az adatszolgáltatás tételeinek számaItem count of the invoiceExchange')

    _ElementMap.update({
        __insDate.name() : __insDate,
        __insCusUser.name() : __insCusUser,
        __source.name() : __source,
        __transactionId.name() : __transactionId,
        __requestStatus.name() : __requestStatus,
        __technicalAnnulment.name() : __technicalAnnulment,
        __originalRequestVersion.name() : __originalRequestVersion,
        __itemCount.name() : __itemCount
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TransactionType = TransactionType
Namespace.addCategoryObject('typeBinding', 'TransactionType', TransactionType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType with content type ELEMENT_ONLY
class BasicOnlineInvoiceRequestType (_ImportedBinding_common.BasicRequestType):
    """Online Számla rendszerre specifikus általános kérés adatokOnline Invoice specific basic request data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicOnlineInvoiceRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 530, 1)
    _ElementMap = _ImportedBinding_common.BasicRequestType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.BasicRequestType._AttributeMap.copy()
    # Base type is _ImportedBinding_common.BasicRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'software'), 'software', '__httpschemas_nav_gov_huOSA3_0api_BasicOnlineInvoiceRequestType_httpschemas_nav_gov_huOSA3_0apisoftware', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5), )

    
    software = property(__software.value, __software.set, None, 'A számlázóprogram adataiBilling software data')

    _ElementMap.update({
        __software.name() : __software
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicOnlineInvoiceRequestType = BasicOnlineInvoiceRequestType
Namespace.addCategoryObject('typeBinding', 'BasicOnlineInvoiceRequestType', BasicOnlineInvoiceRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType with content type ELEMENT_ONLY
class BasicOnlineInvoiceResponseType (_ImportedBinding_common.BasicResponseType):
    """Online Számla rendszerre specifikus általános válasz adatokOnline Invoice specific basic response data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicOnlineInvoiceResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 548, 1)
    _ElementMap = _ImportedBinding_common.BasicResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.BasicResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_common.BasicResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'software'), 'software', '__httpschemas_nav_gov_huOSA3_0api_BasicOnlineInvoiceResponseType_httpschemas_nav_gov_huOSA3_0apisoftware', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5), )

    
    software = property(__software.value, __software.set, None, 'A számlázóprogram adataiBilling software data')

    _ElementMap.update({
        __software.name() : __software
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicOnlineInvoiceResponseType = BasicOnlineInvoiceResponseType
Namespace.addCategoryObject('typeBinding', 'BasicOnlineInvoiceResponseType', BasicOnlineInvoiceResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}GeneralErrorResponseType with content type ELEMENT_ONLY
class GeneralErrorResponseType (_ImportedBinding_common.GeneralErrorHeaderResponseType):
    """Online Számla rendszerre specifikus általános hibaválasz típusOnline Invoice specific general error response type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneralErrorResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 638, 1)
    _ElementMap = _ImportedBinding_common.GeneralErrorHeaderResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.GeneralErrorHeaderResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_common.GeneralErrorHeaderResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'software'), 'software', '__httpschemas_nav_gov_huOSA3_0api_GeneralErrorResponseType_httpschemas_nav_gov_huOSA3_0apisoftware', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 646, 5), )

    
    software = property(__software.value, __software.set, None, 'A számlázóprogram adataiBilling software data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}technicalValidationMessages uses Python identifier technicalValidationMessages
    __technicalValidationMessages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'technicalValidationMessages'), 'technicalValidationMessages', '__httpschemas_nav_gov_huOSA3_0api_GeneralErrorResponseType_httpschemas_nav_gov_huOSA3_0apitechnicalValidationMessages', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 652, 5), )

    
    technicalValidationMessages = property(__technicalValidationMessages.value, __technicalValidationMessages.set, None, 'Technikai validációs üzenetekTechnical validation messages')

    _ElementMap.update({
        __software.name() : __software,
        __technicalValidationMessages.name() : __technicalValidationMessages
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GeneralErrorResponseType = GeneralErrorResponseType
Namespace.addCategoryObject('typeBinding', 'GeneralErrorResponseType', GeneralErrorResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}ManageAnnulmentRequestType with content type ELEMENT_ONLY
class ManageAnnulmentRequestType (BasicOnlineInvoiceRequestType):
    """A POST /manageAnnulment REST operáció kérés típusaRequest type of the POST /manageAnnulment REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManageAnnulmentRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1188, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}exchangeToken uses Python identifier exchangeToken
    __exchangeToken = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken'), 'exchangeToken', '__httpschemas_nav_gov_huOSA3_0api_ManageAnnulmentRequestType_httpschemas_nav_gov_huOSA3_0apiexchangeToken', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1196, 5), )

    
    exchangeToken = property(__exchangeToken.value, __exchangeToken.set, None, 'A tranzakcióhoz kiadott egyedi és dekódolt tokenThe decoded unique token issued for the current transaction')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}annulmentOperations uses Python identifier annulmentOperations
    __annulmentOperations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperations'), 'annulmentOperations', '__httpschemas_nav_gov_huOSA3_0api_ManageAnnulmentRequestType_httpschemas_nav_gov_huOSA3_0apiannulmentOperations', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1202, 5), )

    
    annulmentOperations = property(__annulmentOperations.value, __annulmentOperations.set, None, 'A kéréshez tartozó kötegelt technikai érvénytelenítésekBatch technical annulment operations of the request')

    _ElementMap.update({
        __exchangeToken.name() : __exchangeToken,
        __annulmentOperations.name() : __annulmentOperations
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ManageAnnulmentRequestType = ManageAnnulmentRequestType
Namespace.addCategoryObject('typeBinding', 'ManageAnnulmentRequestType', ManageAnnulmentRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}ManageInvoiceRequestType with content type ELEMENT_ONLY
class ManageInvoiceRequestType (BasicOnlineInvoiceRequestType):
    """A POST /manageInvoice REST operáció kérés típusaRequest type of the POST /manageInvoice REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManageInvoiceRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1212, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}exchangeToken uses Python identifier exchangeToken
    __exchangeToken = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken'), 'exchangeToken', '__httpschemas_nav_gov_huOSA3_0api_ManageInvoiceRequestType_httpschemas_nav_gov_huOSA3_0apiexchangeToken', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1220, 5), )

    
    exchangeToken = property(__exchangeToken.value, __exchangeToken.set, None, 'A tranzakcióhoz kiadott egyedi és dekódolt tokenThe decoded unique token issued for the current transaction')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperations uses Python identifier invoiceOperations
    __invoiceOperations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperations'), 'invoiceOperations', '__httpschemas_nav_gov_huOSA3_0api_ManageInvoiceRequestType_httpschemas_nav_gov_huOSA3_0apiinvoiceOperations', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1226, 5), )

    
    invoiceOperations = property(__invoiceOperations.value, __invoiceOperations.set, None, 'A kéréshez tartozó kötegelt számlaműveletekBatch invoice operations of the request')

    _ElementMap.update({
        __exchangeToken.name() : __exchangeToken,
        __invoiceOperations.name() : __invoiceOperations
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ManageInvoiceRequestType = ManageInvoiceRequestType
Namespace.addCategoryObject('typeBinding', 'ManageInvoiceRequestType', ManageInvoiceRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestRequestType with content type ELEMENT_ONLY
class QueryInvoiceChainDigestRequestType (BasicOnlineInvoiceRequestType):
    """A POST /queryInvoiceChainDigest REST operáció kérés típusaRequest type of the POST /queryInvoiceChainDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceChainDigestRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1390, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'page'), 'page', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceChainDigestRequestType_httpschemas_nav_gov_huOSA3_0apipage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1398, 5), )

    
    page = property(__page.value, __page.set, None, 'A lekérdezni kívánt lap számaThe queried page count')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceChainQuery uses Python identifier invoiceChainQuery
    __invoiceChainQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainQuery'), 'invoiceChainQuery', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceChainDigestRequestType_httpschemas_nav_gov_huOSA3_0apiinvoiceChainQuery', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1404, 5), )

    
    invoiceChainQuery = property(__invoiceChainQuery.value, __invoiceChainQuery.set, None, 'Számlalánc kivonat lekérdezés számlaszám paramétereInvoice number param of the invoice chain digest query')

    _ElementMap.update({
        __page.name() : __page,
        __invoiceChainQuery.name() : __invoiceChainQuery
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryInvoiceChainDigestRequestType = QueryInvoiceChainDigestRequestType
Namespace.addCategoryObject('typeBinding', 'QueryInvoiceChainDigestRequestType', QueryInvoiceChainDigestRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestResponseType with content type ELEMENT_ONLY
class QueryInvoiceChainDigestResponseType (BasicOnlineInvoiceResponseType):
    """A POST /queryInvoiceChainDigest REST operáció válasz típusaResponse type of the POST /queryInvoiceChainDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceChainDigestResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1414, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceChainDigestResult uses Python identifier invoiceChainDigestResult
    __invoiceChainDigestResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainDigestResult'), 'invoiceChainDigestResult', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceChainDigestResponseType_httpschemas_nav_gov_huOSA3_0apiinvoiceChainDigestResult', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1422, 5), )

    
    invoiceChainDigestResult = property(__invoiceChainDigestResult.value, __invoiceChainDigestResult.set, None, 'Számlalánc kivonat lekérdezés eredményeiInvoice chain digest query result')

    _ElementMap.update({
        __invoiceChainDigestResult.name() : __invoiceChainDigestResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryInvoiceChainDigestResponseType = QueryInvoiceChainDigestResponseType
Namespace.addCategoryObject('typeBinding', 'QueryInvoiceChainDigestResponseType', QueryInvoiceChainDigestResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceCheckResponseType with content type ELEMENT_ONLY
class QueryInvoiceCheckResponseType (BasicOnlineInvoiceResponseType):
    """A POST /queryInvoiceCheck REST operáció válasz típusaResponse type of the POST /queryInvoiceCheck REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceCheckResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1432, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceCheckResult uses Python identifier invoiceCheckResult
    __invoiceCheckResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceCheckResult'), 'invoiceCheckResult', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceCheckResponseType_httpschemas_nav_gov_huOSA3_0apiinvoiceCheckResult', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1440, 5), )

    
    invoiceCheckResult = property(__invoiceCheckResult.value, __invoiceCheckResult.set, None, 'Jelöli, ha a lekérdezett számlaszám érvényesként szerepel a rendszerben és a lekérdező adószáma kiállítóként vagy eladóként szerepel a számlánIndicates whether the queried invoice number exists in the system as a valid invoice, if the tax number of the querying entity is present on the invoice either as supplier or customer')

    _ElementMap.update({
        __invoiceCheckResult.name() : __invoiceCheckResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryInvoiceCheckResponseType = QueryInvoiceCheckResponseType
Namespace.addCategoryObject('typeBinding', 'QueryInvoiceCheckResponseType', QueryInvoiceCheckResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataRequestType with content type ELEMENT_ONLY
class QueryInvoiceDataRequestType (BasicOnlineInvoiceRequestType):
    """A POST /queryInvoiceData REST operáció kérés típusaRequest type of the POST /queryInvoiceData REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDataRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1450, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumberQuery uses Python identifier invoiceNumberQuery
    __invoiceNumberQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumberQuery'), 'invoiceNumberQuery', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceDataRequestType_httpschemas_nav_gov_huOSA3_0apiinvoiceNumberQuery', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1458, 5), )

    
    invoiceNumberQuery = property(__invoiceNumberQuery.value, __invoiceNumberQuery.set, None, 'Számla lekérdezés számlaszám paramétereInvoice number param of the Invoice query')

    _ElementMap.update({
        __invoiceNumberQuery.name() : __invoiceNumberQuery
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryInvoiceDataRequestType = QueryInvoiceDataRequestType
Namespace.addCategoryObject('typeBinding', 'QueryInvoiceDataRequestType', QueryInvoiceDataRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataResponseType with content type ELEMENT_ONLY
class QueryInvoiceDataResponseType (BasicOnlineInvoiceResponseType):
    """A POST /queryInvoiceData REST operáció válasz típusaResponse type of the POST /queryInvoiceData REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDataResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1468, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDataResult uses Python identifier invoiceDataResult
    __invoiceDataResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDataResult'), 'invoiceDataResult', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceDataResponseType_httpschemas_nav_gov_huOSA3_0apiinvoiceDataResult', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1476, 5), )

    
    invoiceDataResult = property(__invoiceDataResult.value, __invoiceDataResult.set, None, 'A számla lekérdezés eredményeInvoice data query result')

    _ElementMap.update({
        __invoiceDataResult.name() : __invoiceDataResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryInvoiceDataResponseType = QueryInvoiceDataResponseType
Namespace.addCategoryObject('typeBinding', 'QueryInvoiceDataResponseType', QueryInvoiceDataResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestRequestType with content type ELEMENT_ONLY
class QueryInvoiceDigestRequestType (BasicOnlineInvoiceRequestType):
    """A POST /queryInvoiceDigest REST operáció kérés típusaRequest type of the POST /queryInvoiceDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDigestRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1486, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'page'), 'page', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceDigestRequestType_httpschemas_nav_gov_huOSA3_0apipage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1494, 5), )

    
    page = property(__page.value, __page.set, None, 'A lekérdezni kívánt lap számaThe queried page count')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDirection uses Python identifier invoiceDirection
    __invoiceDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection'), 'invoiceDirection', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceDigestRequestType_httpschemas_nav_gov_huOSA3_0apiinvoiceDirection', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1500, 5), )

    
    invoiceDirection = property(__invoiceDirection.value, __invoiceDirection.set, None, 'Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceQueryParams uses Python identifier invoiceQueryParams
    __invoiceQueryParams = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceQueryParams'), 'invoiceQueryParams', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceDigestRequestType_httpschemas_nav_gov_huOSA3_0apiinvoiceQueryParams', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1506, 5), )

    
    invoiceQueryParams = property(__invoiceQueryParams.value, __invoiceQueryParams.set, None, 'Számla lekérdezési paraméterekInvoice query parameters')

    _ElementMap.update({
        __page.name() : __page,
        __invoiceDirection.name() : __invoiceDirection,
        __invoiceQueryParams.name() : __invoiceQueryParams
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryInvoiceDigestRequestType = QueryInvoiceDigestRequestType
Namespace.addCategoryObject('typeBinding', 'QueryInvoiceDigestRequestType', QueryInvoiceDigestRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestResponseType with content type ELEMENT_ONLY
class QueryInvoiceDigestResponseType (BasicOnlineInvoiceResponseType):
    """A POST /queryInvoiceDigest REST operáció válasz típusaResponse type of the POST /queryInvoiceDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDigestResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1516, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDigestResult uses Python identifier invoiceDigestResult
    __invoiceDigestResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceDigestResult'), 'invoiceDigestResult', '__httpschemas_nav_gov_huOSA3_0api_QueryInvoiceDigestResponseType_httpschemas_nav_gov_huOSA3_0apiinvoiceDigestResult', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1524, 5), )

    
    invoiceDigestResult = property(__invoiceDigestResult.value, __invoiceDigestResult.set, None, 'A számla kivonat lekérdezés eredményeiInvoice digest query results')

    _ElementMap.update({
        __invoiceDigestResult.name() : __invoiceDigestResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryInvoiceDigestResponseType = QueryInvoiceDigestResponseType
Namespace.addCategoryObject('typeBinding', 'QueryInvoiceDigestResponseType', QueryInvoiceDigestResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerRequestType with content type ELEMENT_ONLY
class QueryTaxpayerRequestType (BasicOnlineInvoiceRequestType):
    """A POST /queryTaxpayer REST operáció kérés típusaRequest type of the POST /queryTaxpayer REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTaxpayerRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1534, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxNumber uses Python identifier taxNumber
    __taxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), 'taxNumber', '__httpschemas_nav_gov_huOSA3_0api_QueryTaxpayerRequestType_httpschemas_nav_gov_huOSA3_0apitaxNumber', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1542, 5), )

    
    taxNumber = property(__taxNumber.value, __taxNumber.set, None, 'A lekérdezett adózó adószámaTax number of the queried taxpayer')

    _ElementMap.update({
        __taxNumber.name() : __taxNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTaxpayerRequestType = QueryTaxpayerRequestType
Namespace.addCategoryObject('typeBinding', 'QueryTaxpayerRequestType', QueryTaxpayerRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerResponseType with content type ELEMENT_ONLY
class QueryTaxpayerResponseType (BasicOnlineInvoiceResponseType):
    """A POST /queryTaxpayer REST operáció válasz típusaResponse type of the POST /queryTaxpayer REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTaxpayerResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1552, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}infoDate uses Python identifier infoDate
    __infoDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infoDate'), 'infoDate', '__httpschemas_nav_gov_huOSA3_0api_QueryTaxpayerResponseType_httpschemas_nav_gov_huOSA3_0apiinfoDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1560, 5), )

    
    infoDate = property(__infoDate.value, __infoDate.set, None, 'Az adatok utolsó változásának időpontjaLast date on which the data was changed')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerValidity uses Python identifier taxpayerValidity
    __taxpayerValidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerValidity'), 'taxpayerValidity', '__httpschemas_nav_gov_huOSA3_0api_QueryTaxpayerResponseType_httpschemas_nav_gov_huOSA3_0apitaxpayerValidity', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1566, 5), )

    
    taxpayerValidity = property(__taxpayerValidity.value, __taxpayerValidity.set, None, 'Jelzi, hogy a lekérdezett adózó létezik és érvényes-eIndicates whether the queried taxpayer is existing and valid')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerData uses Python identifier taxpayerData
    __taxpayerData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxpayerData'), 'taxpayerData', '__httpschemas_nav_gov_huOSA3_0api_QueryTaxpayerResponseType_httpschemas_nav_gov_huOSA3_0apitaxpayerData', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1572, 5), )

    
    taxpayerData = property(__taxpayerData.value, __taxpayerData.set, None, 'Az adózó lekérdezés válasz adataiResponse data of the taxpayer query')

    _ElementMap.update({
        __infoDate.name() : __infoDate,
        __taxpayerValidity.name() : __taxpayerValidity,
        __taxpayerData.name() : __taxpayerData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTaxpayerResponseType = QueryTaxpayerResponseType
Namespace.addCategoryObject('typeBinding', 'QueryTaxpayerResponseType', QueryTaxpayerResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListRequestType with content type ELEMENT_ONLY
class QueryTransactionListRequestType (BasicOnlineInvoiceRequestType):
    """A POST /queryTransactionList REST operáció kérés típusaRequest type of the POST /queryTransactionList REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionListRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1582, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'page'), 'page', '__httpschemas_nav_gov_huOSA3_0api_QueryTransactionListRequestType_httpschemas_nav_gov_huOSA3_0apipage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1590, 5), )

    
    page = property(__page.value, __page.set, None, 'A lekérdezni kívánt lap számaThe queried page count')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}insDate uses Python identifier insDate
    __insDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'insDate'), 'insDate', '__httpschemas_nav_gov_huOSA3_0api_QueryTransactionListRequestType_httpschemas_nav_gov_huOSA3_0apiinsDate', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1596, 5), )

    
    insDate = property(__insDate.value, __insDate.set, None, "A lekérdezni kívánt tranzakciók kiadásának szerver oldali ideje UTC időbenThe queried transaction's insert date on server side in UTC time")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}requestStatus uses Python identifier requestStatus
    __requestStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requestStatus'), 'requestStatus', '__httpschemas_nav_gov_huOSA3_0api_QueryTransactionListRequestType_httpschemas_nav_gov_huOSA3_0apirequestStatus', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1602, 5), )

    
    requestStatus = property(__requestStatus.value, __requestStatus.set, None, 'A kérés feldolgozási státuszaProcessing status of the request')

    _ElementMap.update({
        __page.name() : __page,
        __insDate.name() : __insDate,
        __requestStatus.name() : __requestStatus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTransactionListRequestType = QueryTransactionListRequestType
Namespace.addCategoryObject('typeBinding', 'QueryTransactionListRequestType', QueryTransactionListRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListResponseType with content type ELEMENT_ONLY
class QueryTransactionListResponseType (BasicOnlineInvoiceResponseType):
    """A POST /queryTransactionList REST operáció válasz típusaResponse type of the POST /queryTransactionList REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionListResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1612, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionListResult uses Python identifier transactionListResult
    __transactionListResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionListResult'), 'transactionListResult', '__httpschemas_nav_gov_huOSA3_0api_QueryTransactionListResponseType_httpschemas_nav_gov_huOSA3_0apitransactionListResult', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1620, 5), )

    
    transactionListResult = property(__transactionListResult.value, __transactionListResult.set, None, 'Tranzakció lekérdezési eredményeiTransaction query results')

    _ElementMap.update({
        __transactionListResult.name() : __transactionListResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTransactionListResponseType = QueryTransactionListResponseType
Namespace.addCategoryObject('typeBinding', 'QueryTransactionListResponseType', QueryTransactionListResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusRequestType with content type ELEMENT_ONLY
class QueryTransactionStatusRequestType (BasicOnlineInvoiceRequestType):
    """A POST /queryTransactionStatus REST operáció kérés típusaRequest type of the POST /queryTransactionStatus REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionStatusRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1630, 1)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httpschemas_nav_gov_huOSA3_0api_QueryTransactionStatusRequestType_httpschemas_nav_gov_huOSA3_0apitransactionId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1638, 5), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, 'Az adatszolgáltatás tranzakció azonosítójaTransaction identifier of the data exchange')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}returnOriginalRequest uses Python identifier returnOriginalRequest
    __returnOriginalRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnOriginalRequest'), 'returnOriginalRequest', '__httpschemas_nav_gov_huOSA3_0api_QueryTransactionStatusRequestType_httpschemas_nav_gov_huOSA3_0apireturnOriginalRequest', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1644, 5), )

    
    returnOriginalRequest = property(__returnOriginalRequest.value, __returnOriginalRequest.set, None, 'Jelöli, ha a kliens által beküldött eredeti tartalmat is vissza kell adni a válaszbanIndicates if the original client data should also be returned in the response')

    _ElementMap.update({
        __transactionId.name() : __transactionId,
        __returnOriginalRequest.name() : __returnOriginalRequest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTransactionStatusRequestType = QueryTransactionStatusRequestType
Namespace.addCategoryObject('typeBinding', 'QueryTransactionStatusRequestType', QueryTransactionStatusRequestType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusResponseType with content type ELEMENT_ONLY
class QueryTransactionStatusResponseType (BasicOnlineInvoiceResponseType):
    """A POST /queryTransactionStatus REST operáció válasz típusaResponse type of the POST /queryTransactionStatus REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionStatusResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1654, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}processingResults uses Python identifier processingResults
    __processingResults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processingResults'), 'processingResults', '__httpschemas_nav_gov_huOSA3_0api_QueryTransactionStatusResponseType_httpschemas_nav_gov_huOSA3_0apiprocessingResults', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1662, 5), )

    
    processingResults = property(__processingResults.value, __processingResults.set, None, 'A kérésben szereplő számlák feldolgozási státuszaProcessing status of the invoices in the request')

    _ElementMap.update({
        __processingResults.name() : __processingResults
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTransactionStatusResponseType = QueryTransactionStatusResponseType
Namespace.addCategoryObject('typeBinding', 'QueryTransactionStatusResponseType', QueryTransactionStatusResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TokenExchangeResponseType with content type ELEMENT_ONLY
class TokenExchangeResponseType (BasicOnlineInvoiceResponseType):
    """A POST /tokenExchange REST operáció válasz típusaResponse type of the POST /tokenExchange REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TokenExchangeResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1890, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}encodedExchangeToken uses Python identifier encodedExchangeToken
    __encodedExchangeToken = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'encodedExchangeToken'), 'encodedExchangeToken', '__httpschemas_nav_gov_huOSA3_0api_TokenExchangeResponseType_httpschemas_nav_gov_huOSA3_0apiencodedExchangeToken', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1898, 5), )

    
    encodedExchangeToken = property(__encodedExchangeToken.value, __encodedExchangeToken.set, None, 'A kiadott exchange token AES-128 ECB algoritmussal kódolt alakjaThe issued exchange token in AES-128 ECB encoded form')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}tokenValidityFrom uses Python identifier tokenValidityFrom
    __tokenValidityFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityFrom'), 'tokenValidityFrom', '__httpschemas_nav_gov_huOSA3_0api_TokenExchangeResponseType_httpschemas_nav_gov_huOSA3_0apitokenValidityFrom', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1904, 5), )

    
    tokenValidityFrom = property(__tokenValidityFrom.value, __tokenValidityFrom.set, None, 'A kiadott token érvényességének kezdeteValidity start of the issued exchange token')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}tokenValidityTo uses Python identifier tokenValidityTo
    __tokenValidityTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityTo'), 'tokenValidityTo', '__httpschemas_nav_gov_huOSA3_0api_TokenExchangeResponseType_httpschemas_nav_gov_huOSA3_0apitokenValidityTo', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1910, 5), )

    
    tokenValidityTo = property(__tokenValidityTo.value, __tokenValidityTo.set, None, 'A kiadott token érvényességének végeValidity end of the issued exchange token')

    _ElementMap.update({
        __encodedExchangeToken.name() : __encodedExchangeToken,
        __tokenValidityFrom.name() : __tokenValidityFrom,
        __tokenValidityTo.name() : __tokenValidityTo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TokenExchangeResponseType = TokenExchangeResponseType
Namespace.addCategoryObject('typeBinding', 'TokenExchangeResponseType', TokenExchangeResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/api}TransactionResponseType with content type ELEMENT_ONLY
class TransactionResponseType (BasicOnlineInvoiceResponseType):
    """A POST /manageInvoice és a POST /manageAnnulment REST operáció közös válasz típusaCommon response type of the POST /manageInvoice and the POST /manageAnnulment REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1972, 1)
    _ElementMap = BasicOnlineInvoiceResponseType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceResponseType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/api}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httpschemas_nav_gov_huOSA3_0api_TransactionResponseType_httpschemas_nav_gov_huOSA3_0apitransactionId', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1980, 5), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, 'A kért operáció tranzakció azonosítójaTransaction identifier of the requested operation')

    _ElementMap.update({
        __transactionId.name() : __transactionId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TransactionResponseType = TransactionResponseType
Namespace.addCategoryObject('typeBinding', 'TransactionResponseType', TransactionResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (BasicOnlineInvoiceRequestType):
    """A POST /tokenExchange REST operáció kérésének root elementjeRequest root element of the POST /tokenExchange REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2260, 2)
    _ElementMap = BasicOnlineInvoiceRequestType._ElementMap.copy()
    _AttributeMap = BasicOnlineInvoiceRequestType._AttributeMap.copy()
    # Base type is BasicOnlineInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (GeneralErrorResponseType):
    """Online Számla rendszerre specifikus általános hibaválaszOnline Invoice specific general error response"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2051, 2)
    _ElementMap = GeneralErrorResponseType._ElementMap.copy()
    _AttributeMap = GeneralErrorResponseType._AttributeMap.copy()
    # Base type is GeneralErrorResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}GeneralErrorResponseType
    
    # Element technicalValidationMessages ({http://schemas.nav.gov.hu/OSA/3.0/api}technicalValidationMessages) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}GeneralErrorResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (ManageAnnulmentRequestType):
    """A POST /manageAnnulment REST operáció kérésének root elementjeRequest root element of the POST /manageAnnulment REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2062, 2)
    _ElementMap = ManageAnnulmentRequestType._ElementMap.copy()
    _AttributeMap = ManageAnnulmentRequestType._AttributeMap.copy()
    # Base type is ManageAnnulmentRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element exchangeToken ({http://schemas.nav.gov.hu/OSA/3.0/api}exchangeToken) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}ManageAnnulmentRequestType
    
    # Element annulmentOperations ({http://schemas.nav.gov.hu/OSA/3.0/api}annulmentOperations) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}ManageAnnulmentRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (TransactionResponseType):
    """A POST /manageAnnulment REST operáció válaszának root elementjeResponse root element of the POST /manageAnnulment REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2073, 2)
    _ElementMap = TransactionResponseType._ElementMap.copy()
    _AttributeMap = TransactionResponseType._AttributeMap.copy()
    # Base type is TransactionResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element transactionId ({http://schemas.nav.gov.hu/OSA/3.0/api}transactionId) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}TransactionResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (ManageInvoiceRequestType):
    """A POST /manageInvoice REST operáció kérésének root elementjeRequest root element of the POST /manageInvoice REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2084, 2)
    _ElementMap = ManageInvoiceRequestType._ElementMap.copy()
    _AttributeMap = ManageInvoiceRequestType._AttributeMap.copy()
    # Base type is ManageInvoiceRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element exchangeToken ({http://schemas.nav.gov.hu/OSA/3.0/api}exchangeToken) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}ManageInvoiceRequestType
    
    # Element invoiceOperations ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceOperations) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}ManageInvoiceRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (TransactionResponseType):
    """A POST /manageInvoice REST operáció válaszának root elementjeResponse root element of the POST /manageInvoice REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2095, 2)
    _ElementMap = TransactionResponseType._ElementMap.copy()
    _AttributeMap = TransactionResponseType._AttributeMap.copy()
    # Base type is TransactionResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element transactionId ({http://schemas.nav.gov.hu/OSA/3.0/api}transactionId) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}TransactionResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (QueryInvoiceChainDigestRequestType):
    """A POST /queryInvoiceChainDigest REST operáció kérésének root elementjeRequest root element of the POST /queryInvoiceChainDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2106, 2)
    _ElementMap = QueryInvoiceChainDigestRequestType._ElementMap.copy()
    _AttributeMap = QueryInvoiceChainDigestRequestType._AttributeMap.copy()
    # Base type is QueryInvoiceChainDigestRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element page ({http://schemas.nav.gov.hu/OSA/3.0/api}page) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestRequestType
    
    # Element invoiceChainQuery ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceChainQuery) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (QueryInvoiceChainDigestResponseType):
    """A POST /queryInvoiceChainDigest REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceChainDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2117, 2)
    _ElementMap = QueryInvoiceChainDigestResponseType._ElementMap.copy()
    _AttributeMap = QueryInvoiceChainDigestResponseType._AttributeMap.copy()
    # Base type is QueryInvoiceChainDigestResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element invoiceChainDigestResult ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceChainDigestResult) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (QueryInvoiceDataRequestType):
    """A POST /queryInvoiceCheck REST operáció kérésének root elementjeRequest root element of the POST /queryInvoiceCheck REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2128, 2)
    _ElementMap = QueryInvoiceDataRequestType._ElementMap.copy()
    _AttributeMap = QueryInvoiceDataRequestType._AttributeMap.copy()
    # Base type is QueryInvoiceDataRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element invoiceNumberQuery ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumberQuery) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (QueryInvoiceCheckResponseType):
    """A POST /queryInvoiceCheck REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceCheck REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2139, 2)
    _ElementMap = QueryInvoiceCheckResponseType._ElementMap.copy()
    _AttributeMap = QueryInvoiceCheckResponseType._AttributeMap.copy()
    # Base type is QueryInvoiceCheckResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element invoiceCheckResult ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceCheckResult) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceCheckResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (QueryInvoiceDataRequestType):
    """A POST /queryInvoiceData REST operáció kérésének root elementjeRequest root element of the POST /queryInvoiceData REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2150, 2)
    _ElementMap = QueryInvoiceDataRequestType._ElementMap.copy()
    _AttributeMap = QueryInvoiceDataRequestType._AttributeMap.copy()
    # Base type is QueryInvoiceDataRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element invoiceNumberQuery ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceNumberQuery) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (QueryInvoiceDataResponseType):
    """A POST /queryInvoiceData REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceData REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2161, 2)
    _ElementMap = QueryInvoiceDataResponseType._ElementMap.copy()
    _AttributeMap = QueryInvoiceDataResponseType._AttributeMap.copy()
    # Base type is QueryInvoiceDataResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element invoiceDataResult ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDataResult) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (QueryInvoiceDigestRequestType):
    """A POST /queryInvoiceDigest REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2172, 2)
    _ElementMap = QueryInvoiceDigestRequestType._ElementMap.copy()
    _AttributeMap = QueryInvoiceDigestRequestType._AttributeMap.copy()
    # Base type is QueryInvoiceDigestRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element page ({http://schemas.nav.gov.hu/OSA/3.0/api}page) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestRequestType
    
    # Element invoiceDirection ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDirection) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestRequestType
    
    # Element invoiceQueryParams ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceQueryParams) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (QueryInvoiceDigestResponseType):
    """A POST /queryInvoiceDigest REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceDigest REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2183, 2)
    _ElementMap = QueryInvoiceDigestResponseType._ElementMap.copy()
    _AttributeMap = QueryInvoiceDigestResponseType._AttributeMap.copy()
    # Base type is QueryInvoiceDigestResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element invoiceDigestResult ({http://schemas.nav.gov.hu/OSA/3.0/api}invoiceDigestResult) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (QueryTaxpayerRequestType):
    """A POST /queryTaxpayer REST operáció kérésének root elementjeRequest root element of the POST /queryTaxpayer REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2194, 2)
    _ElementMap = QueryTaxpayerRequestType._ElementMap.copy()
    _AttributeMap = QueryTaxpayerRequestType._AttributeMap.copy()
    # Base type is QueryTaxpayerRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element taxNumber ({http://schemas.nav.gov.hu/OSA/3.0/api}taxNumber) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (QueryTaxpayerResponseType):
    """A POST /queryTaxpayer REST operáció válaszának root elementjeResponse root element of the POST /queryTaxpayer REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2205, 2)
    _ElementMap = QueryTaxpayerResponseType._ElementMap.copy()
    _AttributeMap = QueryTaxpayerResponseType._AttributeMap.copy()
    # Base type is QueryTaxpayerResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element infoDate ({http://schemas.nav.gov.hu/OSA/3.0/api}infoDate) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerResponseType
    
    # Element taxpayerValidity ({http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerValidity) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerResponseType
    
    # Element taxpayerData ({http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerData) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (QueryTransactionListRequestType):
    """A POST /queryTransactionList REST operáció kérésének root elementjeRequest root element of the POST /queryTransactionList REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2216, 2)
    _ElementMap = QueryTransactionListRequestType._ElementMap.copy()
    _AttributeMap = QueryTransactionListRequestType._AttributeMap.copy()
    # Base type is QueryTransactionListRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element page ({http://schemas.nav.gov.hu/OSA/3.0/api}page) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListRequestType
    
    # Element insDate ({http://schemas.nav.gov.hu/OSA/3.0/api}insDate) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListRequestType
    
    # Element requestStatus ({http://schemas.nav.gov.hu/OSA/3.0/api}requestStatus) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (QueryTransactionListResponseType):
    """A POST /queryTransactionList REST operáció válaszának root elementjeResponse root element of the POST /queryTransactionList REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2227, 2)
    _ElementMap = QueryTransactionListResponseType._ElementMap.copy()
    _AttributeMap = QueryTransactionListResponseType._AttributeMap.copy()
    # Base type is QueryTransactionListResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element transactionListResult ({http://schemas.nav.gov.hu/OSA/3.0/api}transactionListResult) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (QueryTransactionStatusRequestType):
    """A POST /queryTransactionStatus REST operáció kérésének root elementjeRequest root element of the POST /queryTransactionStatus REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2238, 2)
    _ElementMap = QueryTransactionStatusRequestType._ElementMap.copy()
    _AttributeMap = QueryTransactionStatusRequestType._AttributeMap.copy()
    # Base type is QueryTransactionStatusRequestType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element user ({http://schemas.nav.gov.hu/NTCA/1.0/common}user) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicRequestType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceRequestType
    
    # Element transactionId ({http://schemas.nav.gov.hu/OSA/3.0/api}transactionId) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusRequestType
    
    # Element returnOriginalRequest ({http://schemas.nav.gov.hu/OSA/3.0/api}returnOriginalRequest) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (QueryTransactionStatusResponseType):
    """A POST /queryTransactionStatus REST operáció válaszának root elementjeResponse root element of the POST /queryTransactionStatus REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2249, 2)
    _ElementMap = QueryTransactionStatusResponseType._ElementMap.copy()
    _AttributeMap = QueryTransactionStatusResponseType._AttributeMap.copy()
    # Base type is QueryTransactionStatusResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element processingResults ({http://schemas.nav.gov.hu/OSA/3.0/api}processingResults) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (TokenExchangeResponseType):
    """A POST /tokenExchange REST operáció válaszának root elementjeResponse root element of the POST /tokenExchange REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2271, 2)
    _ElementMap = TokenExchangeResponseType._ElementMap.copy()
    _AttributeMap = TokenExchangeResponseType._AttributeMap.copy()
    # Base type is TokenExchangeResponseType
    
    # Element header ({http://schemas.nav.gov.hu/NTCA/1.0/common}header) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element result ({http://schemas.nav.gov.hu/NTCA/1.0/common}result) inherited from {http://schemas.nav.gov.hu/NTCA/1.0/common}BasicResponseType
    
    # Element software ({http://schemas.nav.gov.hu/OSA/3.0/api}software) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}BasicOnlineInvoiceResponseType
    
    # Element encodedExchangeToken ({http://schemas.nav.gov.hu/OSA/3.0/api}encodedExchangeToken) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}TokenExchangeResponseType
    
    # Element tokenValidityFrom ({http://schemas.nav.gov.hu/OSA/3.0/api}tokenValidityFrom) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}TokenExchangeResponseType
    
    # Element tokenValidityTo ({http://schemas.nav.gov.hu/OSA/3.0/api}tokenValidityTo) inherited from {http://schemas.nav.gov.hu/OSA/3.0/api}TokenExchangeResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


TokenExchangeRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TokenExchangeRequest'), CTD_ANON, documentation='A POST /tokenExchange REST operáció kérésének root elementjeRequest root element of the POST /tokenExchange REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2255, 1))
Namespace.addCategoryObject('elementBinding', TokenExchangeRequest.name().localName(), TokenExchangeRequest)

GeneralErrorResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneralErrorResponse'), CTD_ANON_, documentation='Online Számla rendszerre specifikus általános hibaválaszOnline Invoice specific general error response', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2046, 1))
Namespace.addCategoryObject('elementBinding', GeneralErrorResponse.name().localName(), GeneralErrorResponse)

ManageAnnulmentRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ManageAnnulmentRequest'), CTD_ANON_2, documentation='A POST /manageAnnulment REST operáció kérésének root elementjeRequest root element of the POST /manageAnnulment REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2057, 1))
Namespace.addCategoryObject('elementBinding', ManageAnnulmentRequest.name().localName(), ManageAnnulmentRequest)

ManageAnnulmentResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ManageAnnulmentResponse'), CTD_ANON_3, documentation='A POST /manageAnnulment REST operáció válaszának root elementjeResponse root element of the POST /manageAnnulment REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2068, 1))
Namespace.addCategoryObject('elementBinding', ManageAnnulmentResponse.name().localName(), ManageAnnulmentResponse)

ManageInvoiceRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ManageInvoiceRequest'), CTD_ANON_4, documentation='A POST /manageInvoice REST operáció kérésének root elementjeRequest root element of the POST /manageInvoice REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2079, 1))
Namespace.addCategoryObject('elementBinding', ManageInvoiceRequest.name().localName(), ManageInvoiceRequest)

ManageInvoiceResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ManageInvoiceResponse'), CTD_ANON_5, documentation='A POST /manageInvoice REST operáció válaszának root elementjeResponse root element of the POST /manageInvoice REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2090, 1))
Namespace.addCategoryObject('elementBinding', ManageInvoiceResponse.name().localName(), ManageInvoiceResponse)

QueryInvoiceChainDigestRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceChainDigestRequest'), CTD_ANON_6, documentation='A POST /queryInvoiceChainDigest REST operáció kérésének root elementjeRequest root element of the POST /queryInvoiceChainDigest REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2101, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceChainDigestRequest.name().localName(), QueryInvoiceChainDigestRequest)

QueryInvoiceChainDigestResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceChainDigestResponse'), CTD_ANON_7, documentation='A POST /queryInvoiceChainDigest REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceChainDigest REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2112, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceChainDigestResponse.name().localName(), QueryInvoiceChainDigestResponse)

QueryInvoiceCheckRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceCheckRequest'), CTD_ANON_8, documentation='A POST /queryInvoiceCheck REST operáció kérésének root elementjeRequest root element of the POST /queryInvoiceCheck REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2123, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceCheckRequest.name().localName(), QueryInvoiceCheckRequest)

QueryInvoiceCheckResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceCheckResponse'), CTD_ANON_9, documentation='A POST /queryInvoiceCheck REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceCheck REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2134, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceCheckResponse.name().localName(), QueryInvoiceCheckResponse)

QueryInvoiceDataRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDataRequest'), CTD_ANON_10, documentation='A POST /queryInvoiceData REST operáció kérésének root elementjeRequest root element of the POST /queryInvoiceData REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2145, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceDataRequest.name().localName(), QueryInvoiceDataRequest)

QueryInvoiceDataResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDataResponse'), CTD_ANON_11, documentation='A POST /queryInvoiceData REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceData REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2156, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceDataResponse.name().localName(), QueryInvoiceDataResponse)

QueryInvoiceDigestRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDigestRequest'), CTD_ANON_12, documentation='A POST /queryInvoiceDigest REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceDigest REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2167, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceDigestRequest.name().localName(), QueryInvoiceDigestRequest)

QueryInvoiceDigestResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryInvoiceDigestResponse'), CTD_ANON_13, documentation='A POST /queryInvoiceDigest REST operáció válaszának root elementjeResponse root element of the POST /queryInvoiceDigest REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2178, 1))
Namespace.addCategoryObject('elementBinding', QueryInvoiceDigestResponse.name().localName(), QueryInvoiceDigestResponse)

QueryTaxpayerRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTaxpayerRequest'), CTD_ANON_14, documentation='A POST /queryTaxpayer REST operáció kérésének root elementjeRequest root element of the POST /queryTaxpayer REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2189, 1))
Namespace.addCategoryObject('elementBinding', QueryTaxpayerRequest.name().localName(), QueryTaxpayerRequest)

QueryTaxpayerResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTaxpayerResponse'), CTD_ANON_15, documentation='A POST /queryTaxpayer REST operáció válaszának root elementjeResponse root element of the POST /queryTaxpayer REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2200, 1))
Namespace.addCategoryObject('elementBinding', QueryTaxpayerResponse.name().localName(), QueryTaxpayerResponse)

QueryTransactionListRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionListRequest'), CTD_ANON_16, documentation='A POST /queryTransactionList REST operáció kérésének root elementjeRequest root element of the POST /queryTransactionList REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2211, 1))
Namespace.addCategoryObject('elementBinding', QueryTransactionListRequest.name().localName(), QueryTransactionListRequest)

QueryTransactionListResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionListResponse'), CTD_ANON_17, documentation='A POST /queryTransactionList REST operáció válaszának root elementjeResponse root element of the POST /queryTransactionList REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2222, 1))
Namespace.addCategoryObject('elementBinding', QueryTransactionListResponse.name().localName(), QueryTransactionListResponse)

QueryTransactionStatusRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionStatusRequest'), CTD_ANON_18, documentation='A POST /queryTransactionStatus REST operáció kérésének root elementjeRequest root element of the POST /queryTransactionStatus REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2233, 1))
Namespace.addCategoryObject('elementBinding', QueryTransactionStatusRequest.name().localName(), QueryTransactionStatusRequest)

QueryTransactionStatusResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTransactionStatusResponse'), CTD_ANON_19, documentation='A POST /queryTransactionStatus REST operáció válaszának root elementjeResponse root element of the POST /queryTransactionStatus REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2244, 1))
Namespace.addCategoryObject('elementBinding', QueryTransactionStatusResponse.name().localName(), QueryTransactionStatusResponse)

TokenExchangeResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TokenExchangeResponse'), CTD_ANON_20, documentation='A POST /tokenExchange REST operáció válaszának root elementjeResponse root element of the POST /tokenExchange REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2266, 1))
Namespace.addCategoryObject('elementBinding', TokenExchangeResponse.name().localName(), TokenExchangeResponse)



AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=AdditionalQueryParamsType, documentation='A számla kiállítójának vagy vevőjének adószáma (a keresési feltétel az invoiceDirection tag értékétől függ)Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 364, 3)))

AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=AdditionalQueryParamsType, documentation='A számla kiállítójának vagy vevőjének csoport tag adószáma (a keresési feltétel az invoiceDirection tag értékétől függ)Tax number of group member of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 370, 3)))

AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), QueryNameType, scope=AdditionalQueryParamsType, documentation='A számla kiállítójának vagy vevőjének keresőparamétere szó eleji egyezőségre (a keresési feltétel az invoiceDirection tag értékétől függ)Query param of the supplier or the customer of the invoice for leading match pattern (the search criteria depends on the value of the invoiceDirection tag)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 376, 3)))

AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory'), _ImportedBinding_base.InvoiceCategoryType, scope=AdditionalQueryParamsType, documentation='A számla típusaType of invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 382, 3)))

AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), _ImportedBinding_base.PaymentMethodType, scope=AdditionalQueryParamsType, documentation='Fizetés módjaMethod of payment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 388, 3)))

AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance'), _ImportedBinding_base.InvoiceAppearanceType, scope=AdditionalQueryParamsType, documentation='A számla megjelenési formájaForm of appearance of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 394, 3)))

AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), SourceType, scope=AdditionalQueryParamsType, documentation='Az adatszolgáltatás forrásaData exchange source', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 400, 3)))

AdditionalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currency'), _ImportedBinding_common.CurrencyType, scope=AdditionalQueryParamsType, documentation='A számla pénznemeCurrency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 406, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 364, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 370, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 376, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 382, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 388, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 394, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 400, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 406, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 364, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'groupMemberTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 370, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 376, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 382, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 388, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 394, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 400, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 406, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdditionalQueryParamsType._Automaton = _BuildAutomaton()




AnnulmentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentVerificationStatus'), AnnulmentVerificationStatusType, scope=AnnulmentDataType, documentation='Technikai érvénytelenítő kérések jóváhagyási státuszaVerification status of technical annulment requests', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 420, 3)))

AnnulmentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentDecisionDate'), _ImportedBinding_base.InvoiceTimestampType, scope=AnnulmentDataType, documentation='A technikai érvénytelenítés jóváhagyásának vagy elutasításának időpontja UTC időbenDate of verification or rejection of the technical annulment in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 426, 3)))

AnnulmentDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentDecisionUser'), _ImportedBinding_common.LoginType, scope=AnnulmentDataType, documentation="A technikai érvénytelenítést jóváhagyó vagy elutasító felhasználó neveLogin name of the user deciding over the technical annulment's verification or rejection", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 432, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 426, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 432, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnnulmentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentVerificationStatus')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 420, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnnulmentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentDecisionDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 426, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AnnulmentDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentDecisionUser')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 432, 3))
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
AnnulmentDataType._Automaton = _BuildAutomaton_()




AnnulmentOperationListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperation'), AnnulmentOperationType, scope=AnnulmentOperationListType, documentation='A kéréshez tartozó technikai érvénytelenítő műveletTechnical annulment operation of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 446, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=100, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 446, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnnulmentOperationListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 446, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AnnulmentOperationListType._Automaton = _BuildAutomaton_2()




AnnulmentOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), _ImportedBinding_base.InvoiceIndexType, scope=AnnulmentOperationType, documentation='A technikai érvénytelenítés sorszáma a kérésen belülSequence number of the technical annulment within the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 460, 3)))

AnnulmentOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperation'), ManageAnnulmentOperationType, scope=AnnulmentOperationType, documentation='A kért technikai érvénytelenítés művelet típusaType of the desired technical annulment operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 466, 3)))

AnnulmentOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceAnnulment'), pyxb.binding.datatypes.base64Binary, scope=AnnulmentOperationType, documentation='Technikai érvénytelenítés adatok BASE64-ben kódolt tartalmaTechnical annulment data in BASE64 encoded form', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 472, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnulmentOperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 460, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnulmentOperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 466, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnnulmentOperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAnnulment')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 472, 3))
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
AnnulmentOperationType._Automaton = _BuildAutomaton_3()




AuditDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insdate'), _ImportedBinding_base.InvoiceTimestampType, scope=AuditDataType, documentation='A beszúrás időpontja UTC időbenInsert date in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 486, 3)))

AuditDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insCusUser'), _ImportedBinding_common.LoginType, scope=AuditDataType, documentation='A beszúrást végző technikai felhasználóInserting technical user name', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 492, 3)))

AuditDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), SourceType, scope=AuditDataType, documentation='Az adatszolgáltatás forrásaData exchange source', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 498, 3)))

AuditDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), _ImportedBinding_common.EntityIdType, scope=AuditDataType, documentation='A számla tranzakció azonosítója, ha az gépi interfészen került beküldésreTransaction ID of the invoice if it was exchanged via M2M interface', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 504, 3)))

AuditDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), _ImportedBinding_base.InvoiceIndexType, scope=AuditDataType, documentation='A számla sorszáma a kérésen belülSequence number of the invoice within the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 510, 3)))

AuditDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=AuditDataType, documentation='A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 516, 3)))

AuditDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), OriginalRequestVersionType, scope=AuditDataType, documentation='Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 522, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 504, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 510, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 516, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuditDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insdate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 486, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuditDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insCusUser')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 492, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuditDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 498, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuditDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 504, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuditDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 510, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuditDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batchIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 516, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AuditDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 522, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AuditDataType._Automaton = _BuildAutomaton_4()




BusinessValidationResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validationResultCode'), _ImportedBinding_common.BusinessResultCodeType, scope=BusinessValidationResultType, documentation='Validációs eredményValidation result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 572, 3)))

BusinessValidationResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validationErrorCode'), _ImportedBinding_common.SimpleText100NotBlankType, scope=BusinessValidationResultType, documentation='Validációs hibakódValidation error code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 578, 3)))

BusinessValidationResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'message'), _ImportedBinding_common.SimpleText512NotBlankType, scope=BusinessValidationResultType, documentation='Feldolgozási üzenetProcessing message', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 584, 3)))

BusinessValidationResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointer'), PointerType, scope=BusinessValidationResultType, documentation='Feldolgozási kurzor adatokProcessing cursor data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 590, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 578, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 584, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 590, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BusinessValidationResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validationResultCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 572, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BusinessValidationResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validationErrorCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 578, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BusinessValidationResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'message')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 584, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BusinessValidationResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pointer')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 590, 3))
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
BusinessValidationResultType._Automaton = _BuildAutomaton_5()




DateIntervalParamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateFrom'), _ImportedBinding_base.InvoiceDateType, scope=DateIntervalParamType, documentation='Dátum intervallum nagyobb vagy egyenlő paramétereDate interval greater or equals parameter', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 604, 3)))

DateIntervalParamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateTo'), _ImportedBinding_base.InvoiceDateType, scope=DateIntervalParamType, documentation='Dátum intervallum kisebb vagy egyenlő paramétereDate interval less or equals parameter', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 610, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateIntervalParamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateFrom')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 604, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateIntervalParamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateTo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 610, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateIntervalParamType._Automaton = _BuildAutomaton_6()




DateTimeIntervalParamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateTimeFrom'), _ImportedBinding_base.InvoiceTimestampType, scope=DateTimeIntervalParamType, documentation='Időpontos intervallum nagyobb vagy egyenlő paramétere UTC idő szerintDatetime interval greater or equals parameter', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 624, 3)))

DateTimeIntervalParamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateTimeTo'), _ImportedBinding_base.InvoiceTimestampType, scope=DateTimeIntervalParamType, documentation='Időpontos intervallum kisebb vagy egyenlő paramétere UTC idő szerintDatetime interval less or equals parameter', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 630, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateTimeIntervalParamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateTimeFrom')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 624, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateTimeIntervalParamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateTimeTo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 630, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateTimeIntervalParamType._Automaton = _BuildAutomaton_7()




InvoiceChainDigestResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentPage'), _ImportedBinding_common.ResponsePageType, scope=InvoiceChainDigestResultType, documentation='A jelenleg lekérdezett lapszámThe currently queried page count', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 668, 3)))

InvoiceChainDigestResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'availablePage'), _ImportedBinding_common.ResponsePageType, scope=InvoiceChainDigestResultType, documentation='A lekérdezés eredménye szerint elérhető utolsó lapszámThe highest available page count matching the query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 674, 3)))

InvoiceChainDigestResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainElement'), InvoiceChainElementType, scope=InvoiceChainDigestResultType, documentation='Számlalánc elemInvoice chain element', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 680, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 680, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentPage')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 668, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availablePage')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 674, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainElement')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 680, 3))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceChainDigestResultType._Automaton = _BuildAutomaton_8()




InvoiceChainDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceChainDigestType, documentation='Számla vagy módosító okirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pontSequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 694, 3)))

InvoiceChainDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=InvoiceChainDigestType, documentation='A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 700, 3)))

InvoiceChainDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), ManageInvoiceOperationType, scope=InvoiceChainDigestType, documentation='Számlaművelet típusInvoice operation type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 706, 3)))

InvoiceChainDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceChainDigestType, documentation="A kibocsátó adószámaThe supplier's tax number", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 712, 3)))

InvoiceChainDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceChainDigestType, documentation="A vevő adószámaThe buyer's tax number", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 718, 3)))

InvoiceChainDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insDate'), _ImportedBinding_base.InvoiceTimestampType, scope=InvoiceChainDigestType, documentation='A beszúrás időpontja UTC időbenInsert date in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 724, 3)))

InvoiceChainDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), OriginalRequestVersionType, scope=InvoiceChainDigestType, documentation='Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 730, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 700, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 718, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 694, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batchIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 700, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 706, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 712, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 718, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 724, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceChainDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 730, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceChainDigestType._Automaton = _BuildAutomaton_9()




InvoiceChainElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainDigest'), InvoiceChainDigestType, scope=InvoiceChainElementType, documentation='Számlalánc kivonat adatokInvoice chain digest data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 744, 3)))

InvoiceChainElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceLines'), InvoiceLinesType, scope=InvoiceChainElementType, documentation='A számlán vagy módosító okiraton szereplő tételek kivonatos adataiProduct/service digest data appearing on the invoice or the modification document', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 750, 3)))

InvoiceChainElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceReferenceData'), InvoiceReferenceDataType, scope=InvoiceChainElementType, documentation='A módosítás vagy érvénytelenítés adataiModification or cancellation data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 756, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 750, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 756, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceChainElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainDigest')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 744, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceChainElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceLines')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 750, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceChainElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceReferenceData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 756, 3))
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
InvoiceChainElementType._Automaton = _BuildAutomaton_10()




InvoiceChainQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceChainQueryType, documentation='Számla vagy módosító okirat sorszámaSequential number of the original or modification invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 770, 3)))

InvoiceChainQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection'), InvoiceDirectionType, scope=InvoiceChainQueryType, documentation='Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 776, 3)))

InvoiceChainQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceChainQueryType, documentation='A számla kiállítójának vagy vevőjének adószáma (a keresési feltétel az invoiceDirection tag értékétől függ)Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 782, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 782, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceChainQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 770, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceChainQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 776, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceChainQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 782, 3))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceChainQueryType._Automaton = _BuildAutomaton_11()




InvoiceDataResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceData'), pyxb.binding.datatypes.base64Binary, scope=InvoiceDataResultType, documentation='Számla adatok BASE64-ben kódolt tartalmaInvoice data in BASE64 encoded form', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 796, 3)))

InvoiceDataResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'auditData'), AuditDataType, scope=InvoiceDataResultType, documentation='A számla audit adataiInvoice audit data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 802, 3)))

InvoiceDataResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'compressedContentIndicator'), pyxb.binding.datatypes.boolean, scope=InvoiceDataResultType, documentation='Jelöli, ha az invoice tartalmát a BASE64 dekódolást követően még ki kell tömöríteni az olvasáshozIndicates if the content of the invoice needs to be decompressed to be read following the BASE64 decoding', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 808, 3)))

InvoiceDataResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electronicInvoiceHash'), _ImportedBinding_common.CryptoType, scope=InvoiceDataResultType, documentation='Elektronikus számla vagy módosító okirat állomány hash lenyomataElectronic invoice or modification document file hash value', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 814, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 814, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDataResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 796, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDataResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'auditData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 802, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceDataResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'compressedContentIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 808, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceDataResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electronicInvoiceHash')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 814, 3))
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
InvoiceDataResultType._Automaton = _BuildAutomaton_12()




InvoiceDigestResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentPage'), _ImportedBinding_common.ResponsePageType, scope=InvoiceDigestResultType, documentation='A jelenleg lekérdezett lapszámThe currently queried page count', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 828, 3)))

InvoiceDigestResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'availablePage'), _ImportedBinding_common.ResponsePageType, scope=InvoiceDigestResultType, documentation='A lekérdezés eredménye szerint elérhető utolsó lapszámThe highest available page count matching the query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 834, 3)))

InvoiceDigestResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDigest'), InvoiceDigestType, scope=InvoiceDigestResultType, documentation='Számla kivonat lekérdezési eredményInvoice digest query result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 840, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 840, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentPage')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 828, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availablePage')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 834, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDigest')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 840, 3))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceDigestResultType._Automaton = _BuildAutomaton_13()




InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceDigestType, documentation='Számla vagy módosító okirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pontSequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 854, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=InvoiceDigestType, documentation='A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 860, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), ManageInvoiceOperationType, scope=InvoiceDigestType, documentation='Számlaművelet típusInvoice operation type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 866, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory'), _ImportedBinding_base.InvoiceCategoryType, scope=InvoiceDigestType, documentation='A számla típusaType of invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 872, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDigestType, documentation='Számla vagy módosító okirat kiállításának dátumaInvoice or modification document issue date', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 878, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceDigestType, documentation="A kibocsátó adószámaThe supplier's tax number", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 884, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierGroupMemberTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceDigestType, documentation="A kibocsátó csoporttag számaThe supplier's group tax number", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 890, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierName'), _ImportedBinding_common.SimpleText512NotBlankType, scope=InvoiceDigestType, documentation='Az eladó (szállító) neveName of the seller (supplier)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 896, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceDigestType, documentation="A vevő adószámaThe buyer's tax number", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 902, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerGroupMemberTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceDigestType, documentation="A vevő csoporttag számaThe buyer's group tax number", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 908, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerName'), _ImportedBinding_common.SimpleText512NotBlankType, scope=InvoiceDigestType, documentation='A vevő neveName of the customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 914, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), _ImportedBinding_base.PaymentMethodType, scope=InvoiceDigestType, documentation='Fizetés módjaMethod of payment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 920, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentDate'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDigestType, documentation='Fizetési határidőDeadline for payment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 926, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance'), _ImportedBinding_base.InvoiceAppearanceType, scope=InvoiceDigestType, documentation='A számla megjelenési formájaForm of appearance of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 932, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), SourceType, scope=InvoiceDigestType, documentation='Az adatszolgáltatás forrásaData exchange source', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 938, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryDate'), _ImportedBinding_base.InvoiceDateType, scope=InvoiceDigestType, documentation='Számla teljesítési dátumaInvoice delivery date', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 944, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currency'), _ImportedBinding_common.CurrencyType, scope=InvoiceDigestType, documentation='A számla pénznemeCurrency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 950, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount'), _ImportedBinding_base.MonetaryType, scope=InvoiceDigestType, documentation='A számla nettó összege a számla pénznemébenInvoice net amount expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 956, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF'), _ImportedBinding_base.MonetaryType, scope=InvoiceDigestType, documentation='A számla nettó összege forintbanInvoice net amount expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 962, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount'), _ImportedBinding_base.MonetaryType, scope=InvoiceDigestType, documentation='A számla ÁFA összege a számla pénznemébenInvoice VAT amount expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 968, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF'), _ImportedBinding_base.MonetaryType, scope=InvoiceDigestType, documentation='A számla ÁFA összege forintbanInvoice VAT amount expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 974, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), _ImportedBinding_common.EntityIdType, scope=InvoiceDigestType, documentation='Az adatszolgáltatás tranzakció azonosítójaTransaction identifier of the data exchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 980, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), _ImportedBinding_base.InvoiceIndexType, scope=InvoiceDigestType, documentation='A számla sorszáma a kérésen belülSequence number of the invoice within the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 986, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceDigestType, documentation='Az eredeti számla sorszáma, melyre a módosítás vonatkozikSequence number of the original invoice, on which the modification occurs', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 992, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=InvoiceDigestType, documentation='A számlára vonatkozó módosító okirat egyedi sorszámaThe unique sequence number referring to the original invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 998, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insDate'), _ImportedBinding_base.InvoiceTimestampType, scope=InvoiceDigestType, documentation='A beszúrás időpontja UTC időbenInsert date in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1004, 3)))

InvoiceDigestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'completenessIndicator'), pyxb.binding.datatypes.boolean, scope=InvoiceDigestType, documentation='Jelöli, ha az adatszolgáltatás maga a számla (a számlán nem szerepel több adat)Indicates whether the data exchange is identical with the invoice (the invoice does not contain any more data)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1010, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 860, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 890, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 902, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 908, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 914, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 920, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 926, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 932, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 938, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 944, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 950, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 956, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 962, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 968, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 974, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 980, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 986, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 992, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 998, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1010, 3))
    counters.add(cc_19)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 854, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batchIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 860, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 866, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceCategory')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 872, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 878, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 884, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierGroupMemberTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 890, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 896, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 902, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerGroupMemberTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 908, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 914, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 920, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 926, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAppearance')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 932, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 938, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDeliveryDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 944, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 950, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 956, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 962, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 968, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 974, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 980, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 986, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 992, 3))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 998, 3))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1004, 3))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceDigestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'completenessIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1010, 3))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True) ]))
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
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, True) ]))
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
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, True) ]))
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
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, True) ]))
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
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, True) ]))
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
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, True) ]))
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
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, True) ]))
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
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, True) ]))
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
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, True) ]))
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
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
         ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_26._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceDigestType._Automaton = _BuildAutomaton_14()




InvoiceLinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxLineNumber'), _ImportedBinding_base.LineNumberType, scope=InvoiceLinesType, documentation='A sorok száma közül a legmagasabb, amit a számla tartalmazThe highest line number value the invoice contains', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1024, 3)))

InvoiceLinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'newCreatedLines'), NewCreatedLinesType, scope=InvoiceLinesType, documentation='A módosító okirat által újként létrehozott számlasorokNew invoice lines created by the modification document', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1030, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1030, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceLinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxLineNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1024, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceLinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'newCreatedLines')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1030, 3))
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
InvoiceLinesType._Automaton = _BuildAutomaton_15()




InvoiceNumberQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceNumberQueryType, documentation='Számla vagy módosító okirat sorszámaSequential number of the original or modification invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1044, 3)))

InvoiceNumberQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection'), InvoiceDirectionType, scope=InvoiceNumberQueryType, documentation='Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1050, 3)))

InvoiceNumberQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=InvoiceNumberQueryType, documentation='A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1056, 3)))

InvoiceNumberQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=InvoiceNumberQueryType, documentation="Vevő oldali lekérdezés esetén a számla kiállítójának adószáma, ha több érvényes számla is megtalálható azonos sorszámmalThe supplier's tax number in case of querying as customer, if the query result found more than one valid invoices with the same invoice number", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1062, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1056, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1062, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceNumberQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1044, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceNumberQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1050, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceNumberQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batchIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1056, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceNumberQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplierTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1062, 3))
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
InvoiceNumberQueryType._Automaton = _BuildAutomaton_16()




InvoiceOperationListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'compressedContent'), pyxb.binding.datatypes.boolean, scope=InvoiceOperationListType, documentation='Tömörített tartalom jelzése a feldolgozási folyamat számáraCompressed content indicator for the processing flow', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1076, 3)))

InvoiceOperationListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), InvoiceOperationType, scope=InvoiceOperationListType, documentation='A kéréshez tartozó számlaműveletInvoice operation of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1082, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=100, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1082, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceOperationListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'compressedContent')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1076, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceOperationListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1082, 3))
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
InvoiceOperationListType._Automaton = _BuildAutomaton_17()




InvoiceOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), _ImportedBinding_base.InvoiceIndexType, scope=InvoiceOperationType, documentation='A számla sorszáma a kérésen belülSequence number of the invoice within the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1096, 3)))

InvoiceOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), ManageInvoiceOperationType, scope=InvoiceOperationType, documentation='A kért számla művelet típusaType of the desired invoice operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1102, 3)))

InvoiceOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceData'), pyxb.binding.datatypes.base64Binary, scope=InvoiceOperationType, documentation='Számla adatok BASE64-ben kódolt tartalmaInvoice data in BASE64 encoded form', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1108, 3)))

InvoiceOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electronicInvoiceHash'), _ImportedBinding_common.CryptoType, scope=InvoiceOperationType, documentation='Elektronikus számla vagy módosító okirat állomány hash lenyomataElectronic invoice or modification document file hash value', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1114, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1114, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceOperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1096, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceOperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1102, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceOperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1108, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceOperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electronicInvoiceHash')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1114, 3))
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
InvoiceOperationType._Automaton = _BuildAutomaton_18()




InvoiceQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mandatoryQueryParams'), MandatoryQueryParamsType, scope=InvoiceQueryParamsType, documentation='A számla lekérdezés kötelező paramétereiMandatory params of the invoice query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1128, 3)))

InvoiceQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalQueryParams'), AdditionalQueryParamsType, scope=InvoiceQueryParamsType, documentation='A számla lekérdezés kiegészítő paramétereiAdditional params of the invoice query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1134, 3)))

InvoiceQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relationalQueryParams'), RelationalQueryParamsType, scope=InvoiceQueryParamsType, documentation='A számla lekérdezés relációs paramétereiRelational params of the invoice query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1140, 3)))

InvoiceQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionQueryParams'), TransactionQueryParamsType, scope=InvoiceQueryParamsType, documentation='A számla lekérdezés tranzakciós paramétereiTransactional params of the invoice query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1146, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1134, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1140, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1146, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mandatoryQueryParams')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1128, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalQueryParams')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1134, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relationalQueryParams')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1140, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InvoiceQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionQueryParams')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1146, 3))
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
InvoiceQueryParamsType._Automaton = _BuildAutomaton_19()




InvoiceReferenceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceReferenceDataType, documentation='Az eredeti számla sorszáma, melyre a módosítás vonatkozik  - ÁFA tv. 170. § (1) c)Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1160, 3)))

InvoiceReferenceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modifyWithoutMaster'), pyxb.binding.datatypes.boolean, scope=InvoiceReferenceDataType, documentation='Annak jelzése, hogy a módosítás olyan alapszámlára hivatkozik, amelyről nem történt és nem is fog történni adatszolgáltatásIndicates whether the modification references to an original invoice which is not and will not be exchanged', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1166, 3)))

InvoiceReferenceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modificationTimestamp'), _ImportedBinding_base.InvoiceTimestampType, scope=InvoiceReferenceDataType, documentation='A módosító okirat készítésének időbélyege a forrásrendszerben UTC időbenCreation date timestamp of the modification document in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1173, 4)))

InvoiceReferenceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=InvoiceReferenceDataType, documentation='A számlára vonatkozó módosító okirat egyedi sorszámaThe unique sequence number referring to the original invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1179, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceReferenceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1160, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceReferenceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modifyWithoutMaster')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1166, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceReferenceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modificationTimestamp')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1173, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceReferenceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modificationIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1179, 4))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceReferenceDataType._Automaton = _BuildAutomaton_20()




MandatoryQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate'), DateIntervalParamType, scope=MandatoryQueryParamsType, documentation='Számla kiállításának dátumtartományaDate range of the invoice issue date', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1242, 3)))

MandatoryQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insDate'), DateTimeIntervalParamType, scope=MandatoryQueryParamsType, documentation='Számla adatszolgáltatás feldolgozásának időpont tartománya UTC idő szerintDatetime range of processing data exchange in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1248, 3)))

MandatoryQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=MandatoryQueryParamsType, documentation='Az eredeti számla sorszáma, melyre a módosítás vonatkozikSequence number of the original invoice, on which the modification occurs', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1254, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MandatoryQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceIssueDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1242, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MandatoryQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1248, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MandatoryQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1254, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MandatoryQueryParamsType._Automaton = _BuildAutomaton_21()




NewCreatedLinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNumberIntervalStart'), _ImportedBinding_base.LineNumberType, scope=NewCreatedLinesType, documentation='Számla sor intervallum kezdeteInvoice line interval start', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1268, 3)))

NewCreatedLinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineNumberIntervalEnd'), _ImportedBinding_base.LineNumberType, scope=NewCreatedLinesType, documentation='Számla sor intervallum vége (inkluzív)Invoice line interval end (inclusive)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1274, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NewCreatedLinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNumberIntervalStart')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1268, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NewCreatedLinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineNumberIntervalEnd')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1274, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NewCreatedLinesType._Automaton = _BuildAutomaton_22()




PointerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tag'), _ImportedBinding_common.SimpleText1024NotBlankType, scope=PointerType, documentation='Tag hivatkozásTag reference', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1288, 3)))

PointerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), _ImportedBinding_common.SimpleText1024NotBlankType, scope=PointerType, documentation='Érték hivatkozásValue reference', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1294, 3)))

PointerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'line'), _ImportedBinding_base.LineNumberType, scope=PointerType, documentation='SorhivatkozásLine reference', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1300, 3)))

PointerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=PointerType, documentation='Kötegelt számla művelet esetén az eredeti számla sorszáma, melyre a módosítás vonatkozikIn case of a batch operation, the sequence number of the original invoice, on which the modification occurs', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1306, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1288, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1294, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1300, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1306, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1288, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PointerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1294, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PointerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'line')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1300, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PointerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalInvoiceNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1306, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PointerType._Automaton = _BuildAutomaton_23()




ProcessingResultListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processingResult'), ProcessingResultType, scope=ProcessingResultListType, documentation='Számla feldolgozási eredményInvoice processing result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1320, 3)))

ProcessingResultListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), OriginalRequestVersionType, scope=ProcessingResultListType, documentation='Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1326, 3)))

ProcessingResultListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentData'), AnnulmentDataType, scope=ProcessingResultListType, documentation='Technikai érvénytelenítés státusz adataiStatus data of technical annulment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1332, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1332, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessingResultListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processingResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1320, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProcessingResultListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1326, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingResultListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1332, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProcessingResultListType._Automaton = _BuildAutomaton_24()




ProcessingResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), _ImportedBinding_base.InvoiceIndexType, scope=ProcessingResultType, documentation='A számla sorszáma a kérésen belülSequence number of the invoice within the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1346, 3)))

ProcessingResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batchIndex'), _ImportedBinding_base.InvoiceUnboundedIndexType, scope=ProcessingResultType, documentation='A módosító okirat sorszáma a kötegen belülSequence number of the modification document within the batch', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1352, 3)))

ProcessingResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceStatus'), InvoiceStatusType, scope=ProcessingResultType, documentation='A számla feldolgozási státuszaProcessing status of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1358, 3)))

ProcessingResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'technicalValidationMessages'), _ImportedBinding_common.TechnicalValidationResultType, scope=ProcessingResultType, documentation='Technikai validációs üzenetekTechnical validation messages', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1364, 3)))

ProcessingResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'businessValidationMessages'), BusinessValidationResultType, scope=ProcessingResultType, documentation='Üzleti validációs üzenetekBusiness validation messages', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1370, 3)))

ProcessingResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'compressedContentIndicator'), pyxb.binding.datatypes.boolean, scope=ProcessingResultType, documentation='Jelöli, ha az originalRequest tartalmát a BASE64 dekódolást követően még ki kell tömöríteni az olvasáshozIndicates if the content of the originalRequest needs to be decompressed to be read following the BASE64 decoding', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1376, 3)))

ProcessingResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalRequest'), pyxb.binding.datatypes.base64Binary, scope=ProcessingResultType, documentation='Számla adatok BASE64-ben kódolt tartalmaInvoice data in BASE64 encoded form', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1382, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1352, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1364, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1370, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1382, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessingResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1346, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessingResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batchIndex')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1352, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessingResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceStatus')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1358, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessingResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'technicalValidationMessages')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1364, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessingResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'businessValidationMessages')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1370, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProcessingResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'compressedContentIndicator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1376, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalRequest')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1382, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProcessingResultType._Automaton = _BuildAutomaton_25()




RelationalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDelivery'), RelationQueryDateType, scope=RelationalQueryParamsType, documentation='Számla teljesítési dátumának kereső paramétereQuery parameter of the invoice delivery date', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1678, 3)))

RelationalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentDate'), RelationQueryDateType, scope=RelationalQueryParamsType, documentation='A számla fizetési határidejének kereső paramétereQuery parameter of the invoice payment date', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1684, 3)))

RelationalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount'), RelationQueryMonetaryType, scope=RelationalQueryParamsType, documentation='A számla nettó összeg kereső paramétere a számla pénznemébenQuery parameter of the invoice net amount expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1690, 3)))

RelationalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF'), RelationQueryMonetaryType, scope=RelationalQueryParamsType, documentation='A számla nettó összegének kereső paramétere forintbanQuery parameter of the invoice net amount expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1696, 3)))

RelationalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount'), RelationQueryMonetaryType, scope=RelationalQueryParamsType, documentation='A számla ÁFA összegének kereső paramétere a számla pénznemébenQuery parameter of the invoice VAT amount expressed in the currency of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1702, 3)))

RelationalQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF'), RelationQueryMonetaryType, scope=RelationalQueryParamsType, documentation='A számla ÁFA összegének kereső paramétere forintbanQuery parameter of the invoice VAT amount expressed in HUF', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1708, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1678, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1684, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1690, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1696, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1702, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1708, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelationalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDelivery')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1678, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RelationalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1684, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RelationalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1690, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RelationalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNetAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1696, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RelationalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1702, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RelationalQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceVatAmountHUF')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1708, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RelationalQueryParamsType._Automaton = _BuildAutomaton_26()




RelationQueryDateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'queryOperator'), QueryOperatorType, scope=RelationQueryDateType, documentation='Kereső operátorQuery operator', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1722, 3)))

RelationQueryDateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'queryValue'), _ImportedBinding_base.InvoiceDateType, scope=RelationQueryDateType, documentation='Kereső értékQuery value', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1728, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RelationQueryDateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'queryOperator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1722, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RelationQueryDateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'queryValue')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1728, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RelationQueryDateType._Automaton = _BuildAutomaton_27()




RelationQueryMonetaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'queryOperator'), QueryOperatorType, scope=RelationQueryMonetaryType, documentation='Kereső operátorQuery operator', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1742, 3)))

RelationQueryMonetaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'queryValue'), _ImportedBinding_base.MonetaryType, scope=RelationQueryMonetaryType, documentation='Kereső értékQuery value', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1748, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RelationQueryMonetaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'queryOperator')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1742, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RelationQueryMonetaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'queryValue')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1748, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RelationQueryMonetaryType._Automaton = _BuildAutomaton_28()




SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareId'), SoftwareIdType, scope=SoftwareType, documentation='A számlázóprogram azonosítójaBilling software ID', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1762, 3)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareName'), _ImportedBinding_common.SimpleText50NotBlankType, scope=SoftwareType, documentation='A számlázóprogram neveBilling software name', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1768, 3)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareOperation'), SoftwareOperationType, scope=SoftwareType, documentation='A számlázóprogram működési típusa (lokális program vagy online számlázó szolgáltatás)Billing software operation type (local program or online billing service)', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1774, 3)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareMainVersion'), _ImportedBinding_common.SimpleText15NotBlankType, scope=SoftwareType, documentation='A számlázóprogram főverziójaBilling software main version', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1780, 3)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareDevName'), _ImportedBinding_common.SimpleText512NotBlankType, scope=SoftwareType, documentation="A számlázóprogram fejlesztőjének neveName of the billing software's developer", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1786, 3)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareDevContact'), _ImportedBinding_common.SimpleText200NotBlankType, scope=SoftwareType, documentation="A számlázóprogram fejlesztőjének elektronikus elérhetőségeElectronic contact of the billing software's developer", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1792, 3)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareDevCountryCode'), _ImportedBinding_common.CountryCodeType, scope=SoftwareType, documentation="A számlázóprogram fejlesztőjének ISO-3166 alpha2 országkódjaISO-3166 alpha2 country code of the billing software's developer", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1798, 3)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareDevTaxNumber'), _ImportedBinding_common.SimpleText50NotBlankType, scope=SoftwareType, documentation="A számlázóprogram fejlesztőjének adószámaTax number of the billing software's developer", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1804, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1798, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1804, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1762, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1768, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1774, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareMainVersion')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1780, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareDevName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1786, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareDevContact')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1792, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareDevCountryCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1798, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareDevTaxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1804, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SoftwareType._Automaton = _BuildAutomaton_29()




TaxpayerAddressItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressType'), TaxpayerAddressTypeType, scope=TaxpayerAddressItemType, documentation='Adózói cím típusTaxpayer address type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1818, 3)))

TaxpayerAddressItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddress'), _ImportedBinding_base.DetailedAddressType, scope=TaxpayerAddressItemType, documentation='Az adózó címadataiAddress data of the taxpayer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1824, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxpayerAddressItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressType')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1818, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxpayerAddressItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddress')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1824, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxpayerAddressItemType._Automaton = _BuildAutomaton_30()




TaxpayerAddressListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressItem'), TaxpayerAddressItemType, scope=TaxpayerAddressListType, documentation='Adózói címsor adatTaxpayer address item', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1838, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxpayerAddressListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressItem')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1838, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxpayerAddressListType._Automaton = _BuildAutomaton_31()




TaxpayerDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerName'), _ImportedBinding_common.SimpleText512NotBlankType, scope=TaxpayerDataType, documentation='Az adózó neveName of the taxpayer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1852, 3)))

TaxpayerDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerShortName'), _ImportedBinding_common.SimpleText200NotBlankType, scope=TaxpayerDataType, documentation='Az adózó rövidített neveShortened name of the taxpayer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1858, 3)))

TaxpayerDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxNumberDetail'), _ImportedBinding_base.TaxNumberType, scope=TaxpayerDataType, documentation='Az adószám részletes adataiDetailed data of the tax number', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1864, 3)))

TaxpayerDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'incorporation'), IncorporationType, scope=TaxpayerDataType, documentation='Gazdasági típusIncorporation type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1870, 3)))

TaxpayerDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vatGroupMembership'), _ImportedBinding_common.TaxpayerIdType, scope=TaxpayerDataType, documentation='Az adózó ÁFA csoport tagságaVAT group membership of the taxpayer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1876, 3)))

TaxpayerDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressList'), TaxpayerAddressListType, scope=TaxpayerDataType, documentation='Adózói cím lista típusTaxpayer address list type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1882, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1858, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1876, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1882, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxpayerDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1852, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxpayerDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerShortName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1858, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxpayerDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxNumberDetail')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1864, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxpayerDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'incorporation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1870, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxpayerDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vatGroupMembership')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1876, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxpayerDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerAddressList')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1882, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxpayerDataType._Automaton = _BuildAutomaton_32()




TransactionListResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentPage'), _ImportedBinding_common.ResponsePageType, scope=TransactionListResultType, documentation='A jelenleg lekérdezett lapszámThe currently queried page count', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1926, 3)))

TransactionListResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'availablePage'), _ImportedBinding_common.ResponsePageType, scope=TransactionListResultType, documentation='A lekérdezés eredménye szerint elérhető utolsó lapszámThe highest available page count matching the query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1932, 3)))

TransactionListResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transaction'), TransactionType, scope=TransactionListResultType, documentation='Tranzakció lekérdezési eredményTransaction query result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1938, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1938, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionListResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentPage')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1926, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionListResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availablePage')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1932, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionListResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transaction')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1938, 3))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransactionListResultType._Automaton = _BuildAutomaton_33()




TransactionQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), _ImportedBinding_common.EntityIdType, scope=TransactionQueryParamsType, documentation='Az adatszolgáltatás tranzakció azonosítójaTransaction identifier of the data exchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1952, 3)))

TransactionQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), _ImportedBinding_base.InvoiceIndexType, scope=TransactionQueryParamsType, documentation='A számla sorszáma a kérésen belülSequence number of the invoice within the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1958, 3)))

TransactionQueryParamsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation'), ManageInvoiceOperationType, scope=TransactionQueryParamsType, documentation='Számlaművelet típusInvoice operation type', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1964, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1958, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1964, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1952, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1958, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionQueryParamsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperation')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1964, 3))
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
TransactionQueryParamsType._Automaton = _BuildAutomaton_34()




TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insDate'), _ImportedBinding_base.InvoiceTimestampType, scope=TransactionType, documentation='A beszúrás időpontja UTC időbenInsert date in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1996, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insCusUser'), _ImportedBinding_common.LoginType, scope=TransactionType, documentation='A beszúrást végző felhasználóInserting user name', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2002, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), SourceType, scope=TransactionType, documentation='Az adatszolgáltatás forrásaData exchange source', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2008, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), _ImportedBinding_common.EntityIdType, scope=TransactionType, documentation='A számla tranzakció azonosítójaTransaction ID of the invoice', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2014, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requestStatus'), RequestStatusType, scope=TransactionType, documentation='A kérés feldolgozási státuszaProcessing status of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2020, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'technicalAnnulment'), pyxb.binding.datatypes.boolean, scope=TransactionType, documentation='Jelöli ha a tranzakció technikai érvénytelenítést tartalmazIndicates whether the transaction contains technical annulment', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2026, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion'), OriginalRequestVersionType, scope=TransactionType, documentation='Az adatszolgáltatás requestVersion értékerequestVersion value of the invoice exchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2032, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemCount'), _ImportedBinding_base.InvoiceIndexType, scope=TransactionType, documentation='Az adatszolgáltatás tételeinek számaItem count of the invoiceExchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2038, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1996, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insCusUser')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2002, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2008, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2014, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requestStatus')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2020, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'technicalAnnulment')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2026, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalRequestVersion')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2032, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemCount')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 2038, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransactionType._Automaton = _BuildAutomaton_35()




BasicOnlineInvoiceRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'software'), SoftwareType, scope=BasicOnlineInvoiceRequestType, documentation='A számlázóprogram adataiBilling software data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicOnlineInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicOnlineInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BasicOnlineInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
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
BasicOnlineInvoiceRequestType._Automaton = _BuildAutomaton_36()




BasicOnlineInvoiceResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'software'), SoftwareType, scope=BasicOnlineInvoiceResponseType, documentation='A számlázóprogram adataiBilling software data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicOnlineInvoiceResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BasicOnlineInvoiceResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BasicOnlineInvoiceResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
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
BasicOnlineInvoiceResponseType._Automaton = _BuildAutomaton_37()




GeneralErrorResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'software'), SoftwareType, scope=GeneralErrorResponseType, documentation='A számlázóprogram adataiBilling software data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 646, 5)))

GeneralErrorResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'technicalValidationMessages'), _ImportedBinding_common.TechnicalValidationResultType, scope=GeneralErrorResponseType, documentation='Technikai validációs üzenetekTechnical validation messages', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 652, 5)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 652, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeneralErrorResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeneralErrorResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneralErrorResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 646, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneralErrorResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'technicalValidationMessages')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 652, 5))
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
GeneralErrorResponseType._Automaton = _BuildAutomaton_38()




ManageAnnulmentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken'), _ImportedBinding_common.SimpleText50NotBlankType, scope=ManageAnnulmentRequestType, documentation='A tranzakcióhoz kiadott egyedi és dekódolt tokenThe decoded unique token issued for the current transaction', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1196, 5)))

ManageAnnulmentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperations'), AnnulmentOperationListType, scope=ManageAnnulmentRequestType, documentation='A kéréshez tartozó kötegelt technikai érvénytelenítésekBatch technical annulment operations of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1202, 5)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageAnnulmentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageAnnulmentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageAnnulmentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageAnnulmentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1196, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ManageAnnulmentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperations')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1202, 5))
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
ManageAnnulmentRequestType._Automaton = _BuildAutomaton_39()




ManageInvoiceRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken'), _ImportedBinding_common.SimpleText50NotBlankType, scope=ManageInvoiceRequestType, documentation='A tranzakcióhoz kiadott egyedi és dekódolt tokenThe decoded unique token issued for the current transaction', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1220, 5)))

ManageInvoiceRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperations'), InvoiceOperationListType, scope=ManageInvoiceRequestType, documentation='A kéréshez tartozó kötegelt számlaműveletekBatch invoice operations of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1226, 5)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManageInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1220, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ManageInvoiceRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperations')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1226, 5))
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
ManageInvoiceRequestType._Automaton = _BuildAutomaton_40()




QueryInvoiceChainDigestRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'page'), _ImportedBinding_common.RequestPageType, scope=QueryInvoiceChainDigestRequestType, documentation='A lekérdezni kívánt lap számaThe queried page count', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1398, 5)))

QueryInvoiceChainDigestRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainQuery'), InvoiceChainQueryType, scope=QueryInvoiceChainDigestRequestType, documentation='Számlalánc kivonat lekérdezés számlaszám paramétereInvoice number param of the invoice chain digest query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1404, 5)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'page')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1398, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainQuery')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1404, 5))
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
QueryInvoiceChainDigestRequestType._Automaton = _BuildAutomaton_41()




QueryInvoiceChainDigestResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainDigestResult'), InvoiceChainDigestResultType, scope=QueryInvoiceChainDigestResponseType, documentation='Számlalánc kivonat lekérdezés eredményeiInvoice chain digest query result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1422, 5)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceChainDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainDigestResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1422, 5))
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
QueryInvoiceChainDigestResponseType._Automaton = _BuildAutomaton_42()




QueryInvoiceCheckResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceCheckResult'), pyxb.binding.datatypes.boolean, scope=QueryInvoiceCheckResponseType, documentation='Jelöli, ha a lekérdezett számlaszám érvényesként szerepel a rendszerben és a lekérdező adószáma kiállítóként vagy eladóként szerepel a számlánIndicates whether the queried invoice number exists in the system as a valid invoice, if the tax number of the querying entity is present on the invoice either as supplier or customer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1440, 5)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceCheckResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceCheckResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceCheckResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceCheckResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceCheckResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1440, 5))
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
QueryInvoiceCheckResponseType._Automaton = _BuildAutomaton_43()




QueryInvoiceDataRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumberQuery'), InvoiceNumberQueryType, scope=QueryInvoiceDataRequestType, documentation='Számla lekérdezés számlaszám paramétereInvoice number param of the Invoice query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1458, 5)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumberQuery')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1458, 5))
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
QueryInvoiceDataRequestType._Automaton = _BuildAutomaton_44()




QueryInvoiceDataResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDataResult'), InvoiceDataResultType, scope=QueryInvoiceDataResponseType, documentation='A számla lekérdezés eredményeInvoice data query result', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1476, 5)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1476, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDataResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDataResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1476, 5))
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
QueryInvoiceDataResponseType._Automaton = _BuildAutomaton_45()




QueryInvoiceDigestRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'page'), _ImportedBinding_common.RequestPageType, scope=QueryInvoiceDigestRequestType, documentation='A lekérdezni kívánt lap számaThe queried page count', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1494, 5)))

QueryInvoiceDigestRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection'), InvoiceDirectionType, scope=QueryInvoiceDigestRequestType, documentation='Kimenő vagy bejövő számla keresési paramétereInbound or outbound invoice query parameter', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1500, 5)))

QueryInvoiceDigestRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceQueryParams'), InvoiceQueryParamsType, scope=QueryInvoiceDigestRequestType, documentation='Számla lekérdezési paraméterekInvoice query parameters', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1506, 5)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'page')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1494, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1500, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceQueryParams')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1506, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryInvoiceDigestRequestType._Automaton = _BuildAutomaton_46()




QueryInvoiceDigestResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceDigestResult'), InvoiceDigestResultType, scope=QueryInvoiceDigestResponseType, documentation='A számla kivonat lekérdezés eredményeiInvoice digest query results', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1524, 5)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryInvoiceDigestResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDigestResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1524, 5))
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
QueryInvoiceDigestResponseType._Automaton = _BuildAutomaton_47()




QueryTaxpayerRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxNumber'), _ImportedBinding_common.TaxpayerIdType, scope=QueryTaxpayerRequestType, documentation='A lekérdezett adózó adószámaTax number of the queried taxpayer', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1542, 5)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1542, 5))
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
QueryTaxpayerRequestType._Automaton = _BuildAutomaton_48()




QueryTaxpayerResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infoDate'), pyxb.binding.datatypes.dateTime, scope=QueryTaxpayerResponseType, documentation='Az adatok utolsó változásának időpontjaLast date on which the data was changed', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1560, 5)))

QueryTaxpayerResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerValidity'), pyxb.binding.datatypes.boolean, scope=QueryTaxpayerResponseType, documentation='Jelzi, hogy a lekérdezett adózó létezik és érvényes-eIndicates whether the queried taxpayer is existing and valid', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1566, 5)))

QueryTaxpayerResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxpayerData'), TaxpayerDataType, scope=QueryTaxpayerResponseType, documentation='Az adózó lekérdezés válasz adataiResponse data of the taxpayer query', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1572, 5)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1560, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1566, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1572, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infoDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1560, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerValidity')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1566, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(QueryTaxpayerResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1572, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTaxpayerResponseType._Automaton = _BuildAutomaton_49()




QueryTransactionListRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'page'), _ImportedBinding_common.RequestPageType, scope=QueryTransactionListRequestType, documentation='A lekérdezni kívánt lap számaThe queried page count', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1590, 5)))

QueryTransactionListRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'insDate'), DateTimeIntervalParamType, scope=QueryTransactionListRequestType, documentation="A lekérdezni kívánt tranzakciók kiadásának szerver oldali ideje UTC időbenThe queried transaction's insert date on server side in UTC time", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1596, 5)))

QueryTransactionListRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requestStatus'), RequestStatusType, scope=QueryTransactionListRequestType, documentation='A kérés feldolgozási státuszaProcessing status of the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1602, 5)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1602, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'page')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1590, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1596, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requestStatus')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1602, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTransactionListRequestType._Automaton = _BuildAutomaton_50()




QueryTransactionListResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionListResult'), TransactionListResultType, scope=QueryTransactionListResponseType, documentation='Tranzakció lekérdezési eredményeiTransaction query results', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1620, 5)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTransactionListResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionListResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1620, 5))
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
QueryTransactionListResponseType._Automaton = _BuildAutomaton_51()




QueryTransactionStatusRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), _ImportedBinding_common.EntityIdType, scope=QueryTransactionStatusRequestType, documentation='Az adatszolgáltatás tranzakció azonosítójaTransaction identifier of the data exchange', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1638, 5)))

QueryTransactionStatusRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnOriginalRequest'), pyxb.binding.datatypes.boolean, scope=QueryTransactionStatusRequestType, documentation='Jelöli, ha a kliens által beküldött eredeti tartalmat is vissza kell adni a válaszbanIndicates if the original client data should also be returned in the response', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1644, 5)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1644, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1638, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnOriginalRequest')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1644, 5))
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTransactionStatusRequestType._Automaton = _BuildAutomaton_52()




QueryTransactionStatusResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processingResults'), ProcessingResultListType, scope=QueryTransactionStatusResponseType, documentation='A kérésben szereplő számlák feldolgozási státuszaProcessing status of the invoices in the request', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1662, 5)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1662, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTransactionStatusResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processingResults')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1662, 5))
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
QueryTransactionStatusResponseType._Automaton = _BuildAutomaton_53()




TokenExchangeResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'encodedExchangeToken'), pyxb.binding.datatypes.base64Binary, scope=TokenExchangeResponseType, documentation='A kiadott exchange token AES-128 ECB algoritmussal kódolt alakjaThe issued exchange token in AES-128 ECB encoded form', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1898, 5)))

TokenExchangeResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityFrom'), _ImportedBinding_base.InvoiceTimestampType, scope=TokenExchangeResponseType, documentation='A kiadott token érvényességének kezdeteValidity start of the issued exchange token', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1904, 5)))

TokenExchangeResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityTo'), _ImportedBinding_base.InvoiceTimestampType, scope=TokenExchangeResponseType, documentation='A kiadott token érvényességének végeValidity end of the issued exchange token', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1910, 5)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TokenExchangeResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TokenExchangeResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TokenExchangeResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TokenExchangeResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'encodedExchangeToken')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1898, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TokenExchangeResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityFrom')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1904, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TokenExchangeResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityTo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1910, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TokenExchangeResponseType._Automaton = _BuildAutomaton_54()




TransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), _ImportedBinding_common.EntityIdType, scope=TransactionResponseType, documentation='A kért operáció tranzakció azonosítójaTransaction identifier of the requested operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1980, 5)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1980, 5))
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
TransactionResponseType._Automaton = _BuildAutomaton_55()




def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
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
CTD_ANON._Automaton = _BuildAutomaton_56()




def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 652, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 646, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'technicalValidationMessages')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 652, 5))
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
CTD_ANON_._Automaton = _BuildAutomaton_57()




def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1196, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentOperations')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1202, 5))
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
CTD_ANON_2._Automaton = _BuildAutomaton_58()




def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1980, 5))
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
CTD_ANON_3._Automaton = _BuildAutomaton_59()




def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exchangeToken')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1220, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceOperations')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1226, 5))
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
CTD_ANON_4._Automaton = _BuildAutomaton_60()




def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1980, 5))
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
CTD_ANON_5._Automaton = _BuildAutomaton_61()




def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'page')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1398, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainQuery')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1404, 5))
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
CTD_ANON_6._Automaton = _BuildAutomaton_62()




def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceChainDigestResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1422, 5))
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
CTD_ANON_7._Automaton = _BuildAutomaton_63()




def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumberQuery')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1458, 5))
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
CTD_ANON_8._Automaton = _BuildAutomaton_64()




def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceCheckResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1440, 5))
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
CTD_ANON_9._Automaton = _BuildAutomaton_65()




def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceNumberQuery')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1458, 5))
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
CTD_ANON_10._Automaton = _BuildAutomaton_66()




def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1476, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDataResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1476, 5))
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
CTD_ANON_11._Automaton = _BuildAutomaton_67()




def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'page')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1494, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDirection')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1500, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceQueryParams')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1506, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_68()




def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceDigestResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1524, 5))
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
CTD_ANON_13._Automaton = _BuildAutomaton_69()




def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxNumber')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1542, 5))
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
CTD_ANON_14._Automaton = _BuildAutomaton_70()




def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1560, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1566, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1572, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infoDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1560, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerValidity')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1566, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxpayerData')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1572, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_71()




def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1602, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'page')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1590, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'insDate')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1596, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requestStatus')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1602, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_72()




def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionListResult')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1620, 5))
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
CTD_ANON_17._Automaton = _BuildAutomaton_73()




def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1644, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 526, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'user')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 538, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1638, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnOriginalRequest')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1644, 5))
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_74()




def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1662, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processingResults')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1662, 5))
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
CTD_ANON_19._Automaton = _BuildAutomaton_75()




def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'header')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 546, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(_Namespace_common, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/common.xsd', 552, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 556, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'encodedExchangeToken')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1898, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityFrom')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1904, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tokenValidityTo')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceApi.xsd', 1910, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_76()

