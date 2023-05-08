import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.relation_query_date_type import \
    RelationQueryDateType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.relation_query_monetary_type import \
    RelationQueryMonetaryType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class RelationalQueryParamsType(GeneratedsSuper):
    """RelationalQueryParamsType -- A számla lekérdezés relációs paraméterei
    Relational params of the invoice query
    invoiceDelivery -- Számla teljesítési dátumának kereső paramétere
    Query parameter of the invoice delivery date
    paymentDate -- A számla fizetési határidejének kereső paramétere
    Query parameter of the invoice payment date
    invoiceNetAmount -- A számla nettó összeg kereső paramétere a számla pénznemében
    Query parameter of the invoice net amount expressed in the currency of the invoice
    invoiceNetAmountHUF -- A számla nettó összegének kereső paramétere forintban
    Query parameter of the invoice net amount expressed in HUF
    invoiceVatAmount -- A számla ÁFA összegének kereső paramétere a számla pénznemében
    Query parameter of the invoice VAT amount expressed in the currency of the invoice
    invoiceVatAmountHUF -- A számla ÁFA összegének kereső paramétere forintban
    Query parameter of the invoice VAT amount expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoiceDelivery=None, paymentDate=None, invoiceNetAmount=None, invoiceNetAmountHUF=None, invoiceVatAmount=None, invoiceVatAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if invoiceDelivery is None:
            self.invoiceDelivery = []
        else:
            self.invoiceDelivery = invoiceDelivery
        self.invoiceDelivery_nsprefix_ = None
        if paymentDate is None:
            self.paymentDate = []
        else:
            self.paymentDate = paymentDate
        self.paymentDate_nsprefix_ = None
        if invoiceNetAmount is None:
            self.invoiceNetAmount = []
        else:
            self.invoiceNetAmount = invoiceNetAmount
        self.invoiceNetAmount_nsprefix_ = None
        if invoiceNetAmountHUF is None:
            self.invoiceNetAmountHUF = []
        else:
            self.invoiceNetAmountHUF = invoiceNetAmountHUF
        self.invoiceNetAmountHUF_nsprefix_ = None
        if invoiceVatAmount is None:
            self.invoiceVatAmount = []
        else:
            self.invoiceVatAmount = invoiceVatAmount
        self.invoiceVatAmount_nsprefix_ = None
        if invoiceVatAmountHUF is None:
            self.invoiceVatAmountHUF = []
        else:
            self.invoiceVatAmountHUF = invoiceVatAmountHUF
        self.invoiceVatAmountHUF_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RelationalQueryParamsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RelationalQueryParamsType.subclass:
            return RelationalQueryParamsType.subclass(*args_, **kwargs_)
        else:
            return RelationalQueryParamsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceDelivery(self):
        return self.invoiceDelivery
    def set_invoiceDelivery(self, invoiceDelivery):
        self.invoiceDelivery = invoiceDelivery
    def add_invoiceDelivery(self, value):
        self.invoiceDelivery.append(value)
    def insert_invoiceDelivery_at(self, index, value):
        self.invoiceDelivery.insert(index, value)
    def replace_invoiceDelivery_at(self, index, value):
        self.invoiceDelivery[index] = value
    def get_paymentDate(self):
        return self.paymentDate
    def set_paymentDate(self, paymentDate):
        self.paymentDate = paymentDate
    def add_paymentDate(self, value):
        self.paymentDate.append(value)
    def insert_paymentDate_at(self, index, value):
        self.paymentDate.insert(index, value)
    def replace_paymentDate_at(self, index, value):
        self.paymentDate[index] = value
    def get_invoiceNetAmount(self):
        return self.invoiceNetAmount
    def set_invoiceNetAmount(self, invoiceNetAmount):
        self.invoiceNetAmount = invoiceNetAmount
    def add_invoiceNetAmount(self, value):
        self.invoiceNetAmount.append(value)
    def insert_invoiceNetAmount_at(self, index, value):
        self.invoiceNetAmount.insert(index, value)
    def replace_invoiceNetAmount_at(self, index, value):
        self.invoiceNetAmount[index] = value
    def get_invoiceNetAmountHUF(self):
        return self.invoiceNetAmountHUF
    def set_invoiceNetAmountHUF(self, invoiceNetAmountHUF):
        self.invoiceNetAmountHUF = invoiceNetAmountHUF
    def add_invoiceNetAmountHUF(self, value):
        self.invoiceNetAmountHUF.append(value)
    def insert_invoiceNetAmountHUF_at(self, index, value):
        self.invoiceNetAmountHUF.insert(index, value)
    def replace_invoiceNetAmountHUF_at(self, index, value):
        self.invoiceNetAmountHUF[index] = value
    def get_invoiceVatAmount(self):
        return self.invoiceVatAmount
    def set_invoiceVatAmount(self, invoiceVatAmount):
        self.invoiceVatAmount = invoiceVatAmount
    def add_invoiceVatAmount(self, value):
        self.invoiceVatAmount.append(value)
    def insert_invoiceVatAmount_at(self, index, value):
        self.invoiceVatAmount.insert(index, value)
    def replace_invoiceVatAmount_at(self, index, value):
        self.invoiceVatAmount[index] = value
    def get_invoiceVatAmountHUF(self):
        return self.invoiceVatAmountHUF
    def set_invoiceVatAmountHUF(self, invoiceVatAmountHUF):
        self.invoiceVatAmountHUF = invoiceVatAmountHUF
    def add_invoiceVatAmountHUF(self, value):
        self.invoiceVatAmountHUF.append(value)
    def insert_invoiceVatAmountHUF_at(self, index, value):
        self.invoiceVatAmountHUF.insert(index, value)
    def replace_invoiceVatAmountHUF_at(self, index, value):
        self.invoiceVatAmountHUF[index] = value
    def _hasContent(self):
        if (
            self.invoiceDelivery or
            self.paymentDate or
            self.invoiceNetAmount or
            self.invoiceNetAmountHUF or
            self.invoiceVatAmount or
            self.invoiceVatAmountHUF
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='RelationalQueryParamsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RelationalQueryParamsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RelationalQueryParamsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelationalQueryParamsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RelationalQueryParamsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RelationalQueryParamsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='RelationalQueryParamsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for invoiceDelivery_ in self.invoiceDelivery:
            namespaceprefix_ = self.invoiceDelivery_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceDelivery_nsprefix_) else ''
            invoiceDelivery_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceDelivery', pretty_print=pretty_print)
        for paymentDate_ in self.paymentDate:
            namespaceprefix_ = self.paymentDate_nsprefix_ + ':' if (UseCapturedNS_ and self.paymentDate_nsprefix_) else ''
            paymentDate_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='paymentDate', pretty_print=pretty_print)
        for invoiceNetAmount_ in self.invoiceNetAmount:
            namespaceprefix_ = self.invoiceNetAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceNetAmount_nsprefix_) else ''
            invoiceNetAmount_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceNetAmount', pretty_print=pretty_print)
        for invoiceNetAmountHUF_ in self.invoiceNetAmountHUF:
            namespaceprefix_ = self.invoiceNetAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceNetAmountHUF_nsprefix_) else ''
            invoiceNetAmountHUF_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceNetAmountHUF', pretty_print=pretty_print)
        for invoiceVatAmount_ in self.invoiceVatAmount:
            namespaceprefix_ = self.invoiceVatAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceVatAmount_nsprefix_) else ''
            invoiceVatAmount_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceVatAmount', pretty_print=pretty_print)
        for invoiceVatAmountHUF_ in self.invoiceVatAmountHUF:
            namespaceprefix_ = self.invoiceVatAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceVatAmountHUF_nsprefix_) else ''
            invoiceVatAmountHUF_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='invoiceVatAmountHUF', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='RelationalQueryParamsType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        for invoiceDelivery_ in self.invoiceDelivery:
            invoiceDelivery_.to_etree(element, name_='invoiceDelivery', mapping_=mapping_, nsmap_=nsmap_)
        for paymentDate_ in self.paymentDate:
            paymentDate_.to_etree(element, name_='paymentDate', mapping_=mapping_, nsmap_=nsmap_)
        for invoiceNetAmount_ in self.invoiceNetAmount:
            invoiceNetAmount_.to_etree(element, name_='invoiceNetAmount', mapping_=mapping_, nsmap_=nsmap_)
        for invoiceNetAmountHUF_ in self.invoiceNetAmountHUF:
            invoiceNetAmountHUF_.to_etree(element, name_='invoiceNetAmountHUF', mapping_=mapping_, nsmap_=nsmap_)
        for invoiceVatAmount_ in self.invoiceVatAmount:
            invoiceVatAmount_.to_etree(element, name_='invoiceVatAmount', mapping_=mapping_, nsmap_=nsmap_)
        for invoiceVatAmountHUF_ in self.invoiceVatAmountHUF:
            invoiceVatAmountHUF_.to_etree(element, name_='invoiceVatAmountHUF', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='RelationalQueryParamsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('invoiceDelivery=[\n')
        level += 1
        for invoiceDelivery_ in self.invoiceDelivery:
            showIndent(outfile, level)
            outfile.write('model_.RelationQueryDateType(\n')
            invoiceDelivery_.exportLiteral(outfile, level, name_='RelationQueryDateType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('paymentDate=[\n')
        level += 1
        for paymentDate_ in self.paymentDate:
            showIndent(outfile, level)
            outfile.write('model_.RelationQueryDateType(\n')
            paymentDate_.exportLiteral(outfile, level, name_='RelationQueryDateType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('invoiceNetAmount=[\n')
        level += 1
        for invoiceNetAmount_ in self.invoiceNetAmount:
            showIndent(outfile, level)
            outfile.write('model_.RelationQueryMonetaryType(\n')
            invoiceNetAmount_.exportLiteral(outfile, level, name_='RelationQueryMonetaryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('invoiceNetAmountHUF=[\n')
        level += 1
        for invoiceNetAmountHUF_ in self.invoiceNetAmountHUF:
            showIndent(outfile, level)
            outfile.write('model_.RelationQueryMonetaryType(\n')
            invoiceNetAmountHUF_.exportLiteral(outfile, level, name_='RelationQueryMonetaryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('invoiceVatAmount=[\n')
        level += 1
        for invoiceVatAmount_ in self.invoiceVatAmount:
            showIndent(outfile, level)
            outfile.write('model_.RelationQueryMonetaryType(\n')
            invoiceVatAmount_.exportLiteral(outfile, level, name_='RelationQueryMonetaryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('invoiceVatAmountHUF=[\n')
        level += 1
        for invoiceVatAmountHUF_ in self.invoiceVatAmountHUF:
            showIndent(outfile, level)
            outfile.write('model_.RelationQueryMonetaryType(\n')
            invoiceVatAmountHUF_.exportLiteral(outfile, level, name_='RelationQueryMonetaryType')
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
        if nodeName_ == 'invoiceDelivery':
            obj_ = RelationQueryDateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceDelivery.append(obj_)
            obj_.original_tagname_ = 'invoiceDelivery'
        elif nodeName_ == 'paymentDate':
            obj_ = RelationQueryDateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.paymentDate.append(obj_)
            obj_.original_tagname_ = 'paymentDate'
        elif nodeName_ == 'invoiceNetAmount':
            obj_ = RelationQueryMonetaryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceNetAmount.append(obj_)
            obj_.original_tagname_ = 'invoiceNetAmount'
        elif nodeName_ == 'invoiceNetAmountHUF':
            obj_ = RelationQueryMonetaryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceNetAmountHUF.append(obj_)
            obj_.original_tagname_ = 'invoiceNetAmountHUF'
        elif nodeName_ == 'invoiceVatAmount':
            obj_ = RelationQueryMonetaryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceVatAmount.append(obj_)
            obj_.original_tagname_ = 'invoiceVatAmount'
        elif nodeName_ == 'invoiceVatAmountHUF':
            obj_ = RelationQueryMonetaryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.invoiceVatAmountHUF.append(obj_)
            obj_.original_tagname_ = 'invoiceVatAmountHUF'
