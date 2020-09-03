# -*- coding:utf-8 -*-
import os
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from pageobject.address_book_page import AddressBook
from pageobject.base_page import BasePage

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


# 将不同app的参数统一放入yaml中再获取
def get_cap():
    with open(rootPath + "/data/caps.yaml", encoding="utf-8") as f:
        data_list = yaml.safe_load(f)
        # desire_cap_weixin = data_list["desire_cap_weixin"]
        # desire_cap_xueqiu = data_list["desire_cap_xueqiu"]
        return data_list


class MainPage(BasePage):
    addresslist_elemenet = (MobileBy.XPATH, "//*[@text='通讯录']")

    def main_page(self):
        if self.driver is None:
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", get_cap()["desire_cap_weixin"])
            self.driver.implicitly_wait(10)
        return self

    def goto_address_book(self):
        self.find_and_click(self.addresslist_elemenet)
        return AddressBook(self.driver)
