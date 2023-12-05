# The following file specifies the expected behavior of a calculator. You should recognize the Given-When-Then style of representing tests.
# This same structure can be reapplied to describe the intended behavior of any system, in a concise and consistent manner.

from behave import given, when, then

@given('the calculator is on')
def step_given_calculator_on(context):
    context.calculator_on = True

@when('the user adds two numbers')
def step_when_user_adds_numbers(context):
    context.result_sum = 5 + 3

@then('the result should be the sum')
def step_then_result_sum(context):
    assert context.result_sum == 8

@when('the user multiplies two numbers')
def step_when_user_multiplies_numbers(context):
    context.result_product = 5 * 3

@then('the result should be the product')
def step_then_result_product(context):
    assert context.result_product == 15
