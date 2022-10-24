import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AircraftType(GeneratedsSuper):
    """AircraftType -- Légi közlekedési eszköz
    Aircraft
    takeOffWeight -- Felszállási tömeg kilogrammban
    Take-off weight in kilogram
    airCargo -- Értéke true ha a jármű az ÁFA tv. 259. § 25. c) szerinti kivétel alá tartozik
    The value is true if the means of transport is exempt from VAT as per section 259 [25] (c)
    operationHours -- Repült órák száma
    Number of aviated hours

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, takeOffWeight=None, airCargo=None, operationHours=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.takeOffWeight = takeOffWeight
        self.validate_QuantityType(self.takeOffWeight)
        self.takeOffWeight_nsprefix_ = None
        self.airCargo = airCargo
        self.airCargo_nsprefix_ = "xs"
        self.operationHours = operationHours
        self.validate_QuantityType(self.operationHours)
        self.operationHours_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AircraftType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AircraftType.subclass:
            return AircraftType.subclass(*args_, **kwargs_)
        else:
            return AircraftType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_takeOffWeight(self):
        return self.takeOffWeight
    def set_takeOffWeight(self, takeOffWeight):
        self.takeOffWeight = takeOffWeight
    def get_airCargo(self):
        return self.airCargo
    def set_airCargo(self, airCargo):
        self.airCargo = airCargo
    def get_operationHours(self):
        return self.operationHours
    def set_operationHours(self, operationHours):
        self.operationHours = operationHours
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
            self.takeOffWeight is not None or
            self.airCargo is not None or
            self.operationHours is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='AircraftType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AircraftType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AircraftType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AircraftType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AircraftType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AircraftType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='AircraftType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.takeOffWeight is not None:
            namespaceprefix_ = self.takeOffWeight_nsprefix_ + ':' if (UseCapturedNS_ and self.takeOffWeight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stakeOffWeight>%s</%stakeOffWeight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.takeOffWeight, input_name='takeOffWeight'), namespaceprefix_ , eol_))
        if self.airCargo is not None:
            namespaceprefix_ = self.airCargo_nsprefix_ + ':' if (UseCapturedNS_ and self.airCargo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sairCargo>%s</%sairCargo>%s' % (namespaceprefix_ , self.gds_format_boolean(self.airCargo, input_name='airCargo'), namespaceprefix_ , eol_))
        if self.operationHours is not None:
            namespaceprefix_ = self.operationHours_nsprefix_ + ':' if (UseCapturedNS_ and self.operationHours_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soperationHours>%s</%soperationHours>%s' % (namespaceprefix_ , self.gds_format_decimal(self.operationHours, input_name='operationHours'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AircraftType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.takeOffWeight is not None:
            takeOffWeight_ = self.takeOffWeight
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}takeOffWeight').text = self.gds_format_decimal(takeOffWeight_)
        if self.airCargo is not None:
            airCargo_ = self.airCargo
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}airCargo').text = self.gds_format_boolean(airCargo_)
        if self.operationHours is not None:
            operationHours_ = self.operationHours
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}operationHours').text = self.gds_format_decimal(operationHours_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AircraftType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.takeOffWeight is not None:
            showIndent(outfile, level)
            outfile.write('takeOffWeight=%f,\n' % self.takeOffWeight)
        if self.airCargo is not None:
            showIndent(outfile, level)
            outfile.write('airCargo=%s,\n' % self.airCargo)
        if self.operationHours is not None:
            showIndent(outfile, level)
            outfile.write('operationHours=%f,\n' % self.operationHours)
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
        if nodeName_ == 'takeOffWeight' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'takeOffWeight')
            fval_ = self.gds_validate_decimal(fval_, node, 'takeOffWeight')
            self.takeOffWeight = fval_
            self.takeOffWeight_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.takeOffWeight)
        elif nodeName_ == 'airCargo':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'airCargo')
            ival_ = self.gds_validate_boolean(ival_, node, 'airCargo')
            self.airCargo = ival_
            self.airCargo_nsprefix_ = child_.prefix
        elif nodeName_ == 'operationHours' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'operationHours')
            fval_ = self.gds_validate_decimal(fval_, node, 'operationHours')
            self.operationHours = fval_
            self.operationHours_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.operationHours)
