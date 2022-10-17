import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.annulment_data_type import \
    AnnulmentDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ProcessingResultListType(GeneratedsSuper):
    """ProcessingResultListType -- A kéréshez tartozó feldolgozási eredmények
    Processing results of the request
    processingResult -- Számla feldolgozási eredmény
    Invoice processing result
    originalRequestVersion -- Az adatszolgáltatás requestVersion értéke
    requestVersion value of the invoice exchange
    annulmentData -- Technikai érvénytelenítés státusz adatai
    Status data of technical annulment

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, processingResult=None, originalRequestVersion=None, annulmentData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if processingResult is None:
            self.processingResult = []
        else:
            self.processingResult = processingResult
        self.processingResult_nsprefix_ = None
        self.originalRequestVersion = originalRequestVersion
        self.validate_OriginalRequestVersionType(self.originalRequestVersion)
        self.originalRequestVersion_nsprefix_ = None
        self.annulmentData = annulmentData
        self.annulmentData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProcessingResultListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProcessingResultListType.subclass:
            return ProcessingResultListType.subclass(*args_, **kwargs_)
        else:
            return ProcessingResultListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_processingResult(self):
        return self.processingResult
    def set_processingResult(self, processingResult):
        self.processingResult = processingResult
    def add_processingResult(self, value):
        self.processingResult.append(value)
    def insert_processingResult_at(self, index, value):
        self.processingResult.insert(index, value)
    def replace_processingResult_at(self, index, value):
        self.processingResult[index] = value
    def get_originalRequestVersion(self):
        return self.originalRequestVersion
    def set_originalRequestVersion(self, originalRequestVersion):
        self.originalRequestVersion = originalRequestVersion
    def get_annulmentData(self):
        return self.annulmentData
    def set_annulmentData(self, annulmentData):
        self.annulmentData = annulmentData
    def validate_OriginalRequestVersionType(self, value):
        result = True
        # Validate type OriginalRequestVersionType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['1.0', '1.1', '2.0', '3.0']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on OriginalRequestVersionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on OriginalRequestVersionType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on OriginalRequestVersionType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.processingResult or
            self.originalRequestVersion is not None or
            self.annulmentData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProcessingResultListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProcessingResultListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProcessingResultListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProcessingResultListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProcessingResultListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProcessingResultListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProcessingResultListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for processingResult_ in self.processingResult:
            namespaceprefix_ = self.processingResult_nsprefix_ + ':' if (UseCapturedNS_ and self.processingResult_nsprefix_) else ''
            processingResult_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='processingResult', pretty_print=pretty_print)
        if self.originalRequestVersion is not None:
            namespaceprefix_ = self.originalRequestVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.originalRequestVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalRequestVersion>%s</%soriginalRequestVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.originalRequestVersion), input_name='originalRequestVersion')), namespaceprefix_ , eol_))
        if self.annulmentData is not None:
            namespaceprefix_ = self.annulmentData_nsprefix_ + ':' if (UseCapturedNS_ and self.annulmentData_nsprefix_) else ''
            self.annulmentData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='annulmentData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProcessingResultListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        for processingResult_ in self.processingResult:
            processingResult_.to_etree(element, name_='processingResult', mapping_=mapping_, nsmap_=nsmap_)
        if self.originalRequestVersion is not None:
            originalRequestVersion_ = self.originalRequestVersion
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion').text = self.gds_format_string(originalRequestVersion_)
        if self.annulmentData is not None:
            annulmentData_ = self.annulmentData
            annulmentData_.to_etree(element, name_='annulmentData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProcessingResultListType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('processingResult=[\n')
        level += 1
        for processingResult_ in self.processingResult:
            showIndent(outfile, level)
            outfile.write('model_.ProcessingResultType(\n')
            processingResult_.exportLiteral(outfile, level, name_='ProcessingResultType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.originalRequestVersion is not None:
            showIndent(outfile, level)
            outfile.write('originalRequestVersion=%s,\n' % self.gds_encode(quote_python(self.originalRequestVersion)))
        if self.annulmentData is not None:
            showIndent(outfile, level)
            outfile.write('annulmentData=model_.AnnulmentDataType(\n')
            self.annulmentData.exportLiteral(outfile, level, name_='annulmentData')
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
        if nodeName_ == 'processingResult':
            obj_ = ProcessingResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.processingResult.append(obj_)
            obj_.original_tagname_ = 'processingResult'
        elif nodeName_ == 'originalRequestVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalRequestVersion')
            value_ = self.gds_validate_string(value_, node, 'originalRequestVersion')
            self.originalRequestVersion = value_
            self.originalRequestVersion_nsprefix_ = child_.prefix
            # validate type OriginalRequestVersionType
            self.validate_OriginalRequestVersionType(self.originalRequestVersion)
        elif nodeName_ == 'annulmentData':
            obj_ = AnnulmentDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.annulmentData = obj_
            obj_.original_tagname_ = 'annulmentData'
