import datetime as datetime_

import pytz

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_


class InvoiceReferenceDataType(GeneratedsSuper):
    """InvoiceReferenceDataType -- A módosítás vagy érvénytelenítés adatai
    Modification or cancellation data
    originalInvoiceNumber -- Az eredeti számla sorszáma, melyre a módosítás vonatkozik - ÁFA tv. 170. § (1) c)
            Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law
    modifyWithoutMaster -- Annak jelzése, hogy a módosítás olyan alapszámlára hivatkozik, amelyről nem történt
                        és nem is fog történni adatszolgáltatás
            Indicates whether the modification references to an original invoice which is not and will not be exchanged
    modificationTimestamp -- A módosító okirat készítésének idő bélyege a forrásrendszerben UTC időben
            Creation date timestamp of the modification document in UTC time
    modificationIndex -- A számlára vonatkozó módosító okirat egyedi sorszáma
            The unique sequence number referring to the original invoice

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, originalInvoiceNumber=None, modifyWithoutMaster=None, modificationTimestamp=None,
                 modificationIndex=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.originalInvoiceNumber = originalInvoiceNumber
        self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
        self.originalInvoiceNumber_nsprefix_ = "common"
        self.modifyWithoutMaster = modifyWithoutMaster
        self.modifyWithoutMaster_nsprefix_ = "xs"
        if isinstance(modificationTimestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(modificationTimestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = modificationTimestamp
        self.modificationTimestamp = initvalue_
        self.modificationTimestamp_nsprefix_ = "base"
        self.modificationIndex = modificationIndex
        self.validate_InvoiceUnboundedIndexType(self.modificationIndex)
        self.modificationIndex_nsprefix_ = "base"

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceReferenceDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceReferenceDataType.subclass:
            return InvoiceReferenceDataType.subclass(*args_, **kwargs_)
        else:
            return InvoiceReferenceDataType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_originalInvoiceNumber(self):
        return self.originalInvoiceNumber

    def set_originalInvoiceNumber(self, originalInvoiceNumber):
        self.originalInvoiceNumber = originalInvoiceNumber

    def get_modifyWithoutMaster(self):
        return self.modifyWithoutMaster

    def set_modifyWithoutMaster(self, modifyWithoutMaster):
        self.modifyWithoutMaster = modifyWithoutMaster

    def get_modificationTimestamp(self):
        return self.modificationTimestamp

    def set_modificationTimestamp(self, modificationTimestamp):
        self.modificationTimestamp = modificationTimestamp

    def get_modificationIndex(self):
        return self.modificationIndex

    def set_modificationIndex(self, modificationIndex):
        self.modificationIndex = modificationIndex

    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_,))
                result = False
        return result

    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]

    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime_.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {
                        "value": value, "lineno": lineno})
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (
                encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_,))
                result = False
        return result

    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]

    def validate_InvoiceUnboundedIndexType(self, value):
        result = True
        # Validate type InvoiceUnboundedIndexType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceUnboundedIndexType' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.originalInvoiceNumber is not None or
                self.modifyWithoutMaster is not None or
                self.modificationTimestamp is not None or
                self.modificationIndex is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
               name_='InvoiceReferenceDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceReferenceDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceReferenceDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceReferenceDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceReferenceDataType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='InvoiceReferenceDataType'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='',
                        namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ',
                        name_='InvoiceReferenceDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.originalInvoiceNumber is not None:
            namespaceprefix_ = self.originalInvoiceNumber_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.originalInvoiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalInvoiceNumber>%s</%soriginalInvoiceNumber>%s' % (namespaceprefix_,
                                                                                       self.gds_encode(
                                                                                           self.gds_format_string(
                                                                                               quote_xml(
                                                                                                   self.originalInvoiceNumber),
                                                                                               input_name='originalInvoiceNumber')),
                                                                                       namespaceprefix_, eol_))
        if self.modifyWithoutMaster is not None:
            namespaceprefix_ = self.modifyWithoutMaster_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.modifyWithoutMaster_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smodifyWithoutMaster>%s</%smodifyWithoutMaster>%s' % (
            namespaceprefix_, self.gds_format_boolean(self.modifyWithoutMaster, input_name='modifyWithoutMaster'),
            namespaceprefix_, eol_))
        if self.modificationTimestamp is not None:
            namespaceprefix_ = self.modificationTimestamp_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.modificationTimestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smodificationTimestamp>%s</%smodificationTimestamp>%s' % (
            namespaceprefix_, self.gds_format_datetime(self.modificationTimestamp, input_name='modificationTimestamp'),
            namespaceprefix_, eol_))
        if self.modificationIndex is not None:
            namespaceprefix_ = self.modificationIndex_nsprefix_ + ':' if (
                        UseCapturedNS_ and self.modificationIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smodificationIndex>%s</%smodificationIndex>%s' % (
            namespaceprefix_, self.gds_format_integer(self.modificationIndex, input_name='modificationIndex'),
            namespaceprefix_, eol_))

    def to_etree(self, parent_element=None, name_='InvoiceReferenceDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/api}' + name_, nsmap=nsmap_)
        if self.originalInvoiceNumber is not None:
            originalInvoiceNumber_ = self.originalInvoiceNumber
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}originalInvoiceNumber').text = self.gds_format_string(
                originalInvoiceNumber_)
        if self.modifyWithoutMaster is not None:
            modifyWithoutMaster_ = self.modifyWithoutMaster
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}modifyWithoutMaster').text = self.gds_format_boolean(
                modifyWithoutMaster_)
        if self.modificationTimestamp is not None:
            modificationTimestamp_ = self.modificationTimestamp
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}modificationTimestamp').text = self.gds_format_datetime(
                modificationTimestamp_)
        if self.modificationIndex is not None:
            modificationIndex_ = self.modificationIndex
            etree_.SubElement(element,
                              '{http://schemas.nav.gov.hu/OSA/3.0/api}modificationIndex').text = self.gds_format_integer(
                modificationIndex_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element

    def exportLiteral(self, outfile, level, name_='InvoiceReferenceDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)

    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass

    def _exportLiteralChildren(self, outfile, level, name_):
        if self.originalInvoiceNumber is not None:
            showIndent(outfile, level)
            outfile.write('originalInvoiceNumber=%s,\n' % self.gds_encode(quote_python(self.originalInvoiceNumber)))
        if self.modifyWithoutMaster is not None:
            showIndent(outfile, level)
            outfile.write('modifyWithoutMaster=%s,\n' % self.modifyWithoutMaster)
        if self.modificationTimestamp is not None:
            showIndent(outfile, level)
            outfile.write(
                'modificationTimestamp=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(
                    self.modificationTimestamp, input_name='modificationTimestamp'))
        if self.modificationIndex is not None:
            showIndent(outfile, level)
            outfile.write('modificationIndex=%d,\n' % self.modificationIndex)

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
        if nodeName_ == 'originalInvoiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalInvoiceNumber')
            value_ = self.gds_validate_string(value_, node, 'originalInvoiceNumber')
            self.originalInvoiceNumber = value_
            self.originalInvoiceNumber_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.originalInvoiceNumber)
        elif nodeName_ == 'modifyWithoutMaster':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'modifyWithoutMaster')
            ival_ = self.gds_validate_boolean(ival_, node, 'modifyWithoutMaster')
            self.modifyWithoutMaster = ival_
            self.modifyWithoutMaster_nsprefix_ = child_.prefix
        elif nodeName_ == 'modificationTimestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.modificationTimestamp = dval_
            self.modificationTimestamp_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.modificationTimestamp)
        elif nodeName_ == 'modificationIndex' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'modificationIndex')
            ival_ = self.gds_validate_integer(ival_, node, 'modificationIndex')
            self.modificationIndex = ival_
            self.modificationIndex_nsprefix_ = child_.prefix
            # validate type InvoiceUnboundedIndexType
            self.validate_InvoiceUnboundedIndexType(self.modificationIndex)
