from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_result_type import \
    BasicResultType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class GeneralExceptionResponse(BasicResultType):
    """GeneralExceptionResponse -- Az összes REST operációra vonatkozó kivétel válasz generikus elementje
    General exception response of every REST operation

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicResultType

    def __init__(self, funcCode=None, errorCode=None, message=None, notifications=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tns"
        super(globals().get("GeneralExceptionResponse"), self).__init__(funcCode, errorCode, message, notifications,
                                                                        **kwargs_)

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GeneralExceptionResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GeneralExceptionResponse.subclass:
            return GeneralExceptionResponse.subclass(*args_, **kwargs_)
        else:
            return GeneralExceptionResponse(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (
                super(GeneralExceptionResponse, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='GeneralExceptionResponse',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GeneralExceptionResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GeneralExceptionResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GeneralExceptionResponse')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GeneralExceptionResponse',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='GeneralExceptionResponse'):
        super(GeneralExceptionResponse, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                                                                name_='GeneralExceptionResponse')

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"',
                        name_='GeneralExceptionResponse', fromsubclass_=False, pretty_print=True):
        super(GeneralExceptionResponse, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_,
                                                              True, pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='GeneralExceptionResponse', mapping_=None, nsmap_=None):
        element = super(GeneralExceptionResponse, self).to_etree(parent_element, name_, mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='GeneralExceptionResponse'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(GeneralExceptionResponse, self)._exportLiteralAttributes(outfile, level, already_processed, name_)

    def _exportLiteralChildren(self, outfile, level, name_):
        super(GeneralExceptionResponse, self)._exportLiteralChildren(outfile, level, name_)

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
        super(GeneralExceptionResponse, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(GeneralExceptionResponse, self)._buildChildren(child_, node, nodeName_, True)
        pass
