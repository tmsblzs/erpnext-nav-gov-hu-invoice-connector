from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    ModulenotfoundExp_, CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, \
    showIndent, GenerateDSNamespaceTypePrefixes_, SaveElementTreeNode, Tag_pattern_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_header_type import BasicHeaderType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_result_type import BasicResultType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class BasicResponseType(GeneratedsSuper):
    """BasicResponseType -- Alap válasz adatok
    Basic response data
    header -- A válasz tranzakcionális adatai
                Transactional data of the response
    result -- Alap válaszeredmény adatok
                Basic result data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, header=None, result=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.header = header
        self.header_nsprefix_ = None
        self.result = result
        self.result_nsprefix_ = None
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BasicResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BasicResponseType.subclass:
            return BasicResponseType.subclass(*args_, **kwargs_)
        else:
            return BasicResponseType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                self.header is not None or
                self.result is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='BasicResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BasicResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BasicResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BasicResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BasicResponseType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BasicResponseType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='BasicResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.header is not None:
            namespaceprefix_ = self.header_nsprefix_ + ':' if (UseCapturedNS_ and self.header_nsprefix_) else ''
            self.header.export(outfile, level, namespaceprefix_, namespacedef_='', name_='header',
                               pretty_print=pretty_print)
        if self.result is not None:
            namespaceprefix_ = self.result_nsprefix_ + ':' if (UseCapturedNS_ and self.result_nsprefix_) else ''
            self.result.export(outfile, level, namespaceprefix_, namespacedef_='', name_='result',
                               pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='BasicResponseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_,
                                        nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.header is not None:
            header_ = self.header
            header_.to_etree(element, name_='header', mapping_=mapping_, nsmap_=nsmap_)
        if self.result is not None:
            result_ = self.result
            result_.to_etree(element, name_='result', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='BasicResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.header is not None:
            showIndent(outfile, level)
            outfile.write('header=model_.BasicHeaderType(\n')
            self.header.exportLiteral(outfile, level, name_='header')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.result is not None:
            showIndent(outfile, level)
            outfile.write('result=model_.BasicResultType(\n')
            self.result.exportLiteral(outfile, level, name_='result')
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

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'header':
            obj_ = BasicHeaderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.header = obj_
            obj_.original_tagname_ = 'header'
        elif nodeName_ == 'result':
            class_obj_ = self.get_class_obj_(child_, BasicResultType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.result = obj_
            obj_.original_tagname_ = 'result'
