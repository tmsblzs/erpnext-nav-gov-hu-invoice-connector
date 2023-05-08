import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.tax_number_type import TaxNumberType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.taxpayer_address_list_type import \
    TaxpayerAddressListType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class TaxpayerDataType(GeneratedsSuper):
    """TaxpayerDataType -- Az adózó lekérdezés válasz adatai
    Response data of the taxpayer query
    taxpayerName -- Az adózó neve
    Name of the taxpayer
    taxpayerShortName -- Az adózó rövidített neve
    Shortened name of the taxpayer
    taxNumberDetail -- Az adószám részletes adatai
    Detailed data of the tax number
    incorporation -- Gazdasági típus
    Incorporation type
    vatGroupMembership -- Az adózó ÁFA csoport tagsága
    VAT group membership of the taxpayer
    taxpayerAddressList -- Adózói cím lista típus
    Taxpayer address_list list type

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, taxpayerName=None, taxpayerShortName=None, taxNumberDetail=None, incorporation=None, vatGroupMembership=None, taxpayerAddressList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.taxpayerName = taxpayerName
        self.validate_SimpleText512NotBlankType(self.taxpayerName)
        self.taxpayerName_nsprefix_ = "common"
        self.taxpayerShortName = taxpayerShortName
        self.validate_SimpleText200NotBlankType(self.taxpayerShortName)
        self.taxpayerShortName_nsprefix_ = "common"
        self.taxNumberDetail = taxNumberDetail
        self.taxNumberDetail_nsprefix_ = "base"
        self.incorporation = incorporation
        self.validate_IncorporationType(self.incorporation)
        self.incorporation_nsprefix_ = None
        self.vatGroupMembership = vatGroupMembership
        self.validate_TaxpayerIdType(self.vatGroupMembership)
        self.vatGroupMembership_nsprefix_ = "common"
        self.taxpayerAddressList = taxpayerAddressList
        self.taxpayerAddressList_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TaxpayerDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TaxpayerDataType.subclass:
            return TaxpayerDataType.subclass(*args_, **kwargs_)
        else:
            return TaxpayerDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_taxpayerName(self):
        return self.taxpayerName
    def set_taxpayerName(self, taxpayerName):
        self.taxpayerName = taxpayerName
    def get_taxpayerShortName(self):
        return self.taxpayerShortName
    def set_taxpayerShortName(self, taxpayerShortName):
        self.taxpayerShortName = taxpayerShortName
    def get_taxNumberDetail(self):
        return self.taxNumberDetail
    def set_taxNumberDetail(self, taxNumberDetail):
        self.taxNumberDetail = taxNumberDetail
    def get_incorporation(self):
        return self.incorporation
    def set_incorporation(self, incorporation):
        self.incorporation = incorporation
    def get_vatGroupMembership(self):
        return self.vatGroupMembership
    def set_vatGroupMembership(self, vatGroupMembership):
        self.vatGroupMembership = vatGroupMembership
    def get_taxpayerAddressList(self):
        return self.taxpayerAddressList
    def set_taxpayerAddressList(self, taxpayerAddressList):
        self.taxpayerAddressList = taxpayerAddressList
    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_SimpleText200NotBlankType(self, value):
        result = True
        # Validate type SimpleText200NotBlankType, a restriction on AtomicStringType200.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText200NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText200NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText200NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText200NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText200NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_IncorporationType(self, value):
        result = True
        # Validate type IncorporationType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['ORGANIZATION', 'SELF_EMPLOYED', 'TAXABLE_PERSON']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on IncorporationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on IncorporationType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on IncorporationType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_TaxpayerIdType(self, value):
        result = True
        # Validate type TaxpayerIdType, a restriction on AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TaxpayerIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TaxpayerIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TaxpayerIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TaxpayerIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TaxpayerIdType_patterns_, ))
                result = False
        return result
    validate_TaxpayerIdType_patterns_ = [['^([0-9]{8})$']]
    def _hasContent(self):
        if (
            self.taxpayerName is not None or
            self.taxpayerShortName is not None or
            self.taxNumberDetail is not None or
            self.incorporation is not None or
            self.vatGroupMembership is not None or
            self.taxpayerAddressList is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='TaxpayerDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TaxpayerDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TaxpayerDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TaxpayerDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TaxpayerDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TaxpayerDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='TaxpayerDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.taxpayerName is not None:
            namespaceprefix_ = self.taxpayerName_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxpayerName>%s</%staxpayerName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxpayerName), input_name='taxpayerName')), namespaceprefix_ , eol_))
        if self.taxpayerShortName is not None:
            namespaceprefix_ = self.taxpayerShortName_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerShortName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxpayerShortName>%s</%staxpayerShortName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxpayerShortName), input_name='taxpayerShortName')), namespaceprefix_ , eol_))
        if self.taxNumberDetail is not None:
            namespaceprefix_ = self.taxNumberDetail_nsprefix_ + ':' if (UseCapturedNS_ and self.taxNumberDetail_nsprefix_) else ''
            self.taxNumberDetail.export(outfile, level, namespaceprefix_, namespacedef_='', name_='taxNumberDetail', pretty_print=pretty_print)
        if self.incorporation is not None:
            namespaceprefix_ = self.incorporation_nsprefix_ + ':' if (UseCapturedNS_ and self.incorporation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sincorporation>%s</%sincorporation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.incorporation), input_name='incorporation')), namespaceprefix_ , eol_))
        if self.vatGroupMembership is not None:
            namespaceprefix_ = self.vatGroupMembership_nsprefix_ + ':' if (UseCapturedNS_ and self.vatGroupMembership_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatGroupMembership>%s</%svatGroupMembership>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.vatGroupMembership), input_name='vatGroupMembership')), namespaceprefix_ , eol_))
        if self.taxpayerAddressList is not None:
            namespaceprefix_ = self.taxpayerAddressList_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerAddressList_nsprefix_) else ''
            self.taxpayerAddressList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='taxpayerAddressList', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='TaxpayerDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.taxpayerName is not None:
            taxpayerName_ = self.taxpayerName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerName').text = self.gds_format_string(taxpayerName_)
        if self.taxpayerShortName is not None:
            taxpayerShortName_ = self.taxpayerShortName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerShortName').text = self.gds_format_string(taxpayerShortName_)
        if self.taxNumberDetail is not None:
            taxNumberDetail_ = self.taxNumberDetail
            taxNumberDetail_.to_etree(element, name_='taxNumberDetail', mapping_=mapping_, nsmap_=nsmap_)
        if self.incorporation is not None:
            incorporation_ = self.incorporation
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}incorporation').text = self.gds_format_string(incorporation_)
        if self.vatGroupMembership is not None:
            vatGroupMembership_ = self.vatGroupMembership
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}vatGroupMembership').text = self.gds_format_string(vatGroupMembership_)
        if self.taxpayerAddressList is not None:
            taxpayerAddressList_ = self.taxpayerAddressList
            taxpayerAddressList_.to_etree(element, name_='taxpayerAddressList', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TaxpayerDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.taxpayerName is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerName=%s,\n' % self.gds_encode(quote_python(self.taxpayerName)))
        if self.taxpayerShortName is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerShortName=%s,\n' % self.gds_encode(quote_python(self.taxpayerShortName)))
        if self.taxNumberDetail is not None:
            showIndent(outfile, level)
            outfile.write('taxNumberDetail=model_.TaxNumberType(\n')
            self.taxNumberDetail.exportLiteral(outfile, level, name_='taxNumberDetail')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.incorporation is not None:
            showIndent(outfile, level)
            outfile.write('incorporation=%s,\n' % self.gds_encode(quote_python(self.incorporation)))
        if self.vatGroupMembership is not None:
            showIndent(outfile, level)
            outfile.write('vatGroupMembership=%s,\n' % self.gds_encode(quote_python(self.vatGroupMembership)))
        if self.taxpayerAddressList is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerAddressList=model_.TaxpayerAddressListType(\n')
            self.taxpayerAddressList.exportLiteral(outfile, level, name_='taxpayerAddressList')
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
        if nodeName_ == 'taxpayerName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxpayerName')
            value_ = self.gds_validate_string(value_, node, 'taxpayerName')
            self.taxpayerName = value_
            self.taxpayerName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.taxpayerName)
        elif nodeName_ == 'taxpayerShortName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxpayerShortName')
            value_ = self.gds_validate_string(value_, node, 'taxpayerShortName')
            self.taxpayerShortName = value_
            self.taxpayerShortName_nsprefix_ = child_.prefix
            # validate type SimpleText200NotBlankType
            self.validate_SimpleText200NotBlankType(self.taxpayerShortName)
        elif nodeName_ == 'taxNumberDetail':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.taxNumberDetail = obj_
            obj_.original_tagname_ = 'taxNumberDetail'
        elif nodeName_ == 'incorporation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'incorporation')
            value_ = self.gds_validate_string(value_, node, 'incorporation')
            self.incorporation = value_
            self.incorporation_nsprefix_ = child_.prefix
            # validate type IncorporationType
            self.validate_IncorporationType(self.incorporation)
        elif nodeName_ == 'vatGroupMembership':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'vatGroupMembership')
            value_ = self.gds_validate_string(value_, node, 'vatGroupMembership')
            self.vatGroupMembership = value_
            self.vatGroupMembership_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.vatGroupMembership)
        elif nodeName_ == 'taxpayerAddressList':
            obj_ = TaxpayerAddressListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.taxpayerAddressList = obj_
            obj_.original_tagname_ = 'taxpayerAddressList'
