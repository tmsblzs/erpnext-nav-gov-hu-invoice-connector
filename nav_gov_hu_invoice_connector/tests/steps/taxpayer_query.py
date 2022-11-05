from behave import *

use_step_matcher("re")


@given("Open new customer add form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given   Open new customer add form')


@when("Enter at least the first eight number of the tax number of the customer")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When    Enter at least the first eight number of the taxnumber of the customer')


@step("Click Nav menu Query taxpayer menuitem")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     Click Nav menu Query taxpayer menuitem')


@when("Enter tax number that length is less than eight number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When    Enter tax number that length is less than eight number')


@then("Show error message tax number is not valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then    Show error message tax number is not valid')


@when("Enter tax number that is not exists")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When    Enter tax number that is not exists')


@then("Show error message the given tax number is not exists")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then    Show error message the given tax number is not exists')


@given("Enter a tax number that is already saved for a customer")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given   Enter a tax number that is already saved for a customer')


@when("Display a dialog 'Would you like to modified an existing customer\?'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When    Display a dialog \'Would you like to modified an existing customer?\'')


@step("Answer 'No'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     Answer \'No\'')


@then("Not modified the existing customer")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then    Not modified the existing customer')


@then("Adjust the existing customer's data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then    Adjust the existing customer\'s data')


@step("Answer 'Yes'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     Answer \'Yes\'')


@step("Display dialog window with taxpayer data and answer 'Yes'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     Display dialog window with taxpayer data and answer \'Yes\'')


@then("Save tax payer data to database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then    Save tax payer data to database')


@step("Display dialog window with taxpayer data and answer 'No'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     Display dialog window with taxpayer data and answer \'No\'')


@then("Not save tax payer data to database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then    Not save tax payer data to database')


@given("Open an existing customer form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given   Open an existing customer form')


@when("Adjust tax number for an existing customer")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When    Adjust tax number for an existing customer')