from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_request_type import \
    BasicRequestType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_response_type import \
    BasicResponseType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.software_type import SoftwareType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class BasicOnlineInvoiceResponseType(BasicResponseType):
    """BasicOnlineInvoiceResponseType -- Online Számla rendszerre specifikus általános válasz adatok
      Online Invoice specific basic response data
    software -- A számlázó program adatai
    Billing software data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicResponseType

    def __init__(self, header=None, result=None, software=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("BasicOnlineInvoiceResponseType"), self).__init__(header, result, extensiontype_, **kwargs_)
        self.software = software
        self.software_nsprefix_ = None
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BasicOnlineInvoiceResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BasicOnlineInvoiceResponseType.subclass:
            return BasicOnlineInvoiceResponseType.subclass(*args_, **kwargs_)
        else:
            return BasicOnlineInvoiceResponseType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_software(self):
        return self.software

    def set_software(self, software):
        self.software = software

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                self.software is not None or
                super(BasicOnlineInvoiceResponseType, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='BasicOnlineInvoiceResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BasicOnlineInvoiceResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BasicOnlineInvoiceResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                               name_='BasicOnlineInvoiceResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                 name_='BasicOnlineInvoiceResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='BasicOnlineInvoiceResponseType'):
        super(BasicOnlineInvoiceResponseType, self)._exportAttributes(outfile, level, already_processed,
                                                                      namespaceprefix_,
                                                                      name_='BasicOnlineInvoiceResponseType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='BasicOnlineInvoiceResponseType', fromsubclass_=False, pretty_print=True):
        super(BasicOnlineInvoiceResponseType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_,
                                                                    name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.software is not None:
            namespaceprefix_ = self.software_nsprefix_ + ':' if (UseCapturedNS_ and self.software_nsprefix_) else ''
            self.software.export(outfile, level, namespaceprefix_, namespacedef_='', name_='software',
                                 pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='BasicOnlineInvoiceResponseType', mapping_=None, nsmap_=None):
        element = super(BasicOnlineInvoiceResponseType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.software is not None:
            software_ = self.software
            software_.to_etree(element, name_='software', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='BasicOnlineInvoiceResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(BasicOnlineInvoiceResponseType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)

    def _exportLiteralChildren(self, outfile, level, name_):
        super(BasicOnlineInvoiceResponseType, self)._exportLiteralChildren(outfile, level, name_)
        if self.software is not None:
            showIndent(outfile, level)
            outfile.write('software=model_.SoftwareType(\n')
            self.software.exportLiteral(outfile, level, name_='software')
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
        super(BasicOnlineInvoiceResponseType, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'software':
            obj_ = SoftwareType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.software = obj_
            obj_.original_tagname_ = 'software'
        super(BasicOnlineInvoiceResponseType, self)._buildChildren(child_, node, nodeName_, True)
