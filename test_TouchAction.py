from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):

        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        """
        打开Chrome
        打卡URL： http://www.baidu.com
        向搜索框中输入‘selenium测试’
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        """
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_css_selector('[id="kw"]')
        ele.send_keys("selenium测试")
        ele_search = self.driver.find_element_by_css_selector('[id="su"]')
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele, 0, 10000).perform()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-s', '-v','test_TouchAction.py'])