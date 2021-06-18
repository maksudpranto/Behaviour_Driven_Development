from selenium import webdriver
from behave import *
from webdriver_manager.chrome import ChromeDriverManager


@given(u'Launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'Open Facebook page')
def open_facebook(context):
    context.driver.get("https://facebook.com")


@then(u'Verify the title')
def verify_title(context):
    title = context.driver.title

    assert title == "Facebook – log in or sign up"


@then(u'Close the browser')
def close_browser(context):
    context.driver.close()
