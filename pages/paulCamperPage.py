import time

class paulCamperPage():

    def __init__(self, driver):
        self.driver = driver
        self.vehicle_dropDown_xpath = "//span[@data-test-id='FilterCamperType' and text()='Vehicle']"
        self.bodyStyle_text_xpath = "//span[text()='Body style']"
        self.selectAll_text_xpath = "//div[text()='Select all']"
        self.selectAll_checkBox_xpath = "(//span[@class='checkbox___2AreI'])[8]"

    def click_Vehicle(self):
        self.driver.find_element("xpath", self.vehicle_dropDown_xpath).click()
        time.sleep(5)

    def verify_BodyStyle(self):
        body = self.driver.find_element("xpath", self.bodyStyle_text_xpath).text
        assert body == "BODY STYLE"

    def verify_selectAll_text(self):
        SelectAllText = self.driver.find_element("xpath", self.selectAll_text_xpath).text
        assert SelectAllText == "Select all"

    def click_selectAll_checkBox(self):
        checkBox_SelectAll = self.driver.find_element("xpath", self.selectAll_checkBox_xpath)
        checkBox_SelectAll.click()
