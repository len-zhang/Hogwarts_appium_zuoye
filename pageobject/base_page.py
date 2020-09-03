# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _current_element: WebElement = None

    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    def switch_main(self):
        self.driver.launch_app()
        return self

    def quit(self):
        return self.driver.quit()

    def find(self, locate):
        return self.driver.find_element(*locate)

    def finds(self, locate):
        return self.driver.find_elements(*locate)

    def find_and_click(self, locate):
        self.find(locate).click()
        return self

    def find_and_sendkeys(self, locate, value):
        self.find(locate).send_keys(value)
        return self

    def findbyscroll_and_click(self, value):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{value}").instance(0));')
        self.find(element).click()
        return self

    def get_toasttext(self, locate):
        text = self.find(locate).text
        return text
