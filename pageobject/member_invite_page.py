# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from pageobject.add_member_page import AddMember
from pageobject.base_page import BasePage


class MemberInvite(BasePage):
    addmember_menul_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def goto_addmemberpage(self):
        self.find_and_click(self.addmember_menul_element)
        return AddMember(self.driver)

    def get_toast(self):
        return self.get_toasttext(self.toast_element)
