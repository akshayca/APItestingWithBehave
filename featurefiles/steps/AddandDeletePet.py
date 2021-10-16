import requests
from behave import *
from utilities.apiresources import *
from utilities.payload import *


@given('the pet details which needs to be added to the Petstore')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + apiresources.addpet
    context.headers = {"Content-Type": "application/json"}
    context.payload = addpetpayloadDefault()


@when(u'we execute the AddPet PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers, )


@then(u'the pet is successfully added')
def step_impl(context):
    try:
        response_json = context.response.json()
        context.petId = response_json['id']
    except:
        print("An exception occured")
        print(context.response.text)


@then(u'status code of response should be {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode


@given(u'the pet details with {name} and {status}')
def step_impl(context, name, status):
    context.url = getconfig()['API']['endpoint'] + apiresources.addpet
    context.headers = {"Content-Type": "application/json"}
    context.payload = addpetpayload(name, status)
