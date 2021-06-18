from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from behave import *


@given(u'I launch chrome browser')
def browser_launch(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when(u'I open Orange HRM Homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'I enter username "{username}" and Password "{password}"')
def enter_data(context, username, password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when(u'I click login button')
def login_click(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'User must successfully logged in')
def verify_login(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    assert text == "Dashboard"
    context.driver.close()
