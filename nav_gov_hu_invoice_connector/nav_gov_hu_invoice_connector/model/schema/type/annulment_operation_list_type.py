import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.annulment_operation_type import \
    AnnulmentOperationType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AnnulmentOperationListType(GeneratedsSuper):
    """AnnulmentOperationListType -- A kéréshez tartozókötegelt technikai érvénytelenítések
    Batch technical annulment operations of the request
    annulmentOperation -- A kéréshez tartozó technikai érvénytelenítő művelet
            Technical annulment operation of the request

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, annulmentOperation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if annulmentOperation is None:
            self.annulmentOperation = []
        else:
            self.annulmentOperation = annulmentOperation
        self.annulmentOperation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AnnulmentOperationListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AnnulmentOperationListType.subclass:
            return AnnulmentOperationListType.subclass(*args_, **kwargs_)
        else:
            return AnnulmentOperationListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_annulmentOperation(self):
        return self.annulmentOperation
    def set_annulmentOperation(self, annulmentOperation):
        self.annulmentOperation = annulmentOperation
    def add_annulmentOperation(self, value):
        self.annulmentOperation.append(value)
    def insert_annulmentOperation_at(self, index, value):
        self.annulmentOperation.insert(index, value)
    def replace_annulmentOperation_at(self, index, value):
        self.annulmentOperation[index] = value
    def _hasContent(self):
        if (
            self.annulmentOperation
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AnnulmentOperationListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AnnulmentOperationListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AnnulmentOperationListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AnnulmentOperationListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AnnulmentOperationListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AnnulmentOperationListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AnnulmentOperationListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for annulmentOperation_ in self.annulmentOperation:
            namespaceprefix_ = self.annulmentOperation_nsprefix_ + ':' if (UseCapturedNS_ and self.annulmentOperation_nsprefix_) else ''
            annulmentOperation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='annulmentOperation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AnnulmentOperationListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        for annulmentOperation_ in self.annulmentOperation:
            annulmentOperation_.to_etree(element, name_='annulmentOperation', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AnnulmentOperationListType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('annulmentOperation=[\n')
        level += 1
        for annulmentOperation_ in self.annulmentOperation:
            showIndent(outfile, level)
            outfile.write('model_.AnnulmentOperationType(\n')
            annulmentOperation_.exportLiteral(outfile, level, name_='AnnulmentOperationType')
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
        if nodeName_ == 'annulmentOperation':
            obj_ = AnnulmentOperationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.annulmentOperation.append(obj_)
            obj_.original_tagname_ = 'annulmentOperation'
