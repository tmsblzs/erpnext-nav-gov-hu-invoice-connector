import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, raise_parse_error

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class LineModificationReferenceType(GeneratedsSuper):
    """LineModificationReferenceType -- Módosításról történő adatszolgáltatás esetén
        a tételsor módosítás jellegének jelölése
    Marking the goal of modification of the line (in the case of data supply about changes/updates only)
    lineNumberReference -- Az eredeti számla módosítással érintett tételének sorszáma (lineNumber).
        Új tétel létrehozása esetén az új tétel sorszáma, a meglévő tételsorok számozásának folytatásaként
    Line number of the original invoice, which the modification occurs with. In case of create operation the tag shall contain the new line number, as a sequential increment of the the existing lines set
    lineOperation -- A számlatétel módosításának jellege
    Line modification type

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineNumberReference=None, lineOperation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNumberReference = lineNumberReference
        self.validate_LineNumberType(self.lineNumberReference)
        self.lineNumberReference_nsprefix_ = "base"
        self.lineOperation = lineOperation
        self.validate_LineOperationType(self.lineOperation)
        self.lineOperation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineModificationReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineModificationReferenceType.subclass:
            return LineModificationReferenceType.subclass(*args_, **kwargs_)
        else:
            return LineModificationReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineNumberReference(self):
        return self.lineNumberReference
    def set_lineNumberReference(self, lineNumberReference):
        self.lineNumberReference = lineNumberReference
    def get_lineOperation(self):
        return self.lineOperation
    def set_lineOperation(self, lineOperation):
        self.lineOperation = lineOperation
    def validate_LineNumberType(self, value):
        result = True
        # Validate type LineNumberType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_LineOperationType(self, value):
        result = True
        # Validate type LineOperationType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['CREATE', 'MODIFY']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LineOperationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LineOperationType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LineOperationType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineNumberReference is not None or
            self.lineOperation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineModificationReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineModificationReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineModificationReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineModificationReferenceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineModificationReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineModificationReferenceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineModificationReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNumberReference is not None:
            namespaceprefix_ = self.lineNumberReference_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNumberReference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNumberReference>%s</%slineNumberReference>%s' % (namespaceprefix_ , self.gds_format_integer(self.lineNumberReference, input_name='lineNumberReference'), namespaceprefix_ , eol_))
        if self.lineOperation is not None:
            namespaceprefix_ = self.lineOperation_nsprefix_ + ':' if (UseCapturedNS_ and self.lineOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineOperation>%s</%slineOperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lineOperation), input_name='lineOperation')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineModificationReferenceType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineNumberReference is not None:
            lineNumberReference_ = self.lineNumberReference
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNumberReference').text = self.gds_format_integer(lineNumberReference_)
        if self.lineOperation is not None:
            lineOperation_ = self.lineOperation
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineOperation').text = self.gds_format_string(lineOperation_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineModificationReferenceType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNumberReference is not None:
            showIndent(outfile, level)
            outfile.write('lineNumberReference=%d,\n' % self.lineNumberReference)
        if self.lineOperation is not None:
            showIndent(outfile, level)
            outfile.write('lineOperation=%s,\n' % self.gds_encode(quote_python(self.lineOperation)))
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
        if nodeName_ == 'lineNumberReference' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'lineNumberReference')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'lineNumberReference')
            self.lineNumberReference = ival_
            self.lineNumberReference_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.lineNumberReference)
        elif nodeName_ == 'lineOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lineOperation')
            value_ = self.gds_validate_string(value_, node, 'lineOperation')
            self.lineOperation = value_
            self.lineOperation_nsprefix_ = child_.prefix
            # validate type LineOperationType
            self.validate_LineOperationType(self.lineOperation)
