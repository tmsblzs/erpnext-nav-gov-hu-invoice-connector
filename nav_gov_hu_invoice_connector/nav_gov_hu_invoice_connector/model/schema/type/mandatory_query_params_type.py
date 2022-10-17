import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.date_interval_param_type import \
    DateIntervalParamType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.date_time_interval_param_type import \
    DateTimeIntervalParamType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class MandatoryQueryParamsType(GeneratedsSuper):
    """MandatoryQueryParamsType -- A számla lekérdezés kötelező paraméterei
       Mandatory params of the invoice query invoiceIssueDate -- Számla kiállításának dátumtartománya
            Date range of the invoice issue date
    insDate -- Számla adatszolgáltatás feldolgozásának időpont tartománya UTC idő szerint
    Datetime range of processing data exchange in UTC time
    originalInvoiceNumber -- Az eredeti számla sorszáma, melyre a módosítás vonatkozik
    Sequence number of the original invoice, on which the modification occurs
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoiceIssueDate=None, insDate=None, originalInvoiceNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceIssueDate = invoiceIssueDate
        self.invoiceIssueDate_nsprefix_ = None
        self.insDate = insDate
        self.insDate_nsprefix_ = None
        self.originalInvoiceNumber = originalInvoiceNumber
        self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
        self.originalInvoiceNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MandatoryQueryParamsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MandatoryQueryParamsType.subclass:
            return MandatoryQueryParamsType.subclass(*args_, **kwargs_)
        else:
            return MandatoryQueryParamsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceIssueDate(self):
        return self.invoiceIssueDate
    def set_invoiceIssueDate(self, invoiceIssueDate):
        self.invoiceIssueDate = invoiceIssueDate
    def get_insDate(self):
        return self.insDate
    def set_insDate(self, insDate):
        self.insDate = insDate
    def get_originalInvoiceNumber(self):
        return self.originalInvoiceNumber
    def set_originalInvoiceNumber(self, originalInvoiceNumber):
        self.originalInvoiceNumber = originalInvoiceNumber
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
            self.invoiceIssueDate is not None or
            self.insDate is not None or
            self.originalInvoiceNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MandatoryQueryParamsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MandatoryQueryParamsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MandatoryQueryParamsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MandatoryQueryParamsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MandatoryQueryParamsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MandatoryQueryParamsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MandatoryQueryParamsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceIssueDate is not None:
            namespaceprefix_ = self.invoiceIssueDate_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceIssueDate_nsprefix_) else ''
            self.invoiceIssueDate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceIssueDate', pretty_print=pretty_print)
        if self.insDate is not None:
            namespaceprefix_ = self.insDate_nsprefix_ + ':' if (UseCapturedNS_ and self.insDate_nsprefix_) else ''
            self.insDate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='insDate', pretty_print=pretty_print)
        if self.originalInvoiceNumber is not None:
            namespaceprefix_ = self.originalInvoiceNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.originalInvoiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalInvoiceNumber>%s</%soriginalInvoiceNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.originalInvoiceNumber), input_name='originalInvoiceNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='MandatoryQueryParamsType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.invoiceIssueDate is not None:
            invoiceIssueDate_ = self.invoiceIssueDate
            invoiceIssueDate_.to_etree(element, name_='invoiceIssueDate', mapping_=mapping_, nsmap_=nsmap_)
        if self.insDate is not None:
            insDate_ = self.insDate
            insDate_.to_etree(element, name_='insDate', mapping_=mapping_, nsmap_=nsmap_)
        if self.originalInvoiceNumber is not None:
            originalInvoiceNumber_ = self.originalInvoiceNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber').text = self.gds_format_string(originalInvoiceNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MandatoryQueryParamsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceIssueDate is not None:
            showIndent(outfile, level)
            outfile.write('invoiceIssueDate=model_.DateIntervalParamType(\n')
            self.invoiceIssueDate.exportLiteral(outfile, level, name_='invoiceIssueDate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.insDate is not None:
            showIndent(outfile, level)
            outfile.write('insDate=model_.DateTimeIntervalParamType(\n')
            self.insDate.exportLiteral(outfile, level, name_='insDate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.originalInvoiceNumber is not None:
            showIndent(outfile, level)
            outfile.write('originalInvoiceNumber=%s,\n' % self.gds_encode(quote_python(self.originalInvoiceNumber)))
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
        if nodeName_ == 'invoiceIssueDate':
            obj_ = DateIntervalParamType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceIssueDate = obj_
            obj_.original_tagname_ = 'invoiceIssueDate'
        elif nodeName_ == 'insDate':
            obj_ = DateTimeIntervalParamType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.insDate = obj_
            obj_.original_tagname_ = 'insDate'
        elif nodeName_ == 'originalInvoiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalInvoiceNumber')
            value_ = self.gds_validate_string(value_, node, 'originalInvoiceNumber')
            self.originalInvoiceNumber = value_
            self.originalInvoiceNumber_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
