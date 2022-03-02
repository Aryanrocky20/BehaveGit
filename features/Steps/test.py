from behave import *           ##### given, when, then

@given(u'Print "First Scenario - Single Parameter"')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given Print "First Scenario - Single Parameter"')
    print("First Scenario - Single Parameter")


@when(u'Two variables "{a}" and "{b}"')
def step_impl(context, a, b):
    context.var1 = int(a)
    context.var2 = int(b)


@then(u'Add Two Variable')
def step_impl(context):
    context.sum = context.var1 + context.var2
    print(context.sum)


@then(u'Check output is "{c}"')
def step_impl(context, c):
    context.var3 = int(c)
    if context.sum == context.var3:
        assert True
    else:
        assert False


@given(u'Print "Second Scenario - Multiple Parameter"')
def step_impl(context):
    print("Second Scenario - Multiple Parameter")

#
# @when(u'Two variables "15" and "10"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Two variables "15" and "10"')
#
#
# @when(u'Two variables "6" and "12"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Two variables "6" and "12"')
#
#
# @then(u'Check output is "18"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Check output is "18"')
#
#
# @when(u'Two variables "50" and "10"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Two variables "50" and "10"')
#
#
# @then(u'Check output is "60"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Check output is "60"')
#
#
# @when(u'Two variables "50" and "20"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Two variables "50" and "20"')
#
#
# @then(u'Check output is "75"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Check output is "75"')
