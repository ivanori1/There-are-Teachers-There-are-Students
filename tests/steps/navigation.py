from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000')


@step('I am on the page "(.*)"')
def step_impl(context, urlLink):
    expected_url = "http://127.0.0.1:5000/" + urlLink
    assert context.browser.current_url == expected_url
