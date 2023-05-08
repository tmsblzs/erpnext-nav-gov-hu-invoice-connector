import os

from behave import *
from unittest import mock

from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.file_helper import FileHelper
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.helper.response_helper import parse_response
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.hook.scheduler_tasks import import_purchase_invoices
from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.schema.type.function_code_type import \
    FunctionCodeType

use_step_matcher("re")


DEFAULT_XML_PATH = "nav_gov_hu_invoice_connector/tests/drivers"

@when("No purchase invoice")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.response.invoiceDigestResult.availablePage)
    assert context.response.invoiceDigestResult.availablePage == 0


@then("Return without error")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.result.funcCode == FunctionCodeType.OK


@given("Querying purchase invoice")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with mock.patch('nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.service.purchase_invoice.NavApi') \
            as mock_nav_api:
        filename = os.path.join(os.getcwd(), DEFAULT_XML_PATH, 'no-purchase-invoice.xml')
        with open(filename, 'r') as file:
            xml_data = file.read()
        query_invoice_digest_response = parse_response(xml_data)
        query_invoice_digest = mock_nav_api.return_value
        query_invoice_digest.method.return_value = query_invoice_digest_response
        context.response = import_purchase_invoices()
