# generated/binding_3.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:6dd5abfc103f7d78651aec059fe4e25df817a5a2
# Generated 2022-06-05 12:05:14.792632 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://schemas.nav.gov.hu/OSA/3.0/metrics

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
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.nav.gov.hu/OSA/3.0/metrics', create_if_missing=True)
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


# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/metrics}LanguageType
class LanguageType (_ImportedBinding_common.AtomicStringType2, pyxb.binding.basis.enumeration_mixin):

    """Nyelv megnevezés típusLanguage naming type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 11, 1)
    _Documentation = 'Nyelv megnevezés típusLanguage naming type'
LanguageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LanguageType, enum_prefix=None)
LanguageType.HU = LanguageType._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
LanguageType.EN = LanguageType._CF_enumeration.addEnumeration(unicode_value='EN', tag='EN')
LanguageType.DE = LanguageType._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
LanguageType._InitializeFacetMap(LanguageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LanguageType', LanguageType)
_module_typeBindings.LanguageType = LanguageType

# Atomic simple type: {http://schemas.nav.gov.hu/OSA/3.0/metrics}MetricTypeType
class MetricTypeType (_ImportedBinding_common.AtomicStringType15, pyxb.binding.basis.enumeration_mixin):

    """Metrika típusának leírójaMetric's descriptor type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetricTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 37, 1)
    _Documentation = "Metrika típusának leírójaMetric's descriptor type"
MetricTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MetricTypeType, enum_prefix=None)
MetricTypeType.COUNTER = MetricTypeType._CF_enumeration.addEnumeration(unicode_value='COUNTER', tag='COUNTER')
MetricTypeType.GAUGE = MetricTypeType._CF_enumeration.addEnumeration(unicode_value='GAUGE', tag='GAUGE')
MetricTypeType.HISTOGRAM = MetricTypeType._CF_enumeration.addEnumeration(unicode_value='HISTOGRAM', tag='HISTOGRAM')
MetricTypeType.SUMMARY = MetricTypeType._CF_enumeration.addEnumeration(unicode_value='SUMMARY', tag='SUMMARY')
MetricTypeType._InitializeFacetMap(MetricTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MetricTypeType', MetricTypeType)
_module_typeBindings.MetricTypeType = MetricTypeType

# Complex type {http://schemas.nav.gov.hu/OSA/3.0/metrics}MetricDefinitionType with content type ELEMENT_ONLY
class MetricDefinitionType (pyxb.binding.basis.complexTypeDefinition):
    """Metrika definíció típusMetric definition type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetricDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 69, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metricName uses Python identifier metricName
    __metricName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metricName'), 'metricName', '__httpschemas_nav_gov_huOSA3_0metrics_MetricDefinitionType_httpschemas_nav_gov_huOSA3_0metricsmetricName', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 75, 3), )

    
    metricName = property(__metricName.value, __metricName.set, None, "Metrika neveMetric's name")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metricType uses Python identifier metricType
    __metricType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metricType'), 'metricType', '__httpschemas_nav_gov_huOSA3_0metrics_MetricDefinitionType_httpschemas_nav_gov_huOSA3_0metricsmetricType', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 81, 3), )

    
    metricType = property(__metricType.value, __metricType.set, None, "Metrika típusaMetric's type")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metricDescription uses Python identifier metricDescription
    __metricDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metricDescription'), 'metricDescription', '__httpschemas_nav_gov_huOSA3_0metrics_MetricDefinitionType_httpschemas_nav_gov_huOSA3_0metricsmetricDescription', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 87, 3), )

    
    metricDescription = property(__metricDescription.value, __metricDescription.set, None, "Metrika leírásaMetric's description")

    _ElementMap.update({
        __metricName.name() : __metricName,
        __metricType.name() : __metricType,
        __metricDescription.name() : __metricDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MetricDefinitionType = MetricDefinitionType
Namespace.addCategoryObject('typeBinding', 'MetricDefinitionType', MetricDefinitionType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/metrics}MetricDescriptionType with content type ELEMENT_ONLY
class MetricDescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Metrika leírás típusMetric description type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetricDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 95, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'language'), 'language', '__httpschemas_nav_gov_huOSA3_0metrics_MetricDescriptionType_httpschemas_nav_gov_huOSA3_0metricslanguage', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 101, 3), )

    
    language = property(__language.value, __language.set, None, 'Nyelv megnevezésLanguage naming')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}localizedDescription uses Python identifier localizedDescription
    __localizedDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'localizedDescription'), 'localizedDescription', '__httpschemas_nav_gov_huOSA3_0metrics_MetricDescriptionType_httpschemas_nav_gov_huOSA3_0metricslocalizedDescription', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 107, 3), )

    
    localizedDescription = property(__localizedDescription.value, __localizedDescription.set, None, 'Lokalizált leírásLocalized description')

    _ElementMap.update({
        __language.name() : __language,
        __localizedDescription.name() : __localizedDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MetricDescriptionType = MetricDescriptionType
Namespace.addCategoryObject('typeBinding', 'MetricDescriptionType', MetricDescriptionType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/metrics}MetricType with content type ELEMENT_ONLY
class MetricType (pyxb.binding.basis.complexTypeDefinition):
    """Metrika típusMetric data type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetricType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 115, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metricDefinition uses Python identifier metricDefinition
    __metricDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metricDefinition'), 'metricDefinition', '__httpschemas_nav_gov_huOSA3_0metrics_MetricType_httpschemas_nav_gov_huOSA3_0metricsmetricDefinition', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 121, 3), )

    
    metricDefinition = property(__metricDefinition.value, __metricDefinition.set, None, 'Metrika definícióMetric definition')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metricValues uses Python identifier metricValues
    __metricValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metricValues'), 'metricValues', '__httpschemas_nav_gov_huOSA3_0metrics_MetricType_httpschemas_nav_gov_huOSA3_0metricsmetricValues', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 127, 3), )

    
    metricValues = property(__metricValues.value, __metricValues.set, None, 'Metrika értékekMetric values')

    _ElementMap.update({
        __metricDefinition.name() : __metricDefinition,
        __metricValues.name() : __metricValues
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MetricType = MetricType
Namespace.addCategoryObject('typeBinding', 'MetricType', MetricType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/metrics}MetricValueType with content type ELEMENT_ONLY
class MetricValueType (pyxb.binding.basis.complexTypeDefinition):
    """Metrika érték típusMetric value type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetricValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 135, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpschemas_nav_gov_huOSA3_0metrics_MetricValueType_httpschemas_nav_gov_huOSA3_0metricsvalue', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 141, 3), )

    
    value_ = property(__value.value, __value.set, None, "Metrika értékeMetric's value")

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpschemas_nav_gov_huOSA3_0metrics_MetricValueType_httpschemas_nav_gov_huOSA3_0metricstimestamp', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 147, 3), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, 'Metrika értékének időpontja UTC időbenTime of metric value in UTC time')

    _ElementMap.update({
        __value.name() : __value,
        __timestamp.name() : __timestamp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MetricValueType = MetricValueType
Namespace.addCategoryObject('typeBinding', 'MetricValueType', MetricValueType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/metrics}QueryServiceMetricsListResponseType with content type ELEMENT_ONLY
class QueryServiceMetricsListResponseType (pyxb.binding.basis.complexTypeDefinition):
    """A GET /queryServiceMetrics/list REST operáció válasz típusaResponse type of the GET /queryServiceMetrics/list REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryServiceMetricsListResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 155, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metricDefinition uses Python identifier metricDefinition
    __metricDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metricDefinition'), 'metricDefinition', '__httpschemas_nav_gov_huOSA3_0metrics_QueryServiceMetricsListResponseType_httpschemas_nav_gov_huOSA3_0metricsmetricDefinition', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 161, 3), )

    
    metricDefinition = property(__metricDefinition.value, __metricDefinition.set, None, 'Metrika definícióiMetric definitions')

    _ElementMap.update({
        __metricDefinition.name() : __metricDefinition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryServiceMetricsListResponseType = QueryServiceMetricsListResponseType
Namespace.addCategoryObject('typeBinding', 'QueryServiceMetricsListResponseType', QueryServiceMetricsListResponseType)


# Complex type {http://schemas.nav.gov.hu/OSA/3.0/metrics}QueryServiceMetricsResponseType with content type ELEMENT_ONLY
class QueryServiceMetricsResponseType (pyxb.binding.basis.complexTypeDefinition):
    """A GET /queryServiceMetrics REST operáció válasz típusaResponse type of the GET /queryServiceMetrics REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryServiceMetricsResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 169, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httpschemas_nav_gov_huOSA3_0metrics_QueryServiceMetricsResponseType_httpschemas_nav_gov_huOSA3_0metricsresult', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 175, 3), )

    
    result = property(__result.value, __result.set, None, 'Alap válaszeredmény adatokBasic result data')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metricsLastUpdateTime uses Python identifier metricsLastUpdateTime
    __metricsLastUpdateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metricsLastUpdateTime'), 'metricsLastUpdateTime', '__httpschemas_nav_gov_huOSA3_0metrics_QueryServiceMetricsResponseType_httpschemas_nav_gov_huOSA3_0metricsmetricsLastUpdateTime', False, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 181, 3), )

    
    metricsLastUpdateTime = property(__metricsLastUpdateTime.value, __metricsLastUpdateTime.set, None, 'A metrikák utolsó frissítésének időpontja UTC időbenLast update time of metrics in UTC time')

    
    # Element {http://schemas.nav.gov.hu/OSA/3.0/metrics}metric uses Python identifier metric
    __metric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metric'), 'metric', '__httpschemas_nav_gov_huOSA3_0metrics_QueryServiceMetricsResponseType_httpschemas_nav_gov_huOSA3_0metricsmetric', True, pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 187, 3), )

    
    metric = property(__metric.value, __metric.set, None, 'Metrika adataiMetric data')

    _ElementMap.update({
        __result.name() : __result,
        __metricsLastUpdateTime.name() : __metricsLastUpdateTime,
        __metric.name() : __metric
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryServiceMetricsResponseType = QueryServiceMetricsResponseType
Namespace.addCategoryObject('typeBinding', 'QueryServiceMetricsResponseType', QueryServiceMetricsResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (QueryServiceMetricsListResponseType):
    """A GET /queryServiceMetrics/list REST operáció válaszának root elementjeResponse root element of the GET /queryServiceMetrics/list REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 200, 2)
    _ElementMap = QueryServiceMetricsListResponseType._ElementMap.copy()
    _AttributeMap = QueryServiceMetricsListResponseType._AttributeMap.copy()
    # Base type is QueryServiceMetricsListResponseType
    
    # Element metricDefinition ({http://schemas.nav.gov.hu/OSA/3.0/metrics}metricDefinition) inherited from {http://schemas.nav.gov.hu/OSA/3.0/metrics}QueryServiceMetricsListResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (QueryServiceMetricsResponseType):
    """A GET /queryServiceMetrics REST operáció válaszának root elementjeResponse root element of the GET /queryServiceMetrics REST operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 211, 2)
    _ElementMap = QueryServiceMetricsResponseType._ElementMap.copy()
    _AttributeMap = QueryServiceMetricsResponseType._AttributeMap.copy()
    # Base type is QueryServiceMetricsResponseType
    
    # Element result ({http://schemas.nav.gov.hu/OSA/3.0/metrics}result) inherited from {http://schemas.nav.gov.hu/OSA/3.0/metrics}QueryServiceMetricsResponseType
    
    # Element metricsLastUpdateTime ({http://schemas.nav.gov.hu/OSA/3.0/metrics}metricsLastUpdateTime) inherited from {http://schemas.nav.gov.hu/OSA/3.0/metrics}QueryServiceMetricsResponseType
    
    # Element metric ({http://schemas.nav.gov.hu/OSA/3.0/metrics}metric) inherited from {http://schemas.nav.gov.hu/OSA/3.0/metrics}QueryServiceMetricsResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


QueryServiceMetricsListResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryServiceMetricsListResponse'), CTD_ANON, documentation='A GET /queryServiceMetrics/list REST operáció válaszának root elementjeResponse root element of the GET /queryServiceMetrics/list REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 195, 1))
Namespace.addCategoryObject('elementBinding', QueryServiceMetricsListResponse.name().localName(), QueryServiceMetricsListResponse)

QueryServiceMetricsResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryServiceMetricsResponse'), CTD_ANON_, documentation='A GET /queryServiceMetrics REST operáció válaszának root elementjeResponse root element of the GET /queryServiceMetrics REST operation', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 206, 1))
Namespace.addCategoryObject('elementBinding', QueryServiceMetricsResponse.name().localName(), QueryServiceMetricsResponse)



MetricDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metricName'), _ImportedBinding_common.SimpleText200NotBlankType, scope=MetricDefinitionType, documentation="Metrika neveMetric's name", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 75, 3)))

MetricDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metricType'), MetricTypeType, scope=MetricDefinitionType, documentation="Metrika típusaMetric's type", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 81, 3)))

MetricDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metricDescription'), MetricDescriptionType, scope=MetricDefinitionType, documentation="Metrika leírásaMetric's description", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 87, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 87, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MetricDefinitionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricName')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 75, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MetricDefinitionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricType')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 81, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MetricDefinitionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricDescription')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 87, 3))
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
MetricDefinitionType._Automaton = _BuildAutomaton()




MetricDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), LanguageType, scope=MetricDescriptionType, documentation='Nyelv megnevezésLanguage naming', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 101, 3)))

MetricDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'localizedDescription'), _ImportedBinding_common.SimpleText512NotBlankType, scope=MetricDescriptionType, documentation='Lokalizált leírásLocalized description', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 107, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MetricDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 101, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MetricDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'localizedDescription')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 107, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MetricDescriptionType._Automaton = _BuildAutomaton_()




MetricType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metricDefinition'), MetricDefinitionType, scope=MetricType, documentation='Metrika definícióMetric definition', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 121, 3)))

MetricType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metricValues'), MetricValueType, scope=MetricType, documentation='Metrika értékekMetric values', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 127, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=60, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 127, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MetricType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricDefinition')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 121, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MetricType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricValues')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 127, 3))
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
MetricType._Automaton = _BuildAutomaton_2()




MetricValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), _ImportedBinding_common.GenericDecimalType, scope=MetricValueType, documentation="Metrika értékeMetric's value", location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 141, 3)))

MetricValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), _ImportedBinding_base.InvoiceTimestampType, scope=MetricValueType, documentation='Metrika értékének időpontja UTC időbenTime of metric value in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 147, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MetricValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 141, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MetricValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 147, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MetricValueType._Automaton = _BuildAutomaton_3()




QueryServiceMetricsListResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metricDefinition'), MetricDefinitionType, scope=QueryServiceMetricsListResponseType, documentation='Metrika definícióiMetric definitions', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 161, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 161, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryServiceMetricsListResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricDefinition')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 161, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
QueryServiceMetricsListResponseType._Automaton = _BuildAutomaton_4()




QueryServiceMetricsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), _ImportedBinding_common.BasicResultType, scope=QueryServiceMetricsResponseType, documentation='Alap válaszeredmény adatokBasic result data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 175, 3)))

QueryServiceMetricsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metricsLastUpdateTime'), _ImportedBinding_base.InvoiceTimestampType, scope=QueryServiceMetricsResponseType, documentation='A metrikák utolsó frissítésének időpontja UTC időbenLast update time of metrics in UTC time', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 181, 3)))

QueryServiceMetricsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metric'), MetricType, scope=QueryServiceMetricsResponseType, documentation='Metrika adataiMetric data', location=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 187, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 181, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 187, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryServiceMetricsResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 175, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryServiceMetricsResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricsLastUpdateTime')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 181, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QueryServiceMetricsResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metric')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 187, 3))
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
QueryServiceMetricsResponseType._Automaton = _BuildAutomaton_5()




def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 161, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricDefinition')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 161, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_6()




def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 181, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 187, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 175, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metricsLastUpdateTime')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 181, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metric')), pyxb.utils.utility.Location('/home/frappe/OSA_Schemas/v3/serviceMetrics.xsd', 187, 3))
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
CTD_ANON_._Automaton = _BuildAutomaton_7()

