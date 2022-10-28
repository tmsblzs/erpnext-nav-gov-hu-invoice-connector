import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.simple_address_type import \
    SimpleAddressType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class DieselOilPurchaseType(GeneratedsSuper):
    """DieselOilPurchaseType -- Gázolaj adózottan történő beszerzésének adatai
    –
    45/2016 (XI. 29.) NGM rendelet 75.
    §
    (1) a)
    Data of gas oil acquisition after taxation
    –
    point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)
    purchaseLocation -- Gázolaj beszerzés helye
    Place of purchase of the gas oil
    purchaseDate -- Gázolaj beszerzés dátuma
    Date of purchase of gas oil
    vehicleRegistrationNumber -- Kereskedelmi jármű forgalmi rendszáma (csak betűkés számok)
    Registration number of vehicle (letters and numbers only)
    dieselOilQuantity -- Gépi bérmunka-szolgáltatás során felhasznált gázolaj mennyisége literben
    –
    Jöt. 117. § (2) Fordítandó
    helyett: Quantity of diesel oil used for contract work and machinery hire service in liter
    –
    Act LXVIII of 2016 on Excise Tax section 117 (2)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, purchaseLocation=None, purchaseDate=None, vehicleRegistrationNumber=None, dieselOilQuantity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.purchaseLocation = purchaseLocation
        self.purchaseLocation_nsprefix_ = "base"
        if isinstance(purchaseDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(purchaseDate, '%Y-%m-%d').date()
        else:
            initvalue_ = purchaseDate
        self.purchaseDate = initvalue_
        self.purchaseDate_nsprefix_ = "base"
        self.vehicleRegistrationNumber = vehicleRegistrationNumber
        self.validate_PlateNumberType(self.vehicleRegistrationNumber)
        self.vehicleRegistrationNumber_nsprefix_ = "common"
        self.dieselOilQuantity = dieselOilQuantity
        self.validate_QuantityType(self.dieselOilQuantity)
        self.dieselOilQuantity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DieselOilPurchaseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DieselOilPurchaseType.subclass:
            return DieselOilPurchaseType.subclass(*args_, **kwargs_)
        else:
            return DieselOilPurchaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_purchaseLocation(self):
        return self.purchaseLocation
    def set_purchaseLocation(self, purchaseLocation):
        self.purchaseLocation = purchaseLocation
    def get_purchaseDate(self):
        return self.purchaseDate
    def set_purchaseDate(self, purchaseDate):
        self.purchaseDate = purchaseDate
    def get_vehicleRegistrationNumber(self):
        return self.vehicleRegistrationNumber
    def set_vehicleRegistrationNumber(self, vehicleRegistrationNumber):
        self.vehicleRegistrationNumber = vehicleRegistrationNumber
    def get_dieselOilQuantity(self):
        return self.dieselOilQuantity
    def set_dieselOilQuantity(self, dieselOilQuantity):
        self.dieselOilQuantity = dieselOilQuantity
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
    def validate_PlateNumberType(self, value):
        result = True
        # Validate type PlateNumberType, a restriction on AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PlateNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PlateNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PlateNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PlateNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_PlateNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PlateNumberType_patterns_, ))
                result = False
        return result
    validate_PlateNumberType_patterns_ = [['^([A-Z0-9ÖŐÜŰ]{2,30})$']]
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
            self.purchaseLocation is not None or
            self.purchaseDate is not None or
            self.vehicleRegistrationNumber is not None or
            self.dieselOilQuantity is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DieselOilPurchaseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DieselOilPurchaseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DieselOilPurchaseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DieselOilPurchaseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DieselOilPurchaseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DieselOilPurchaseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DieselOilPurchaseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.purchaseLocation is not None:
            namespaceprefix_ = self.purchaseLocation_nsprefix_ + ':' if (UseCapturedNS_ and self.purchaseLocation_nsprefix_) else ''
            self.purchaseLocation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='purchaseLocation', pretty_print=pretty_print)
        if self.purchaseDate is not None:
            namespaceprefix_ = self.purchaseDate_nsprefix_ + ':' if (UseCapturedNS_ and self.purchaseDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spurchaseDate>%s</%spurchaseDate>%s' % (namespaceprefix_ , self.gds_format_date(self.purchaseDate, input_name='purchaseDate'), namespaceprefix_ , eol_))
        if self.vehicleRegistrationNumber is not None:
            namespaceprefix_ = self.vehicleRegistrationNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.vehicleRegistrationNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svehicleRegistrationNumber>%s</%svehicleRegistrationNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.vehicleRegistrationNumber), input_name='vehicleRegistrationNumber')), namespaceprefix_ , eol_))
        if self.dieselOilQuantity is not None:
            namespaceprefix_ = self.dieselOilQuantity_nsprefix_ + ':' if (UseCapturedNS_ and self.dieselOilQuantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdieselOilQuantity>%s</%sdieselOilQuantity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.dieselOilQuantity, input_name='dieselOilQuantity'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='DieselOilPurchaseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.purchaseLocation is not None:
            purchaseLocation_ = self.purchaseLocation
            purchaseLocation_.to_etree(element, name_='purchaseLocation', mapping_=mapping_, nsmap_=nsmap_)
        if self.purchaseDate is not None:
            purchaseDate_ = self.purchaseDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}purchaseDate').text = self.gds_format_date(purchaseDate_)
        if self.vehicleRegistrationNumber is not None:
            vehicleRegistrationNumber_ = self.vehicleRegistrationNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vehicleRegistrationNumber').text = self.gds_format_string(vehicleRegistrationNumber_)
        if self.dieselOilQuantity is not None:
            dieselOilQuantity_ = self.dieselOilQuantity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}dieselOilQuantity').text = self.gds_format_decimal(dieselOilQuantity_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DieselOilPurchaseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.purchaseLocation is not None:
            showIndent(outfile, level)
            outfile.write('purchaseLocation=model_.SimpleAddressType(\n')
            self.purchaseLocation.exportLiteral(outfile, level, name_='purchaseLocation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.purchaseDate is not None:
            showIndent(outfile, level)
            outfile.write('purchaseDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.purchaseDate, input_name='purchaseDate'))
        if self.vehicleRegistrationNumber is not None:
            showIndent(outfile, level)
            outfile.write('vehicleRegistrationNumber=%s,\n' % self.gds_encode(quote_python(self.vehicleRegistrationNumber)))
        if self.dieselOilQuantity is not None:
            showIndent(outfile, level)
            outfile.write('dieselOilQuantity=%f,\n' % self.dieselOilQuantity)
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
        if nodeName_ == 'purchaseLocation':
            obj_ = SimpleAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.purchaseLocation = obj_
            obj_.original_tagname_ = 'purchaseLocation'
        elif nodeName_ == 'purchaseDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.purchaseDate = dval_
            self.purchaseDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.purchaseDate)
        elif nodeName_ == 'vehicleRegistrationNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'vehicleRegistrationNumber')
            value_ = self.gds_validate_string(value_, node, 'vehicleRegistrationNumber')
            self.vehicleRegistrationNumber = value_
            self.vehicleRegistrationNumber_nsprefix_ = child_.prefix
            # validate type PlateNumberType
            self.validate_PlateNumberType(self.vehicleRegistrationNumber)
        elif nodeName_ == 'dieselOilQuantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'dieselOilQuantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'dieselOilQuantity')
            self.dieselOilQuantity = fval_
            self.dieselOilQuantity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.dieselOilQuantity)
