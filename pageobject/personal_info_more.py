# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from pageobject.base_page import BasePage
from pageobject.edit_member import EditMember


class PersonalMore(BasePage):
    editmem_element = (MobileBy.XPATH, f"//*[@text='编辑成员']")

    def edit_member(self):
        self.find_and_click(self.editmem_element)
        return EditMember(self.driver)
