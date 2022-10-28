import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class VehicleType(GeneratedsSuper):
    """VehicleType -- Szárazföldi közlekedési eszköz további adatai
    Other data in relation to motorised land vehicle
    engineCapacity -- Hengerűrtartalom köbcentiméterben
    Engine capacity in cubic centimetre
    enginePower -- Teljesítmény kW-ban
    Engine power in kW
    kms -- Futott kilométerek száma
    Travelled distance in km

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, engineCapacity=None, enginePower=None, kms=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.engineCapacity = engineCapacity
        self.validate_QuantityType(self.engineCapacity)
        self.engineCapacity_nsprefix_ = None
        self.enginePower = enginePower
        self.validate_QuantityType(self.enginePower)
        self.enginePower_nsprefix_ = None
        self.kms = kms
        self.validate_QuantityType(self.kms)
        self.kms_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VehicleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VehicleType.subclass:
            return VehicleType.subclass(*args_, **kwargs_)
        else:
            return VehicleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_engineCapacity(self):
        return self.engineCapacity
    def set_engineCapacity(self, engineCapacity):
        self.engineCapacity = engineCapacity
    def get_enginePower(self):
        return self.enginePower
    def set_enginePower(self, enginePower):
        self.enginePower = enginePower
    def get_kms(self):
        return self.kms
    def set_kms(self, kms):
        self.kms = kms
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.engineCapacity is not None or
            self.enginePower is not None or
            self.kms is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='VehicleType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VehicleType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VehicleType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VehicleType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VehicleType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VehicleType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='VehicleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.engineCapacity is not None:
            namespaceprefix_ = self.engineCapacity_nsprefix_ + ':' if (UseCapturedNS_ and self.engineCapacity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sengineCapacity>%s</%sengineCapacity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.engineCapacity, input_name='engineCapacity'), namespaceprefix_ , eol_))
        if self.enginePower is not None:
            namespaceprefix_ = self.enginePower_nsprefix_ + ':' if (UseCapturedNS_ and self.enginePower_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%senginePower>%s</%senginePower>%s' % (namespaceprefix_ , self.gds_format_decimal(self.enginePower, input_name='enginePower'), namespaceprefix_ , eol_))
        if self.kms is not None:
            namespaceprefix_ = self.kms_nsprefix_ + ':' if (UseCapturedNS_ and self.kms_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%skms>%s</%skms>%s' % (namespaceprefix_ , self.gds_format_decimal(self.kms, input_name='kms'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VehicleType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.engineCapacity is not None:
            engineCapacity_ = self.engineCapacity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}engineCapacity').text = self.gds_format_decimal(engineCapacity_)
        if self.enginePower is not None:
            enginePower_ = self.enginePower
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}enginePower').text = self.gds_format_decimal(enginePower_)
        if self.kms is not None:
            kms_ = self.kms
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}kms').text = self.gds_format_decimal(kms_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VehicleType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.engineCapacity is not None:
            showIndent(outfile, level)
            outfile.write('engineCapacity=%f,\n' % self.engineCapacity)
        if self.enginePower is not None:
            showIndent(outfile, level)
            outfile.write('enginePower=%f,\n' % self.enginePower)
        if self.kms is not None:
            showIndent(outfile, level)
            outfile.write('kms=%f,\n' % self.kms)
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
        if nodeName_ == 'engineCapacity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'engineCapacity')
            fval_ = self.gds_validate_decimal(fval_, node, 'engineCapacity')
            self.engineCapacity = fval_
            self.engineCapacity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.engineCapacity)
        elif nodeName_ == 'enginePower' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'enginePower')
            fval_ = self.gds_validate_decimal(fval_, node, 'enginePower')
            self.enginePower = fval_
            self.enginePower_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.enginePower)
        elif nodeName_ == 'kms' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'kms')
            fval_ = self.gds_validate_decimal(fval_, node, 'kms')
            self.kms = fval_
            self.kms_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.kms)
