import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_main_type import \
    InvoiceMainType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class InvoiceDataType(GeneratedsSuper):
    """InvoiceDataType -- A számla adatszolgáltatás adatai
    Invoice exchange data
    invoiceNumber -- Számla vagy módosítóokirat sorszáma - ÁFA tv. 169. § b) vagy 170. § (1) bek. b) pont
    Sequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law
    invoiceIssueDate -- Számla vagy módosító okirat kelte - ÁFA tv. 169. § a), ÁFA tv. 170. § (1) bek. a)
    Date of issue of the invoice or the modification document - section 169 (a) of the VAT law, section 170 (1) a) of the VAT law
    completenessIndicator -- Jelöli, ha az adatszolgáltatás maga a számla (a számlán nem szerepel több adat)
    Indicates whether the data exchange is identical with the invoice (the invoice does not contain any more data)
    invoiceMain -- Számlaadatok leírására szolgáló közös típus
    A common type to describe invoice information

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoiceNumber=None, invoiceIssueDate=None, completenessIndicator=None, invoiceMain=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceNumber = invoiceNumber
        self.validate_SimpleText50NotBlankType(self.invoiceNumber)
        self.invoiceNumber_nsprefix_ = "common"
        if isinstance(invoiceIssueDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(invoiceIssueDate, '%Y-%m-%d').date()
        else:
            initvalue_ = invoiceIssueDate
        self.invoiceIssueDate = initvalue_
        self.invoiceIssueDate_nsprefix_ = "base"
        self.completenessIndicator = completenessIndicator
        self.completenessIndicator_nsprefix_ = "xs"
        self.invoiceMain = invoiceMain
        self.invoiceMain_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceDataType.subclass:
            return InvoiceDataType.subclass(*args_, **kwargs_)
        else:
            return InvoiceDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceNumber(self):
        return self.invoiceNumber
    def set_invoiceNumber(self, invoiceNumber):
        self.invoiceNumber = invoiceNumber
    def get_invoiceIssueDate(self):
        return self.invoiceIssueDate
    def set_invoiceIssueDate(self, invoiceIssueDate):
        self.invoiceIssueDate = invoiceIssueDate
    def get_completenessIndicator(self):
        return self.completenessIndicator
    def set_completenessIndicator(self, completenessIndicator):
        self.completenessIndicator = completenessIndicator
    def get_invoiceMain(self):
        return self.invoiceMain
    def set_invoiceMain(self, invoiceMain):
        self.invoiceMain = invoiceMain
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
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
    def _hasContent(self):
        if (
            self.invoiceNumber is not None or
            self.invoiceIssueDate is not None or
            self.completenessIndicator is not None or
            self.invoiceMain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceDataType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='InvoiceDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceNumber is not None:
            namespaceprefix_ = self.invoiceNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNumber>%s</%sinvoiceNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoiceNumber), input_name='invoiceNumber')), namespaceprefix_ , eol_))
        if self.invoiceIssueDate is not None:
            namespaceprefix_ = self.invoiceIssueDate_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceIssueDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceIssueDate>%s</%sinvoiceIssueDate>%s' % (namespaceprefix_ , self.gds_format_date(self.invoiceIssueDate, input_name='invoiceIssueDate'), namespaceprefix_ , eol_))
        if self.completenessIndicator is not None:
            namespaceprefix_ = self.completenessIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.completenessIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompletenessIndicator>%s</%scompletenessIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.completenessIndicator, input_name='completenessIndicator'), namespaceprefix_ , eol_))
        if self.invoiceMain is not None:
            namespaceprefix_ = self.invoiceMain_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceMain_nsprefix_) else ''
            self.invoiceMain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceMain', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InvoiceDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.invoiceNumber is not None:
            invoiceNumber_ = self.invoiceNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNumber').text = self.gds_format_string(invoiceNumber_)
        if self.invoiceIssueDate is not None:
            invoiceIssueDate_ = self.invoiceIssueDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceIssueDate').text = self.gds_format_date(invoiceIssueDate_)
        if self.completenessIndicator is not None:
            completenessIndicator_ = self.completenessIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}completenessIndicator').text = self.gds_format_boolean(completenessIndicator_)
        if self.invoiceMain is not None:
            invoiceMain_ = self.invoiceMain
            invoiceMain_.to_etree(element, name_='invoiceMain', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='InvoiceDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceNumber is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNumber=%s,\n' % self.gds_encode(quote_python(self.invoiceNumber)))
        if self.invoiceIssueDate is not None:
            showIndent(outfile, level)
            outfile.write('invoiceIssueDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.invoiceIssueDate, input_name='invoiceIssueDate'))
        if self.completenessIndicator is not None:
            showIndent(outfile, level)
            outfile.write('completenessIndicator=%s,\n' % self.completenessIndicator)
        if self.invoiceMain is not None:
            showIndent(outfile, level)
            outfile.write('invoiceMain=model_.InvoiceMainType(\n')
            self.invoiceMain.exportLiteral(outfile, level, name_='invoiceMain')
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'invoiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoiceNumber')
            value_ = self.gds_validate_string(value_, node, 'invoiceNumber')
            self.invoiceNumber = value_
            self.invoiceNumber_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.invoiceNumber)
        elif nodeName_ == 'invoiceIssueDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.invoiceIssueDate = dval_
            self.invoiceIssueDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.invoiceIssueDate)
        elif nodeName_ == 'completenessIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'completenessIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'completenessIndicator')
            self.completenessIndicator = ival_
            self.completenessIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'invoiceMain':
            obj_ = InvoiceMainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceMain = obj_
            obj_.original_tagname_ = 'invoiceMain'
