from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    ModulenotfoundExp_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    UseCapturedNS_, showIndent, quote_xml, quote_python, SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceDefs_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class TechnicalValidationResultType(GeneratedsSuper):
    """TechnicalValidationResultType -- Technikai validációs választípus
    Technical validation response type
    validationResultCode -- Validációs eredmény
                Validation result
    validationErrorCode -- Validációs hibakód
                Validation error code
    message -- Feldolgozási üzenet
                Processing message

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, validationResultCode=None, validationErrorCode=None, message=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.validationResultCode = validationResultCode
        self.validate_TechnicalResultCodeType(self.validationResultCode)
        self.validationResultCode_nsprefix_ = None
        self.validationErrorCode = validationErrorCode
        self.validate_SimpleText100NotBlankType(self.validationErrorCode)
        self.validationErrorCode_nsprefix_ = None
        self.message = message
        self.validate_SimpleText1024NotBlankType(self.message)
        self.message_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TechnicalValidationResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TechnicalValidationResultType.subclass:
            return TechnicalValidationResultType.subclass(*args_, **kwargs_)
        else:
            return TechnicalValidationResultType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_validationResultCode(self):
        return self.validationResultCode

    def set_validationResultCode(self, validationResultCode):
        self.validationResultCode = validationResultCode

    def get_validationErrorCode(self):
        return self.validationErrorCode

    def set_validationErrorCode(self, validationErrorCode):
        self.validationErrorCode = validationErrorCode

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

    def validate_TechnicalResultCodeType(self, value):
        result = True
        # Validate type TechnicalResultCodeType, a restriction on AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['CRITICAL', 'ERROR']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TechnicalResultCodeType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TechnicalResultCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TechnicalResultCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

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
                self.validationResultCode is not None or
                self.validationErrorCode is not None or
                self.message is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='TechnicalValidationResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TechnicalValidationResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TechnicalValidationResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                               name_='TechnicalValidationResultType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                 name_='TechnicalValidationResultType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='TechnicalValidationResultType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='TechnicalValidationResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.validationResultCode is not None:
            namespaceprefix_ = self.validationResultCode_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.validationResultCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalidationResultCode>%s</%svalidationResultCode>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.validationResultCode), input_name='validationResultCode')),
                                                                                     namespaceprefix_, eol_))
        if self.validationErrorCode is not None:
            namespaceprefix_ = self.validationErrorCode_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.validationErrorCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalidationErrorCode>%s</%svalidationErrorCode>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.validationErrorCode), input_name='validationErrorCode')),
                                                                                   namespaceprefix_, eol_))
        if self.message is not None:
            namespaceprefix_ = self.message_nsprefix_ + ':' if (UseCapturedNS_ and self.message_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smessage>%s</%smessage>%s' % (
            namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.message), input_name='message')),
            namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='TechnicalValidationResultType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_,
                                        nsmap=nsmap_)
        if self.validationResultCode is not None:
            validationResultCode_ = self.validationResultCode
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}validationResultCode').text = self.gds_format_string(
                validationResultCode_)
        if self.validationErrorCode is not None:
            validationErrorCode_ = self.validationErrorCode
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}validationErrorCode').text = self.gds_format_string(
                validationErrorCode_)
        if self.message is not None:
            message_ = self.message
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}message').text = self.gds_format_string(
                message_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='TechnicalValidationResultType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.validationResultCode is not None:
            showIndent(outfile, level)
            outfile.write('validationResultCode=%s,\n' % self.gds_encode(quote_python(self.validationResultCode)))
        if self.validationErrorCode is not None:
            showIndent(outfile, level)
            outfile.write('validationErrorCode=%s,\n' % self.gds_encode(quote_python(self.validationErrorCode)))
        if self.message is not None:
            showIndent(outfile, level)
            outfile.write('message=%s,\n' % self.gds_encode(quote_python(self.message)))

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
        if nodeName_ == 'validationResultCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'validationResultCode')
            value_ = self.gds_validate_string(value_, node, 'validationResultCode')
            self.validationResultCode = value_
            self.validationResultCode_nsprefix_ = child_.prefix
            # validate type TechnicalResultCodeType
            self.validate_TechnicalResultCodeType(self.validationResultCode)
        elif nodeName_ == 'validationErrorCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'validationErrorCode')
            value_ = self.gds_validate_string(value_, node, 'validationErrorCode')
            self.validationErrorCode = value_
            self.validationErrorCode_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.validationErrorCode)
        elif nodeName_ == 'message':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'message')
            value_ = self.gds_validate_string(value_, node, 'message')
            self.message = value_
            self.message_nsprefix_ = child_.prefix
            # validate type SimpleText1024NotBlankType
            self.validate_SimpleText1024NotBlankType(self.message)
