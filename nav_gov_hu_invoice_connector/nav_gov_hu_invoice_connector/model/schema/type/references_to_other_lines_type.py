import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ReferencesToOtherLinesType(GeneratedsSuper):
    """ReferencesToOtherLinesType -- Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükséges
    References to connected items if it is necessary according to VAT law
    referenceToOtherLine -- Hivatkozások kapcsolódó tételekre, ha ez az ÁFA törvény alapján szükséges
    References to connected items if it is necessary according to VAT law

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, referenceToOtherLine=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if referenceToOtherLine is None:
            self.referenceToOtherLine = []
        else:
            self.referenceToOtherLine = referenceToOtherLine
        self.referenceToOtherLine_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferencesToOtherLinesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferencesToOtherLinesType.subclass:
            return ReferencesToOtherLinesType.subclass(*args_, **kwargs_)
        else:
            return ReferencesToOtherLinesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_referenceToOtherLine(self):
        return self.referenceToOtherLine
    def set_referenceToOtherLine(self, referenceToOtherLine):
        self.referenceToOtherLine = referenceToOtherLine
    def add_referenceToOtherLine(self, value):
        self.referenceToOtherLine.append(value)
    def insert_referenceToOtherLine_at(self, index, value):
        self.referenceToOtherLine.insert(index, value)
    def replace_referenceToOtherLine_at(self, index, value):
        self.referenceToOtherLine[index] = value
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
    def _hasContent(self):
        if (
            self.referenceToOtherLine
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ReferencesToOtherLinesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferencesToOtherLinesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferencesToOtherLinesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferencesToOtherLinesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferencesToOtherLinesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReferencesToOtherLinesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ReferencesToOtherLinesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for referenceToOtherLine_ in self.referenceToOtherLine:
            namespaceprefix_ = self.referenceToOtherLine_nsprefix_ + ':' if (UseCapturedNS_ and self.referenceToOtherLine_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreferenceToOtherLine>%s</%sreferenceToOtherLine>%s' % (namespaceprefix_ , self.gds_format_integer(referenceToOtherLine_, input_name='referenceToOtherLine'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ReferencesToOtherLinesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for referenceToOtherLine_ in self.referenceToOtherLine:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}referenceToOtherLine').text = self.gds_format_integer(referenceToOtherLine_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ReferencesToOtherLinesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('referenceToOtherLine=[\n')
        level += 1
        for referenceToOtherLine_ in self.referenceToOtherLine:
            showIndent(outfile, level)
            outfile.write('%d,\n' % referenceToOtherLine_)
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
        if nodeName_ == 'referenceToOtherLine' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'referenceToOtherLine')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'referenceToOtherLine')
            self.referenceToOtherLine.append(ival_)
            self.referenceToOtherLine_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.referenceToOtherLine[-1])
