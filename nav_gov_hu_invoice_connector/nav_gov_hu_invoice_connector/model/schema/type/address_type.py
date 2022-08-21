from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.detailed_address_type import \
    DetailedAddressType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.simple_address_type import \
    SimpleAddressType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_

class AddressType(GeneratedsSuper):
    """AddressType -- Cím típus, amely vagy egyszerű, vagy részletes címet tartalmaz
    Format of address_list that includes either a simple or a detailed address_list
    simpleAddress -- Egyszerű cím
                Simple address_list
    detailedAddress -- Részletes cím
                Detailed address_list

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, simpleAddress=None, detailedAddress=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.simpleAddress = simpleAddress
        self.simpleAddress_nsprefix_ = None
        self.detailedAddress = detailedAddress
        self.detailedAddress_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AddressType.subclass:
            return AddressType.subclass(*args_, **kwargs_)
        else:
            return AddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_simpleAddress(self):
        return self.simpleAddress
    def set_simpleAddress(self, simpleAddress):
        self.simpleAddress = simpleAddress
    def get_detailedAddress(self):
        return self.detailedAddress
    def set_detailedAddress(self, detailedAddress):
        self.detailedAddress = detailedAddress
    def _hasContent(self):
        if (
            self.simpleAddress is not None or
            self.detailedAddress is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.simpleAddress is not None:
            namespaceprefix_ = self.simpleAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.simpleAddress_nsprefix_) else ''
            self.simpleAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='simpleAddress', pretty_print=pretty_print)
        if self.detailedAddress is not None:
            namespaceprefix_ = self.detailedAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.detailedAddress_nsprefix_) else ''
            self.detailedAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='detailedAddress', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AddressType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/base}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/base}' + name_, nsmap=nsmap_)
        if self.simpleAddress is not None:
            simpleAddress_ = self.simpleAddress
            simpleAddress_.to_etree(element, name_='simpleAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.detailedAddress is not None:
            detailedAddress_ = self.detailedAddress
            detailedAddress_.to_etree(element, name_='detailedAddress', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AddressType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.simpleAddress is not None:
            showIndent(outfile, level)
            outfile.write('simpleAddress=model_.SimpleAddressType(\n')
            self.simpleAddress.exportLiteral(outfile, level, name_='simpleAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.detailedAddress is not None:
            showIndent(outfile, level)
            outfile.write('detailedAddress=model_.DetailedAddressType(\n')
            self.detailedAddress.exportLiteral(outfile, level, name_='detailedAddress')
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
        if nodeName_ == 'simpleAddress':
            obj_ = SimpleAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.simpleAddress = obj_
            obj_.original_tagname_ = 'simpleAddress'
        elif nodeName_ == 'detailedAddress':
            obj_ = DetailedAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.detailedAddress = obj_
            obj_.original_tagname_ = 'detailedAddress'
