from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.additional_query_params_type import \
    AdditionalQueryParamsType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceQueryParamsType(GeneratedsSuper):
    """InvoiceQueryParamsType -- Számla lekérdezési paraméterek
    Invoice query parameters
    mandatoryQueryParams -- A számla lekérdezés kötelező paraméterei
            Mandatory params of the invoice query
    additionalQueryParams -- A számla lekérdezés kiegészítő paraméterei
            Additional params of the invoice query
    relationalQueryParams -- A számla lekérdezés relációs paraméterei
            Relational params of the invoice query
    transactionQueryParams -- A számla lekérdezés tranzakciós paraméterei
            Transactional params of the invoice query

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, mandatoryQueryParams=None, additionalQueryParams=None, relationalQueryParams=None,
                 transactionQueryParams=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.mandatoryQueryParams = mandatoryQueryParams
        self.mandatoryQueryParams_nsprefix_ = None
        self.additionalQueryParams = additionalQueryParams
        self.additionalQueryParams_nsprefix_ = None
        self.relationalQueryParams = relationalQueryParams
        self.relationalQueryParams_nsprefix_ = None
        self.transactionQueryParams = transactionQueryParams
        self.transactionQueryParams_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceQueryParamsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceQueryParamsType.subclass:
            return InvoiceQueryParamsType.subclass(*args_, **kwargs_)
        else:
            return InvoiceQueryParamsType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_mandatoryQueryParams(self):
        return self.mandatoryQueryParams

    def set_mandatoryQueryParams(self, mandatoryQueryParams):
        self.mandatoryQueryParams = mandatoryQueryParams

    def get_additionalQueryParams(self):
        return self.additionalQueryParams

    def set_additionalQueryParams(self, additionalQueryParams):
        self.additionalQueryParams = additionalQueryParams

    def get_relationalQueryParams(self):
        return self.relationalQueryParams

    def set_relationalQueryParams(self, relationalQueryParams):
        self.relationalQueryParams = relationalQueryParams

    def get_transactionQueryParams(self):
        return self.transactionQueryParams

    def set_transactionQueryParams(self, transactionQueryParams):
        self.transactionQueryParams = transactionQueryParams

    def _hasContent(self):
        if (
                self.mandatoryQueryParams is not None or
                self.additionalQueryParams is not None or
                self.relationalQueryParams is not None or
                self.transactionQueryParams is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='InvoiceQueryParamsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceQueryParamsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceQueryParamsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceQueryParamsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceQueryParamsType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceQueryParamsType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='InvoiceQueryParamsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.mandatoryQueryParams is not None:
            namespaceprefix_ = self.mandatoryQueryParams_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.mandatoryQueryParams_nsprefix_) else ''
            self.mandatoryQueryParams.export(outfile, level, namespaceprefix_, namespacedef_='',
                                             name_='mandatoryQueryParams', pretty_print=pretty_print)
        if self.additionalQueryParams is not None:
            namespaceprefix_ = self.additionalQueryParams_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.additionalQueryParams_nsprefix_) else ''
            self.additionalQueryParams.export(outfile, level, namespaceprefix_, namespacedef_='',
                                              name_='additionalQueryParams', pretty_print=pretty_print)
        if self.relationalQueryParams is not None:
            namespaceprefix_ = self.relationalQueryParams_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.relationalQueryParams_nsprefix_) else ''
            self.relationalQueryParams.export(outfile, level, namespaceprefix_, namespacedef_='',
                                              name_='relationalQueryParams', pretty_print=pretty_print)
        if self.transactionQueryParams is not None:
            namespaceprefix_ = self.transactionQueryParams_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.transactionQueryParams_nsprefix_) else ''
            self.transactionQueryParams.export(outfile, level, namespaceprefix_, namespacedef_='',
                                               name_='transactionQueryParams', pretty_print=pretty_print)

    def to_etree(self, parent_element=None, name_='InvoiceQueryParamsType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.mandatoryQueryParams is not None:
            mandatoryQueryParams_ = self.mandatoryQueryParams
            mandatoryQueryParams_.to_etree(element, name_='mandatoryQueryParams', mapping_=mapping_, nsmap_=nsmap_)
        if self.additionalQueryParams is not None:
            additionalQueryParams_ = self.additionalQueryParams
            additionalQueryParams_.to_etree(element, name_='additionalQueryParams', mapping_=mapping_, nsmap_=nsmap_)
        if self.relationalQueryParams is not None:
            relationalQueryParams_ = self.relationalQueryParams
            relationalQueryParams_.to_etree(element, name_='relationalQueryParams', mapping_=mapping_, nsmap_=nsmap_)
        if self.transactionQueryParams is not None:
            transactionQueryParams_ = self.transactionQueryParams
            transactionQueryParams_.to_etree(element, name_='transactionQueryParams', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceQueryParamsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.mandatoryQueryParams is not None:
            showIndent(outfile, level)
            outfile.write('mandatoryQueryParams=model_.MandatoryQueryParamsType(\n')
            self.mandatoryQueryParams.exportLiteral(outfile, level, name_='mandatoryQueryParams')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.additionalQueryParams is not None:
            showIndent(outfile, level)
            outfile.write('additionalQueryParams=model_.AdditionalQueryParamsType(\n')
            self.additionalQueryParams.exportLiteral(outfile, level, name_='additionalQueryParams')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.relationalQueryParams is not None:
            showIndent(outfile, level)
            outfile.write('relationalQueryParams=model_.RelationalQueryParamsType(\n')
            self.relationalQueryParams.exportLiteral(outfile, level, name_='relationalQueryParams')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.transactionQueryParams is not None:
            showIndent(outfile, level)
            outfile.write('transactionQueryParams=model_.TransactionQueryParamsType(\n')
            self.transactionQueryParams.exportLiteral(outfile, level, name_='transactionQueryParams')
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
        if nodeName_ == 'mandatoryQueryParams':
            obj_ = MandatoryQueryParamsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.mandatoryQueryParams = obj_
            obj_.original_tagname_ = 'mandatoryQueryParams'
        elif nodeName_ == 'additionalQueryParams':
            obj_ = AdditionalQueryParamsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.additionalQueryParams = obj_
            obj_.original_tagname_ = 'additionalQueryParams'
        elif nodeName_ == 'relationalQueryParams':
            obj_ = RelationalQueryParamsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.relationalQueryParams = obj_
            obj_.original_tagname_ = 'relationalQueryParams'
        elif nodeName_ == 'transactionQueryParams':
            obj_ = TransactionQueryParamsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.transactionQueryParams = obj_
            obj_.original_tagname_ = 'transactionQueryParams'
