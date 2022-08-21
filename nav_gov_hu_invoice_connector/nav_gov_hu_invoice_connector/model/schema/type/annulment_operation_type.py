import base64

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, raise_parse_error

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AnnulmentOperationType(GeneratedsSuper):
    """AnnulmentOperationType -- A kéréshez tartozó technikai érvénytelenítő művelet
    Technical annulment operation of the request
    index -- A technikai érvénytelenítés sorszáma a kérésen belül
            Sequence number of the technical annulment within the request
    annulmentOperation -- A kért technikai érvénytelenítés művelet típusa
            Type of the desired technical annulment operation
    invoiceAnnulment -- Technikai érvénytelenítés adatok BASE64-ben kódolt tartalma
            Technical annulment data in BASE64 encoded form

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, index=None, annulmentOperation=None, invoiceAnnulment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.index = index
        self.validate_InvoiceIndexType(self.index)
        self.index_nsprefix_ = "base"
        self.annulmentOperation = annulmentOperation
        self.validate_ManageAnnulmentOperationType(self.annulmentOperation)
        self.annulmentOperation_nsprefix_ = None
        self.invoiceAnnulment = invoiceAnnulment
        self.invoiceAnnulment_nsprefix_ = "xs"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AnnulmentOperationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AnnulmentOperationType.subclass:
            return AnnulmentOperationType.subclass(*args_, **kwargs_)
        else:
            return AnnulmentOperationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_annulmentOperation(self):
        return self.annulmentOperation
    def set_annulmentOperation(self, annulmentOperation):
        self.annulmentOperation = annulmentOperation
    def get_invoiceAnnulment(self):
        return self.invoiceAnnulment
    def set_invoiceAnnulment(self, invoiceAnnulment):
        self.invoiceAnnulment = invoiceAnnulment
    def validate_InvoiceIndexType(self, value):
        result = True
        # Validate type InvoiceIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceIndexType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on InvoiceIndexType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_ManageAnnulmentOperationType(self, value):
        result = True
        # Validate type ManageAnnulmentOperationType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['ANNUL']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ManageAnnulmentOperationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ManageAnnulmentOperationType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ManageAnnulmentOperationType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.index is not None or
            self.annulmentOperation is not None or
            self.invoiceAnnulment is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='AnnulmentOperationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AnnulmentOperationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AnnulmentOperationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AnnulmentOperationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AnnulmentOperationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AnnulmentOperationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='AnnulmentOperationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.index is not None:
            namespaceprefix_ = self.index_nsprefix_ + ':' if (UseCapturedNS_ and self.index_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindex>%s</%sindex>%s' % (namespaceprefix_ , self.gds_format_integer(self.index, input_name='index'), namespaceprefix_ , eol_))
        if self.annulmentOperation is not None:
            namespaceprefix_ = self.annulmentOperation_nsprefix_ + ':' if (UseCapturedNS_ and self.annulmentOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentOperation>%s</%sannulmentOperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.annulmentOperation), input_name='annulmentOperation')), namespaceprefix_ , eol_))
        if self.invoiceAnnulment is not None:
            namespaceprefix_ = self.invoiceAnnulment_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceAnnulment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceAnnulment>%s</%sinvoiceAnnulment>%s' % (namespaceprefix_ , self.gds_format_base64(self.invoiceAnnulment, input_name='invoiceAnnulment'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AnnulmentOperationType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.index is not None:
            index_ = self.index
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}index').text = self.gds_format_integer(index_)
        if self.annulmentOperation is not None:
            annulmentOperation_ = self.annulmentOperation
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}annulmentOperation').text = self.gds_format_string(annulmentOperation_)
        if self.invoiceAnnulment is not None:
            invoiceAnnulment_ = self.invoiceAnnulment
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}invoiceAnnulment').text = self.gds_format_base64(invoiceAnnulment_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AnnulmentOperationType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.index is not None:
            showIndent(outfile, level)
            outfile.write('index=%d,\n' % self.index)
        if self.annulmentOperation is not None:
            showIndent(outfile, level)
            outfile.write('annulmentOperation=%s,\n' % self.gds_encode(quote_python(self.annulmentOperation)))
        if self.invoiceAnnulment is not None:
            showIndent(outfile, level)
            outfile.write('invoiceAnnulment=model_.base64Binary(\n')
            self.invoiceAnnulment.exportLiteral(outfile, level, name_='invoiceAnnulment')
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
        if nodeName_ == 'index' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'index')
            ival_ = self.gds_validate_integer(ival_, node, 'index')
            self.index = ival_
            self.index_nsprefix_ = child_.prefix
            # validate type InvoiceIndexType
            self.validate_InvoiceIndexType(self.index)
        elif nodeName_ == 'annulmentOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'annulmentOperation')
            value_ = self.gds_validate_string(value_, node, 'annulmentOperation')
            self.annulmentOperation = value_
            self.annulmentOperation_nsprefix_ = child_.prefix
            # validate type ManageAnnulmentOperationType
            self.validate_ManageAnnulmentOperationType(self.annulmentOperation)
        elif nodeName_ == 'invoiceAnnulment':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'invoiceAnnulment')
            else:
                bval_ = None
            self.invoiceAnnulment = bval_
            self.invoiceAnnulment_nsprefix_ = child_.prefix
