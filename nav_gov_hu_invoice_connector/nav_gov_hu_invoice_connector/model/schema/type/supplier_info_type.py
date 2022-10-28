import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.address_type import AddressType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.tax_number_type import TaxNumberType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class SupplierInfoType(GeneratedsSuper):
    """SupplierInfoType -- A szállító (eladó) adatai
    Invoice supplier (seller) data
    supplierTaxNumber -- Belföldi adószám vagy csoportazonosító szám
    Tax number or group identification number
    groupMemberTaxNumber -- Csoport tag adószáma, ha a termékbeszerzés vagy szolgáltatás nyújtása
        csoportazonosító szám alatt történt
    Tax number of group member, when the supply of goods or services is done under group identification number
    communityVatNumber -- Közösségi adószám
    Community tax number
    supplierName -- Az eladó (szállító) neve
    Name of the seller (supplier)
    supplierAddress -- Az eladó (szállító) címe
    Address of the seller (supplier)
    supplierBankAccountNumber -- Az eladó (szállító) bankszámlaszáma
    Bank account number of the seller (supplier)
    individualExemption -- Értéke true, amennyiben az eladó (szállító) alanyi ÁFA mentes
    Value is true if the seller (supplier) is individually exempted from VAT
    exciseLicenceNum -- Az eladó adóraktári engedélyének vagy jövedéki engedélyének száma (2016. évi LXVIII. tv.)
    Number of supplier’s tax warehouse license or excise license (Act LXVIII of 2016)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, supplierTaxNumber=None, groupMemberTaxNumber=None, communityVatNumber=None, supplierName=None, supplierAddress=None, supplierBankAccountNumber=None, individualExemption=None, exciseLicenceNum=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.supplierTaxNumber = supplierTaxNumber
        self.supplierTaxNumber_nsprefix_ = "base"
        self.groupMemberTaxNumber = groupMemberTaxNumber
        self.groupMemberTaxNumber_nsprefix_ = "base"
        self.communityVatNumber = communityVatNumber
        self.validate_CommunityVatNumberType(self.communityVatNumber)
        self.communityVatNumber_nsprefix_ = "common"
        self.supplierName = supplierName
        self.validate_SimpleText512NotBlankType(self.supplierName)
        self.supplierName_nsprefix_ = "common"
        self.supplierAddress = supplierAddress
        self.supplierAddress_nsprefix_ = "base"
        self.supplierBankAccountNumber = supplierBankAccountNumber
        self.validate_BankAccountNumberType(self.supplierBankAccountNumber)
        self.supplierBankAccountNumber_nsprefix_ = "common"
        self.individualExemption = individualExemption
        self.individualExemption_nsprefix_ = "xs"
        self.exciseLicenceNum = exciseLicenceNum
        self.validate_SimpleText50NotBlankType(self.exciseLicenceNum)
        self.exciseLicenceNum_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SupplierInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SupplierInfoType.subclass:
            return SupplierInfoType.subclass(*args_, **kwargs_)
        else:
            return SupplierInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_supplierTaxNumber(self):
        return self.supplierTaxNumber
    def set_supplierTaxNumber(self, supplierTaxNumber):
        self.supplierTaxNumber = supplierTaxNumber
    def get_groupMemberTaxNumber(self):
        return self.groupMemberTaxNumber
    def set_groupMemberTaxNumber(self, groupMemberTaxNumber):
        self.groupMemberTaxNumber = groupMemberTaxNumber
    def get_communityVatNumber(self):
        return self.communityVatNumber
    def set_communityVatNumber(self, communityVatNumber):
        self.communityVatNumber = communityVatNumber
    def get_supplierName(self):
        return self.supplierName
    def set_supplierName(self, supplierName):
        self.supplierName = supplierName
    def get_supplierAddress(self):
        return self.supplierAddress
    def set_supplierAddress(self, supplierAddress):
        self.supplierAddress = supplierAddress
    def get_supplierBankAccountNumber(self):
        return self.supplierBankAccountNumber
    def set_supplierBankAccountNumber(self, supplierBankAccountNumber):
        self.supplierBankAccountNumber = supplierBankAccountNumber
    def get_individualExemption(self):
        return self.individualExemption
    def set_individualExemption(self, individualExemption):
        self.individualExemption = individualExemption
    def get_exciseLicenceNum(self):
        return self.exciseLicenceNum
    def set_exciseLicenceNum(self, exciseLicenceNum):
        self.exciseLicenceNum = exciseLicenceNum
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
    def validate_BankAccountNumberType(self, value):
        result = True
        # Validate type BankAccountNumberType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 34:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on BankAccountNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on BankAccountNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on BankAccountNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on BankAccountNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_BankAccountNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_BankAccountNumberType_patterns_, ))
                result = False
        return result
    validate_BankAccountNumberType_patterns_ = [['^([0-9]{8}[-][0-9]{8}[-][0-9]{8}|[0-9]{8}[-][0-9]{8}|[A-Z]{2}[0-9]{2}[0-9A-Za-z]{11,30})$']]
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
            self.supplierTaxNumber is not None or
            self.groupMemberTaxNumber is not None or
            self.communityVatNumber is not None or
            self.supplierName is not None or
            self.supplierAddress is not None or
            self.supplierBankAccountNumber is not None or
            self.individualExemption is not None or
            self.exciseLicenceNum is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='SupplierInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SupplierInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SupplierInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SupplierInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SupplierInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SupplierInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='SupplierInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.supplierTaxNumber is not None:
            namespaceprefix_ = self.supplierTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierTaxNumber_nsprefix_) else ''
            self.supplierTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplierTaxNumber', pretty_print=pretty_print)
        if self.groupMemberTaxNumber is not None:
            namespaceprefix_ = self.groupMemberTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.groupMemberTaxNumber_nsprefix_) else ''
            self.groupMemberTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='groupMemberTaxNumber', pretty_print=pretty_print)
        if self.communityVatNumber is not None:
            namespaceprefix_ = self.communityVatNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.communityVatNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scommunityVatNumber>%s</%scommunityVatNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.communityVatNumber), input_name='communityVatNumber')), namespaceprefix_ , eol_))
        if self.supplierName is not None:
            namespaceprefix_ = self.supplierName_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierName>%s</%ssupplierName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.supplierName), input_name='supplierName')), namespaceprefix_ , eol_))
        if self.supplierAddress is not None:
            namespaceprefix_ = self.supplierAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierAddress_nsprefix_) else ''
            self.supplierAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplierAddress', pretty_print=pretty_print)
        if self.supplierBankAccountNumber is not None:
            namespaceprefix_ = self.supplierBankAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierBankAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierBankAccountNumber>%s</%ssupplierBankAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.supplierBankAccountNumber), input_name='supplierBankAccountNumber')), namespaceprefix_ , eol_))
        if self.individualExemption is not None:
            namespaceprefix_ = self.individualExemption_nsprefix_ + ':' if (UseCapturedNS_ and self.individualExemption_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindividualExemption>%s</%sindividualExemption>%s' % (namespaceprefix_ , self.gds_format_boolean(self.individualExemption, input_name='individualExemption'), namespaceprefix_ , eol_))
        if self.exciseLicenceNum is not None:
            namespaceprefix_ = self.exciseLicenceNum_nsprefix_ + ':' if (UseCapturedNS_ and self.exciseLicenceNum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexciseLicenceNum>%s</%sexciseLicenceNum>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.exciseLicenceNum), input_name='exciseLicenceNum')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SupplierInfoType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.supplierTaxNumber is not None:
            supplierTaxNumber_ = self.supplierTaxNumber
            supplierTaxNumber_.to_etree(element, name_='supplierTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if self.groupMemberTaxNumber is not None:
            groupMemberTaxNumber_ = self.groupMemberTaxNumber
            groupMemberTaxNumber_.to_etree(element, name_='groupMemberTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if self.communityVatNumber is not None:
            communityVatNumber_ = self.communityVatNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}communityVatNumber').text = self.gds_format_string(communityVatNumber_)
        if self.supplierName is not None:
            supplierName_ = self.supplierName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}supplierName').text = self.gds_format_string(supplierName_)
        if self.supplierAddress is not None:
            supplierAddress_ = self.supplierAddress
            supplierAddress_.to_etree(element, name_='supplierAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.supplierBankAccountNumber is not None:
            supplierBankAccountNumber_ = self.supplierBankAccountNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}supplierBankAccountNumber').text = self.gds_format_string(supplierBankAccountNumber_)
        if self.individualExemption is not None:
            individualExemption_ = self.individualExemption
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}individualExemption').text = self.gds_format_boolean(individualExemption_)
        if self.exciseLicenceNum is not None:
            exciseLicenceNum_ = self.exciseLicenceNum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}exciseLicenceNum').text = self.gds_format_string(exciseLicenceNum_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SupplierInfoType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.supplierTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('supplierTaxNumber=model_.TaxNumberType(\n')
            self.supplierTaxNumber.exportLiteral(outfile, level, name_='supplierTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.groupMemberTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('groupMemberTaxNumber=model_.TaxNumberType(\n')
            self.groupMemberTaxNumber.exportLiteral(outfile, level, name_='groupMemberTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.communityVatNumber is not None:
            showIndent(outfile, level)
            outfile.write('communityVatNumber=%s,\n' % self.gds_encode(quote_python(self.communityVatNumber)))
        if self.supplierName is not None:
            showIndent(outfile, level)
            outfile.write('supplierName=%s,\n' % self.gds_encode(quote_python(self.supplierName)))
        if self.supplierAddress is not None:
            showIndent(outfile, level)
            outfile.write('supplierAddress=model_.AddressType(\n')
            self.supplierAddress.exportLiteral(outfile, level, name_='supplierAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.supplierBankAccountNumber is not None:
            showIndent(outfile, level)
            outfile.write('supplierBankAccountNumber=%s,\n' % self.gds_encode(quote_python(self.supplierBankAccountNumber)))
        if self.individualExemption is not None:
            showIndent(outfile, level)
            outfile.write('individualExemption=%s,\n' % self.individualExemption)
        if self.exciseLicenceNum is not None:
            showIndent(outfile, level)
            outfile.write('exciseLicenceNum=%s,\n' % self.gds_encode(quote_python(self.exciseLicenceNum)))
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
        if nodeName_ == 'supplierTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplierTaxNumber = obj_
            obj_.original_tagname_ = 'supplierTaxNumber'
        elif nodeName_ == 'groupMemberTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.groupMemberTaxNumber = obj_
            obj_.original_tagname_ = 'groupMemberTaxNumber'
        elif nodeName_ == 'communityVatNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'communityVatNumber')
            value_ = self.gds_validate_string(value_, node, 'communityVatNumber')
            self.communityVatNumber = value_
            self.communityVatNumber_nsprefix_ = child_.prefix
            # validate type CommunityVatNumberType
            self.validate_CommunityVatNumberType(self.communityVatNumber)
        elif nodeName_ == 'supplierName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierName')
            value_ = self.gds_validate_string(value_, node, 'supplierName')
            self.supplierName = value_
            self.supplierName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.supplierName)
        elif nodeName_ == 'supplierAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplierAddress = obj_
            obj_.original_tagname_ = 'supplierAddress'
        elif nodeName_ == 'supplierBankAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierBankAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'supplierBankAccountNumber')
            self.supplierBankAccountNumber = value_
            self.supplierBankAccountNumber_nsprefix_ = child_.prefix
            # validate type BankAccountNumberType
            self.validate_BankAccountNumberType(self.supplierBankAccountNumber)
        elif nodeName_ == 'individualExemption':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'individualExemption')
            ival_ = self.gds_validate_boolean(ival_, node, 'individualExemption')
            self.individualExemption = ival_
            self.individualExemption_nsprefix_ = child_.prefix
        elif nodeName_ == 'exciseLicenceNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'exciseLicenceNum')
            value_ = self.gds_validate_string(value_, node, 'exciseLicenceNum')
            self.exciseLicenceNum = value_
            self.exciseLicenceNum_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.exciseLicenceNum)
