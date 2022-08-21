from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, GenerateDSNamespaceDefs_, \
    UseCapturedNS_, showIndent, ModulenotfoundExp_, quote_xml, SaveElementTreeNode, Tag_pattern_, CryptoType, \
    quote_python

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_

class UserHeaderType(GeneratedsSuper):
    """UserHeaderType -- A kérés authentikációs adatai
    Authentication data of the request
    login -- A technikai felhasználó login neve
                Login name of the technical user
    passwordHash -- A technikai felhasználó jelszavának hash értéke
                Hash value of the technical user's password
    taxNumber -- A rendszerben regisztrált adózó adószáma, aki nevében a technikai felhasználó tevékenykedik
                The taxpayer's tax number, whose name the technical user operates in
    requestSignature -- A kérés aláírásának hash értéke
                Hash value of the request's signature

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, login=None, passwordHash=None, taxNumber=None, requestSignature=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "common"
        self.login = login
        self.validate_LoginType(self.login)
        self.login_nsprefix_ = "common"
        self.passwordHash = passwordHash
        self.passwordHash_nsprefix_ = "common"
        self.taxNumber = taxNumber
        self.validate_TaxpayerIdType(self.taxNumber)
        self.taxNumber_nsprefix_ = "common"
        self.requestSignature = requestSignature
        self.requestSignature_nsprefix_ = "common"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UserHeaderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UserHeaderType.subclass:
            return UserHeaderType.subclass(*args_, **kwargs_)
        else:
            return UserHeaderType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_passwordHash(self):
        return self.passwordHash

    def set_passwordHash(self, passwordHash):
        self.passwordHash = passwordHash

    def get_taxNumber(self):
        return self.taxNumber

    def set_taxNumber(self, taxNumber):
        self.taxNumber = taxNumber

    def get_requestSignature(self):
        return self.requestSignature

    def set_requestSignature(self, requestSignature):
        self.requestSignature = requestSignature

    def validate_LoginType(self, value):
        result = True
        # Validate type LoginType, a restriction on AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LoginType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LoginType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LoginType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LoginType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_LoginType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_LoginType_patterns_,))
                result = False
        return result

    validate_LoginType_patterns_ = [['^([a-zA-Z0-9]{6,15})$']]

    def validate_TaxpayerIdType(self, value):
        result = True
        # Validate type TaxpayerIdType, a restriction on AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on TaxpayerIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TaxpayerIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TaxpayerIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TaxpayerIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_TaxpayerIdType_patterns_,))
                result = False
        return result

    validate_TaxpayerIdType_patterns_ = [['^([0-9]{8})$']]

    def _hasContent(self):
        if (
                self.login is not None or
                self.passwordHash is not None or
                self.taxNumber is not None or
                self.requestSignature is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='UserHeaderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UserHeaderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UserHeaderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UserHeaderType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UserHeaderType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UserHeaderType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='UserHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.login is not None:
            namespaceprefix_ = self.login_nsprefix_ + ':' if (UseCapturedNS_ and self.login_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slogin>%s</%slogin>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.login), input_name='login')),
                namespaceprefix_, eol_))
        if self.passwordHash is not None:
            namespaceprefix_ = self.passwordHash_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.passwordHash_nsprefix_) else ''
            self.passwordHash.export(outfile, level, namespaceprefix_, namespacedef_='', name_='passwordHash',
                                     pretty_print=pretty_print)
        if self.taxNumber is not None:
            namespaceprefix_ = self.taxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.taxNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxNumber>%s</%staxNumber>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.taxNumber), input_name='taxNumber')), namespaceprefix_, eol_))
        if self.requestSignature is not None:
            namespaceprefix_ = self.requestSignature_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.requestSignature_nsprefix_) else ''
            self.requestSignature.export(outfile, level, namespaceprefix_, namespacedef_='', name_='requestSignature',
                                         pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='UserHeaderType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_,
                                        nsmap=nsmap_)
        if self.login is not None:
            login_ = self.login
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}login').text = self.gds_format_string(login_)
        if self.passwordHash is not None:
            passwordHash_ = self.passwordHash
            passwordHash_.to_etree(element, name_='passwordHash', mapping_=mapping_, nsmap_=nsmap_)
        if self.taxNumber is not None:
            taxNumber_ = self.taxNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}taxNumber').text = self.gds_format_string(
                taxNumber_)
        if self.requestSignature is not None:
            requestSignature_ = self.requestSignature
            requestSignature_.to_etree(element, name_='requestSignature', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='UserHeaderType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.login is not None:
            showIndent(outfile, level)
            outfile.write('login=%s,\n' % self.gds_encode(quote_python(self.login)))
        if self.passwordHash is not None:
            showIndent(outfile, level)
            outfile.write('passwordHash=model_.CryptoType(\n')
            self.passwordHash.exportLiteral(outfile, level, name_='passwordHash')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.taxNumber is not None:
            showIndent(outfile, level)
            outfile.write('taxNumber=%s,\n' % self.gds_encode(quote_python(self.taxNumber)))
        if self.requestSignature is not None:
            showIndent(outfile, level)
            outfile.write('requestSignature=model_.CryptoType(\n')
            self.requestSignature.exportLiteral(outfile, level, name_='requestSignature')
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
        if nodeName_ == 'login':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'login')
            value_ = self.gds_validate_string(value_, node, 'login')
            self.login = value_
            self.login_nsprefix_ = child_.prefix
            # validate type LoginType
            self.validate_LoginType(self.login)
        elif nodeName_ == 'passwordHash':
            obj_ = CryptoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.passwordHash = obj_
            obj_.original_tagname_ = 'passwordHash'
        elif nodeName_ == 'taxNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxNumber')
            value_ = self.gds_validate_string(value_, node, 'taxNumber')
            self.taxNumber = value_
            self.taxNumber_nsprefix_ = child_.prefix
            # validate type TaxpayerIdType
            self.validate_TaxpayerIdType(self.taxNumber)
        elif nodeName_ == 'requestSignature':
            obj_ = CryptoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.requestSignature = obj_
            obj_.original_tagname_ = 'requestSignature'
