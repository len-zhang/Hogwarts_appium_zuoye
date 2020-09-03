# -*- coding:utf-8 -*-
import os
import pytest
import yaml
from pageobject.main_page import MainPage

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


def get_test_data():
    name_list = []
    with open(rootPath + "/data/test_data.yaml", encoding="utf-8") as f:
        test_data = yaml.safe_load(f)
        for i in test_data:
            name_list.append(i[0])
        return [test_data, name_list]


class TestAppium:
    def setup_class(self):
        self.mainpage = MainPage()  # 将MainPage类实例化
        self.mainpage.main_page()  # 调用MainPage类中的main_page方法，使得driver能够被初始化，同时设置好隐式等待

    def teardown_class(self):
        self.mainpage.quit()

    @pytest.mark.parametrize('test_name,test_gender,test_phonenum', get_test_data()[0])
    def test_add_member(self, test_name, test_gender, test_phonenum):
        a = self.mainpage.goto_address_book().add_member().goto_addmemberpage() \
            .edit_name(test_name).edit_gender(test_gender).edit_phone_number(test_phonenum) \
            .click_save().get_toast()
        self.mainpage.switch_main()  # 重新加载launch页，使得下一条新数据的用例可以从首页开始执行
        assert a == "添加成功"

    @pytest.mark.parametrize('test_name', get_test_data()[1])
    def test_del_member(self, test_name):
        b = self.mainpage.goto_address_book().search().input_and_find(test_name).more().edit_member().del_member() \
            .search(test_name)
        assert len(b) == 1
        self.mainpage.switch_main()
