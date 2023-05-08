from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, Validate_simpletypes_, encode_str_2_3, quote_xml, \
    quote_python

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class SimpleAddressType(GeneratedsSuper):
    """SimpleAddressType -- Egyszerű címtípus
    Simple address_list type
    countryCode -- Az országkód az ISO 3166 alpha-2 szabvány szerint
                ISO 3166 alpha-2 country code
    region -- Tartomány kódja (amennyiben értelmezhető az adott országban) az ISO 3166-2 alpha 2 szabvány szerint
                ISO 3166 alpha-2 province code (if appropriate in a given country)
    postalCode -- Irányítószám (amennyiben nem értelmezhető, 0000 értékkel kell kitölteni)
                ZIP code (If can not be interpreted, need to be filled "0000")
    city -- Település
                Settlement
    additionalAddressDetail -- További címadatok (pl. közterület neve és jellege, házszám, emelet, ajtó, helyrajzi szám, stb.)
                Further address_list data (name and type of public place, house number, floor, door, lot number, etc.)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, countryCode=None, region=None, postalCode=None, city=None, additionalAddressDetail=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.countryCode = countryCode
        self.validate_CountryCodeType(self.countryCode)
        self.countryCode_nsprefix_ = "common"
        self.region = region
        self.validate_SimpleText50NotBlankType(self.region)
        self.region_nsprefix_ = "common"
        self.postalCode = postalCode
        self.validate_PostalCodeType(self.postalCode)
        self.postalCode_nsprefix_ = "common"
        self.city = city
        self.validate_SimpleText255NotBlankType(self.city)
        self.city_nsprefix_ = "common"
        self.additionalAddressDetail = additionalAddressDetail
        self.validate_SimpleText255NotBlankType(self.additionalAddressDetail)
        self.additionalAddressDetail_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SimpleAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SimpleAddressType.subclass:
            return SimpleAddressType.subclass(*args_, **kwargs_)
        else:
            return SimpleAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_countryCode(self):
        return self.countryCode
    def set_countryCode(self, countryCode):
        self.countryCode = countryCode
    def get_region(self):
        return self.region
    def set_region(self, region):
        self.region = region
    def get_postalCode(self):
        return self.postalCode
    def set_postalCode(self, postalCode):
        self.postalCode = postalCode
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_additionalAddressDetail(self):
        return self.additionalAddressDetail
    def set_additionalAddressDetail(self, additionalAddressDetail):
        self.additionalAddressDetail = additionalAddressDetail
    def validate_CountryCodeType(self, value):
        result = True
        # Validate type CountryCodeType, a restriction on AtomicStringType2.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on CountryCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CountryCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CountryCodeType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CountryCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CountryCodeType_patterns_, ))
                result = False
        return result
    validate_CountryCodeType_patterns_ = [['^([A-Z]{2})$']]
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
    def validate_PostalCodeType(self, value):
        result = True
        # Validate type PostalCodeType, a restriction on AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PostalCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PostalCodeType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PostalCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PostalCodeType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_PostalCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PostalCodeType_patterns_, ))
                result = False
        return result
    validate_PostalCodeType_patterns_ = [['^([A-Z0-9][A-Z0-9\\s\\-]{1,8}[A-Z0-9])$']]
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
    def _hasContent(self):
        if (
            self.countryCode is not None or
            self.region is not None or
            self.postalCode is not None or
            self.city is not None or
            self.additionalAddressDetail is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='SimpleAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SimpleAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SimpleAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SimpleAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SimpleAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SimpleAddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='SimpleAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.countryCode is not None:
            namespaceprefix_ = self.countryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.countryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountryCode>%s</%scountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.countryCode), input_name='countryCode')), namespaceprefix_ , eol_))
        if self.region is not None:
            namespaceprefix_ = self.region_nsprefix_ + ':' if (UseCapturedNS_ and self.region_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sregion>%s</%sregion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.region), input_name='region')), namespaceprefix_ , eol_))
        if self.postalCode is not None:
            namespaceprefix_ = self.postalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.postalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostalCode>%s</%spostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postalCode), input_name='postalCode')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.additionalAddressDetail is not None:
            namespaceprefix_ = self.additionalAddressDetail_nsprefix_ + ':' if (UseCapturedNS_ and self.additionalAddressDetail_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadditionalAddressDetail>%s</%sadditionalAddressDetail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.additionalAddressDetail), input_name='additionalAddressDetail')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SimpleAddressType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/base}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/base}' + name_, nsmap=nsmap_)
        if self.countryCode is not None:
            countryCode_ = self.countryCode
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}countryCode').text = self.gds_format_string(countryCode_)
        if self.region is not None:
            region_ = self.region
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}region').text = self.gds_format_string(region_)
        if self.postalCode is not None:
            postalCode_ = self.postalCode
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}postalCode').text = self.gds_format_string(postalCode_)
        if self.city is not None:
            city_ = self.city
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}city').text = self.gds_format_string(city_)
        if self.additionalAddressDetail is not None:
            additionalAddressDetail_ = self.additionalAddressDetail
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/base}additionalAddressDetail').text = self.gds_format_string(additionalAddressDetail_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SimpleAddressType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.countryCode is not None:
            showIndent(outfile, level)
            outfile.write('countryCode=%s,\n' % self.gds_encode(quote_python(self.countryCode)))
        if self.region is not None:
            showIndent(outfile, level)
            outfile.write('region=%s,\n' % self.gds_encode(quote_python(self.region)))
        if self.postalCode is not None:
            showIndent(outfile, level)
            outfile.write('postalCode=%s,\n' % self.gds_encode(quote_python(self.postalCode)))
        if self.city is not None:
            showIndent(outfile, level)
            outfile.write('city=%s,\n' % self.gds_encode(quote_python(self.city)))
        if self.additionalAddressDetail is not None:
            showIndent(outfile, level)
            outfile.write('additionalAddressDetail=%s,\n' % self.gds_encode(quote_python(self.additionalAddressDetail)))
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
        if nodeName_ == 'countryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCode')
            value_ = self.gds_validate_string(value_, node, 'countryCode')
            self.countryCode = value_
            self.countryCode_nsprefix_ = child_.prefix
            # validate type CountryCodeType
            self.validate_CountryCodeType(self.countryCode)
        elif nodeName_ == 'region':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'region')
            value_ = self.gds_validate_string(value_, node, 'region')
            self.region = value_
            self.region_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.region)
        elif nodeName_ == 'postalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postalCode')
            value_ = self.gds_validate_string(value_, node, 'postalCode')
            self.postalCode = value_
            self.postalCode_nsprefix_ = child_.prefix
            # validate type PostalCodeType
            self.validate_PostalCodeType(self.postalCode)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.city)
        elif nodeName_ == 'additionalAddressDetail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'additionalAddressDetail')
            value_ = self.gds_validate_string(value_, node, 'additionalAddressDetail')
            self.additionalAddressDetail = value_
            self.additionalAddressDetail_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.additionalAddressDetail)
