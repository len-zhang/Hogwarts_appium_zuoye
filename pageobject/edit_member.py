# -*- coding:utf-8 -*-
import time
from appium.webdriver.common.mobileby import MobileBy

from pageobject.base_page import BasePage


class EditMember(BasePage):
    ok_element = (MobileBy.XPATH, f"//*[@text='确定']")
    del_mem_element = (MobileBy.ID, "com.tencent.wework:id/e_1")

    def del_member(self):
        self.find_and_click(self.del_mem_element)
        self.find_and_click(self.ok_element)
        time.sleep(2)
        from pageobject.contact_search import ContactSearch
        return ContactSearch(self.driver)
