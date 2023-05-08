import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AuditDataType(GeneratedsSuper):
    """AuditDataType -- A számla audit adatai
    Invoice audit data
    insdate -- A beszúrás időpontja UTC időben
            Insert date in UTC time
    insCusUser -- A beszúrást végző technikai felhasználó
            Inserting technical user name
    source -- Az adatszolgáltatás forrása
            Data exchange source
    transactionId -- A számla tranzakció azonosítója, ha az gépi interfészen került beküldésre
            Transaction ID of the invoice if it was exchanged via M2M interface
    index -- A számla sorszáma a kérésen belül
            Sequence number of the invoice within the request
    batchIndex -- A módosító okirat sorszáma a kötegen belül
            Sequence number of the modification document within the batch
    originalRequestVersion -- Az adatszolgáltatás requestVersion értéke
            requestVersion value of the invoice exchange

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, insdate=None, insCusUser=None, source=None, transactionId=None, index=None, batchIndex=None, originalRequestVersion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(insdate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(insdate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = insdate
        self.insdate = initvalue_
        self.insdate_nsprefix_ = "base"
        self.insCusUser = insCusUser
        self.validate_LoginType(self.insCusUser)
        self.insCusUser_nsprefix_ = "common"
        self.source = source
        self.validate_SourceType(self.source)
        self.source_nsprefix_ = None
        self.transactionId = transactionId
        self.validate_EntityIdType(self.transactionId)
        self.transactionId_nsprefix_ = "common"
        self.index = index
        self.validate_InvoiceIndexType(self.index)
        self.index_nsprefix_ = "base"
        self.batchIndex = batchIndex
        self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        self.batchIndex_nsprefix_ = "base"
        self.originalRequestVersion = originalRequestVersion
        self.validate_OriginalRequestVersionType(self.originalRequestVersion)
        self.originalRequestVersion_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AuditDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AuditDataType.subclass:
            return AuditDataType.subclass(*args_, **kwargs_)
        else:
            return AuditDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_insdate(self):
        return self.insdate
    def set_insdate(self, insdate):
        self.insdate = insdate
    def get_insCusUser(self):
        return self.insCusUser
    def set_insCusUser(self, insCusUser):
        self.insCusUser = insCusUser
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_batchIndex(self):
        return self.batchIndex
    def set_batchIndex(self, batchIndex):
        self.batchIndex = batchIndex
    def get_originalRequestVersion(self):
        return self.originalRequestVersion
    def set_originalRequestVersion(self, originalRequestVersion):
        self.originalRequestVersion = originalRequestVersion
    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_, ))
                result = False
        return result
    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]
    def validate_LoginType(self, value):
        result = True
        # Validate type LoginType, a restriction on AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LoginType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LoginType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LoginType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LoginType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_LoginType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_LoginType_patterns_, ))
                result = False
        return result
    validate_LoginType_patterns_ = [['^([a-zA-Z0-9]{6,15})$']]
    def validate_SourceType(self, value):
        result = True
        # Validate type SourceType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['WEB', 'XML', 'MGM', 'OPG', 'OSZ']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on SourceType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SourceType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SourceType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_EntityIdType(self, value):
        result = True
        # Validate type EntityIdType, a restriction on AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EntityIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EntityIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EntityIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_EntityIdType_patterns_, ))
                result = False
        return result
    validate_EntityIdType_patterns_ = [['^([+a-zA-Z0-9_]{1,30})$']]
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
    def validate_InvoiceUnboundedIndexType(self, value):
        result = True
        # Validate type InvoiceUnboundedIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceUnboundedIndexType' % {"value": value, "lineno": lineno} )
                result = False
        return result
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
            self.insdate is not None or
            self.insCusUser is not None or
            self.source is not None or
            self.transactionId is not None or
            self.index is not None or
            self.batchIndex is not None or
            self.originalRequestVersion is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AuditDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AuditDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AuditDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AuditDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AuditDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AuditDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='AuditDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.insdate is not None:
            namespaceprefix_ = self.insdate_nsprefix_ + ':' if (UseCapturedNS_ and self.insdate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinsdate>%s</%sinsdate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.insdate, input_name='insdate'), namespaceprefix_ , eol_))
        if self.insCusUser is not None:
            namespaceprefix_ = self.insCusUser_nsprefix_ + ':' if (UseCapturedNS_ and self.insCusUser_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinsCusUser>%s</%sinsCusUser>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.insCusUser), input_name='insCusUser')), namespaceprefix_ , eol_))
        if self.source is not None:
            namespaceprefix_ = self.source_nsprefix_ + ':' if (UseCapturedNS_ and self.source_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssource>%s</%ssource>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.source), input_name='source')), namespaceprefix_ , eol_))
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transactionId), input_name='transactionId')), namespaceprefix_ , eol_))
        if self.index is not None:
            namespaceprefix_ = self.index_nsprefix_ + ':' if (UseCapturedNS_ and self.index_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindex>%s</%sindex>%s' % (namespaceprefix_ , self.gds_format_integer(self.index, input_name='index'), namespaceprefix_ , eol_))
        if self.batchIndex is not None:
            namespaceprefix_ = self.batchIndex_nsprefix_ + ':' if (UseCapturedNS_ and self.batchIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbatchIndex>%s</%sbatchIndex>%s' % (namespaceprefix_ , self.gds_format_integer(self.batchIndex, input_name='batchIndex'), namespaceprefix_ , eol_))
        if self.originalRequestVersion is not None:
            namespaceprefix_ = self.originalRequestVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.originalRequestVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalRequestVersion>%s</%soriginalRequestVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.originalRequestVersion), input_name='originalRequestVersion')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AuditDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.insdate is not None:
            insdate_ = self.insdate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}insdate').text = self.gds_format_datetime(insdate_)
        if self.insCusUser is not None:
            insCusUser_ = self.insCusUser
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}insCusUser').text = self.gds_format_string(insCusUser_)
        if self.source is not None:
            source_ = self.source
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}source').text = self.gds_format_string(source_)
        if self.transactionId is not None:
            transactionId_ = self.transactionId
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}transactionId').text = self.gds_format_string(transactionId_)
        if self.index is not None:
            index_ = self.index
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}index').text = self.gds_format_integer(index_)
        if self.batchIndex is not None:
            batchIndex_ = self.batchIndex
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}batchIndex').text = self.gds_format_integer(batchIndex_)
        if self.originalRequestVersion is not None:
            originalRequestVersion_ = self.originalRequestVersion
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion').text = self.gds_format_string(originalRequestVersion_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AuditDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.insdate is not None:
            showIndent(outfile, level)
            outfile.write('insdate=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.insdate, input_name='insdate'))
        if self.insCusUser is not None:
            showIndent(outfile, level)
            outfile.write('insCusUser=%s,\n' % self.gds_encode(quote_python(self.insCusUser)))
        if self.source is not None:
            showIndent(outfile, level)
            outfile.write('source=%s,\n' % self.gds_encode(quote_python(self.source)))
        if self.transactionId is not None:
            showIndent(outfile, level)
            outfile.write('transactionId=%s,\n' % self.gds_encode(quote_python(self.transactionId)))
        if self.index is not None:
            showIndent(outfile, level)
            outfile.write('index=%d,\n' % self.index)
        if self.batchIndex is not None:
            showIndent(outfile, level)
            outfile.write('batchIndex=%d,\n' % self.batchIndex)
        if self.originalRequestVersion is not None:
            showIndent(outfile, level)
            outfile.write('originalRequestVersion=%s,\n' % self.gds_encode(quote_python(self.originalRequestVersion)))
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
        if nodeName_ == 'insdate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.insdate = dval_
            self.insdate_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.insdate)
        elif nodeName_ == 'insCusUser':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'insCusUser')
            value_ = self.gds_validate_string(value_, node, 'insCusUser')
            self.insCusUser = value_
            self.insCusUser_nsprefix_ = child_.prefix
            # validate type LoginType
            self.validate_LoginType(self.insCusUser)
        elif nodeName_ == 'source':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'source')
            value_ = self.gds_validate_string(value_, node, 'source')
            self.source = value_
            self.source_nsprefix_ = child_.prefix
            # validate type SourceType
            self.validate_SourceType(self.source)
        elif nodeName_ == 'transactionId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transactionId')
            value_ = self.gds_validate_string(value_, node, 'transactionId')
            self.transactionId = value_
            self.transactionId_nsprefix_ = child_.prefix
            # validate type EntityIdType
            self.validate_EntityIdType(self.transactionId)
        elif nodeName_ == 'index' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'index')
            ival_ = self.gds_validate_integer(ival_, node, 'index')
            self.index = ival_
            self.index_nsprefix_ = child_.prefix
            # validate type InvoiceIndexType
            self.validate_InvoiceIndexType(self.index)
        elif nodeName_ == 'batchIndex' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'batchIndex')
            ival_ = self.gds_validate_integer(ival_, node, 'batchIndex')
            self.batchIndex = ival_
            self.batchIndex_nsprefix_ = child_.prefix
            # validate type InvoiceUnboundedIndexType
            self.validate_InvoiceUnboundedIndexType(self.batchIndex)
        elif nodeName_ == 'originalRequestVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalRequestVersion')
            value_ = self.gds_validate_string(value_, node, 'originalRequestVersion')
            self.originalRequestVersion = value_
            self.originalRequestVersion_nsprefix_ = child_.prefix
            # validate type OriginalRequestVersionType
            self.validate_OriginalRequestVersionType(self.originalRequestVersion)
