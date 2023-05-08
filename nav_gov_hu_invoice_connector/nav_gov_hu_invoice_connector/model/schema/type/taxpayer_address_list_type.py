import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.taxpayer_address_item_type import \
    TaxpayerAddressItemType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class TaxpayerAddressListType(GeneratedsSuper):
    """TaxpayerAddressListType -- Adózói cím lista típus
    Taxpayer address_list list type
    taxpayerAddressItem -- Adózói címsor adat
    Taxpayer address_list item

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, taxpayerAddressItem=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if taxpayerAddressItem is None:
            self.taxpayerAddressItem = []
        else:
            self.taxpayerAddressItem = taxpayerAddressItem
        self.taxpayerAddressItem_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TaxpayerAddressListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TaxpayerAddressListType.subclass:
            return TaxpayerAddressListType.subclass(*args_, **kwargs_)
        else:
            return TaxpayerAddressListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_taxpayerAddressItem(self):
        return self.taxpayerAddressItem
    def set_taxpayerAddressItem(self, taxpayerAddressItem):
        self.taxpayerAddressItem = taxpayerAddressItem
    def add_taxpayerAddressItem(self, value):
        self.taxpayerAddressItem.append(value)
    def insert_taxpayerAddressItem_at(self, index, value):
        self.taxpayerAddressItem.insert(index, value)
    def replace_taxpayerAddressItem_at(self, index, value):
        self.taxpayerAddressItem[index] = value
    def _hasContent(self):
        if (
            self.taxpayerAddressItem
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='TaxpayerAddressListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TaxpayerAddressListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TaxpayerAddressListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TaxpayerAddressListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TaxpayerAddressListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TaxpayerAddressListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='TaxpayerAddressListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for taxpayerAddressItem_ in self.taxpayerAddressItem:
            namespaceprefix_ = self.taxpayerAddressItem_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerAddressItem_nsprefix_) else ''
            taxpayerAddressItem_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='taxpayerAddressItem', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='TaxpayerAddressListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        for taxpayerAddressItem_ in self.taxpayerAddressItem:
            taxpayerAddressItem_.to_etree(element, name_='taxpayerAddressItem', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TaxpayerAddressListType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('taxpayerAddressItem=[\n')
        level += 1
        for taxpayerAddressItem_ in self.taxpayerAddressItem:
            showIndent(outfile, level)
            outfile.write('model_.TaxpayerAddressItemType(\n')
            taxpayerAddressItem_.exportLiteral(outfile, level, name_='TaxpayerAddressItemType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'taxpayerAddressItem':
            obj_ = TaxpayerAddressItemType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.taxpayerAddressItem.append(obj_)
            obj_.original_tagname_ = 'taxpayerAddressItem'
