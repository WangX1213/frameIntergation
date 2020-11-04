from time import sleep

from selenium import webdriver

from base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com/")
        self.driver.find_element_by_link_text('登录').click()
        print(self.driver.current_window_handle) #打印当前页面的 handle
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles) #打印所有页面的handle
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("userman")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys(13500000001)
        sleep(2)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('1037844676@qq.com')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('WangXing12..')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)