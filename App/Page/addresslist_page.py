
#通讯录页面
from appium.webdriver.common.mobileby import MobileBy

#from App.Page.member_invite_menu_page import MemberInviteMenuPage

from App.Page.basepage import BasePage


class AddressListPage(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver
    def click_addmember(self):

        # 点击添加成员 -- 使用页面滑动方式
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()\
        #                          .scrollable(true).instance(0))\
        #                          .scrollIntoView(new UiSelector()\
        #                          .text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        from App.Page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
