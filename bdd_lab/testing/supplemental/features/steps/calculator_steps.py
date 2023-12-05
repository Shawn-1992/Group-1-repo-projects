# The following file specifies the expected behavior of a calculator. You should recognize the Given-When-Then style
# of representing testing. This same structure can be reapplied to describe the intended behavior of any system,
# in a concise and consistent manner.

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


@when('the user divides two numbers')
def step_when_user_divides_numbers(context):
    context.result_quotient = 10 / 2


@then('the result should be the quotient')
def step_then_result_quotient(context):
    assert context.result_quotient == 5


@when('the user subtracts two numbers')
def step_when_user_subtracts_numbers(context):
    context.result_difference = 8 - 3


@then('the result should be the difference')
def step_then_result_difference(context):
    assert context.result_difference == 5


@when('the user subtracts a larger number from a smaller number')
def step_when_user_subtracts_larger_from_smaller(context):
    context.result_negative_difference = 3 - 8


@then('the result should be a negative difference')
def step_then_result_negative_difference(context):
    assert context.result_negative_difference == -5
