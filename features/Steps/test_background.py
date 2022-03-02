from behave import given, when, then


@given(u'Print "This is Background"')
def step_impl(context):
    print("This is Background")


@then(u'Print "It prints Background everytime"')
def step_impl(context):
    print("It prints Background everytime")


@given(u'Print "is Background Printed"')
def step_impl(context):
    print("is Background Printed")


@when(u'Print "I think so"')
def step_impl(context):
    print("I think so")


@then(u'Print "It\'s passed"')
def step_impl(context):
    print("It\'s passed")


@given(u'Print "Does second Background Printed"')
def step_impl(context):
    print("Does second Background Printed")


@when(u'Print "I am not sure"')
def step_impl(context):
    print("I am not sure")


@then(u'Print "Lets Pass"')
def step_impl(context):
    print("Lets Pass")