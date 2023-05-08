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


class FiscalRepresentativeType(GeneratedsSuper):
    """FiscalRepresentativeType -- A pénzügyi képviselő adatai
    Fiscal representative data
    fiscalRepresentativeTaxNumber -- A pénzügyi képviselő adószáma
    Tax number of the fiscal representative
    fiscalRepresentativeName -- A pénz ügyi képviselő neve
    Name of the fiscal representative
    fiscalRepresentativeAddress -- Pénz ügyi képviselő címe
    Address of the fiscal representative
    fiscalRepresentativeBankAccountNumber -- Pénz ügyi képviselő által a számla kibocsátó (eladó)
        számára megnyitott bankszámla bankszámlaszáma
    Bank account number opened by the fiscal representative for the issuer of the invoice (supplier)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, fiscalRepresentativeTaxNumber=None, fiscalRepresentativeName=None, fiscalRepresentativeAddress=None, fiscalRepresentativeBankAccountNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fiscalRepresentativeTaxNumber = fiscalRepresentativeTaxNumber
        self.fiscalRepresentativeTaxNumber_nsprefix_ = "base"
        self.fiscalRepresentativeName = fiscalRepresentativeName
        self.validate_SimpleText512NotBlankType(self.fiscalRepresentativeName)
        self.fiscalRepresentativeName_nsprefix_ = "common"
        self.fiscalRepresentativeAddress = fiscalRepresentativeAddress
        self.fiscalRepresentativeAddress_nsprefix_ = "base"
        self.fiscalRepresentativeBankAccountNumber = fiscalRepresentativeBankAccountNumber
        self.validate_BankAccountNumberType(self.fiscalRepresentativeBankAccountNumber)
        self.fiscalRepresentativeBankAccountNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FiscalRepresentativeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FiscalRepresentativeType.subclass:
            return FiscalRepresentativeType.subclass(*args_, **kwargs_)
        else:
            return FiscalRepresentativeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_fiscalRepresentativeTaxNumber(self):
        return self.fiscalRepresentativeTaxNumber
    def set_fiscalRepresentativeTaxNumber(self, fiscalRepresentativeTaxNumber):
        self.fiscalRepresentativeTaxNumber = fiscalRepresentativeTaxNumber
    def get_fiscalRepresentativeName(self):
        return self.fiscalRepresentativeName
    def set_fiscalRepresentativeName(self, fiscalRepresentativeName):
        self.fiscalRepresentativeName = fiscalRepresentativeName
    def get_fiscalRepresentativeAddress(self):
        return self.fiscalRepresentativeAddress
    def set_fiscalRepresentativeAddress(self, fiscalRepresentativeAddress):
        self.fiscalRepresentativeAddress = fiscalRepresentativeAddress
    def get_fiscalRepresentativeBankAccountNumber(self):
        return self.fiscalRepresentativeBankAccountNumber
    def set_fiscalRepresentativeBankAccountNumber(self, fiscalRepresentativeBankAccountNumber):
        self.fiscalRepresentativeBankAccountNumber = fiscalRepresentativeBankAccountNumber
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
            self.fiscalRepresentativeTaxNumber is not None or
            self.fiscalRepresentativeName is not None or
            self.fiscalRepresentativeAddress is not None or
            self.fiscalRepresentativeBankAccountNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='FiscalRepresentativeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FiscalRepresentativeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FiscalRepresentativeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FiscalRepresentativeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FiscalRepresentativeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FiscalRepresentativeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='FiscalRepresentativeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.fiscalRepresentativeTaxNumber is not None:
            namespaceprefix_ = self.fiscalRepresentativeTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeTaxNumber_nsprefix_) else ''
            self.fiscalRepresentativeTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fiscalRepresentativeTaxNumber', pretty_print=pretty_print)
        if self.fiscalRepresentativeName is not None:
            namespaceprefix_ = self.fiscalRepresentativeName_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfiscalRepresentativeName>%s</%sfiscalRepresentativeName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fiscalRepresentativeName), input_name='fiscalRepresentativeName')), namespaceprefix_ , eol_))
        if self.fiscalRepresentativeAddress is not None:
            namespaceprefix_ = self.fiscalRepresentativeAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeAddress_nsprefix_) else ''
            self.fiscalRepresentativeAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fiscalRepresentativeAddress', pretty_print=pretty_print)
        if self.fiscalRepresentativeBankAccountNumber is not None:
            namespaceprefix_ = self.fiscalRepresentativeBankAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeBankAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfiscalRepresentativeBankAccountNumber>%s</%sfiscalRepresentativeBankAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fiscalRepresentativeBankAccountNumber), input_name='fiscalRepresentativeBankAccountNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='FiscalRepresentativeType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.fiscalRepresentativeTaxNumber is not None:
            fiscalRepresentativeTaxNumber_ = self.fiscalRepresentativeTaxNumber
            fiscalRepresentativeTaxNumber_.to_etree(element, name_='fiscalRepresentativeTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if self.fiscalRepresentativeName is not None:
            fiscalRepresentativeName_ = self.fiscalRepresentativeName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeName').text = self.gds_format_string(fiscalRepresentativeName_)
        if self.fiscalRepresentativeAddress is not None:
            fiscalRepresentativeAddress_ = self.fiscalRepresentativeAddress
            fiscalRepresentativeAddress_.to_etree(element, name_='fiscalRepresentativeAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.fiscalRepresentativeBankAccountNumber is not None:
            fiscalRepresentativeBankAccountNumber_ = self.fiscalRepresentativeBankAccountNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeBankAccountNumber').text = self.gds_format_string(fiscalRepresentativeBankAccountNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='FiscalRepresentativeType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.fiscalRepresentativeTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeTaxNumber=model_.TaxNumberType(\n')
            self.fiscalRepresentativeTaxNumber.exportLiteral(outfile, level, name_='fiscalRepresentativeTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fiscalRepresentativeName is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeName=%s,\n' % self.gds_encode(quote_python(self.fiscalRepresentativeName)))
        if self.fiscalRepresentativeAddress is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeAddress=model_.AddressType(\n')
            self.fiscalRepresentativeAddress.exportLiteral(outfile, level, name_='fiscalRepresentativeAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fiscalRepresentativeBankAccountNumber is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeBankAccountNumber=%s,\n' % self.gds_encode(quote_python(self.fiscalRepresentativeBankAccountNumber)))
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
        if nodeName_ == 'fiscalRepresentativeTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fiscalRepresentativeTaxNumber = obj_
            obj_.original_tagname_ = 'fiscalRepresentativeTaxNumber'
        elif nodeName_ == 'fiscalRepresentativeName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fiscalRepresentativeName')
            value_ = self.gds_validate_string(value_, node, 'fiscalRepresentativeName')
            self.fiscalRepresentativeName = value_
            self.fiscalRepresentativeName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.fiscalRepresentativeName)
        elif nodeName_ == 'fiscalRepresentativeAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fiscalRepresentativeAddress = obj_
            obj_.original_tagname_ = 'fiscalRepresentativeAddress'
        elif nodeName_ == 'fiscalRepresentativeBankAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fiscalRepresentativeBankAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'fiscalRepresentativeBankAccountNumber')
            self.fiscalRepresentativeBankAccountNumber = value_
            self.fiscalRepresentativeBankAccountNumber_nsprefix_ = child_.prefix
            # validate type BankAccountNumberType
            self.validate_BankAccountNumberType(self.fiscalRepresentativeBankAccountNumber)
