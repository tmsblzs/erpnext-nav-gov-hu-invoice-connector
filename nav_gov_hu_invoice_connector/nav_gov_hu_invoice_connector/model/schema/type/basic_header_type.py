import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class BasicHeaderType(GeneratedsSuper):
    """BasicHeaderType -- A kérés tranzakcionális adatai
    Transactional data of the request
    requestId -- A kérés/válasz azonosítója, minden üzenetváltásnál - adószámonként - egyedi
    Identifier of the request/response, unique with the taxnumber in every data exchange transaction
    timestamp -- A kérés/válasz keletkezésének UTC ideje
    UTC time of the request/response
    requestVersion -- A kérés/válasz verziószáma, hogy a hívó melyik interfész verzió szerint küld adatot
     és várja a választ
    Request version number, indicating which datastructure the client sends data in, and in which the response is expected
    headerVersion -- A header verziószáma
    Header version number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, requestId=None, timestamp=None, requestVersion=None, headerVersion=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "common"
        self.requestId = requestId
        self.validate_EntityIdType(self.requestId)
        self.requestId_nsprefix_ = "common"
        if isinstance(timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = timestamp
        self.timestamp = initvalue_
        self.timestamp_nsprefix_ = "common"
        self.requestVersion = requestVersion
        self.validate_AtomicStringType15(self.requestVersion)
        self.requestVersion_nsprefix_ = "common"
        self.headerVersion = headerVersion
        self.validate_AtomicStringType15(self.headerVersion)
        self.headerVersion_nsprefix_ = "common"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BasicHeaderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BasicHeaderType.subclass:
            return BasicHeaderType.subclass(*args_, **kwargs_)
        else:
            return BasicHeaderType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_requestId(self):
        return self.requestId

    def set_requestId(self, requestId):
        self.requestId = requestId

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_requestVersion(self):
        return self.requestVersion

    def set_requestVersion(self, requestVersion):
        self.requestVersion = requestVersion

    def get_headerVersion(self):
        return self.headerVersion

    def set_headerVersion(self, headerVersion):
        self.headerVersion = headerVersion

    def validate_EntityIdType(self, value):
        result = True
        # Validate type EntityIdType, a restriction on AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EntityIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                    encode_str_2_3(value), self.validate_EntityIdType_patterns_,))
                result = False
        return result

    validate_EntityIdType_patterns_ = [['^([+a-zA-Z0-9_]{1,30})$']]

    def validate_GenericTimestampType(self, value):
        result = True
        # Validate type GenericTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not self.gds_validate_simple_patterns(
                    self.validate_GenericTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                    encode_str_2_3(value), self.validate_GenericTimestampType_patterns_,))
                result = False
        return result

    validate_GenericTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d{1,3})?Z)$']]

    def validate_AtomicStringType15(self, value):
        result = True
        # Validate type AtomicStringType15, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on AtomicStringType15' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on AtomicStringType15' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.requestId is not None or
                self.timestamp is not None or
                self.requestVersion is not None or
                self.headerVersion is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
               name_='BasicHeaderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BasicHeaderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BasicHeaderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BasicHeaderType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BasicHeaderType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BasicHeaderType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ',
                        name_='BasicHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.requestId is not None:
            namespaceprefix_ = self.requestId_nsprefix_ + ':' if (UseCapturedNS_ and self.requestId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequestId>%s</%srequestId>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.requestId), input_name='requestId')), namespaceprefix_, eol_))
        if self.timestamp is not None:
            namespaceprefix_ = self.timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stimestamp>%s</%stimestamp>%s' % (
            namespaceprefix_, self.gds_format_datetime(self.timestamp, input_name='timestamp'), namespaceprefix_, eol_))
        if self.requestVersion is not None:
            namespaceprefix_ = self.requestVersion_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.requestVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequestVersion>%s</%srequestVersion>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.requestVersion), input_name='requestVersion')), namespaceprefix_,
                                                                         eol_))
        if self.headerVersion is not None:
            namespaceprefix_ = self.headerVersion_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.headerVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sheaderVersion>%s</%sheaderVersion>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.headerVersion), input_name='headerVersion')), namespaceprefix_,
                                                                       eol_))

    def to_etree(self, parent_element=None, name_='BasicHeaderType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/NTCA/1.0/common}' + name_,
                                        nsmap=nsmap_)
        if self.requestId is not None:
            requestId_ = self.requestId
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}requestId').text = self.gds_format_string(
                requestId_)
        if self.timestamp is not None:
            timestamp_ = self.timestamp
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}timestamp').text = self.gds_format_datetime(
                timestamp_)
        if self.requestVersion is not None:
            requestVersion_ = self.requestVersion
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}requestVersion').text = self.gds_format_string(
                requestVersion_)
        if self.headerVersion is not None:
            headerVersion_ = self.headerVersion
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/NTCA/1.0/common}headerVersion').text = self.gds_format_string(
                headerVersion_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='BasicHeaderType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.requestId is not None:
            showIndent(outfile, level)
            outfile.write('requestId=%s,\n' % self.gds_encode(quote_python(self.requestId)))
        if self.timestamp is not None:
            showIndent(outfile, level)
            outfile.write('timestamp=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(
                self.timestamp, input_name='timestamp'))
        if self.requestVersion is not None:
            showIndent(outfile, level)
            outfile.write('requestVersion=%s,\n' % self.gds_encode(quote_python(self.requestVersion)))
        if self.headerVersion is not None:
            showIndent(outfile, level)
            outfile.write('headerVersion=%s,\n' % self.gds_encode(quote_python(self.headerVersion)))

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
        if nodeName_ == 'requestId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'requestId')
            value_ = self.gds_validate_string(value_, node, 'requestId')
            self.requestId = value_
            self.requestId_nsprefix_ = child_.prefix
            # validate type EntityIdType
            self.validate_EntityIdType(self.requestId)
        elif nodeName_ == 'timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.timestamp = dval_
            self.timestamp_nsprefix_ = child_.prefix
            # validate type GenericTimestampType
            self.validate_GenericTimestampType(self.timestamp)
        elif nodeName_ == 'requestVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'requestVersion')
            value_ = self.gds_validate_string(value_, node, 'requestVersion')
            self.requestVersion = value_
            self.requestVersion_nsprefix_ = child_.prefix
            # validate type AtomicStringType15
            self.validate_AtomicStringType15(self.requestVersion)
        elif nodeName_ == 'headerVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'headerVersion')
            value_ = self.gds_validate_string(value_, node, 'headerVersion')
            self.headerVersion = value_
            self.headerVersion_nsprefix_ = child_.prefix
            # validate type AtomicStringType15
            self.validate_AtomicStringType15(self.headerVersion)
