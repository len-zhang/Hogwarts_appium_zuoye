# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from pageobject.base_page import BasePage
from pageobject.contact_search import ContactSearch
from pageobject.member_invite_page import MemberInvite


class AddressBook(BasePage):
    addmember_text = "添加成员"
    search_element = (MobileBy.ID, "com.tencent.wework:id/hk9")

    def add_member(self):
        self.findbyscroll_and_click(self.addmember_text)
        return MemberInvite(self.driver)

    def search(self):
        self.find_and_click(self.search_element)
        return ContactSearch(self.driver)
