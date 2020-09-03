# -*- coding:utf-8 -*-
import time
from appium.webdriver.common.mobileby import MobileBy
from pageobject.base_page import BasePage


class AddMember(BasePage):
    name_element = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText')
    gender_element = (MobileBy.XPATH, "//*[@text='男']")
    male_element = (MobileBy.XPATH, "//*[@text='男']")
    female_element = (MobileBy.XPATH, "//*[@text='女']")
    phonenum_element = (MobileBy.ID, "com.tencent.wework:id/f9s")
    save_element = (MobileBy.ID, "com.tencent.wework:id/hk6")

    def edit_name(self, name):
        self.find_and_sendkeys(self.name_element, name)
        return self

    def edit_gender(self, gender):
        time.sleep(2)
        self.find_and_click(self.gender_element)
        if gender == "男":
            self.find_and_click(self.male_element)
        else:
            self.find_and_click(self.female_element)
        return self

    def edit_phone_number(self, phone_num):
        self.find_and_sendkeys(self.phonenum_element, phone_num)
        return self

    def click_save(self):
        self.find_and_click(self.save_element)
        from pageobject.member_invite_page import MemberInvite
        return MemberInvite(self.driver)
