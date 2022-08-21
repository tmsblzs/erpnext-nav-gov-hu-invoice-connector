import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    CurrentSubclassModule_, getSubclassFromModule_, GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, \
    ModulenotfoundExp_, SaveElementTreeNode, Tag_pattern_, Validate_simpletypes_, encode_str_2_3, quote_xml, \
    quote_python, BaseStrType_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class AnnulmentDataType(GeneratedsSuper):
    """AnnulmentDataType -- Technikai érvénytelenítés státusz adatai
            Status data of technical annulment
    annulmentVerificationStatus -- Technikai érvénytelenítő kérések jóváhagyási státusza
            Verification status of technical annulment requests
    annulmentDecisionDate -- A technikai érvénytelenítés jóváhagyásának vagy elutasításának időpontja UTC időben
            Date of verification or rejection of the technical annulment in UTC time
    annulmentDecisionUser -- A technikai érvénytelenítést jóváhagyó vagy elutasító felhasználó neve
            Login name of the user deciding over the technical annulment's verification or rejection

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, annulmentVerificationStatus=None, annulmentDecisionDate=None, annulmentDecisionUser=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.annulmentVerificationStatus = annulmentVerificationStatus
        self.validate_AnnulmentVerificationStatusType(self.annulmentVerificationStatus)
        self.annulmentVerificationStatus_nsprefix_ = None
        if isinstance(annulmentDecisionDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(annulmentDecisionDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = annulmentDecisionDate
        self.annulmentDecisionDate = initvalue_
        self.annulmentDecisionDate_nsprefix_ = "base"
        self.annulmentDecisionUser = annulmentDecisionUser
        self.validate_LoginType(self.annulmentDecisionUser)
        self.annulmentDecisionUser_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AnnulmentDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AnnulmentDataType.subclass:
            return AnnulmentDataType.subclass(*args_, **kwargs_)
        else:
            return AnnulmentDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_annulmentVerificationStatus(self):
        return self.annulmentVerificationStatus
    def set_annulmentVerificationStatus(self, annulmentVerificationStatus):
        self.annulmentVerificationStatus = annulmentVerificationStatus
    def get_annulmentDecisionDate(self):
        return self.annulmentDecisionDate
    def set_annulmentDecisionDate(self, annulmentDecisionDate):
        self.annulmentDecisionDate = annulmentDecisionDate
    def get_annulmentDecisionUser(self):
        return self.annulmentDecisionUser
    def set_annulmentDecisionUser(self, annulmentDecisionUser):
        self.annulmentDecisionUser = annulmentDecisionUser
    def validate_AnnulmentVerificationStatusType(self, value):
        result = True
        # Validate type AnnulmentVerificationStatusType, a restriction on common:AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['NOT_VERIFIABLE', 'VERIFICATION_PENDING', 'VERIFICATION_DONE', 'VERIFICATION_REJECTED']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on AnnulmentVerificationStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on AnnulmentVerificationStatusType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on AnnulmentVerificationStatusType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
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
    def _hasContent(self):
        if (
            self.annulmentVerificationStatus is not None or
            self.annulmentDecisionDate is not None or
            self.annulmentDecisionUser is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='AnnulmentDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AnnulmentDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AnnulmentDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AnnulmentDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AnnulmentDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AnnulmentDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='AnnulmentDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.annulmentVerificationStatus is not None:
            namespaceprefix_ = self.annulmentVerificationStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.annulmentVerificationStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentVerificationStatus>%s</%sannulmentVerificationStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.annulmentVerificationStatus), input_name='annulmentVerificationStatus')), namespaceprefix_ , eol_))
        if self.annulmentDecisionDate is not None:
            namespaceprefix_ = self.annulmentDecisionDate_nsprefix_ + ':' if (UseCapturedNS_ and self.annulmentDecisionDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentDecisionDate>%s</%sannulmentDecisionDate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.annulmentDecisionDate, input_name='annulmentDecisionDate'), namespaceprefix_ , eol_))
        if self.annulmentDecisionUser is not None:
            namespaceprefix_ = self.annulmentDecisionUser_nsprefix_ + ':' if (UseCapturedNS_ and self.annulmentDecisionUser_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannulmentDecisionUser>%s</%sannulmentDecisionUser>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.annulmentDecisionUser), input_name='annulmentDecisionUser')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AnnulmentDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.annulmentVerificationStatus is not None:
            annulmentVerificationStatus_ = self.annulmentVerificationStatus
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}annulmentVerificationStatus').text = self.gds_format_string(annulmentVerificationStatus_)
        if self.annulmentDecisionDate is not None:
            annulmentDecisionDate_ = self.annulmentDecisionDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}annulmentDecisionDate').text = self.gds_format_datetime(annulmentDecisionDate_)
        if self.annulmentDecisionUser is not None:
            annulmentDecisionUser_ = self.annulmentDecisionUser
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/api}annulmentDecisionUser').text = self.gds_format_string(annulmentDecisionUser_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AnnulmentDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.annulmentVerificationStatus is not None:
            showIndent(outfile, level)
            outfile.write('annulmentVerificationStatus=%s,\n' % self.gds_encode(quote_python(self.annulmentVerificationStatus)))
        if self.annulmentDecisionDate is not None:
            showIndent(outfile, level)
            outfile.write('annulmentDecisionDate=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.annulmentDecisionDate, input_name='annulmentDecisionDate'))
        if self.annulmentDecisionUser is not None:
            showIndent(outfile, level)
            outfile.write('annulmentDecisionUser=%s,\n' % self.gds_encode(quote_python(self.annulmentDecisionUser)))
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
        if nodeName_ == 'annulmentVerificationStatus':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'annulmentVerificationStatus')
            value_ = self.gds_validate_string(value_, node, 'annulmentVerificationStatus')
            self.annulmentVerificationStatus = value_
            self.annulmentVerificationStatus_nsprefix_ = child_.prefix
            # validate type AnnulmentVerificationStatusType
            self.validate_AnnulmentVerificationStatusType(self.annulmentVerificationStatus)
        elif nodeName_ == 'annulmentDecisionDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.annulmentDecisionDate = dval_
            self.annulmentDecisionDate_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.annulmentDecisionDate)
        elif nodeName_ == 'annulmentDecisionUser':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'annulmentDecisionUser')
            value_ = self.gds_validate_string(value_, node, 'annulmentDecisionUser')
            self.annulmentDecisionUser = value_
            self.annulmentDecisionUser_nsprefix_ = child_.prefix
            # validate type LoginType
            self.validate_LoginType(self.annulmentDecisionUser)
