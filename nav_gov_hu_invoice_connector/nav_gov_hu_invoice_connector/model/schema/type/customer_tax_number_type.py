import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.tax_number_type import TaxNumberType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class CustomerTaxNumberType(TaxNumberType):
    """CustomerTaxNumberType -- Adószám, amely alatt a számlán szereplő termékbeszerzés
        vagy szolgáltatás igénybevétele történt. Lehet csoportazonosítószám is
    Tax number or group identification number, under which the purchase of goods or services is done
    groupMemberTaxNumber -- Csoport tag adószáma, ha a termékbeszerzés
        vagy szolgáltatás igénybevétele csoportazonosítószám alatt történt
    Tax number of group member, when the purchase of goods or services is done under group identification number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = TaxNumberType
    def __init__(self, taxpayerId=None, vatCode=None, countyCode=None, groupMemberTaxNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("CustomerTaxNumberType"), self).__init__(taxpayerId, vatCode, countyCode,  **kwargs_)
        self.groupMemberTaxNumber = groupMemberTaxNumber
        self.groupMemberTaxNumber_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CustomerTaxNumberType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CustomerTaxNumberType.subclass:
            return CustomerTaxNumberType.subclass(*args_, **kwargs_)
        else:
            return CustomerTaxNumberType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_groupMemberTaxNumber(self):
        return self.groupMemberTaxNumber
    def set_groupMemberTaxNumber(self, groupMemberTaxNumber):
        self.groupMemberTaxNumber = groupMemberTaxNumber
    def _hasContent(self):
        if (
            self.groupMemberTaxNumber is not None or
            super(CustomerTaxNumberType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='CustomerTaxNumberType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CustomerTaxNumberType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CustomerTaxNumberType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomerTaxNumberType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CustomerTaxNumberType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CustomerTaxNumberType'):
        super(CustomerTaxNumberType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomerTaxNumberType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='CustomerTaxNumberType', fromsubclass_=False, pretty_print=True):
        super(CustomerTaxNumberType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.groupMemberTaxNumber is not None:
            namespaceprefix_ = self.groupMemberTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.groupMemberTaxNumber_nsprefix_) else ''
            self.groupMemberTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='groupMemberTaxNumber', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CustomerTaxNumberType', mapping_=None, nsmap_=None):
        element = super(CustomerTaxNumberType, self).to_etree(parent_element, name_, mapping_)
        if self.groupMemberTaxNumber is not None:
            groupMemberTaxNumber_ = self.groupMemberTaxNumber
            groupMemberTaxNumber_.to_etree(element, name_='groupMemberTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CustomerTaxNumberType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(CustomerTaxNumberType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(CustomerTaxNumberType, self)._exportLiteralChildren(outfile, level, name_)
        if self.groupMemberTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('groupMemberTaxNumber=model_.TaxNumberType(\n')
            self.groupMemberTaxNumber.exportLiteral(outfile, level, name_='groupMemberTaxNumber')
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
        super(CustomerTaxNumberType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'groupMemberTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.groupMemberTaxNumber = obj_
            obj_.original_tagname_ = 'groupMemberTaxNumber'
        super(CustomerTaxNumberType, self)._buildChildren(child_, node, nodeName_, True)
