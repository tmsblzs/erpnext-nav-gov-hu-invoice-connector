import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.detailed_address_type import \
    DetailedAddressType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class TaxpayerAddressItemType(GeneratedsSuper):
    """TaxpayerAddressItemType -- Adózói címsor adat
    Taxpayer address_list item
    taxpayerAddressType -- Adózói cím típus
    Taxpayer address_list type
    taxpayerAddress -- Az adózó címadatai
    Address data of the taxpayer

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, taxpayerAddressType=None, taxpayerAddress=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.taxpayerAddressType = taxpayerAddressType
        self.validate_TaxpayerAddressTypeType(self.taxpayerAddressType)
        self.taxpayerAddressType_nsprefix_ = None
        self.taxpayerAddress = taxpayerAddress
        self.taxpayerAddress_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TaxpayerAddressItemType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TaxpayerAddressItemType.subclass:
            return TaxpayerAddressItemType.subclass(*args_, **kwargs_)
        else:
            return TaxpayerAddressItemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_taxpayerAddressType(self):
        return self.taxpayerAddressType
    def set_taxpayerAddressType(self, taxpayerAddressType):
        self.taxpayerAddressType = taxpayerAddressType
    def get_taxpayerAddress(self):
        return self.taxpayerAddress
    def set_taxpayerAddress(self, taxpayerAddress):
        self.taxpayerAddress = taxpayerAddress
    def validate_TaxpayerAddressTypeType(self, value):
        result = True
        # Validate type TaxpayerAddressTypeType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['HQ', 'SITE', 'BRANCH']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TaxpayerAddressTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TaxpayerAddressTypeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TaxpayerAddressTypeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.taxpayerAddressType is not None or
            self.taxpayerAddress is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='TaxpayerAddressItemType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TaxpayerAddressItemType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TaxpayerAddressItemType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TaxpayerAddressItemType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TaxpayerAddressItemType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TaxpayerAddressItemType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='TaxpayerAddressItemType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.taxpayerAddressType is not None:
            namespaceprefix_ = self.taxpayerAddressType_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerAddressType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxpayerAddressType>%s</%staxpayerAddressType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxpayerAddressType), input_name='taxpayerAddressType')), namespaceprefix_ , eol_))
        if self.taxpayerAddress is not None:
            namespaceprefix_ = self.taxpayerAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerAddress_nsprefix_) else ''
            self.taxpayerAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='taxpayerAddress', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='TaxpayerAddressItemType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.taxpayerAddressType is not None:
            taxpayerAddressType_ = self.taxpayerAddressType
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerAddressType').text = self.gds_format_string(taxpayerAddressType_)
        if self.taxpayerAddress is not None:
            taxpayerAddress_ = self.taxpayerAddress
            taxpayerAddress_.to_etree(element, name_='taxpayerAddress', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TaxpayerAddressItemType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.taxpayerAddressType is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerAddressType=%s,\n' % self.gds_encode(quote_python(self.taxpayerAddressType)))
        if self.taxpayerAddress is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerAddress=model_.DetailedAddressType(\n')
            self.taxpayerAddress.exportLiteral(outfile, level, name_='taxpayerAddress')
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
        if nodeName_ == 'taxpayerAddressType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxpayerAddressType')
            value_ = self.gds_validate_string(value_, node, 'taxpayerAddressType')
            self.taxpayerAddressType = value_
            self.taxpayerAddressType_nsprefix_ = child_.prefix
            # validate type TaxpayerAddressTypeType
            self.validate_TaxpayerAddressTypeType(self.taxpayerAddressType)
        elif nodeName_ == 'taxpayerAddress':
            obj_ = DetailedAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.taxpayerAddress = obj_
            obj_.original_tagname_ = 'taxpayerAddress'
