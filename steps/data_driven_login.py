from selenium import webdriver
from behave import *
from webdriver_manager.chrome import ChromeDriverManager


@given(u'Launching the chrome browser')
def browser_launch(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when(u'Open the Homepage')
def homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter the username "{username}" and password "{password}"')
def enter_data(context, username, password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when(u'I click the Login button')
def login_click(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'User successfully logged in when the data is valid')
def verify_login(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
