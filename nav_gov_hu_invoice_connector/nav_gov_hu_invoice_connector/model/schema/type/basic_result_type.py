from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    ModulenotfoundExp_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, GenerateDSNamespaceTypePrefixes_, quote_xml, quote_python, \
    SaveElementTreeNode, Tag_pattern_, find_attr_value_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class BasicResultType(GeneratedsSuper):
    """BasicResultType -- Alap válaszeredmény adatok
    Basic result data
    funcCode -- Feldolgozási eredmény
                Processing result
    errorCode -- A feldolgozási hibakód
                Processing error code
    message -- Feldolgozási üzenet
                Processing message
    notifications -- Egyéb értesítések
                Miscellaneous notifications

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, funcCode=None, errorCode=None, message=None, notifications=None, extensiontype_=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.funcCode = funcCode
        self.validate_FunctionCodeType(self.funcCode)
        self.funcCode_nsprefix_ = None
        self.errorCode = errorCode
        self.validate_SimpleText50NotBlankType(self.errorCode)
        self.errorCode_nsprefix_ = None
        self.message = message
        self.validate_SimpleText1024NotBlankType(self.message)
        self.message_nsprefix_ = None
        self.notifications = notifications
        self.notifications_nsprefix_ = None
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BasicResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BasicResultType.subclass:
            return BasicResultType.subclass(*args_, **kwargs_)
        else:
            return BasicResultType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_funcCode(self):
        return self.funcCode

    def set_funcCode(self, funcCode):
        self.funcCode = funcCode

    def get_errorCode(self):
        return self.errorCode

    def set_errorCode(self, errorCode):
        self.errorCode = errorCode

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

    def get_notifications(self):
        return self.notifications

    def set_notifications(self, notifications):
        self.notifications = notifications

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def validate_FunctionCodeType(self, value):
        result = True
        # Validate type FunctionCodeType, a restriction on AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['OK', 'ERROR']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on FunctionCodeType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FunctionCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FunctionCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

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
                self.funcCode is not None or
                self.errorCode is not None or
                self.message is not None or
                self.notifications is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='BasicResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BasicResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BasicResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BasicResultType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BasicResultType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BasicResultType'):
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
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='BasicResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.funcCode is not None:
            namespaceprefix_ = self.funcCode_nsprefix_ + ':' if (UseCapturedNS_ and self.funcCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfuncCode>%s</%sfuncCode>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.funcCode), input_name='funcCode')),
                namespaceprefix_, eol_))
        if self.errorCode is not None:
            namespaceprefix_ = self.errorCode_nsprefix_ + ':' if (UseCapturedNS_ and self.errorCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%serrorCode>%s</%serrorCode>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.errorCode), input_name='errorCode')), namespaceprefix_, eol_))
        if self.message is not None:
            namespaceprefix_ = self.message_nsprefix_ + ':' if (UseCapturedNS_ and self.message_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smessage>%s</%smessage>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.message), input_name='message')),
                namespaceprefix_, eol_))
        if self.notifications is not None:
            namespaceprefix_ = self.notifications_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.notifications_nsprefix_) else ''
            self.notifications.export(outfile, level, namespaceprefix_, namespacedef_='', name_='notifications',
                                      pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='BasicResultType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_,
                                        nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.funcCode is not None:
            funcCode_ = self.funcCode
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}funcCode').text = self.gds_format_string(
                funcCode_)
        if self.errorCode is not None:
            errorCode_ = self.errorCode
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}errorCode').text = self.gds_format_string(
                errorCode_)
        if self.message is not None:
            message_ = self.message
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}message').text = self.gds_format_string(
                message_)
        if self.notifications is not None:
            notifications_ = self.notifications
            notifications_.to_etree(element, name_='notifications', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='BasicResultType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.funcCode is not None:
            showIndent(outfile, level)
            outfile.write('funcCode=%s,\n' % self.gds_encode(quote_python(self.funcCode)))
        if self.errorCode is not None:
            showIndent(outfile, level)
            outfile.write('errorCode=%s,\n' % self.gds_encode(quote_python(self.errorCode)))
        if self.message is not None:
            showIndent(outfile, level)
            outfile.write('message=%s,\n' % self.gds_encode(quote_python(self.message)))
        if self.notifications is not None:
            showIndent(outfile, level)
            outfile.write('notifications=model_.NotificationsType(\n')
            self.notifications.exportLiteral(outfile, level, name_='notifications')
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
        if nodeName_ == 'funcCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'funcCode')
            value_ = self.gds_validate_string(value_, node, 'funcCode')
            self.funcCode = value_
            self.funcCode_nsprefix_ = child_.prefix
            # validate type FunctionCodeType
            self.validate_FunctionCodeType(self.funcCode)
        elif nodeName_ == 'errorCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'errorCode')
            value_ = self.gds_validate_string(value_, node, 'errorCode')
            self.errorCode = value_
            self.errorCode_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.errorCode)
        elif nodeName_ == 'message':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'message')
            value_ = self.gds_validate_string(value_, node, 'message')
            self.message = value_
            self.message_nsprefix_ = child_.prefix
            # validate type SimpleText1024NotBlankType
            self.validate_SimpleText1024NotBlankType(self.message)
        elif nodeName_ == 'notifications':
            obj_ = NotificationsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.notifications = obj_
            obj_.original_tagname_ = 'notifications'
