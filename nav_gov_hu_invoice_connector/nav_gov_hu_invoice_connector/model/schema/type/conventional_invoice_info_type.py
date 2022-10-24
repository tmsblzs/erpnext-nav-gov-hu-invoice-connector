import datetime as datetime_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.online_invoice import GeneratedsSuper, \
    BaseStrType_, CurrentSubclassModule_, getSubclassFromModule_, Validate_simpletypes_, encode_str_2_3, \
    GenerateDSNamespaceDefs_, UseCapturedNS_, showIndent, quote_xml, ModulenotfoundExp_, quote_python, \
    SaveElementTreeNode, Tag_pattern_
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.contract_numbers_type import \
    ContractNumbersType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.cost_center_type import CostCentersType
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.customer_company_codes_type import \
    CustomerCompanyCodesType

try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


class ConventionalInvoiceInfoType(GeneratedsSuper):
    """ConventionalInvoiceInfoType -- A számlafeldolgozást segítő, egyezményesen nevesített egyéb adatok
    Other conventionally named data to assist in invoice processing
    orderNumbers -- Megrendelés szám(ok)
    Order numbers
    deliveryNotes -- Szállítólevél szám(ok)
    Delivery notes
    shippingDates -- Szállítási dátum(ok)
    Shipping dates
    contractNumbers -- Szerződésszám(ok)
    Contract numbers
    supplierCompanyCodes -- Az eladó vállalati kódja(i)
    Company codes of the supplier
    customerCompanyCodes -- A vevő vállalati kódja(i)
    Company codes of the customer
    dealerCodes -- Beszállító kód(ok)
    Dealer codes
    costCenters -- Költséghely(ek)
    Cost centers
    projectNumbers -- Projektszám(ok)
    Project numbers
    generalLedgerAccountNumbers -- Főkönyvi számlaszám(ok)
    General ledger account numbers
    glnNumbersSupplier -- Kiállítói globális helyazonosító szám(ok)
    Supplier's global location numbers
    glnNumbersCustomer -- Vevői globális helyazonosító szám(ok)
    Customer's global location numbers
    materialNumbers -- Anyagszám(ok)
    Material numbers
    itemNumbers -- Cikkszám(ok)
    Item number(s)
    ekaerIds -- EKÁER azonosító(k)
    EKAER ID-s

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, orderNumbers=None, deliveryNotes=None, shippingDates=None, contractNumbers=None, supplierCompanyCodes=None, customerCompanyCodes=None, dealerCodes=None, costCenters=None, projectNumbers=None, generalLedgerAccountNumbers=None, glnNumbersSupplier=None, glnNumbersCustomer=None, materialNumbers=None, itemNumbers=None, ekaerIds=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.orderNumbers = orderNumbers
        self.orderNumbers_nsprefix_ = None
        self.deliveryNotes = deliveryNotes
        self.deliveryNotes_nsprefix_ = None
        self.shippingDates = shippingDates
        self.shippingDates_nsprefix_ = None
        self.contractNumbers = contractNumbers
        self.contractNumbers_nsprefix_ = None
        self.supplierCompanyCodes = supplierCompanyCodes
        self.supplierCompanyCodes_nsprefix_ = None
        self.customerCompanyCodes = customerCompanyCodes
        self.customerCompanyCodes_nsprefix_ = None
        self.dealerCodes = dealerCodes
        self.dealerCodes_nsprefix_ = None
        self.costCenters = costCenters
        self.costCenters_nsprefix_ = None
        self.projectNumbers = projectNumbers
        self.projectNumbers_nsprefix_ = None
        self.generalLedgerAccountNumbers = generalLedgerAccountNumbers
        self.generalLedgerAccountNumbers_nsprefix_ = None
        self.glnNumbersSupplier = glnNumbersSupplier
        self.glnNumbersSupplier_nsprefix_ = None
        self.glnNumbersCustomer = glnNumbersCustomer
        self.glnNumbersCustomer_nsprefix_ = None
        self.materialNumbers = materialNumbers
        self.materialNumbers_nsprefix_ = None
        self.itemNumbers = itemNumbers
        self.itemNumbers_nsprefix_ = None
        self.ekaerIds = ekaerIds
        self.ekaerIds_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ConventionalInvoiceInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ConventionalInvoiceInfoType.subclass:
            return ConventionalInvoiceInfoType.subclass(*args_, **kwargs_)
        else:
            return ConventionalInvoiceInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orderNumbers(self):
        return self.orderNumbers
    def set_orderNumbers(self, orderNumbers):
        self.orderNumbers = orderNumbers
    def get_deliveryNotes(self):
        return self.deliveryNotes
    def set_deliveryNotes(self, deliveryNotes):
        self.deliveryNotes = deliveryNotes
    def get_shippingDates(self):
        return self.shippingDates
    def set_shippingDates(self, shippingDates):
        self.shippingDates = shippingDates
    def get_contractNumbers(self):
        return self.contractNumbers
    def set_contractNumbers(self, contractNumbers):
        self.contractNumbers = contractNumbers
    def get_supplierCompanyCodes(self):
        return self.supplierCompanyCodes
    def set_supplierCompanyCodes(self, supplierCompanyCodes):
        self.supplierCompanyCodes = supplierCompanyCodes
    def get_customerCompanyCodes(self):
        return self.customerCompanyCodes
    def set_customerCompanyCodes(self, customerCompanyCodes):
        self.customerCompanyCodes = customerCompanyCodes
    def get_dealerCodes(self):
        return self.dealerCodes
    def set_dealerCodes(self, dealerCodes):
        self.dealerCodes = dealerCodes
    def get_costCenters(self):
        return self.costCenters
    def set_costCenters(self, costCenters):
        self.costCenters = costCenters
    def get_projectNumbers(self):
        return self.projectNumbers
    def set_projectNumbers(self, projectNumbers):
        self.projectNumbers = projectNumbers
    def get_generalLedgerAccountNumbers(self):
        return self.generalLedgerAccountNumbers
    def set_generalLedgerAccountNumbers(self, generalLedgerAccountNumbers):
        self.generalLedgerAccountNumbers = generalLedgerAccountNumbers
    def get_glnNumbersSupplier(self):
        return self.glnNumbersSupplier
    def set_glnNumbersSupplier(self, glnNumbersSupplier):
        self.glnNumbersSupplier = glnNumbersSupplier
    def get_glnNumbersCustomer(self):
        return self.glnNumbersCustomer
    def set_glnNumbersCustomer(self, glnNumbersCustomer):
        self.glnNumbersCustomer = glnNumbersCustomer
    def get_materialNumbers(self):
        return self.materialNumbers
    def set_materialNumbers(self, materialNumbers):
        self.materialNumbers = materialNumbers
    def get_itemNumbers(self):
        return self.itemNumbers
    def set_itemNumbers(self, itemNumbers):
        self.itemNumbers = itemNumbers
    def get_ekaerIds(self):
        return self.ekaerIds
    def set_ekaerIds(self, ekaerIds):
        self.ekaerIds = ekaerIds
    def _hasContent(self):
        if (
            self.orderNumbers is not None or
            self.deliveryNotes is not None or
            self.shippingDates is not None or
            self.contractNumbers is not None or
            self.supplierCompanyCodes is not None or
            self.customerCompanyCodes is not None or
            self.dealerCodes is not None or
            self.costCenters is not None or
            self.projectNumbers is not None or
            self.generalLedgerAccountNumbers is not None or
            self.glnNumbersSupplier is not None or
            self.glnNumbersCustomer is not None or
            self.materialNumbers is not None or
            self.itemNumbers is not None or
            self.ekaerIds is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ConventionalInvoiceInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ConventionalInvoiceInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ConventionalInvoiceInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ConventionalInvoiceInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ConventionalInvoiceInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ConventionalInvoiceInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ConventionalInvoiceInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.orderNumbers is not None:
            namespaceprefix_ = self.orderNumbers_nsprefix_ + ':' if (UseCapturedNS_ and self.orderNumbers_nsprefix_) else ''
            self.orderNumbers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='orderNumbers', pretty_print=pretty_print)
        if self.deliveryNotes is not None:
            namespaceprefix_ = self.deliveryNotes_nsprefix_ + ':' if (UseCapturedNS_ and self.deliveryNotes_nsprefix_) else ''
            self.deliveryNotes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='deliveryNotes', pretty_print=pretty_print)
        if self.shippingDates is not None:
            namespaceprefix_ = self.shippingDates_nsprefix_ + ':' if (UseCapturedNS_ and self.shippingDates_nsprefix_) else ''
            self.shippingDates.export(outfile, level, namespaceprefix_, namespacedef_='', name_='shippingDates', pretty_print=pretty_print)
        if self.contractNumbers is not None:
            namespaceprefix_ = self.contractNumbers_nsprefix_ + ':' if (UseCapturedNS_ and self.contractNumbers_nsprefix_) else ''
            self.contractNumbers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='contractNumbers', pretty_print=pretty_print)
        if self.supplierCompanyCodes is not None:
            namespaceprefix_ = self.supplierCompanyCodes_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierCompanyCodes_nsprefix_) else ''
            self.supplierCompanyCodes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplierCompanyCodes', pretty_print=pretty_print)
        if self.customerCompanyCodes is not None:
            namespaceprefix_ = self.customerCompanyCodes_nsprefix_ + ':' if (UseCapturedNS_ and self.customerCompanyCodes_nsprefix_) else ''
            self.customerCompanyCodes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customerCompanyCodes', pretty_print=pretty_print)
        if self.dealerCodes is not None:
            namespaceprefix_ = self.dealerCodes_nsprefix_ + ':' if (UseCapturedNS_ and self.dealerCodes_nsprefix_) else ''
            self.dealerCodes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dealerCodes', pretty_print=pretty_print)
        if self.costCenters is not None:
            namespaceprefix_ = self.costCenters_nsprefix_ + ':' if (UseCapturedNS_ and self.costCenters_nsprefix_) else ''
            self.costCenters.export(outfile, level, namespaceprefix_, namespacedef_='', name_='costCenters', pretty_print=pretty_print)
        if self.projectNumbers is not None:
            namespaceprefix_ = self.projectNumbers_nsprefix_ + ':' if (UseCapturedNS_ and self.projectNumbers_nsprefix_) else ''
            self.projectNumbers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='projectNumbers', pretty_print=pretty_print)
        if self.generalLedgerAccountNumbers is not None:
            namespaceprefix_ = self.generalLedgerAccountNumbers_nsprefix_ + ':' if (UseCapturedNS_ and self.generalLedgerAccountNumbers_nsprefix_) else ''
            self.generalLedgerAccountNumbers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='generalLedgerAccountNumbers', pretty_print=pretty_print)
        if self.glnNumbersSupplier is not None:
            namespaceprefix_ = self.glnNumbersSupplier_nsprefix_ + ':' if (UseCapturedNS_ and self.glnNumbersSupplier_nsprefix_) else ''
            self.glnNumbersSupplier.export(outfile, level, namespaceprefix_, namespacedef_='', name_='glnNumbersSupplier', pretty_print=pretty_print)
        if self.glnNumbersCustomer is not None:
            namespaceprefix_ = self.glnNumbersCustomer_nsprefix_ + ':' if (UseCapturedNS_ and self.glnNumbersCustomer_nsprefix_) else ''
            self.glnNumbersCustomer.export(outfile, level, namespaceprefix_, namespacedef_='', name_='glnNumbersCustomer', pretty_print=pretty_print)
        if self.materialNumbers is not None:
            namespaceprefix_ = self.materialNumbers_nsprefix_ + ':' if (UseCapturedNS_ and self.materialNumbers_nsprefix_) else ''
            self.materialNumbers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='materialNumbers', pretty_print=pretty_print)
        if self.itemNumbers is not None:
            namespaceprefix_ = self.itemNumbers_nsprefix_ + ':' if (UseCapturedNS_ and self.itemNumbers_nsprefix_) else ''
            self.itemNumbers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='itemNumbers', pretty_print=pretty_print)
        if self.ekaerIds is not None:
            namespaceprefix_ = self.ekaerIds_nsprefix_ + ':' if (UseCapturedNS_ and self.ekaerIds_nsprefix_) else ''
            self.ekaerIds.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ekaerIds', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConventionalInvoiceInfoType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.orderNumbers is not None:
            orderNumbers_ = self.orderNumbers
            orderNumbers_.to_etree(element, name_='orderNumbers', mapping_=mapping_, nsmap_=nsmap_)
        if self.deliveryNotes is not None:
            deliveryNotes_ = self.deliveryNotes
            deliveryNotes_.to_etree(element, name_='deliveryNotes', mapping_=mapping_, nsmap_=nsmap_)
        if self.shippingDates is not None:
            shippingDates_ = self.shippingDates
            shippingDates_.to_etree(element, name_='shippingDates', mapping_=mapping_, nsmap_=nsmap_)
        if self.contractNumbers is not None:
            contractNumbers_ = self.contractNumbers
            contractNumbers_.to_etree(element, name_='contractNumbers', mapping_=mapping_, nsmap_=nsmap_)
        if self.supplierCompanyCodes is not None:
            supplierCompanyCodes_ = self.supplierCompanyCodes
            supplierCompanyCodes_.to_etree(element, name_='supplierCompanyCodes', mapping_=mapping_, nsmap_=nsmap_)
        if self.customerCompanyCodes is not None:
            customerCompanyCodes_ = self.customerCompanyCodes
            customerCompanyCodes_.to_etree(element, name_='customerCompanyCodes', mapping_=mapping_, nsmap_=nsmap_)
        if self.dealerCodes is not None:
            dealerCodes_ = self.dealerCodes
            dealerCodes_.to_etree(element, name_='dealerCodes', mapping_=mapping_, nsmap_=nsmap_)
        if self.costCenters is not None:
            costCenters_ = self.costCenters
            costCenters_.to_etree(element, name_='costCenters', mapping_=mapping_, nsmap_=nsmap_)
        if self.projectNumbers is not None:
            projectNumbers_ = self.projectNumbers
            projectNumbers_.to_etree(element, name_='projectNumbers', mapping_=mapping_, nsmap_=nsmap_)
        if self.generalLedgerAccountNumbers is not None:
            generalLedgerAccountNumbers_ = self.generalLedgerAccountNumbers
            generalLedgerAccountNumbers_.to_etree(element, name_='generalLedgerAccountNumbers', mapping_=mapping_, nsmap_=nsmap_)
        if self.glnNumbersSupplier is not None:
            glnNumbersSupplier_ = self.glnNumbersSupplier
            glnNumbersSupplier_.to_etree(element, name_='glnNumbersSupplier', mapping_=mapping_, nsmap_=nsmap_)
        if self.glnNumbersCustomer is not None:
            glnNumbersCustomer_ = self.glnNumbersCustomer
            glnNumbersCustomer_.to_etree(element, name_='glnNumbersCustomer', mapping_=mapping_, nsmap_=nsmap_)
        if self.materialNumbers is not None:
            materialNumbers_ = self.materialNumbers
            materialNumbers_.to_etree(element, name_='materialNumbers', mapping_=mapping_, nsmap_=nsmap_)
        if self.itemNumbers is not None:
            itemNumbers_ = self.itemNumbers
            itemNumbers_.to_etree(element, name_='itemNumbers', mapping_=mapping_, nsmap_=nsmap_)
        if self.ekaerIds is not None:
            ekaerIds_ = self.ekaerIds
            ekaerIds_.to_etree(element, name_='ekaerIds', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ConventionalInvoiceInfoType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.orderNumbers is not None:
            showIndent(outfile, level)
            outfile.write('orderNumbers=model_.OrderNumbersType(\n')
            self.orderNumbers.exportLiteral(outfile, level, name_='orderNumbers')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.deliveryNotes is not None:
            showIndent(outfile, level)
            outfile.write('deliveryNotes=model_.DeliveryNotesType(\n')
            self.deliveryNotes.exportLiteral(outfile, level, name_='deliveryNotes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.shippingDates is not None:
            showIndent(outfile, level)
            outfile.write('shippingDates=model_.ShippingDatesType(\n')
            self.shippingDates.exportLiteral(outfile, level, name_='shippingDates')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.contractNumbers is not None:
            showIndent(outfile, level)
            outfile.write('contractNumbers=model_.ContractNumbersType(\n')
            self.contractNumbers.exportLiteral(outfile, level, name_='contractNumbers')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.supplierCompanyCodes is not None:
            showIndent(outfile, level)
            outfile.write('supplierCompanyCodes=model_.SupplierCompanyCodesType(\n')
            self.supplierCompanyCodes.exportLiteral(outfile, level, name_='supplierCompanyCodes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.customerCompanyCodes is not None:
            showIndent(outfile, level)
            outfile.write('customerCompanyCodes=model_.CustomerCompanyCodesType(\n')
            self.customerCompanyCodes.exportLiteral(outfile, level, name_='customerCompanyCodes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dealerCodes is not None:
            showIndent(outfile, level)
            outfile.write('dealerCodes=model_.DealerCodesType(\n')
            self.dealerCodes.exportLiteral(outfile, level, name_='dealerCodes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.costCenters is not None:
            showIndent(outfile, level)
            outfile.write('costCenters=model_.CostCentersType(\n')
            self.costCenters.exportLiteral(outfile, level, name_='costCenters')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.projectNumbers is not None:
            showIndent(outfile, level)
            outfile.write('projectNumbers=model_.ProjectNumbersType(\n')
            self.projectNumbers.exportLiteral(outfile, level, name_='projectNumbers')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.generalLedgerAccountNumbers is not None:
            showIndent(outfile, level)
            outfile.write('generalLedgerAccountNumbers=model_.GeneralLedgerAccountNumbersType(\n')
            self.generalLedgerAccountNumbers.exportLiteral(outfile, level, name_='generalLedgerAccountNumbers')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.glnNumbersSupplier is not None:
            showIndent(outfile, level)
            outfile.write('glnNumbersSupplier=model_.GlnNumbersType(\n')
            self.glnNumbersSupplier.exportLiteral(outfile, level, name_='glnNumbersSupplier')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.glnNumbersCustomer is not None:
            showIndent(outfile, level)
            outfile.write('glnNumbersCustomer=model_.GlnNumbersType(\n')
            self.glnNumbersCustomer.exportLiteral(outfile, level, name_='glnNumbersCustomer')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.materialNumbers is not None:
            showIndent(outfile, level)
            outfile.write('materialNumbers=model_.MaterialNumbersType(\n')
            self.materialNumbers.exportLiteral(outfile, level, name_='materialNumbers')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.itemNumbers is not None:
            showIndent(outfile, level)
            outfile.write('itemNumbers=model_.ItemNumbersType(\n')
            self.itemNumbers.exportLiteral(outfile, level, name_='itemNumbers')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ekaerIds is not None:
            showIndent(outfile, level)
            outfile.write('ekaerIds=model_.EkaerIdsType(\n')
            self.ekaerIds.exportLiteral(outfile, level, name_='ekaerIds')
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
        if nodeName_ == 'orderNumbers':
            obj_ = OrderNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.orderNumbers = obj_
            obj_.original_tagname_ = 'orderNumbers'
        elif nodeName_ == 'deliveryNotes':
            obj_ = DeliveryNotesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.deliveryNotes = obj_
            obj_.original_tagname_ = 'deliveryNotes'
        elif nodeName_ == 'shippingDates':
            obj_ = ShippingDatesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.shippingDates = obj_
            obj_.original_tagname_ = 'shippingDates'
        elif nodeName_ == 'contractNumbers':
            obj_ = ContractNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contractNumbers = obj_
            obj_.original_tagname_ = 'contractNumbers'
        elif nodeName_ == 'supplierCompanyCodes':
            obj_ = SupplierCompanyCodesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplierCompanyCodes = obj_
            obj_.original_tagname_ = 'supplierCompanyCodes'
        elif nodeName_ == 'customerCompanyCodes':
            obj_ = CustomerCompanyCodesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerCompanyCodes = obj_
            obj_.original_tagname_ = 'customerCompanyCodes'
        elif nodeName_ == 'dealerCodes':
            obj_ = DealerCodesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dealerCodes = obj_
            obj_.original_tagname_ = 'dealerCodes'
        elif nodeName_ == 'costCenters':
            obj_ = CostCentersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.costCenters = obj_
            obj_.original_tagname_ = 'costCenters'
        elif nodeName_ == 'projectNumbers':
            obj_ = ProjectNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.projectNumbers = obj_
            obj_.original_tagname_ = 'projectNumbers'
        elif nodeName_ == 'generalLedgerAccountNumbers':
            obj_ = GeneralLedgerAccountNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.generalLedgerAccountNumbers = obj_
            obj_.original_tagname_ = 'generalLedgerAccountNumbers'
        elif nodeName_ == 'glnNumbersSupplier':
            obj_ = GlnNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.glnNumbersSupplier = obj_
            obj_.original_tagname_ = 'glnNumbersSupplier'
        elif nodeName_ == 'glnNumbersCustomer':
            obj_ = GlnNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.glnNumbersCustomer = obj_
            obj_.original_tagname_ = 'glnNumbersCustomer'
        elif nodeName_ == 'materialNumbers':
            obj_ = MaterialNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.materialNumbers = obj_
            obj_.original_tagname_ = 'materialNumbers'
        elif nodeName_ == 'itemNumbers':
            obj_ = ItemNumbersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.itemNumbers = obj_
            obj_.original_tagname_ = 'itemNumbers'
        elif nodeName_ == 'ekaerIds':
            obj_ = EkaerIdsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ekaerIds = obj_
            obj_.original_tagname_ = 'ekaerIds'
