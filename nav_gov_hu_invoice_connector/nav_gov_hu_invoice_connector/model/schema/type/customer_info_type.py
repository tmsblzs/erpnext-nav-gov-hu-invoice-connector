import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.address_type import AddressType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.customer_vat_data_type import \
    CustomerVatDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class CustomerInfoType(GeneratedsSuper):
    """CustomerInfoType -- A vevő adatai
    Customer data
    customerVatStatus -- Vevő ÁFA szerinti státusza
    Customers status by VAT
    customerVatData -- A vevő ÁFA alanyisági adatai
    VAT subjectivity data of the customer
    customerName -- A vevő neve
    Name of the customer
    customerAddress -- A vevő címe
    Address of the customer
    customerBankAccountNumber -- Vevő bankszámlaszáma
    Bank account number of the customer

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customerVatStatus=None, customerVatData=None, customerName=None, customerAddress=None, customerBankAccountNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customerVatStatus = customerVatStatus
        self.validate_CustomerVatStatusType(self.customerVatStatus)
        self.customerVatStatus_nsprefix_ = None
        self.customerVatData = customerVatData
        self.customerVatData_nsprefix_ = None
        self.customerName = customerName
        self.validate_SimpleText512NotBlankType(self.customerName)
        self.customerName_nsprefix_ = "common"
        self.customerAddress = customerAddress
        self.customerAddress_nsprefix_ = "base"
        self.customerBankAccountNumber = customerBankAccountNumber
        self.validate_BankAccountNumberType(self.customerBankAccountNumber)
        self.customerBankAccountNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CustomerInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CustomerInfoType.subclass:
            return CustomerInfoType.subclass(*args_, **kwargs_)
        else:
            return CustomerInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customerVatStatus(self):
        return self.customerVatStatus
    def set_customerVatStatus(self, customerVatStatus):
        self.customerVatStatus = customerVatStatus
    def get_customerVatData(self):
        return self.customerVatData
    def set_customerVatData(self, customerVatData):
        self.customerVatData = customerVatData
    def get_customerName(self):
        return self.customerName
    def set_customerName(self, customerName):
        self.customerName = customerName
    def get_customerAddress(self):
        return self.customerAddress
    def set_customerAddress(self, customerAddress):
        self.customerAddress = customerAddress
    def get_customerBankAccountNumber(self):
        return self.customerBankAccountNumber
    def set_customerBankAccountNumber(self, customerBankAccountNumber):
        self.customerBankAccountNumber = customerBankAccountNumber
    def validate_CustomerVatStatusType(self, value):
        result = True
        # Validate type CustomerVatStatusType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['DOMESTIC', 'OTHER', 'PRIVATE_PERSON']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on CustomerVatStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CustomerVatStatusType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CustomerVatStatusType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
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
    def _hasContent(self):
        if (
            self.customerVatStatus is not None or
            self.customerVatData is not None or
            self.customerName is not None or
            self.customerAddress is not None or
            self.customerBankAccountNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='CustomerInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CustomerInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CustomerInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomerInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CustomerInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CustomerInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='CustomerInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customerVatStatus is not None:
            namespaceprefix_ = self.customerVatStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.customerVatStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerVatStatus>%s</%scustomerVatStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customerVatStatus), input_name='customerVatStatus')), namespaceprefix_ , eol_))
        if self.customerVatData is not None:
            namespaceprefix_ = self.customerVatData_nsprefix_ + ':' if (UseCapturedNS_ and self.customerVatData_nsprefix_) else ''
            self.customerVatData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customerVatData', pretty_print=pretty_print)
        if self.customerName is not None:
            namespaceprefix_ = self.customerName_nsprefix_ + ':' if (UseCapturedNS_ and self.customerName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerName>%s</%scustomerName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customerName), input_name='customerName')), namespaceprefix_ , eol_))
        if self.customerAddress is not None:
            namespaceprefix_ = self.customerAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.customerAddress_nsprefix_) else ''
            self.customerAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customerAddress', pretty_print=pretty_print)
        if self.customerBankAccountNumber is not None:
            namespaceprefix_ = self.customerBankAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.customerBankAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerBankAccountNumber>%s</%scustomerBankAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customerBankAccountNumber), input_name='customerBankAccountNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='CustomerInfoType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.customerVatStatus is not None:
            customerVatStatus_ = self.customerVatStatus
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}customerVatStatus').text = self.gds_format_string(customerVatStatus_)
        if self.customerVatData is not None:
            customerVatData_ = self.customerVatData
            customerVatData_.to_etree(element, name_='customerVatData', mapping_=mapping_, nsmap_=nsmap_)
        if self.customerName is not None:
            customerName_ = self.customerName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}customerName').text = self.gds_format_string(customerName_)
        if self.customerAddress is not None:
            customerAddress_ = self.customerAddress
            customerAddress_.to_etree(element, name_='customerAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.customerBankAccountNumber is not None:
            customerBankAccountNumber_ = self.customerBankAccountNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}customerBankAccountNumber').text = self.gds_format_string(customerBankAccountNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CustomerInfoType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.customerVatStatus is not None:
            showIndent(outfile, level)
            outfile.write('customerVatStatus=%s,\n' % self.gds_encode(quote_python(self.customerVatStatus)))
        if self.customerVatData is not None:
            showIndent(outfile, level)
            outfile.write('customerVatData=model_.CustomerVatDataType(\n')
            self.customerVatData.exportLiteral(outfile, level, name_='customerVatData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.customerName is not None:
            showIndent(outfile, level)
            outfile.write('customerName=%s,\n' % self.gds_encode(quote_python(self.customerName)))
        if self.customerAddress is not None:
            showIndent(outfile, level)
            outfile.write('customerAddress=model_.AddressType(\n')
            self.customerAddress.exportLiteral(outfile, level, name_='customerAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.customerBankAccountNumber is not None:
            showIndent(outfile, level)
            outfile.write('customerBankAccountNumber=%s,\n' % self.gds_encode(quote_python(self.customerBankAccountNumber)))
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
        if nodeName_ == 'customerVatStatus':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerVatStatus')
            value_ = self.gds_validate_string(value_, node, 'customerVatStatus')
            self.customerVatStatus = value_
            self.customerVatStatus_nsprefix_ = child_.prefix
            # validate type CustomerVatStatusType
            self.validate_CustomerVatStatusType(self.customerVatStatus)
        elif nodeName_ == 'customerVatData':
            obj_ = CustomerVatDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerVatData = obj_
            obj_.original_tagname_ = 'customerVatData'
        elif nodeName_ == 'customerName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerName')
            value_ = self.gds_validate_string(value_, node, 'customerName')
            self.customerName = value_
            self.customerName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.customerName)
        elif nodeName_ == 'customerAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerAddress = obj_
            obj_.original_tagname_ = 'customerAddress'
        elif nodeName_ == 'customerBankAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerBankAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'customerBankAccountNumber')
            self.customerBankAccountNumber = value_
            self.customerBankAccountNumber_nsprefix_ = child_.prefix
            # validate type BankAccountNumberType
            self.validate_BankAccountNumberType(self.customerBankAccountNumber)
