from appium.webdriver.common.mobileby import MobileBy

#from App.Page.addresslist_page import AddressListPage
from App.Page.basepage import BasePage


class MainPage(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver
    address_element = (MobileBy.XPATH, "// *[@text='通讯录']")
    def goto_message(self):
        """
        进入到消息页
        """
        pass

    def goto_address(self):
        """
        进入到通讯录页
        """
        # 点击通讯录
        #self.find(*self.address_element).click()
        self.find_and_click(*self.address_element)
        from App.Page.addresslist_page import AddressListPage
        return AddressListPage(self.driver)