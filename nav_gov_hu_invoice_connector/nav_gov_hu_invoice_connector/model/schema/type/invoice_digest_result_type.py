from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, GenerateDSNamespaceDefs_, UseCapturedNS_, \
    showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.invoice_digest_type import \
    InvoiceDigestType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceDigestResultType(GeneratedsSuper):
    """InvoiceDigestResultType -- Számla lekérdezési eredmények
    Invoice query results
    currentPage -- A jelenleg lekérdezett lapszám
            The currently queried page count
    availablePage -- A lekérdezés eredménye szerint elérhető utolsó lapszám
            The highest available page count matching the query
    invoiceDigest -- Számla kivonat lekérdezési eredmény
            Invoice digest query result

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, currentPage=None, availablePage=None, invoiceDigest=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.currentPage = currentPage
        self.validate_ResponsePageType(self.currentPage)
        self.currentPage_nsprefix_ = "common"
        self.availablePage = availablePage
        self.validate_ResponsePageType(self.availablePage)
        self.availablePage_nsprefix_ = "common"
        if invoiceDigest is None:
            self.invoiceDigest = []
        else:
            self.invoiceDigest = invoiceDigest
        self.invoiceDigest_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceDigestResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceDigestResultType.subclass:
            return InvoiceDigestResultType.subclass(*args_, **kwargs_)
        else:
            return InvoiceDigestResultType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_currentPage(self):
        return self.currentPage

    def set_currentPage(self, currentPage):
        self.currentPage = currentPage

    def get_availablePage(self):
        return self.availablePage

    def set_availablePage(self, availablePage):
        self.availablePage = availablePage

    def get_invoiceDigest(self):
        return self.invoiceDigest

    def set_invoiceDigest(self, invoiceDigest):
        self.invoiceDigest = invoiceDigest

    def add_invoiceDigest(self, value):
        self.invoiceDigest.append(value)

    def insert_invoiceDigest_at(self, index, value):
        self.invoiceDigest.insert(index, value)

    def replace_invoiceDigest_at(self, index, value):
        self.invoiceDigest[index] = value

    def validate_ResponsePageType(self, value):
        result = True
        # Validate type ResponsePageType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ResponsePageType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.currentPage is not None or
                self.availablePage is not None or
                self.invoiceDigest
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='InvoiceDigestResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceDigestResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceDigestResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceDigestResultType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceDigestResultType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='InvoiceDigestResultType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='InvoiceDigestResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.currentPage is not None:
            namespaceprefix_ = self.currentPage_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.currentPage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrentPage>%s</%scurrentPage>%s' % (
            namespaceprefix_, self.gds_format_integer(self.currentPage, input_name='currentPage'), namespaceprefix_,
            eol_))
        if self.availablePage is not None:
            namespaceprefix_ = self.availablePage_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.availablePage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%savailablePage>%s</%savailablePage>%s' % (
            namespaceprefix_, self.gds_format_integer(self.availablePage, input_name='availablePage'), namespaceprefix_,
            eol_))
        for invoiceDigest_ in self.invoiceDigest:
            namespaceprefix_ = self.invoiceDigest_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.invoiceDigest_nsprefix_) else ''
            invoiceDigest_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceDigest',
                                  pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='InvoiceDigestResultType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.currentPage is not None:
            currentPage_ = self.currentPage
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}currentPage').text = self.gds_format_integer(
                currentPage_)
        if self.availablePage is not None:
            availablePage_ = self.availablePage
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}availablePage').text = self.gds_format_integer(
                availablePage_)
        for invoiceDigest_ in self.invoiceDigest:
            invoiceDigest_.to_etree(element, name_='invoiceDigest', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceDigestResultType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.currentPage is not None:
            showIndent(outfile, level)
            outfile.write('currentPage=%d,\n' % self.currentPage)
        if self.availablePage is not None:
            showIndent(outfile, level)
            outfile.write('availablePage=%d,\n' % self.availablePage)
        showIndent(outfile, level)
        outfile.write('invoiceDigest=[\n')
        level += 1
        for invoiceDigest_ in self.invoiceDigest:
            showIndent(outfile, level)
            outfile.write('model_.InvoiceDigestType(\n')
            invoiceDigest_.exportLiteral(outfile, level, name_='InvoiceDigestType')
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
        if nodeName_ == 'currentPage' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'currentPage')
            ival_ = self.gds_validate_integer(ival_, node, 'currentPage')
            self.currentPage = ival_
            self.currentPage_nsprefix_ = child_.prefix
            # validate type ResponsePageType
            self.validate_ResponsePageType(self.currentPage)
        elif nodeName_ == 'availablePage' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'availablePage')
            ival_ = self.gds_validate_integer(ival_, node, 'availablePage')
            self.availablePage = ival_
            self.availablePage_nsprefix_ = child_.prefix
            # validate type ResponsePageType
            self.validate_ResponsePageType(self.availablePage)
        elif nodeName_ == 'invoiceDigest':
            obj_ = InvoiceDigestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceDigest.append(obj_)
            obj_.original_tagname_ = 'invoiceDigest'
