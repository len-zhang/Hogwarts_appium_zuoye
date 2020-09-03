# -*- coding:utf-8 -*-
import time
from appium.webdriver.common.mobileby import MobileBy
from pageobject.base_page import BasePage
from pageobject.personal_info import PersonalInfo


class ContactSearch(BasePage):
    input_element = (MobileBy.ID, "com.tencent.wework:id/g75")

    def search(self, name):
        self.find_and_sendkeys(self.input_element, name)
        time.sleep(2)
        finaly_contact = self.finds((MobileBy.XPATH, f"//*[@text='{name}']"))
        return finaly_contact

    def input_and_find(self, name):
        self.find_and_sendkeys(self.input_element, name)
        time.sleep(2)
        output_elements = (MobileBy.XPATH, f"//*[@text='{name}']")
        self.finds(output_elements)[1].click()
        return PersonalInfo(self.driver)
