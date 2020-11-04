from time import sleep

import action as action
import pytest
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #双击
        dbl_click_element = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')

        #单机
        click_element = self.driver.find_element(By.XPATH, '//input[@value="click me"]')

        #右击
        right_click_element = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        action = ActionChains(self.driver)
        #鼠标单击
        action.click(click_element)
        #鼠标双击
        action.double_click(dbl_click_element)
        #鼠标右击
        action.context_click(right_click_element)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com/")
        ele = self.driver.find_element_by_css_selector('[id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_css_selector('[class="drag"]')
        drop_element = self.driver.find_element_by_xpath("/html/body/div[3]")

        action = ActionChains(self.driver)
        #action.drag_and_drop(drag_element,drop_element).perform()
        #action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v','-s','test_ActionChains.py'])
