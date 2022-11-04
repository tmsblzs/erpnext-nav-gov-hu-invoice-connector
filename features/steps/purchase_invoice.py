from behave import *
from unittest import mock

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.file_helper import FileHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.hook.scheduler_tasks import import_purchase_invoices
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.function_code_type import \
    FunctionCodeType

use_step_matcher("re")


DEFAULT_XML_PATH = "/home/frappe/frappe-bench/apps/nav_gov_hu_invoice_connector/features/drivers"

@when("No purchase invoice")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert (context.response.invoiceDigestResult.availablePage == 0)


@then("Return without error")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert (context.response.result.funcCode == FunctionCodeType.OK)


@given("Querying purchase invoice")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.nav_gov_hu.nav_api.query_invoice_digest') \
            as query_invoice_digest:
        filename = FileHelper().get_abs_path(DEFAULT_XML_PATH, 'no-purchase-invoice.xml')
        with open(filename, 'r') as file:
            xml_data = file.read()
        query_invoice_digest.return_value = xml_data
        context.response = import_purchase_invoices()
