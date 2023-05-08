import datetime as datetime_

import pytz

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


class PaymentEvidenceDocumentDataType(GeneratedsSuper):
    """PaymentEvidenceDocumentDataType -- A termékdíj bevallását igazoló dokumentum adatai
        a 2011. évi LXXXV. tv. 13. § (3) szerint és a 25. §(3) szerint
    Data of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011
    evidenceDocumentNo -- Számla sorszáma vagy egyéb okirat azonosító száma
    Sequential number of the invoice, or other document considered as such
    evidenceDocumentDate -- Számla kelte
    Date of issue of the invoice
    obligatedName -- Kötelezett neve
    Name of obligator
    obligatedAddress -- Kötelezett címe
    Address of obligator
    obligatedTaxNumber -- A kötelezett adószáma
    Tax number of obligated

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, evidenceDocumentNo=None, evidenceDocumentDate=None, obligatedName=None, obligatedAddress=None, obligatedTaxNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.evidenceDocumentNo = evidenceDocumentNo
        self.validate_SimpleText50NotBlankType(self.evidenceDocumentNo)
        self.evidenceDocumentNo_nsprefix_ = "common"
        if isinstance(evidenceDocumentDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(evidenceDocumentDate, '%Y-%m-%d').date()
        else:
            initvalue_ = evidenceDocumentDate
        self.evidenceDocumentDate = initvalue_
        self.evidenceDocumentDate_nsprefix_ = "base"
        self.obligatedName = obligatedName
        self.validate_SimpleText255NotBlankType(self.obligatedName)
        self.obligatedName_nsprefix_ = "common"
        self.obligatedAddress = obligatedAddress
        self.obligatedAddress_nsprefix_ = "base"
        self.obligatedTaxNumber = obligatedTaxNumber
        self.obligatedTaxNumber_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentEvidenceDocumentDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentEvidenceDocumentDataType.subclass:
            return PaymentEvidenceDocumentDataType.subclass(*args_, **kwargs_)
        else:
            return PaymentEvidenceDocumentDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_evidenceDocumentNo(self):
        return self.evidenceDocumentNo
    def set_evidenceDocumentNo(self, evidenceDocumentNo):
        self.evidenceDocumentNo = evidenceDocumentNo
    def get_evidenceDocumentDate(self):
        return self.evidenceDocumentDate
    def set_evidenceDocumentDate(self, evidenceDocumentDate):
        self.evidenceDocumentDate = evidenceDocumentDate
    def get_obligatedName(self):
        return self.obligatedName
    def set_obligatedName(self, obligatedName):
        self.obligatedName = obligatedName
    def get_obligatedAddress(self):
        return self.obligatedAddress
    def set_obligatedAddress(self, obligatedAddress):
        self.obligatedAddress = obligatedAddress
    def get_obligatedTaxNumber(self):
        return self.obligatedTaxNumber
    def set_obligatedTaxNumber(self, obligatedTaxNumber):
        self.obligatedTaxNumber = obligatedTaxNumber
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
            self.evidenceDocumentNo is not None or
            self.evidenceDocumentDate is not None or
            self.obligatedName is not None or
            self.obligatedAddress is not None or
            self.obligatedTaxNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='PaymentEvidenceDocumentDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentEvidenceDocumentDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentEvidenceDocumentDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentEvidenceDocumentDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentEvidenceDocumentDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentEvidenceDocumentDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='PaymentEvidenceDocumentDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.evidenceDocumentNo is not None:
            namespaceprefix_ = self.evidenceDocumentNo_nsprefix_ + ':' if (UseCapturedNS_ and self.evidenceDocumentNo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevidenceDocumentNo>%s</%sevidenceDocumentNo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.evidenceDocumentNo), input_name='evidenceDocumentNo')), namespaceprefix_ , eol_))
        if self.evidenceDocumentDate is not None:
            namespaceprefix_ = self.evidenceDocumentDate_nsprefix_ + ':' if (UseCapturedNS_ and self.evidenceDocumentDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevidenceDocumentDate>%s</%sevidenceDocumentDate>%s' % (namespaceprefix_ , self.gds_format_date(self.evidenceDocumentDate, input_name='evidenceDocumentDate'), namespaceprefix_ , eol_))
        if self.obligatedName is not None:
            namespaceprefix_ = self.obligatedName_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sobligatedName>%s</%sobligatedName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.obligatedName), input_name='obligatedName')), namespaceprefix_ , eol_))
        if self.obligatedAddress is not None:
            namespaceprefix_ = self.obligatedAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedAddress_nsprefix_) else ''
            self.obligatedAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='obligatedAddress', pretty_print=pretty_print)
        if self.obligatedTaxNumber is not None:
            namespaceprefix_ = self.obligatedTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedTaxNumber_nsprefix_) else ''
            self.obligatedTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='obligatedTaxNumber', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='PaymentEvidenceDocumentDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.evidenceDocumentNo is not None:
            evidenceDocumentNo_ = self.evidenceDocumentNo
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}evidenceDocumentNo').text = self.gds_format_string(evidenceDocumentNo_)
        if self.evidenceDocumentDate is not None:
            evidenceDocumentDate_ = self.evidenceDocumentDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}evidenceDocumentDate').text = self.gds_format_date(evidenceDocumentDate_)
        if self.obligatedName is not None:
            obligatedName_ = self.obligatedName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}obligatedName').text = self.gds_format_string(obligatedName_)
        if self.obligatedAddress is not None:
            obligatedAddress_ = self.obligatedAddress
            obligatedAddress_.to_etree(element, name_='obligatedAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.obligatedTaxNumber is not None:
            obligatedTaxNumber_ = self.obligatedTaxNumber
            obligatedTaxNumber_.to_etree(element, name_='obligatedTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PaymentEvidenceDocumentDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.evidenceDocumentNo is not None:
            showIndent(outfile, level)
            outfile.write('evidenceDocumentNo=%s,\n' % self.gds_encode(quote_python(self.evidenceDocumentNo)))
        if self.evidenceDocumentDate is not None:
            showIndent(outfile, level)
            outfile.write('evidenceDocumentDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.evidenceDocumentDate, input_name='evidenceDocumentDate'))
        if self.obligatedName is not None:
            showIndent(outfile, level)
            outfile.write('obligatedName=%s,\n' % self.gds_encode(quote_python(self.obligatedName)))
        if self.obligatedAddress is not None:
            showIndent(outfile, level)
            outfile.write('obligatedAddress=model_.AddressType(\n')
            self.obligatedAddress.exportLiteral(outfile, level, name_='obligatedAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.obligatedTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('obligatedTaxNumber=model_.TaxNumberType(\n')
            self.obligatedTaxNumber.exportLiteral(outfile, level, name_='obligatedTaxNumber')
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
        if nodeName_ == 'evidenceDocumentNo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'evidenceDocumentNo')
            value_ = self.gds_validate_string(value_, node, 'evidenceDocumentNo')
            self.evidenceDocumentNo = value_
            self.evidenceDocumentNo_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.evidenceDocumentNo)
        elif nodeName_ == 'evidenceDocumentDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.evidenceDocumentDate = dval_
            self.evidenceDocumentDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.evidenceDocumentDate)
        elif nodeName_ == 'obligatedName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'obligatedName')
            value_ = self.gds_validate_string(value_, node, 'obligatedName')
            self.obligatedName = value_
            self.obligatedName_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.obligatedName)
        elif nodeName_ == 'obligatedAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.obligatedAddress = obj_
            obj_.original_tagname_ = 'obligatedAddress'
        elif nodeName_ == 'obligatedTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.obligatedTaxNumber = obj_
            obj_.original_tagname_ = 'obligatedTaxNumber'
