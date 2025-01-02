from behave import given, when, then


@given('a sample step')
def step_given(context):
    pass


@when('I run the step')
def step_when(context):
    pass


@then('I should see the result')
def step_then(context):
    pass


@then('the result should be correct')
def step_then_correct(context):
    pass


@then('it should not be wrong')
def step_then_not_incorrect(context):
    assert False, "This step is incorrect"
