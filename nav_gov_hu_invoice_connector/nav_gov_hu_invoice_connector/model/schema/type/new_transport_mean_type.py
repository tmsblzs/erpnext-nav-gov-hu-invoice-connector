import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.aircraft_type import AircraftType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vehicle_type import VehicleType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vessel_type import VesselType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class NewTransportMeanType(GeneratedsSuper):
    """NewTransportMeanType -- Új közlekedési eszközértékesítés ÁFA tv. 89 § ill. 169 § o)
    Supply of new means of transport - section 89 § and 169 (o) of the VAT law
    brand -- Gyártmány/típus
    Product / type
    serialNum -- Alvázszám/gyári szám/Gyártási szám
    Chassis number / serial number / product number
    engineNum -- Motorszám
    Engine number
    firstEntryIntoService -- Első forgalomba helyezés időpontja
    First entry into service
    vehicle -- Szárazföldi közlekedési eszköz további adatai
    Other data in relation to motorised land vehicle
    vessel -- Vízi jármű adatai
    Data of vessel
    aircraft -- Légi közlekedési eszköz
    Aircraft

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, brand=None, serialNum=None, engineNum=None, firstEntryIntoService=None, vehicle=None, vessel=None, aircraft=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.brand = brand
        self.validate_SimpleText50NotBlankType(self.brand)
        self.brand_nsprefix_ = "common"
        self.serialNum = serialNum
        self.validate_SimpleText255NotBlankType(self.serialNum)
        self.serialNum_nsprefix_ = "common"
        self.engineNum = engineNum
        self.validate_SimpleText255NotBlankType(self.engineNum)
        self.engineNum_nsprefix_ = "common"
        if isinstance(firstEntryIntoService, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(firstEntryIntoService, '%Y-%m-%d').date()
        else:
            initvalue_ = firstEntryIntoService
        self.firstEntryIntoService = initvalue_
        self.firstEntryIntoService_nsprefix_ = "base"
        self.vehicle = vehicle
        self.vehicle_nsprefix_ = None
        self.vessel = vessel
        self.vessel_nsprefix_ = None
        self.aircraft = aircraft
        self.aircraft_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NewTransportMeanType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NewTransportMeanType.subclass:
            return NewTransportMeanType.subclass(*args_, **kwargs_)
        else:
            return NewTransportMeanType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_brand(self):
        return self.brand
    def set_brand(self, brand):
        self.brand = brand
    def get_serialNum(self):
        return self.serialNum
    def set_serialNum(self, serialNum):
        self.serialNum = serialNum
    def get_engineNum(self):
        return self.engineNum
    def set_engineNum(self, engineNum):
        self.engineNum = engineNum
    def get_firstEntryIntoService(self):
        return self.firstEntryIntoService
    def set_firstEntryIntoService(self, firstEntryIntoService):
        self.firstEntryIntoService = firstEntryIntoService
    def get_vehicle(self):
        return self.vehicle
    def set_vehicle(self, vehicle):
        self.vehicle = vehicle
    def get_vessel(self):
        return self.vessel
    def set_vessel(self, vessel):
        self.vessel = vessel
    def get_aircraft(self):
        return self.aircraft
    def set_aircraft(self, aircraft):
        self.aircraft = aircraft
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
    def validate_SimpleText255NotBlankType(self, value):
        result = True
        # Validate type SimpleText255NotBlankType, a restriction on AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText255NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText255NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText255NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText255NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText255NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
    def _hasContent(self):
        if (
            self.brand is not None or
            self.serialNum is not None or
            self.engineNum is not None or
            self.firstEntryIntoService is not None or
            self.vehicle is not None or
            self.vessel is not None or
            self.aircraft is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='NewTransportMeanType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NewTransportMeanType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NewTransportMeanType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NewTransportMeanType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NewTransportMeanType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NewTransportMeanType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='NewTransportMeanType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.brand is not None:
            namespaceprefix_ = self.brand_nsprefix_ + ':' if (UseCapturedNS_ and self.brand_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbrand>%s</%sbrand>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.brand), input_name='brand')), namespaceprefix_ , eol_))
        if self.serialNum is not None:
            namespaceprefix_ = self.serialNum_nsprefix_ + ':' if (UseCapturedNS_ and self.serialNum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sserialNum>%s</%sserialNum>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.serialNum), input_name='serialNum')), namespaceprefix_ , eol_))
        if self.engineNum is not None:
            namespaceprefix_ = self.engineNum_nsprefix_ + ':' if (UseCapturedNS_ and self.engineNum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sengineNum>%s</%sengineNum>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.engineNum), input_name='engineNum')), namespaceprefix_ , eol_))
        if self.firstEntryIntoService is not None:
            namespaceprefix_ = self.firstEntryIntoService_nsprefix_ + ':' if (UseCapturedNS_ and self.firstEntryIntoService_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstEntryIntoService>%s</%sfirstEntryIntoService>%s' % (namespaceprefix_ , self.gds_format_date(self.firstEntryIntoService, input_name='firstEntryIntoService'), namespaceprefix_ , eol_))
        if self.vehicle is not None:
            namespaceprefix_ = self.vehicle_nsprefix_ + ':' if (UseCapturedNS_ and self.vehicle_nsprefix_) else ''
            self.vehicle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vehicle', pretty_print=pretty_print)
        if self.vessel is not None:
            namespaceprefix_ = self.vessel_nsprefix_ + ':' if (UseCapturedNS_ and self.vessel_nsprefix_) else ''
            self.vessel.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vessel', pretty_print=pretty_print)
        if self.aircraft is not None:
            namespaceprefix_ = self.aircraft_nsprefix_ + ':' if (UseCapturedNS_ and self.aircraft_nsprefix_) else ''
            self.aircraft.export(outfile, level, namespaceprefix_, namespacedef_='', name_='aircraft', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='NewTransportMeanType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.brand is not None:
            brand_ = self.brand
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}brand').text = self.gds_format_string(brand_)
        if self.serialNum is not None:
            serialNum_ = self.serialNum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}serialNum').text = self.gds_format_string(serialNum_)
        if self.engineNum is not None:
            engineNum_ = self.engineNum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}engineNum').text = self.gds_format_string(engineNum_)
        if self.firstEntryIntoService is not None:
            firstEntryIntoService_ = self.firstEntryIntoService
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}firstEntryIntoService').text = self.gds_format_date(firstEntryIntoService_)
        if self.vehicle is not None:
            vehicle_ = self.vehicle
            vehicle_.to_etree(element, name_='vehicle', mapping_=mapping_, nsmap_=nsmap_)
        if self.vessel is not None:
            vessel_ = self.vessel
            vessel_.to_etree(element, name_='vessel', mapping_=mapping_, nsmap_=nsmap_)
        if self.aircraft is not None:
            aircraft_ = self.aircraft
            aircraft_.to_etree(element, name_='aircraft', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='NewTransportMeanType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.brand is not None:
            showIndent(outfile, level)
            outfile.write('brand=%s,\n' % self.gds_encode(quote_python(self.brand)))
        if self.serialNum is not None:
            showIndent(outfile, level)
            outfile.write('serialNum=%s,\n' % self.gds_encode(quote_python(self.serialNum)))
        if self.engineNum is not None:
            showIndent(outfile, level)
            outfile.write('engineNum=%s,\n' % self.gds_encode(quote_python(self.engineNum)))
        if self.firstEntryIntoService is not None:
            showIndent(outfile, level)
            outfile.write('firstEntryIntoService=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.firstEntryIntoService, input_name='firstEntryIntoService'))
        if self.vehicle is not None:
            showIndent(outfile, level)
            outfile.write('vehicle=model_.VehicleType(\n')
            self.vehicle.exportLiteral(outfile, level, name_='vehicle')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vessel is not None:
            showIndent(outfile, level)
            outfile.write('vessel=model_.VesselType(\n')
            self.vessel.exportLiteral(outfile, level, name_='vessel')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.aircraft is not None:
            showIndent(outfile, level)
            outfile.write('aircraft=model_.AircraftType(\n')
            self.aircraft.exportLiteral(outfile, level, name_='aircraft')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'brand':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'brand')
            value_ = self.gds_validate_string(value_, node, 'brand')
            self.brand = value_
            self.brand_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.brand)
        elif nodeName_ == 'serialNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'serialNum')
            value_ = self.gds_validate_string(value_, node, 'serialNum')
            self.serialNum = value_
            self.serialNum_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.serialNum)
        elif nodeName_ == 'engineNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'engineNum')
            value_ = self.gds_validate_string(value_, node, 'engineNum')
            self.engineNum = value_
            self.engineNum_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.engineNum)
        elif nodeName_ == 'firstEntryIntoService':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.firstEntryIntoService = dval_
            self.firstEntryIntoService_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.firstEntryIntoService)
        elif nodeName_ == 'vehicle':
            obj_ = VehicleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vehicle = obj_
            obj_.original_tagname_ = 'vehicle'
        elif nodeName_ == 'vessel':
            obj_ = VesselType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vessel = obj_
            obj_.original_tagname_ = 'vessel'
        elif nodeName_ == 'aircraft':
            obj_ = AircraftType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.aircraft = obj_
            obj_.original_tagname_ = 'aircraft'
