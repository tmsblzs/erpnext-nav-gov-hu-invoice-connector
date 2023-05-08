import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.detailed_reason_type import \
    DetailedReasonType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.vat_amount_mismatch_type import \
    VatAmountMismatchType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class VatRateType(GeneratedsSuper):
    """VatRateType -- Az adómérték vagy az adómentesértékesítés jelölése
    Marking tax rate or tax exempt supply
    vatPercentage -- Az alkalmazott adómértéke - ÁFA tv. 169. § j)
    Applied tax rate - section 169 (j) of the VAT law
    vatContent -- ÁFA tartalom egyszerűsített számla esetén
    VAT content in case of simplified invoice
    vatExemption -- Az adómentesség jelölése - ÁFA tv. 169. § m)
    Marking tax exemption -  section 169 (m) of the VAT law
    vatOutOfScope -- Az ÁFA törvény hatályán kívüli
    Out of scope of the VAT law
    vatDomesticReverseCharge -- A belföldi fordított adózás jelölése - ÁFA tv. 142. §
    Marking the national is reverse charge taxation - section 142 of the VAT law
    marginSchemeIndicator -- Különbözet szerinti szabályozás jelölése - ÁFA tv. 169. § p) q)
    Marking the margin-scheme taxation as per section 169 (p)(q)
    vatAmountMismatch -- Adóalap és felszámított adóeltérésének esetei
    Different cases of mismatching tax base and levied tax
    noVatCharge -- Nincs felszámított áfa a 17. § alapján
    No VAT charged under Section 17

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatPercentage=None, vatContent=None, vatExemption=None, vatOutOfScope=None, vatDomesticReverseCharge=None, marginSchemeIndicator=None, vatAmountMismatch=None, noVatCharge=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatPercentage = vatPercentage
        self.validate_RateType(self.vatPercentage)
        self.vatPercentage_nsprefix_ = None
        self.vatContent = vatContent
        self.validate_RateType(self.vatContent)
        self.vatContent_nsprefix_ = None
        self.vatExemption = vatExemption
        self.vatExemption_nsprefix_ = None
        self.vatOutOfScope = vatOutOfScope
        self.vatOutOfScope_nsprefix_ = None
        self.vatDomesticReverseCharge = vatDomesticReverseCharge
        self.vatDomesticReverseCharge_nsprefix_ = "xs"
        self.marginSchemeIndicator = marginSchemeIndicator
        self.validate_MarginSchemeType(self.marginSchemeIndicator)
        self.marginSchemeIndicator_nsprefix_ = None
        self.vatAmountMismatch = vatAmountMismatch
        self.vatAmountMismatch_nsprefix_ = None
        self.noVatCharge = noVatCharge
        self.noVatCharge_nsprefix_ = "xs"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateType.subclass:
            return VatRateType.subclass(*args_, **kwargs_)
        else:
            return VatRateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatPercentage(self):
        return self.vatPercentage
    def set_vatPercentage(self, vatPercentage):
        self.vatPercentage = vatPercentage
    def get_vatContent(self):
        return self.vatContent
    def set_vatContent(self, vatContent):
        self.vatContent = vatContent
    def get_vatExemption(self):
        return self.vatExemption
    def set_vatExemption(self, vatExemption):
        self.vatExemption = vatExemption
    def get_vatOutOfScope(self):
        return self.vatOutOfScope
    def set_vatOutOfScope(self, vatOutOfScope):
        self.vatOutOfScope = vatOutOfScope
    def get_vatDomesticReverseCharge(self):
        return self.vatDomesticReverseCharge
    def set_vatDomesticReverseCharge(self, vatDomesticReverseCharge):
        self.vatDomesticReverseCharge = vatDomesticReverseCharge
    def get_marginSchemeIndicator(self):
        return self.marginSchemeIndicator
    def set_marginSchemeIndicator(self, marginSchemeIndicator):
        self.marginSchemeIndicator = marginSchemeIndicator
    def get_vatAmountMismatch(self):
        return self.vatAmountMismatch
    def set_vatAmountMismatch(self, vatAmountMismatch):
        self.vatAmountMismatch = vatAmountMismatch
    def get_noVatCharge(self):
        return self.noVatCharge
    def set_noVatCharge(self, noVatCharge):
        self.noVatCharge = noVatCharge
    def validate_RateType(self, value):
        result = True
        # Validate type RateType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_MarginSchemeType(self, value):
        result = True
        # Validate type MarginSchemeType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['TRAVEL_AGENCY', 'SECOND_HAND', 'ARTWORK', 'ANTIQUES']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on MarginSchemeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on MarginSchemeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on MarginSchemeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.vatPercentage is not None or
            self.vatContent is not None or
            self.vatExemption is not None or
            self.vatOutOfScope is not None or
            self.vatDomesticReverseCharge is not None or
            self.marginSchemeIndicator is not None or
            self.vatAmountMismatch is not None or
            self.noVatCharge is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VatRateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VatRateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatPercentage is not None:
            namespaceprefix_ = self.vatPercentage_nsprefix_ + ':' if (UseCapturedNS_ and self.vatPercentage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatPercentage>%s</%svatPercentage>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatPercentage, input_name='vatPercentage'), namespaceprefix_ , eol_))
        if self.vatContent is not None:
            namespaceprefix_ = self.vatContent_nsprefix_ + ':' if (UseCapturedNS_ and self.vatContent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatContent>%s</%svatContent>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatContent, input_name='vatContent'), namespaceprefix_ , eol_))
        if self.vatExemption is not None:
            namespaceprefix_ = self.vatExemption_nsprefix_ + ':' if (UseCapturedNS_ and self.vatExemption_nsprefix_) else ''
            self.vatExemption.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatExemption', pretty_print=pretty_print)
        if self.vatOutOfScope is not None:
            namespaceprefix_ = self.vatOutOfScope_nsprefix_ + ':' if (UseCapturedNS_ and self.vatOutOfScope_nsprefix_) else ''
            self.vatOutOfScope.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatOutOfScope', pretty_print=pretty_print)
        if self.vatDomesticReverseCharge is not None:
            namespaceprefix_ = self.vatDomesticReverseCharge_nsprefix_ + ':' if (UseCapturedNS_ and self.vatDomesticReverseCharge_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatDomesticReverseCharge>%s</%svatDomesticReverseCharge>%s' % (namespaceprefix_ , self.gds_format_boolean(self.vatDomesticReverseCharge, input_name='vatDomesticReverseCharge'), namespaceprefix_ , eol_))
        if self.marginSchemeIndicator is not None:
            namespaceprefix_ = self.marginSchemeIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.marginSchemeIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smarginSchemeIndicator>%s</%smarginSchemeIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.marginSchemeIndicator), input_name='marginSchemeIndicator')), namespaceprefix_ , eol_))
        if self.vatAmountMismatch is not None:
            namespaceprefix_ = self.vatAmountMismatch_nsprefix_ + ':' if (UseCapturedNS_ and self.vatAmountMismatch_nsprefix_) else ''
            self.vatAmountMismatch.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatAmountMismatch', pretty_print=pretty_print)
        if self.noVatCharge is not None:
            namespaceprefix_ = self.noVatCharge_nsprefix_ + ':' if (UseCapturedNS_ and self.noVatCharge_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snoVatCharge>%s</%snoVatCharge>%s' % (namespaceprefix_ , self.gds_format_boolean(self.noVatCharge, input_name='noVatCharge'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatPercentage is not None:
            vatPercentage_ = self.vatPercentage
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatPercentage').text = self.gds_format_decimal(vatPercentage_)
        if self.vatContent is not None:
            vatContent_ = self.vatContent
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatContent').text = self.gds_format_decimal(vatContent_)
        if self.vatExemption is not None:
            vatExemption_ = self.vatExemption
            vatExemption_.to_etree(element, name_='vatExemption', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatOutOfScope is not None:
            vatOutOfScope_ = self.vatOutOfScope
            vatOutOfScope_.to_etree(element, name_='vatOutOfScope', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatDomesticReverseCharge is not None:
            vatDomesticReverseCharge_ = self.vatDomesticReverseCharge
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatDomesticReverseCharge').text = self.gds_format_boolean(vatDomesticReverseCharge_)
        if self.marginSchemeIndicator is not None:
            marginSchemeIndicator_ = self.marginSchemeIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}marginSchemeIndicator').text = self.gds_format_string(marginSchemeIndicator_)
        if self.vatAmountMismatch is not None:
            vatAmountMismatch_ = self.vatAmountMismatch
            vatAmountMismatch_.to_etree(element, name_='vatAmountMismatch', mapping_=mapping_, nsmap_=nsmap_)
        if self.noVatCharge is not None:
            noVatCharge_ = self.noVatCharge
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}noVatCharge').text = self.gds_format_boolean(noVatCharge_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatPercentage is not None:
            showIndent(outfile, level)
            outfile.write('vatPercentage=%f,\n' % self.vatPercentage)
        if self.vatContent is not None:
            showIndent(outfile, level)
            outfile.write('vatContent=%f,\n' % self.vatContent)
        if self.vatExemption is not None:
            showIndent(outfile, level)
            outfile.write('vatExemption=model_.DetailedReasonType(\n')
            self.vatExemption.exportLiteral(outfile, level, name_='vatExemption')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatOutOfScope is not None:
            showIndent(outfile, level)
            outfile.write('vatOutOfScope=model_.DetailedReasonType(\n')
            self.vatOutOfScope.exportLiteral(outfile, level, name_='vatOutOfScope')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatDomesticReverseCharge is not None:
            showIndent(outfile, level)
            outfile.write('vatDomesticReverseCharge=%s,\n' % self.vatDomesticReverseCharge)
        if self.marginSchemeIndicator is not None:
            showIndent(outfile, level)
            outfile.write('marginSchemeIndicator=%s,\n' % self.gds_encode(quote_python(self.marginSchemeIndicator)))
        if self.vatAmountMismatch is not None:
            showIndent(outfile, level)
            outfile.write('vatAmountMismatch=model_.VatAmountMismatchType(\n')
            self.vatAmountMismatch.exportLiteral(outfile, level, name_='vatAmountMismatch')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.noVatCharge is not None:
            showIndent(outfile, level)
            outfile.write('noVatCharge=%s,\n' % self.noVatCharge)
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
        if nodeName_ == 'vatPercentage' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatPercentage')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatPercentage')
            self.vatPercentage = fval_
            self.vatPercentage_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.vatPercentage)
        elif nodeName_ == 'vatContent' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatContent')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatContent')
            self.vatContent = fval_
            self.vatContent_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.vatContent)
        elif nodeName_ == 'vatExemption':
            obj_ = DetailedReasonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatExemption = obj_
            obj_.original_tagname_ = 'vatExemption'
        elif nodeName_ == 'vatOutOfScope':
            obj_ = DetailedReasonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatOutOfScope = obj_
            obj_.original_tagname_ = 'vatOutOfScope'
        elif nodeName_ == 'vatDomesticReverseCharge':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'vatDomesticReverseCharge')
            ival_ = self.gds_validate_boolean(ival_, node, 'vatDomesticReverseCharge')
            self.vatDomesticReverseCharge = ival_
            self.vatDomesticReverseCharge_nsprefix_ = child_.prefix
        elif nodeName_ == 'marginSchemeIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'marginSchemeIndicator')
            value_ = self.gds_validate_string(value_, node, 'marginSchemeIndicator')
            self.marginSchemeIndicator = value_
            self.marginSchemeIndicator_nsprefix_ = child_.prefix
            # validate type MarginSchemeType
            self.validate_MarginSchemeType(self.marginSchemeIndicator)
        elif nodeName_ == 'vatAmountMismatch':
            obj_ = VatAmountMismatchType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatAmountMismatch = obj_
            obj_.original_tagname_ = 'vatAmountMismatch'
        elif nodeName_ == 'noVatCharge':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'noVatCharge')
            ival_ = self.gds_validate_boolean(ival_, node, 'noVatCharge')
            self.noVatCharge = ival_
            self.noVatCharge_nsprefix_ = child_.prefix
