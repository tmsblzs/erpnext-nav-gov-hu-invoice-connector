import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.customer_tax_number_type import \
    CustomerTaxNumberType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class CustomerVatDataType(GeneratedsSuper):
    """CustomerVatDataType -- A vevő ÁFA alanyisági adatai
    VAT subjectivity data of the customer
    customerTaxNumber -- Belföldi adószám, amely alatt a számlán szereplő termékbeszerzés
        vagy szolgáltatás igénybevétele történt. Lehet csoportazonosítószám is
    Domestic tax number or group identification number, under which the purchase of goods or services is done
    communityVatNumber -- Közösségi adószám
    Community tax number
    thirdStateTaxId -- Harmadik országbeli adóazonosító
    Third state tax identification number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customerTaxNumber=None, communityVatNumber=None, thirdStateTaxId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customerTaxNumber = customerTaxNumber
        self.customerTaxNumber_nsprefix_ = None
        self.communityVatNumber = communityVatNumber
        self.validate_CommunityVatNumberType(self.communityVatNumber)
        self.communityVatNumber_nsprefix_ = "common"
        self.thirdStateTaxId = thirdStateTaxId
        self.validate_SimpleText50NotBlankType(self.thirdStateTaxId)
        self.thirdStateTaxId_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CustomerVatDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CustomerVatDataType.subclass:
            return CustomerVatDataType.subclass(*args_, **kwargs_)
        else:
            return CustomerVatDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customerTaxNumber(self):
        return self.customerTaxNumber
    def set_customerTaxNumber(self, customerTaxNumber):
        self.customerTaxNumber = customerTaxNumber
    def get_communityVatNumber(self):
        return self.communityVatNumber
    def set_communityVatNumber(self, communityVatNumber):
        self.communityVatNumber = communityVatNumber
    def get_thirdStateTaxId(self):
        return self.thirdStateTaxId
    def set_thirdStateTaxId(self, thirdStateTaxId):
        self.thirdStateTaxId = thirdStateTaxId
    def validate_CommunityVatNumberType(self, value):
        result = True
        # Validate type CommunityVatNumberType, a restriction on AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CommunityVatNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CommunityVatNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CommunityVatNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CommunityVatNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CommunityVatNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CommunityVatNumberType_patterns_, ))
                result = False
        return result
    validate_CommunityVatNumberType_patterns_ = [['^([A-Z]{2}[0-9A-Z]{2,13})$']]
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
    def _hasContent(self):
        if (
            self.customerTaxNumber is not None or
            self.communityVatNumber is not None or
            self.thirdStateTaxId is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='CustomerVatDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CustomerVatDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CustomerVatDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomerVatDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CustomerVatDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CustomerVatDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='CustomerVatDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customerTaxNumber is not None:
            namespaceprefix_ = self.customerTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.customerTaxNumber_nsprefix_) else ''
            self.customerTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customerTaxNumber', pretty_print=pretty_print)
        if self.communityVatNumber is not None:
            namespaceprefix_ = self.communityVatNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.communityVatNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scommunityVatNumber>%s</%scommunityVatNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.communityVatNumber), input_name='communityVatNumber')), namespaceprefix_ , eol_))
        if self.thirdStateTaxId is not None:
            namespaceprefix_ = self.thirdStateTaxId_nsprefix_ + ':' if (UseCapturedNS_ and self.thirdStateTaxId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sthirdStateTaxId>%s</%sthirdStateTaxId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.thirdStateTaxId), input_name='thirdStateTaxId')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='CustomerVatDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.customerTaxNumber is not None:
            customerTaxNumber_ = self.customerTaxNumber
            customerTaxNumber_.to_etree(element, name_='customerTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if self.communityVatNumber is not None:
            communityVatNumber_ = self.communityVatNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}communityVatNumber').text = self.gds_format_string(communityVatNumber_)
        if self.thirdStateTaxId is not None:
            thirdStateTaxId_ = self.thirdStateTaxId
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}thirdStateTaxId').text = self.gds_format_string(thirdStateTaxId_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CustomerVatDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.customerTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('customerTaxNumber=model_.CustomerTaxNumberType(\n')
            self.customerTaxNumber.exportLiteral(outfile, level, name_='customerTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.communityVatNumber is not None:
            showIndent(outfile, level)
            outfile.write('communityVatNumber=%s,\n' % self.gds_encode(quote_python(self.communityVatNumber)))
        if self.thirdStateTaxId is not None:
            showIndent(outfile, level)
            outfile.write('thirdStateTaxId=%s,\n' % self.gds_encode(quote_python(self.thirdStateTaxId)))
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
        if nodeName_ == 'customerTaxNumber':
            obj_ = CustomerTaxNumberType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerTaxNumber = obj_
            obj_.original_tagname_ = 'customerTaxNumber'
        elif nodeName_ == 'communityVatNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'communityVatNumber')
            value_ = self.gds_validate_string(value_, node, 'communityVatNumber')
            self.communityVatNumber = value_
            self.communityVatNumber_nsprefix_ = child_.prefix
            # validate type CommunityVatNumberType
            self.validate_CommunityVatNumberType(self.communityVatNumber)
        elif nodeName_ == 'thirdStateTaxId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'thirdStateTaxId')
            value_ = self.gds_validate_string(value_, node, 'thirdStateTaxId')
            self.thirdStateTaxId = value_
            self.thirdStateTaxId_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.thirdStateTaxId)
