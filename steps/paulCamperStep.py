import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.paulCamperPage import paulCamperPage

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

@then('user lands on Paul camper home page')
def openHomePage(context):

    context.driver = webdriver.Chrome(executable_path="data\chromedriver.exe", chrome_options=options)
    context.driver.get("https://paulcamper.com/rent-camper/")
    context.driver.maximize_window()
    context.driver.find_element("xpath", "//button[@id = 'onetrust-reject-all-handler' and text()='Only necessary']").click()
    time.sleep(5)

@then('user clicks on Vehicle dropdown in Filter options')
def clickVehicledropDown(context):
    driver = context.driver
    vehicle = paulCamperPage(driver)
    vehicle.click_Vehicle()

@then('user verify Body Style is present and visible')
def verifyBodyStyle(context):
    driver = context.driver
    bodyStyle = paulCamperPage(driver)
    bodyStyle.verify_BodyStyle()

@then('user clicks on Select all Checkbox and verify its functionality')
def verifySelectAll(context):
    driver = context.driver
    selectAll = paulCamperPage(driver)
    selectAll.verify_selectAll_text()
    selectAll.click_selectAll_checkBox()
    time.sleep(5)
    driver.close()