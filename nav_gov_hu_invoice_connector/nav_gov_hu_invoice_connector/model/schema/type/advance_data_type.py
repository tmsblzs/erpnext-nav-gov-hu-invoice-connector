import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.advance_payment_data_type import \
    AdvancePaymentDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AdvanceDataType(GeneratedsSuper):
    """AdvanceDataType -- Előleghez kapcsolódó adatok
    Advance related data
    advanceIndicator -- Értéke true, ha a számla tétel előleg jellegű
    The value is true if the invoice item is a kind of advance charge
    advancePaymentData -- Előleg fizetéshez kapcsolódó adatok
    Advance payment related data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, advanceIndicator=None, advancePaymentData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.advanceIndicator = advanceIndicator
        self.advanceIndicator_nsprefix_ = "xs"
        self.advancePaymentData = advancePaymentData
        self.advancePaymentData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdvanceDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdvanceDataType.subclass:
            return AdvanceDataType.subclass(*args_, **kwargs_)
        else:
            return AdvanceDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_advanceIndicator(self):
        return self.advanceIndicator
    def set_advanceIndicator(self, advanceIndicator):
        self.advanceIndicator = advanceIndicator
    def get_advancePaymentData(self):
        return self.advancePaymentData
    def set_advancePaymentData(self, advancePaymentData):
        self.advancePaymentData = advancePaymentData
    def _hasContent(self):
        if (
            self.advanceIndicator is not None or
            self.advancePaymentData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AdvanceDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdvanceDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdvanceDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdvanceDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdvanceDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdvanceDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AdvanceDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.advanceIndicator is not None:
            namespaceprefix_ = self.advanceIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.advanceIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadvanceIndicator>%s</%sadvanceIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.advanceIndicator, input_name='advanceIndicator'), namespaceprefix_ , eol_))
        if self.advancePaymentData is not None:
            namespaceprefix_ = self.advancePaymentData_nsprefix_ + ':' if (UseCapturedNS_ and self.advancePaymentData_nsprefix_) else ''
            self.advancePaymentData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='advancePaymentData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AdvanceDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.advanceIndicator is not None:
            advanceIndicator_ = self.advanceIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}advanceIndicator').text = self.gds_format_boolean(advanceIndicator_)
        if self.advancePaymentData is not None:
            advancePaymentData_ = self.advancePaymentData
            advancePaymentData_.to_etree(element, name_='advancePaymentData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AdvanceDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.advanceIndicator is not None:
            showIndent(outfile, level)
            outfile.write('advanceIndicator=%s,\n' % self.advanceIndicator)
        if self.advancePaymentData is not None:
            showIndent(outfile, level)
            outfile.write('advancePaymentData=model_.AdvancePaymentDataType(\n')
            self.advancePaymentData.exportLiteral(outfile, level, name_='advancePaymentData')
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
        if nodeName_ == 'advanceIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'advanceIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'advanceIndicator')
            self.advanceIndicator = ival_
            self.advanceIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'advancePaymentData':
            obj_ = AdvancePaymentDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.advancePaymentData = obj_
            obj_.original_tagname_ = 'advancePaymentData'
