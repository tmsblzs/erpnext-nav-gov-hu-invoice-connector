# generated/binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:394853d73b8ff2a556b581242ebb4cf233e89c0e
# Generated 2022-06-05 12:05:14.792858 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://schemas.nav.gov.hu/OSA/3.0/annul

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
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.nav.gov.hu/OSA/3.0/annul', create_if_missing=True)
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


# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/annul}AnnulmentCodeType
class AnnulmentCodeType (_ImportedBinding_common.AtomicStringType32, pyxb.binding.basis.enumeration_mixin):

    """Technikai érvénytelenítés kód típusaTechnical annulment code type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnnulmentCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 11, 1)
    _Documentation = 'Technikai érvénytelenítés kód típusaTechnical annulment code type'
AnnulmentCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AnnulmentCodeType, enum_prefix=None)
AnnulmentCodeType.ERRATIC_DATA = AnnulmentCodeType._CF_enumeration.addEnumeration(unicode_value='ERRATIC_DATA', tag='ERRATIC_DATA')
AnnulmentCodeType.ERRATIC_INVOICE_NUMBER = AnnulmentCodeType._CF_enumeration.addEnumeration(unicode_value='ERRATIC_INVOICE_NUMBER', tag='ERRATIC_INVOICE_NUMBER')
AnnulmentCodeType.ERRATIC_INVOICE_ISSUE_DATE = AnnulmentCodeType._CF_enumeration.addEnumeration(unicode_value='ERRATIC_INVOICE_ISSUE_DATE', tag='ERRATIC_INVOICE_ISSUE_DATE')
AnnulmentCodeType.ERRATIC_ELECTRONIC_HASH_VALUE = AnnulmentCodeType._CF_enumeration.addEnumeration(unicode_value='ERRATIC_ELECTRONIC_HASH_VALUE', tag='ERRATIC_ELECTRONIC_HASH_VALUE')
AnnulmentCodeType._InitializeFacetMap(AnnulmentCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AnnulmentCodeType', AnnulmentCodeType)
_module_typeBindings.AnnulmentCodeType = AnnulmentCodeType

# Complex type {http://schemas.nav.gov.hu/OSA/3.0/annul}InvoiceAnnulmentType with content type ELEMENT_ONLY
class InvoiceAnnulmentType (pyxb.binding.basis.complexTypeDefinition):
    """Korábbi adatszolgáltatás technikai érvénytelenítésének adataiData of technical annulment concerning previous data exchange"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceAnnulmentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 43, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentReference uses Python identifier annulmentReference
    __annulmentReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentReference'), 'annulmentReference', '__httpschemas_nav_gov_huOSA3_0annul_InvoiceAnnulmentType_httpschemas_nav_gov_huOSA3_0annulannulmentReference', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 49, 3), )

    
    annulmentReference = property(__annulmentReference.value, __annulmentReference.set, None, 'A technikai érvénytelenítéssel érintett számla vagy módosító okirat sorszámaSequential number of the invoice or modification document to be annuled')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentTimestamp uses Python identifier annulmentTimestamp
    __annulmentTimestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentTimestamp'), 'annulmentTimestamp', '__httpschemas_nav_gov_huOSA3_0annul_InvoiceAnnulmentType_httpschemas_nav_gov_huOSA3_0annulannulmentTimestamp', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 55, 3), )

    
    annulmentTimestamp = property(__annulmentTimestamp.value, __annulmentTimestamp.set, None, 'A technikai érvénytelenítés időbélyege a forrásrendszerben UTC idő szerintTimestamp of the technical annulment in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentCode uses Python identifier annulmentCode
    __annulmentCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentCode'), 'annulmentCode', '__httpschemas_nav_gov_huOSA3_0annul_InvoiceAnnulmentType_httpschemas_nav_gov_huOSA3_0annulannulmentCode', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 61, 3), )

    
    annulmentCode = property(__annulmentCode.value, __annulmentCode.set, None, 'A technikai érvénytelenítés kódjaTechnical annulment code')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentReason uses Python identifier annulmentReason
    __annulmentReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annulmentReason'), 'annulmentReason', '__httpschemas_nav_gov_huOSA3_0annul_InvoiceAnnulmentType_httpschemas_nav_gov_huOSA3_0annulannulmentReason', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 67, 3), )

    
    annulmentReason = property(__annulmentReason.value, __annulmentReason.set, None, 'A technikai érvénytelenítés okaTechnical annulment reason')

    _ElementMap.update({
        __annulmentReference.name() : __annulmentReference,
        __annulmentTimestamp.name() : __annulmentTimestamp,
        __annulmentCode.name() : __annulmentCode,
        __annulmentReason.name() : __annulmentReason
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceAnnulmentType = InvoiceAnnulmentType
Namespace.addCategoryObject('typeBinding', 'InvoiceAnnulmentType', InvoiceAnnulmentType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (InvoiceAnnulmentType):
    """XML root element, a technikai érvénytelenítés adatait leíró típus, amelyet BASE64 kódoltan tartalmaz az invoiceApi sémaleíró invoiceAnnulment elementjeXML root element, technical annulment data type in BASE64 encoding, equivalent with the invoiceApi schema definition's invoiceAnnulment element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 80, 2)
    _ElementMap = InvoiceAnnulmentType._ElementMap.copy()
    _AttributeMap = InvoiceAnnulmentType._AttributeMap.copy()
    # Base type is InvoiceAnnulmentType
    
    # Element annulmentReference ({http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentReference) inherited from {http://schemas.nav.gov.hu/OSA/3.0/annul}InvoiceAnnulmentType
    
    # Element annulmentTimestamp ({http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentTimestamp) inherited from {http://schemas.nav.gov.hu/OSA/3.0/annul}InvoiceAnnulmentType
    
    # Element annulmentCode ({http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentCode) inherited from {http://schemas.nav.gov.hu/OSA/3.0/annul}InvoiceAnnulmentType
    
    # Element annulmentReason ({http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentReason) inherited from {http://schemas.nav.gov.hu/OSA/3.0/annul}InvoiceAnnulmentType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


InvoiceAnnulment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InvoiceAnnulment'), CTD_ANON, documentation="XML root element, a technikai érvénytelenítés adatait leíró típus, amelyet BASE64 kódoltan tartalmaz az invoiceApi sémaleíró invoiceAnnulment elementjeXML root element, technical annulment data type in BASE64 encoding, equivalent with the invoiceApi schema definition's invoiceAnnulment element", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 75, 1))
Namespace.addCategoryObject('elementBinding', InvoiceAnnulment.name().localName(), InvoiceAnnulment)



InvoiceAnnulmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentReference'), _ImportedBinding_common.SimpleText50NotBlankType, scope=InvoiceAnnulmentType, documentation='A technikai érvénytelenítéssel érintett számla vagy módosító okirat sorszámaSequential number of the invoice or modification document to be annuled', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 49, 3)))

InvoiceAnnulmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentTimestamp'), _ImportedBinding_base.InvoiceTimestampType, scope=InvoiceAnnulmentType, documentation='A technikai érvénytelenítés időbélyege a forrásrendszerben UTC idő szerintTimestamp of the technical annulment in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 55, 3)))

InvoiceAnnulmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentCode'), AnnulmentCodeType, scope=InvoiceAnnulmentType, documentation='A technikai érvénytelenítés kódjaTechnical annulment code', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 61, 3)))

InvoiceAnnulmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annulmentReason'), _ImportedBinding_common.SimpleText1024NotBlankType, scope=InvoiceAnnulmentType, documentation='A technikai érvénytelenítés okaTechnical annulment reason', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 67, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceAnnulmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentReference')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceAnnulmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentTimestamp')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 55, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceAnnulmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 61, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceAnnulmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentReason')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 67, 3))
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
InvoiceAnnulmentType._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentReference')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentTimestamp')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 55, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentCode')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 61, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annulmentReason')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/invoiceAnnulment.xsd', 67, 3))
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
CTD_ANON._Automaton = _BuildAutomaton_()

