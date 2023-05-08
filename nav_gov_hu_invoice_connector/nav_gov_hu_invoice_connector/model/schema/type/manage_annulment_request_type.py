import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.annulment_operation_list_type import \
    AnnulmentOperationListType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_request_type import \
    BasicOnlineInvoiceRequestType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ManageAnnulmentRequestType(BasicOnlineInvoiceRequestType):
    """ManageAnnulmentRequestType -- A POST /manageAnnulment REST operáció kérés típusa
    Request type of the POST /manageAnnulment REST operation exchangeToken -- A tranzakcióhoz kiadott egyedi és
            dekódolt token
    The decoded unique token issued for the current transaction annulmentOperations -- A kéréshez tartozó kötegelt technikai
            érvénytelenítések
    Batch technical annulment operations of the request

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceRequestType
    def __init__(self, header=None, user=None, software=None, exchangeToken=None, annulmentOperations=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ManageAnnulmentRequestType"), self).__init__(header, user, software, extensiontype_,  **kwargs_)
        self.exchangeToken = exchangeToken
        self.validate_SimpleText50NotBlankType(self.exchangeToken)
        self.exchangeToken_nsprefix_ = "common"
        self.annulmentOperations = annulmentOperations
        self.annulmentOperations_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManageAnnulmentRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManageAnnulmentRequestType.subclass:
            return ManageAnnulmentRequestType.subclass(*args_, **kwargs_)
        else:
            return ManageAnnulmentRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_exchangeToken(self):
        return self.exchangeToken
    def set_exchangeToken(self, exchangeToken):
        self.exchangeToken = exchangeToken
    def get_annulmentOperations(self):
        return self.annulmentOperations
    def set_annulmentOperations(self, annulmentOperations):
        self.annulmentOperations = annulmentOperations
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
    def _hasContent(self):
        if (
            self.exchangeToken is not None or
            self.annulmentOperations is not None or
            super(ManageAnnulmentRequestType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ManageAnnulmentRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManageAnnulmentRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManageAnnulmentRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManageAnnulmentRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManageAnnulmentRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ManageAnnulmentRequestType'):
        super(ManageAnnulmentRequestType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManageAnnulmentRequestType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ManageAnnulmentRequestType', fromsubclass_=False, pretty_print=True):
        super(ManageAnnulmentRequestType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.exchangeToken is not None:
            namespaceprefix_ = self.exchangeToken_nsprefix_ + ':' if (UseCapturedNS_ and self.exchangeToken_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexchangeToken>%s</%sexchangeToken>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.exchangeToken), input_name='exchangeToken')), namespaceprefix_ , eol_))
        if self.annulmentOperations is not None:
            namespaceprefix_ = self.annulmentOperations_nsprefix_ + ':' if (UseCapturedNS_ and self.annulmentOperations_nsprefix_) else ''
            self.annulmentOperations.export(outfile, level, namespaceprefix_, namespacedef_='', name_='annulmentOperations', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ManageAnnulmentRequestType', mapping_=None, nsmap_=None):
        element = super(ManageAnnulmentRequestType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.exchangeToken is not None:
            exchangeToken_ = self.exchangeToken
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}exchangeToken').text = self.gds_format_string(exchangeToken_)
        if self.annulmentOperations is not None:
            annulmentOperations_ = self.annulmentOperations
            annulmentOperations_.to_etree(element, name_='annulmentOperations', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ManageAnnulmentRequestType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(ManageAnnulmentRequestType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(ManageAnnulmentRequestType, self)._exportLiteralChildren(outfile, level, name_)
        if self.exchangeToken is not None:
            showIndent(outfile, level)
            outfile.write('exchangeToken=%s,\n' % self.gds_encode(quote_python(self.exchangeToken)))
        if self.annulmentOperations is not None:
            showIndent(outfile, level)
            outfile.write('annulmentOperations=model_.AnnulmentOperationListType(\n')
            self.annulmentOperations.exportLiteral(outfile, level, name_='annulmentOperations')
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
        super(ManageAnnulmentRequestType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'exchangeToken':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'exchangeToken')
            value_ = self.gds_validate_string(value_, node, 'exchangeToken')
            self.exchangeToken = value_
            self.exchangeToken_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.exchangeToken)
        elif nodeName_ == 'annulmentOperations':
            obj_ = AnnulmentOperationListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.annulmentOperations = obj_
            obj_.original_tagname_ = 'annulmentOperations'
        super(ManageAnnulmentRequestType, self)._buildChildren(child_, node, nodeName_, True)
