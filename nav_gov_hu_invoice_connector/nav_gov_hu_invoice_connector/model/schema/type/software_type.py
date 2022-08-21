from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class SoftwareType(GeneratedsSuper):
    """SoftwareType -- A számlázó program adatai
    Billing software data
    softwareId -- A számlázó program azonosítója
    Billing software ID
    softwareName -- A számlázó program neve
    Billing software name
    softwareOperation -- A számlázó program működési típusa (lokális program vagy online számlázó szolgáltatás)
    Billing software operation type (local program or online billing service)
    softwareMainVersion -- A számlázó program fő verziója
    Billing software main version
    softwareDevName -- A számlázó program fejlesztőjének neve
    Name of the billing software's developer
    softwareDevContact -- A számlázóprogram fejlesztőjének elektronikus elérhetősége
    Electronic contact of the billing software's developer
    softwareDevCountryCode -- A számlázó program fejlesztőjének ISO-3166 alpha2 országkódja
    ISO-3166 alpha2 country code of the billing software's developer
    softwareDevTaxNumber -- A számlázó program fejlesztőjének adószáma
    Tax number of the billing software's developer

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, softwareId=None, softwareName=None, softwareOperation=None, softwareMainVersion=None,
                 softwareDevName=None, softwareDevContact=None, softwareDevCountryCode=None, softwareDevTaxNumber=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.softwareId = softwareId
        self.validate_SoftwareIdType(self.softwareId)
        self.softwareId_nsprefix_ = None
        self.softwareName = softwareName
        self.validate_SimpleText50NotBlankType(self.softwareName)
        self.softwareName_nsprefix_ = None
        self.softwareOperation = softwareOperation
        self.validate_SoftwareOperationType(self.softwareOperation)
        self.softwareOperation_nsprefix_ = None
        self.softwareMainVersion = softwareMainVersion
        self.validate_SimpleText15NotBlankType(self.softwareMainVersion)
        self.softwareMainVersion_nsprefix_ = None
        self.softwareDevName = softwareDevName
        self.validate_SimpleText512NotBlankType(self.softwareDevName)
        self.softwareDevName_nsprefix_ = None
        self.softwareDevContact = softwareDevContact
        self.validate_SimpleText200NotBlankType(self.softwareDevContact)
        self.softwareDevContact_nsprefix_ = None
        self.softwareDevCountryCode = softwareDevCountryCode
        self.validate_CountryCodeType(self.softwareDevCountryCode)
        self.softwareDevCountryCode_nsprefix_ = None
        self.softwareDevTaxNumber = softwareDevTaxNumber
        self.validate_SimpleText50NotBlankType(self.softwareDevTaxNumber)
        self.softwareDevTaxNumber_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SoftwareType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SoftwareType.subclass:
            return SoftwareType.subclass(*args_, **kwargs_)
        else:
            return SoftwareType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_softwareId(self):
        return self.softwareId

    def set_softwareId(self, softwareId):
        self.softwareId = softwareId

    def get_softwareName(self):
        return self.softwareName

    def set_softwareName(self, softwareName):
        self.softwareName = softwareName

    def get_softwareOperation(self):
        return self.softwareOperation

    def set_softwareOperation(self, softwareOperation):
        self.softwareOperation = softwareOperation

    def get_softwareMainVersion(self):
        return self.softwareMainVersion

    def set_softwareMainVersion(self, softwareMainVersion):
        self.softwareMainVersion = softwareMainVersion

    def get_softwareDevName(self):
        return self.softwareDevName

    def set_softwareDevName(self, softwareDevName):
        self.softwareDevName = softwareDevName

    def get_softwareDevContact(self):
        return self.softwareDevContact

    def set_softwareDevContact(self, softwareDevContact):
        self.softwareDevContact = softwareDevContact

    def get_softwareDevCountryCode(self):
        return self.softwareDevCountryCode

    def set_softwareDevCountryCode(self, softwareDevCountryCode):
        self.softwareDevCountryCode = softwareDevCountryCode

    def get_softwareDevTaxNumber(self):
        return self.softwareDevTaxNumber

    def set_softwareDevTaxNumber(self, softwareDevTaxNumber):
        self.softwareDevTaxNumber = softwareDevTaxNumber

    def validate_SoftwareIdType(self, value):
        result = True
        # Validate type SoftwareIdType, a restriction on common:AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on SoftwareIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SoftwareIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SoftwareIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SoftwareIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SoftwareIdType_patterns_,))
                result = False
        return result

    validate_SoftwareIdType_patterns_ = [['^([0-9A-Z\\-]{18})$']]

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

    def validate_SoftwareOperationType(self, value):
        result = True
        # Validate type SoftwareOperationType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['LOCAL_SOFTWARE', 'ONLINE_SERVICE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on SoftwareOperationType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SoftwareOperationType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SoftwareOperationType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_SimpleText15NotBlankType(self, value):
        result = True
        # Validate type SimpleText15NotBlankType, a restriction on AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText15NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText15NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText15NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText15NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText15NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def validate_SimpleText200NotBlankType(self, value):
        result = True
        # Validate type SimpleText200NotBlankType, a restriction on AtomicStringType200.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText200NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText200NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText200NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText200NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText200NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def validate_CountryCodeType(self, value):
        result = True
        # Validate type CountryCodeType, a restriction on AtomicStringType2.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on CountryCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CountryCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CountryCodeType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CountryCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_CountryCodeType_patterns_,))
                result = False
        return result

    validate_CountryCodeType_patterns_ = [['^([A-Z]{2})$']]

    def _hasContent(self):
        if (
                self.softwareId is not None or
                self.softwareName is not None or
                self.softwareOperation is not None or
                self.softwareMainVersion is not None or
                self.softwareDevName is not None or
                self.softwareDevContact is not None or
                self.softwareDevCountryCode is not None or
                self.softwareDevTaxNumber is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
               name_='SoftwareType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SoftwareType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SoftwareType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SoftwareType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SoftwareType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SoftwareType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
                        name_='SoftwareType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.softwareId is not None:
            namespaceprefix_ = self.softwareId_nsprefix_ + ':' if (UseCapturedNS_ and self.softwareId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareId>%s</%ssoftwareId>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.softwareId), input_name='softwareId')), namespaceprefix_, eol_))
        if self.softwareName is not None:
            namespaceprefix_ = self.softwareName_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.softwareName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareName>%s</%ssoftwareName>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.softwareName), input_name='softwareName')), namespaceprefix_,
                                                                     eol_))
        if self.softwareOperation is not None:
            namespaceprefix_ = self.softwareOperation_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.softwareOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareOperation>%s</%ssoftwareOperation>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.softwareOperation), input_name='softwareOperation')),
                                                                               namespaceprefix_, eol_))
        if self.softwareMainVersion is not None:
            namespaceprefix_ = self.softwareMainVersion_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.softwareMainVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareMainVersion>%s</%ssoftwareMainVersion>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.softwareMainVersion), input_name='softwareMainVersion')),
                                                                                   namespaceprefix_, eol_))
        if self.softwareDevName is not None:
            namespaceprefix_ = self.softwareDevName_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.softwareDevName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareDevName>%s</%ssoftwareDevName>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.softwareDevName), input_name='softwareDevName')),
                                                                           namespaceprefix_, eol_))
        if self.softwareDevContact is not None:
            namespaceprefix_ = self.softwareDevContact_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.softwareDevContact_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareDevContact>%s</%ssoftwareDevContact>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.softwareDevContact), input_name='softwareDevContact')),
                                                                                 namespaceprefix_, eol_))
        if self.softwareDevCountryCode is not None:
            namespaceprefix_ = self.softwareDevCountryCode_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.softwareDevCountryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareDevCountryCode>%s</%ssoftwareDevCountryCode>%s' % (namespaceprefix_,
                                                                                         self.gds_encode(
                                                                                             self.gds_format_string(
                                                                                                 quote_xml(
                                                                                                     self.softwareDevCountryCode),
                                                                                                 input_name='softwareDevCountryCode')),
                                                                                         namespaceprefix_, eol_))
        if self.softwareDevTaxNumber is not None:
            namespaceprefix_ = self.softwareDevTaxNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.softwareDevTaxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssoftwareDevTaxNumber>%s</%ssoftwareDevTaxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.softwareDevTaxNumber), input_name='softwareDevTaxNumber')),
                                                                                     namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='SoftwareType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.softwareId is not None:
            softwareId_ = self.softwareId
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareId').text = self.gds_format_string(
                softwareId_)
        if self.softwareName is not None:
            softwareName_ = self.softwareName
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareName').text = self.gds_format_string(
                softwareName_)
        if self.softwareOperation is not None:
            softwareOperation_ = self.softwareOperation
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareOperation').text = self.gds_format_string(
                softwareOperation_)
        if self.softwareMainVersion is not None:
            softwareMainVersion_ = self.softwareMainVersion
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareMainVersion').text = self.gds_format_string(
                softwareMainVersion_)
        if self.softwareDevName is not None:
            softwareDevName_ = self.softwareDevName
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevName').text = self.gds_format_string(
                softwareDevName_)
        if self.softwareDevContact is not None:
            softwareDevContact_ = self.softwareDevContact
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevContact').text = self.gds_format_string(
                softwareDevContact_)
        if self.softwareDevCountryCode is not None:
            softwareDevCountryCode_ = self.softwareDevCountryCode
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevCountryCode').text = self.gds_format_string(
                softwareDevCountryCode_)
        if self.softwareDevTaxNumber is not None:
            softwareDevTaxNumber_ = self.softwareDevTaxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}softwareDevTaxNumber').text = self.gds_format_string(
                softwareDevTaxNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='SoftwareType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.softwareId is not None:
            showIndent(outfile, level)
            outfile.write('softwareId=%s,\n' % self.gds_encode(quote_python(self.softwareId)))
        if self.softwareName is not None:
            showIndent(outfile, level)
            outfile.write('softwareName=%s,\n' % self.gds_encode(quote_python(self.softwareName)))
        if self.softwareOperation is not None:
            showIndent(outfile, level)
            outfile.write('softwareOperation=%s,\n' % self.gds_encode(quote_python(self.softwareOperation)))
        if self.softwareMainVersion is not None:
            showIndent(outfile, level)
            outfile.write('softwareMainVersion=%s,\n' % self.gds_encode(quote_python(self.softwareMainVersion)))
        if self.softwareDevName is not None:
            showIndent(outfile, level)
            outfile.write('softwareDevName=%s,\n' % self.gds_encode(quote_python(self.softwareDevName)))
        if self.softwareDevContact is not None:
            showIndent(outfile, level)
            outfile.write('softwareDevContact=%s,\n' % self.gds_encode(quote_python(self.softwareDevContact)))
        if self.softwareDevCountryCode is not None:
            showIndent(outfile, level)
            outfile.write('softwareDevCountryCode=%s,\n' % self.gds_encode(quote_python(self.softwareDevCountryCode)))
        if self.softwareDevTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('softwareDevTaxNumber=%s,\n' % self.gds_encode(quote_python(self.softwareDevTaxNumber)))

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
        if nodeName_ == 'softwareId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareId')
            value_ = self.gds_validate_string(value_, node, 'softwareId')
            self.softwareId = value_
            self.softwareId_nsprefix_ = child_.prefix
            # validate type SoftwareIdType
            self.validate_SoftwareIdType(self.softwareId)
        elif nodeName_ == 'softwareName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareName')
            value_ = self.gds_validate_string(value_, node, 'softwareName')
            self.softwareName = value_
            self.softwareName_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.softwareName)
        elif nodeName_ == 'softwareOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareOperation')
            value_ = self.gds_validate_string(value_, node, 'softwareOperation')
            self.softwareOperation = value_
            self.softwareOperation_nsprefix_ = child_.prefix
            # validate type SoftwareOperationType
            self.validate_SoftwareOperationType(self.softwareOperation)
        elif nodeName_ == 'softwareMainVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareMainVersion')
            value_ = self.gds_validate_string(value_, node, 'softwareMainVersion')
            self.softwareMainVersion = value_
            self.softwareMainVersion_nsprefix_ = child_.prefix
            # validate type SimpleText15NotBlankType
            self.validate_SimpleText15NotBlankType(self.softwareMainVersion)
        elif nodeName_ == 'softwareDevName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareDevName')
            value_ = self.gds_validate_string(value_, node, 'softwareDevName')
            self.softwareDevName = value_
            self.softwareDevName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.softwareDevName)
        elif nodeName_ == 'softwareDevContact':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareDevContact')
            value_ = self.gds_validate_string(value_, node, 'softwareDevContact')
            self.softwareDevContact = value_
            self.softwareDevContact_nsprefix_ = child_.prefix
            # validate type SimpleText200NotBlankType
            self.validate_SimpleText200NotBlankType(self.softwareDevContact)
        elif nodeName_ == 'softwareDevCountryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareDevCountryCode')
            value_ = self.gds_validate_string(value_, node, 'softwareDevCountryCode')
            self.softwareDevCountryCode = value_
            self.softwareDevCountryCode_nsprefix_ = child_.prefix
            # validate type CountryCodeType
            self.validate_CountryCodeType(self.softwareDevCountryCode)
        elif nodeName_ == 'softwareDevTaxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'softwareDevTaxNumber')
            value_ = self.gds_validate_string(value_, node, 'softwareDevTaxNumber')
            self.softwareDevTaxNumber = value_
            self.softwareDevTaxNumber_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.softwareDevTaxNumber)
