import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class InvoiceAnnulmentType(GeneratedsSuper):
    """InvoiceAnnulmentType -- Korábbi adatszolgáltatás technikai érvénytelenítésének adatai
    Data of technical annulment concerning previous data exchange
    annulmentReference -- A technikai érvénytelenítéssel érintett számla vagy módosító okirat sorszáma
                Sequential number of the invoice or modification document to be annuled
    annulmentTimestamp -- A technikai érvénytelenítés időbélyege a forrásrendszerben UTC idő szerint
                Timestamp of the technical annulment in UTC time
    annulmentCode -- A technikai érvénytelenítés kódja
                Technical annulment code
    annulmentReason -- A technikai érvénytelenítés oka
                Technical annulment reason

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, annulmentReference=None, annulmentTimestamp=None, annulmentCode=None, annulmentReason=None,
                 extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.annulmentReference = annulmentReference
        self.validate_SimpleText50NotBlankType(self.annulmentReference)
        self.annulmentReference_nsprefix_ = "common"
        if isinstance(annulmentTimestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(annulmentTimestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = annulmentTimestamp
        self.annulmentTimestamp = initvalue_
        self.annulmentTimestamp_nsprefix_ = "base"
        self.annulmentCode = annulmentCode
        self.validate_AnnulmentCodeType(self.annulmentCode)
        self.annulmentCode_nsprefix_ = None
        self.annulmentReason = annulmentReason
        self.validate_SimpleText1024NotBlankType(self.annulmentReason)
        self.annulmentReason_nsprefix_ = "common"
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceAnnulmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceAnnulmentType.subclass:
            return InvoiceAnnulmentType.subclass(*args_, **kwargs_)
        else:
            return InvoiceAnnulmentType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_annulmentReference(self):
        return self.annulmentReference

    def set_annulmentReference(self, annulmentReference):
        self.annulmentReference = annulmentReference

    def get_annulmentTimestamp(self):
        return self.annulmentTimestamp

    def set_annulmentTimestamp(self, annulmentTimestamp):
        self.annulmentTimestamp = annulmentTimestamp

    def get_annulmentCode(self):
        return self.annulmentCode

    def set_annulmentCode(self, annulmentCode):
        self.annulmentCode = annulmentCode

    def get_annulmentReason(self):
        return self.annulmentReason

    def set_annulmentReason(self, annulmentReason):
        self.annulmentReason = annulmentReason

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            lineno = self.gds_get_node_lineno_()
            self.gds_collector_.add_message(
                'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {
                    "value": value, "lineno": lineno})
            result = False
        if not self.gds_validate_simple_patterns(
                self.validate_InvoiceTimestampType_patterns_, value):
            self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
            encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_,))
            result = False
        return result

    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]

    def validate_AnnulmentCodeType(self, value):
        result = True
        # Validate type AnnulmentCodeType, a restriction on common:AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['ERRATIC_DATA', 'ERRATIC_INVOICE_NUMBER', 'ERRATIC_INVOICE_ISSUE_DATE',
                            'ERRATIC_ELECTRONIC_HASH_VALUE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on AnnulmentCodeType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on AnnulmentCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on AnnulmentCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_SimpleText1024NotBlankType(self, value):
        result = True
        # Validate type SimpleText1024NotBlankType, a restriction on AtomicStringType1024.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 1024:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText1024NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText1024NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText1024NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText1024NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText1024NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def _hasContent(self):
        if (
                self.annulmentReference is not None or
                self.annulmentTimestamp is not None or
                self.annulmentCode is not None or
                self.annulmentReason is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='InvoiceAnnulmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceAnnulmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceAnnulmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceAnnulmentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceAnnulmentType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceAnnulmentType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='InvoiceAnnulmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.annulmentReference is not None:
            namespaceprefix_ = self.annulmentReference_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.annulmentReference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentReference>%s</%sannulmentReference>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.annulmentReference), input_name='annulmentReference')),
                                                                                 namespaceprefix_, eol_))
        if self.annulmentTimestamp is not None:
            namespaceprefix_ = self.annulmentTimestamp_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.annulmentTimestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentTimestamp>%s</%sannulmentTimestamp>%s' % (
            namespaceprefix_, self.gds_format_datetime(self.annulmentTimestamp, input_name='annulmentTimestamp'),
            namespaceprefix_, eol_))
        if self.annulmentCode is not None:
            namespaceprefix_ = self.annulmentCode_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.annulmentCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentCode>%s</%sannulmentCode>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.annulmentCode), input_name='annulmentCode')), namespaceprefix_,
                                                                       eol_))
        if self.annulmentReason is not None:
            namespaceprefix_ = self.annulmentReason_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.annulmentReason_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentReason>%s</%sannulmentReason>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.annulmentReason), input_name='annulmentReason')),
                                                                           namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='InvoiceAnnulmentType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/annul}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/annul}' + name_,
                                        nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.annulmentReference is not None:
            annulmentReference_ = self.annulmentReference
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentReference').text = self.gds_format_string(
                annulmentReference_)
        if self.annulmentTimestamp is not None:
            annulmentTimestamp_ = self.annulmentTimestamp
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentTimestamp').text = self.gds_format_datetime(
                annulmentTimestamp_)
        if self.annulmentCode is not None:
            annulmentCode_ = self.annulmentCode
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentCode').text = self.gds_format_string(
                annulmentCode_)
        if self.annulmentReason is not None:
            annulmentReason_ = self.annulmentReason
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/annul}annulmentReason').text = self.gds_format_string(
                annulmentReason_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceAnnulmentType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.annulmentReference is not None:
            showIndent(outfile, level)
            outfile.write('annulmentReference=%s,\n' % self.gds_encode(quote_python(self.annulmentReference)))
        if self.annulmentTimestamp is not None:
            showIndent(outfile, level)
            outfile.write(
                'annulmentTimestamp=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(
                    self.annulmentTimestamp, input_name='annulmentTimestamp'))
        if self.annulmentCode is not None:
            showIndent(outfile, level)
            outfile.write('annulmentCode=%s,\n' % self.gds_encode(quote_python(self.annulmentCode)))
        if self.annulmentReason is not None:
            showIndent(outfile, level)
            outfile.write('annulmentReason=%s,\n' % self.gds_encode(quote_python(self.annulmentReason)))

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
        if nodeName_ == 'annulmentReference':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'annulmentReference')
            value_ = self.gds_validate_string(value_, node, 'annulmentReference')
            self.annulmentReference = value_
            self.annulmentReference_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.annulmentReference)
        elif nodeName_ == 'annulmentTimestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.annulmentTimestamp = dval_
            self.annulmentTimestamp_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.annulmentTimestamp)
        elif nodeName_ == 'annulmentCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'annulmentCode')
            value_ = self.gds_validate_string(value_, node, 'annulmentCode')
            self.annulmentCode = value_
            self.annulmentCode_nsprefix_ = child_.prefix
            # validate type AnnulmentCodeType
            self.validate_AnnulmentCodeType(self.annulmentCode)
        elif nodeName_ == 'annulmentReason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'annulmentReason')
            value_ = self.gds_validate_string(value_, node, 'annulmentReason')
            self.annulmentReason = value_
            self.annulmentReason_nsprefix_ = child_.prefix
            # validate type SimpleText1024NotBlankType
            self.validate_SimpleText1024NotBlankType(self.annulmentReason)
