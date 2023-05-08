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


class TransactionType(GeneratedsSuper):
    """TransactionType -- Tranzakció lekérdezési eredmény
    Transaction query result
    insDate -- A beszúrás időpontja UTC időben
    Insert date in UTC time
    insCusUser -- A beszúrást végző felhasználó
    Inserting user name
    source -- Az adatszolgáltatás forrása
    Data exchange source
    transactionId -- A számla tranzakció azonosítója
    Transaction ID of the invoice
    requestStatus -- A kérés feldolgozási státusza
    Processing status of the request
    technicalAnnulment -- Jelöli ha a tranzakció technikai érvénytelenítést tartalmaz
    Indicates whether the transaction contains technical annulment
    originalRequestVersion -- Az adatszolgáltatás requestVersion értéke
    requestVersion value of the invoice exchange
    itemCount -- Az adatszolgáltatás tételeinek száma
    Item count of the invoiceExchange

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, insDate=None, insCusUser=None, source=None, transactionId=None, requestStatus=None, technicalAnnulment=None, originalRequestVersion=None, itemCount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(insDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(insDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = insDate
        self.insDate = initvalue_
        self.insDate_nsprefix_ = "base"
        self.insCusUser = insCusUser
        self.validate_LoginType(self.insCusUser)
        self.insCusUser_nsprefix_ = "common"
        self.source = source
        self.validate_SourceType(self.source)
        self.source_nsprefix_ = None
        self.transactionId = transactionId
        self.validate_EntityIdType(self.transactionId)
        self.transactionId_nsprefix_ = "common"
        self.requestStatus = requestStatus
        self.validate_RequestStatusType(self.requestStatus)
        self.requestStatus_nsprefix_ = None
        self.technicalAnnulment = technicalAnnulment
        self.technicalAnnulment_nsprefix_ = "xs"
        self.originalRequestVersion = originalRequestVersion
        self.validate_OriginalRequestVersionType(self.originalRequestVersion)
        self.originalRequestVersion_nsprefix_ = None
        self.itemCount = itemCount
        self.validate_InvoiceIndexType(self.itemCount)
        self.itemCount_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransactionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransactionType.subclass:
            return TransactionType.subclass(*args_, **kwargs_)
        else:
            return TransactionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_insDate(self):
        return self.insDate
    def set_insDate(self, insDate):
        self.insDate = insDate
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
    def get_requestStatus(self):
        return self.requestStatus
    def set_requestStatus(self, requestStatus):
        self.requestStatus = requestStatus
    def get_technicalAnnulment(self):
        return self.technicalAnnulment
    def set_technicalAnnulment(self, technicalAnnulment):
        self.technicalAnnulment = technicalAnnulment
    def get_originalRequestVersion(self):
        return self.originalRequestVersion
    def set_originalRequestVersion(self, originalRequestVersion):
        self.originalRequestVersion = originalRequestVersion
    def get_itemCount(self):
        return self.itemCount
    def set_itemCount(self, itemCount):
        self.itemCount = itemCount
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
    def validate_RequestStatusType(self, value):
        result = True
        # Validate type RequestStatusType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['RECEIVED', 'PROCESSING', 'SAVED', 'FINISHED', 'NOTIFIED']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on RequestStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RequestStatusType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on RequestStatusType' % {"value" : value, "lineno": lineno} )
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
    def _hasContent(self):
        if (
            self.insDate is not None or
            self.insCusUser is not None or
            self.source is not None or
            self.transactionId is not None or
            self.requestStatus is not None or
            self.technicalAnnulment is not None or
            self.originalRequestVersion is not None or
            self.itemCount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='TransactionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransactionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransactionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransactionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransactionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TransactionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='TransactionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.insDate is not None:
            namespaceprefix_ = self.insDate_nsprefix_ + ':' if (UseCapturedNS_ and self.insDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinsDate>%s</%sinsDate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.insDate, input_name='insDate'), namespaceprefix_ , eol_))
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
        if self.requestStatus is not None:
            namespaceprefix_ = self.requestStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.requestStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequestStatus>%s</%srequestStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.requestStatus), input_name='requestStatus')), namespaceprefix_ , eol_))
        if self.technicalAnnulment is not None:
            namespaceprefix_ = self.technicalAnnulment_nsprefix_ + ':' if (UseCapturedNS_ and self.technicalAnnulment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stechnicalAnnulment>%s</%stechnicalAnnulment>%s' % (namespaceprefix_ , self.gds_format_boolean(self.technicalAnnulment, input_name='technicalAnnulment'), namespaceprefix_ , eol_))
        if self.originalRequestVersion is not None:
            namespaceprefix_ = self.originalRequestVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.originalRequestVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalRequestVersion>%s</%soriginalRequestVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.originalRequestVersion), input_name='originalRequestVersion')), namespaceprefix_ , eol_))
        if self.itemCount is not None:
            namespaceprefix_ = self.itemCount_nsprefix_ + ':' if (UseCapturedNS_ and self.itemCount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sitemCount>%s</%sitemCount>%s' % (namespaceprefix_ , self.gds_format_integer(self.itemCount, input_name='itemCount'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TransactionType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.insDate is not None:
            insDate_ = self.insDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}insDate').text = self.gds_format_datetime(insDate_)
        if self.insCusUser is not None:
            insCusUser_ = self.insCusUser
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}insCusUser').text = self.gds_format_string(insCusUser_)
        if self.source is not None:
            source_ = self.source
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}source').text = self.gds_format_string(source_)
        if self.transactionId is not None:
            transactionId_ = self.transactionId
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}transactionId').text = self.gds_format_string(transactionId_)
        if self.requestStatus is not None:
            requestStatus_ = self.requestStatus
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}requestStatus').text = self.gds_format_string(requestStatus_)
        if self.technicalAnnulment is not None:
            technicalAnnulment_ = self.technicalAnnulment
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}technicalAnnulment').text = self.gds_format_boolean(technicalAnnulment_)
        if self.originalRequestVersion is not None:
            originalRequestVersion_ = self.originalRequestVersion
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}originalRequestVersion').text = self.gds_format_string(originalRequestVersion_)
        if self.itemCount is not None:
            itemCount_ = self.itemCount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}itemCount').text = self.gds_format_integer(itemCount_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TransactionType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.insDate is not None:
            showIndent(outfile, level)
            outfile.write('insDate=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.insDate, input_name='insDate'))
        if self.insCusUser is not None:
            showIndent(outfile, level)
            outfile.write('insCusUser=%s,\n' % self.gds_encode(quote_python(self.insCusUser)))
        if self.source is not None:
            showIndent(outfile, level)
            outfile.write('source=%s,\n' % self.gds_encode(quote_python(self.source)))
        if self.transactionId is not None:
            showIndent(outfile, level)
            outfile.write('transactionId=%s,\n' % self.gds_encode(quote_python(self.transactionId)))
        if self.requestStatus is not None:
            showIndent(outfile, level)
            outfile.write('requestStatus=%s,\n' % self.gds_encode(quote_python(self.requestStatus)))
        if self.technicalAnnulment is not None:
            showIndent(outfile, level)
            outfile.write('technicalAnnulment=%s,\n' % self.technicalAnnulment)
        if self.originalRequestVersion is not None:
            showIndent(outfile, level)
            outfile.write('originalRequestVersion=%s,\n' % self.gds_encode(quote_python(self.originalRequestVersion)))
        if self.itemCount is not None:
            showIndent(outfile, level)
            outfile.write('itemCount=%d,\n' % self.itemCount)
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
        if nodeName_ == 'insDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.insDate = dval_
            self.insDate_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.insDate)
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
        elif nodeName_ == 'requestStatus':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'requestStatus')
            value_ = self.gds_validate_string(value_, node, 'requestStatus')
            self.requestStatus = value_
            self.requestStatus_nsprefix_ = child_.prefix
            # validate type RequestStatusType
            self.validate_RequestStatusType(self.requestStatus)
        elif nodeName_ == 'technicalAnnulment':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'technicalAnnulment')
            ival_ = self.gds_validate_boolean(ival_, node, 'technicalAnnulment')
            self.technicalAnnulment = ival_
            self.technicalAnnulment_nsprefix_ = child_.prefix
        elif nodeName_ == 'originalRequestVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalRequestVersion')
            value_ = self.gds_validate_string(value_, node, 'originalRequestVersion')
            self.originalRequestVersion = value_
            self.originalRequestVersion_nsprefix_ = child_.prefix
            # validate type OriginalRequestVersionType
            self.validate_OriginalRequestVersionType(self.originalRequestVersion)
        elif nodeName_ == 'itemCount' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'itemCount')
            ival_ = self.gds_validate_integer(ival_, node, 'itemCount')
            self.itemCount = ival_
            self.itemCount_nsprefix_ = child_.prefix
            # validate type InvoiceIndexType
            self.validate_InvoiceIndexType(self.itemCount)
