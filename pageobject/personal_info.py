# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from pageobject.base_page import BasePage
from pageobject.personal_info_more import PersonalMore


class PersonalInfo(BasePage):
    more_element = (MobileBy.ID, "com.tencent.wework:id/hjz")

    def more(self):
        self.find_and_click(self.more_element)
        return PersonalMore(self.driver)
