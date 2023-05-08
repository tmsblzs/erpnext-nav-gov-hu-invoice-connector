import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ProductFeeTakeoverDataType(GeneratedsSuper):
    """ProductFeeTakeoverDataType -- A környezetvédelmi termékdíj kötelezettség átvállalásával kapcsolatos adatok
    Data in connection with takeover of environmental protection product fee
    takeoverReason -- Az átvállalás iránya és jogszabályi alapja
    Direction and legal base of takeover
    takeoverAmount -- Az átvállalt termékdíjösszege forintban, ha a vevő vállalja át az eladó termékdíj-kötelezettségét
    Amount in Hungarian forints of the product fee taken over if the purchaser takes over the supplier’s
        product fee liability

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, takeoverReason=None, takeoverAmount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.takeoverReason = takeoverReason
        self.validate_TakeoverType(self.takeoverReason)
        self.takeoverReason_nsprefix_ = None
        self.takeoverAmount = takeoverAmount
        self.validate_MonetaryType(self.takeoverAmount)
        self.takeoverAmount_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeTakeoverDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeTakeoverDataType.subclass:
            return ProductFeeTakeoverDataType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeTakeoverDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_takeoverReason(self):
        return self.takeoverReason
    def set_takeoverReason(self, takeoverReason):
        self.takeoverReason = takeoverReason
    def get_takeoverAmount(self):
        return self.takeoverAmount
    def set_takeoverAmount(self, takeoverAmount):
        self.takeoverAmount = takeoverAmount
    def validate_TakeoverType(self, value):
        result = True
        # Validate type TakeoverType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['01', '02_aa', '02_ab', '02_b', '02_c', '02_d', '02_ea', '02_eb', '02_fa', '02_fb', '02_ga', '02_gb']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TakeoverType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TakeoverType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TakeoverType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.takeoverReason is not None or
            self.takeoverAmount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeTakeoverDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeTakeoverDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeTakeoverDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeTakeoverDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeTakeoverDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeTakeoverDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeTakeoverDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.takeoverReason is not None:
            namespaceprefix_ = self.takeoverReason_nsprefix_ + ':' if (UseCapturedNS_ and self.takeoverReason_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stakeoverReason>%s</%stakeoverReason>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.takeoverReason), input_name='takeoverReason')), namespaceprefix_ , eol_))
        if self.takeoverAmount is not None:
            namespaceprefix_ = self.takeoverAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.takeoverAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stakeoverAmount>%s</%stakeoverAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.takeoverAmount, input_name='takeoverAmount'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProductFeeTakeoverDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.takeoverReason is not None:
            takeoverReason_ = self.takeoverReason
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}takeoverReason').text = self.gds_format_string(takeoverReason_)
        if self.takeoverAmount is not None:
            takeoverAmount_ = self.takeoverAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}takeoverAmount').text = self.gds_format_decimal(takeoverAmount_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeTakeoverDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.takeoverReason is not None:
            showIndent(outfile, level)
            outfile.write('takeoverReason=%s,\n' % self.gds_encode(quote_python(self.takeoverReason)))
        if self.takeoverAmount is not None:
            showIndent(outfile, level)
            outfile.write('takeoverAmount=%f,\n' % self.takeoverAmount)
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
        if nodeName_ == 'takeoverReason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'takeoverReason')
            value_ = self.gds_validate_string(value_, node, 'takeoverReason')
            self.takeoverReason = value_
            self.takeoverReason_nsprefix_ = child_.prefix
            # validate type TakeoverType
            self.validate_TakeoverType(self.takeoverReason)
        elif nodeName_ == 'takeoverAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'takeoverAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'takeoverAmount')
            self.takeoverAmount = fval_
            self.takeoverAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.takeoverAmount)
