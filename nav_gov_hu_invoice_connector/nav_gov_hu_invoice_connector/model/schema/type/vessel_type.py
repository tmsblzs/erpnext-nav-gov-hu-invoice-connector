import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class VesselType(GeneratedsSuper):
    """VesselType -- Vízi jármű adatai
    Data of vessel
    length -- Hajó hossza méterben
    Length of hull in metre
    activityReferred -- Értéke true, ha a jármű az ÁFA tv. 259. § 25. b) szerinti kivétel alá tartozik
    The value is true if the means of transport is exempt from VAT as per section 259 [25] (b)
    sailedHours -- Hajózottórák száma
    Number of sailed hours

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, activityReferred=None, sailedHours=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = length
        self.validate_QuantityType(self.length)
        self.length_nsprefix_ = None
        self.activityReferred = activityReferred
        self.activityReferred_nsprefix_ = "xs"
        self.sailedHours = sailedHours
        self.validate_QuantityType(self.sailedHours)
        self.sailedHours_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VesselType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VesselType.subclass:
            return VesselType.subclass(*args_, **kwargs_)
        else:
            return VesselType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def get_activityReferred(self):
        return self.activityReferred
    def set_activityReferred(self, activityReferred):
        self.activityReferred = activityReferred
    def get_sailedHours(self):
        return self.sailedHours
    def set_sailedHours(self, sailedHours):
        self.sailedHours = sailedHours
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.length is not None or
            self.activityReferred is not None or
            self.sailedHours is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VesselType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VesselType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VesselType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VesselType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VesselType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VesselType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VesselType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.length is not None:
            namespaceprefix_ = self.length_nsprefix_ + ':' if (UseCapturedNS_ and self.length_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slength>%s</%slength>%s' % (namespaceprefix_ , self.gds_format_decimal(self.length, input_name='length'), namespaceprefix_ , eol_))
        if self.activityReferred is not None:
            namespaceprefix_ = self.activityReferred_nsprefix_ + ':' if (UseCapturedNS_ and self.activityReferred_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sactivityReferred>%s</%sactivityReferred>%s' % (namespaceprefix_ , self.gds_format_boolean(self.activityReferred, input_name='activityReferred'), namespaceprefix_ , eol_))
        if self.sailedHours is not None:
            namespaceprefix_ = self.sailedHours_nsprefix_ + ':' if (UseCapturedNS_ and self.sailedHours_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssailedHours>%s</%ssailedHours>%s' % (namespaceprefix_ , self.gds_format_decimal(self.sailedHours, input_name='sailedHours'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VesselType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.length is not None:
            length_ = self.length
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}length').text = self.gds_format_decimal(length_)
        if self.activityReferred is not None:
            activityReferred_ = self.activityReferred
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}activityReferred').text = self.gds_format_boolean(activityReferred_)
        if self.sailedHours is not None:
            sailedHours_ = self.sailedHours
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}sailedHours').text = self.gds_format_decimal(sailedHours_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VesselType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.length is not None:
            showIndent(outfile, level)
            outfile.write('length=%f,\n' % self.length)
        if self.activityReferred is not None:
            showIndent(outfile, level)
            outfile.write('activityReferred=%s,\n' % self.activityReferred)
        if self.sailedHours is not None:
            showIndent(outfile, level)
            outfile.write('sailedHours=%f,\n' % self.sailedHours)
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
        if nodeName_ == 'length' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'length')
            fval_ = self.gds_validate_decimal(fval_, node, 'length')
            self.length = fval_
            self.length_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.length)
        elif nodeName_ == 'activityReferred':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'activityReferred')
            ival_ = self.gds_validate_boolean(ival_, node, 'activityReferred')
            self.activityReferred = ival_
            self.activityReferred_nsprefix_ = child_.prefix
        elif nodeName_ == 'sailedHours' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'sailedHours')
            fval_ = self.gds_validate_decimal(fval_, node, 'sailedHours')
            self.sailedHours = fval_
            self.sailedHours_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.sailedHours)
