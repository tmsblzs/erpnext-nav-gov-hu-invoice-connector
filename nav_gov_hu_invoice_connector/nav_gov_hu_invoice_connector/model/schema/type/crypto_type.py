from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    ModulenotfoundExp_, _cast, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_attrib, SaveElementTreeNode, get_all_text_, \
    Tag_pattern_, find_attr_value_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class CryptoType(GeneratedsSuper):
    """CryptoType -- Kriptográfiai metódust leírótípus
    Denoting type of cryptographic method

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, cryptoType=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "common"
        self.cryptoType = _cast(None, cryptoType)
        self.cryptoType_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CryptoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CryptoType.subclass:
            return CryptoType.subclass(*args_, **kwargs_)
        else:
            return CryptoType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_cryptoType(self):
        return self.cryptoType

    def set_cryptoType(self, cryptoType):
        self.cryptoType = cryptoType

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = valueOf_

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

    def validate_SimpleText50NotBlankType(self, value):
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

    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='CryptoType',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CryptoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CryptoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CryptoType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CryptoType',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CryptoType'):
        if self.cryptoType is not None and 'cryptoType' not in already_processed:
            already_processed.add('cryptoType')
            outfile.write(' cryptoType=%s' % (quote_attrib(self.cryptoType),))

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='CryptoType',
                        fromsubclass_=False, pretty_print=True):
        pass

    def to_etree(self, parent_element=None, name_='CryptoType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_,
                                        nsmap=nsmap_)
        if self.cryptoType is not None:
            element.set('cryptoType', self.cryptoType)
        if self._hasContent():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='CryptoType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.cryptoType is not None and 'cryptoType' not in already_processed:
            already_processed.add('cryptoType')
            showIndent(outfile, level)
            outfile.write('cryptoType=%s,\n' % (self.cryptoType,))

    def _exportLiteralChildren(self, outfile, level, name_):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('cryptoType', node)
        if value is not None and 'cryptoType' not in already_processed:
            already_processed.add('cryptoType')
            self.cryptoType = value
            self.validate_SimpleText50NotBlankType(self.cryptoType)  # validate type SimpleText50NotBlankType

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
