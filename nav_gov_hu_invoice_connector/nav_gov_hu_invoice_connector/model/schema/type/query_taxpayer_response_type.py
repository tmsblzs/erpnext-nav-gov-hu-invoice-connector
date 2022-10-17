import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_, GenerateDSNamespaceTypePrefixes_, find_attr_value_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.basic_online_invoice_response_type import \
    BasicOnlineInvoiceResponseType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.taxpayer_data import TaxpayerDataType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class QueryTaxpayerResponseType(BasicOnlineInvoiceResponseType):
    """QueryTaxpayerResponseType -- A POST /queryTaxpayer REST operációválasz típusa
    Response type of the POST /queryTaxpayer REST operation
    infoDate -- Az adatok utolsó változásának időpontja
    Last date on which the data was changed
    taxpayerValidity -- Jelzi, hogy a lekérdezett adózó létezik és érvényes-e
    Indicates whether the queried taxpayer is existing and valid
    taxpayerData -- Az adózó lekérdezés válasz adatai
    Response data of the taxpayer query

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BasicOnlineInvoiceResponseType
    def __init__(self, header=None, result=None, software=None, infoDate=None, taxpayerValidity=None, taxpayerData=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryTaxpayerResponseType"), self).__init__(header, result, software, extensiontype_,  **kwargs_)
        if isinstance(infoDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(infoDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = infoDate
        self.infoDate = initvalue_
        self.infoDate_nsprefix_ = "xs"
        self.taxpayerValidity = taxpayerValidity
        self.taxpayerValidity_nsprefix_ = "xs"
        self.taxpayerData = taxpayerData
        self.taxpayerData_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryTaxpayerResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryTaxpayerResponseType.subclass:
            return QueryTaxpayerResponseType.subclass(*args_, **kwargs_)
        else:
            return QueryTaxpayerResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_infoDate(self):
        return self.infoDate
    def set_infoDate(self, infoDate):
        self.infoDate = infoDate
    def get_taxpayerValidity(self):
        return self.taxpayerValidity
    def set_taxpayerValidity(self, taxpayerValidity):
        self.taxpayerValidity = taxpayerValidity
    def get_taxpayerData(self):
        return self.taxpayerData
    def set_taxpayerData(self, taxpayerData):
        self.taxpayerData = taxpayerData
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.infoDate is not None or
            self.taxpayerValidity is not None or
            self.taxpayerData is not None or
            super(QueryTaxpayerResponseType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryTaxpayerResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryTaxpayerResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryTaxpayerResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryTaxpayerResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryTaxpayerResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryTaxpayerResponseType'):
        super(QueryTaxpayerResponseType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryTaxpayerResponseType')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryTaxpayerResponseType', fromsubclass_=False, pretty_print=True):
        super(QueryTaxpayerResponseType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.infoDate is not None:
            namespaceprefix_ = self.infoDate_nsprefix_ + ':' if (UseCapturedNS_ and self.infoDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinfoDate>%s</%sinfoDate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.infoDate, input_name='infoDate'), namespaceprefix_ , eol_))
        if self.taxpayerValidity is not None:
            namespaceprefix_ = self.taxpayerValidity_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerValidity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxpayerValidity>%s</%staxpayerValidity>%s' % (namespaceprefix_ , self.gds_format_boolean(self.taxpayerValidity, input_name='taxpayerValidity'), namespaceprefix_ , eol_))
        if self.taxpayerData is not None:
            namespaceprefix_ = self.taxpayerData_nsprefix_ + ':' if (UseCapturedNS_ and self.taxpayerData_nsprefix_) else ''
            self.taxpayerData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='taxpayerData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryTaxpayerResponseType', mapping_=None, nsmap_=None):
        element = super(QueryTaxpayerResponseType, self).to_etree(parent_element, name_, mapping_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.infoDate is not None:
            infoDate_ = self.infoDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}infoDate').text = self.gds_format_datetime(infoDate_)
        if self.taxpayerValidity is not None:
            taxpayerValidity_ = self.taxpayerValidity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}taxpayerValidity').text = self.gds_format_boolean(taxpayerValidity_)
        if self.taxpayerData is not None:
            taxpayerData_ = self.taxpayerData
            taxpayerData_.to_etree(element, name_='taxpayerData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryTaxpayerResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryTaxpayerResponseType, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryTaxpayerResponseType, self)._exportLiteralChildren(outfile, level, name_)
        if self.infoDate is not None:
            showIndent(outfile, level)
            outfile.write('infoDate=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.infoDate, input_name='infoDate'))
        if self.taxpayerValidity is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerValidity=%s,\n' % self.taxpayerValidity)
        if self.taxpayerData is not None:
            showIndent(outfile, level)
            outfile.write('taxpayerData=model_.TaxpayerDataType(\n')
            self.taxpayerData.exportLiteral(outfile, level, name_='taxpayerData')
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
        super(QueryTaxpayerResponseType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'infoDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.infoDate = dval_
            self.infoDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'taxpayerValidity':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'taxpayerValidity')
            ival_ = self.gds_validate_boolean(ival_, node, 'taxpayerValidity')
            self.taxpayerValidity = ival_
            self.taxpayerValidity_nsprefix_ = child_.prefix
        elif nodeName_ == 'taxpayerData':
            obj_ = TaxpayerDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.taxpayerData = obj_
            obj_.original_tagname_ = 'taxpayerData'
        super(QueryTaxpayerResponseType, self)._buildChildren(child_, node, nodeName_, True)
