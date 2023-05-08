from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.general_error_header_response_type import \
    GeneralErrorHeaderResponseType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.software_type import SoftwareType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.technical_validation_result_type import \
    TechnicalValidationResultType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class GeneralErrorResponseType(GeneralErrorHeaderResponseType):
    """GeneralErrorResponseType -- Online Számla rendszerre specifikus általános hibaválasz típus
    Online Invoice specific general error response type
    software -- A számlázó program adatai
    Billing software data
    technicalValidationMessages -- Technikai validációs üzenetek
    Technical validation messages

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = GeneralErrorHeaderResponseType

    def __init__(self, header=None, result=None, software=None, technicalValidationMessages=None, extensiontype_=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("GeneralErrorResponseType"), self).__init__(header, result, extensiontype_, **kwargs_)
        self.software = software
        self.software_nsprefix_ = None
        if technicalValidationMessages is None:
            self.technicalValidationMessages = []
        else:
            self.technicalValidationMessages = technicalValidationMessages
        self.technicalValidationMessages_nsprefix_ = "common"
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GeneralErrorResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GeneralErrorResponseType.subclass:
            return GeneralErrorResponseType.subclass(*args_, **kwargs_)
        else:
            return GeneralErrorResponseType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_software(self):
        return self.software

    def set_software(self, software):
        self.software = software

    def get_technicalValidationMessages(self):
        return self.technicalValidationMessages

    def set_technicalValidationMessages(self, technicalValidationMessages):
        self.technicalValidationMessages = technicalValidationMessages

    def add_technicalValidationMessages(self, value):
        self.technicalValidationMessages.append(value)

    def insert_technicalValidationMessages_at(self, index, value):
        self.technicalValidationMessages.insert(index, value)

    def replace_technicalValidationMessages_at(self, index, value):
        self.technicalValidationMessages[index] = value

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                self.software is not None or
                self.technicalValidationMessages or
                super(GeneralErrorResponseType, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
               name_='GeneralErrorResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GeneralErrorResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GeneralErrorResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GeneralErrorResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GeneralErrorResponseType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='GeneralErrorResponseType'):
        super(GeneralErrorResponseType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                                                                name_='GeneralErrorResponseType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ',
                        name_='GeneralErrorResponseType', fromsubclass_=False, pretty_print=True):
        super(GeneralErrorResponseType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_,
                                                              True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.software is not None:
            namespaceprefix_ = self.software_nsprefix_ + ':' if (UseCapturedNS_ and self.software_nsprefix_) else ''
            self.software.export(outfile, level, namespaceprefix_, namespacedef_='', name_='software',
                                 pretty_print=pretty_print)
        for technicalValidationMessages_ in self.technicalValidationMessages:
            namespaceprefix_ = self.technicalValidationMessages_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.technicalValidationMessages_nsprefix_) else ''
            technicalValidationMessages_.export(outfile, level, namespaceprefix_, namespacedef_='',
                                                name_='technicalValidationMessages', pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='GeneralErrorResponseType', mapping_=None, nsmap_=None):
        element = super(GeneralErrorResponseType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.software is not None:
            software_ = self.software
            software_.to_etree(element, name_='software', mapping_=mapping_, nsmap_=nsmap_)
        for technicalValidationMessages_ in self.technicalValidationMessages:
            technicalValidationMessages_.to_etree(element, name_='technicalValidationMessages', mapping_=mapping_,
                                                  nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='GeneralErrorResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(GeneralErrorResponseType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)

    def _exportLiteralChildren(self, outfile, level, name_):
        super(GeneralErrorResponseType, self)._exportLiteralChildren(outfile, level, name_)
        if self.software is not None:
            showIndent(outfile, level)
            outfile.write('software=model_.SoftwareType(\n')
            self.software.exportLiteral(outfile, level, name_='software')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('technicalValidationMessages=[\n')
        level += 1
        for technicalValidationMessages_ in self.technicalValidationMessages:
            showIndent(outfile, level)
            outfile.write('model_.TechnicalValidationResultType(\n')
            technicalValidationMessages_.exportLiteral(outfile, level, name_='TechnicalValidationResultType')
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
        super(GeneralErrorResponseType, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'software':
            obj_ = SoftwareType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.software = obj_
            obj_.original_tagname_ = 'software'
        elif nodeName_ == 'technicalValidationMessages':
            obj_ = TechnicalValidationResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.technicalValidationMessages.append(obj_)
            obj_.original_tagname_ = 'technicalValidationMessages'
        super(GeneralErrorResponseType, self)._buildChildren(child_, node, nodeName_, True)
