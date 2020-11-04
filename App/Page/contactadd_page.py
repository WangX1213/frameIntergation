"""

编辑联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

#from App.Page.member_invite_menu_page import MemberInviteMenuPage
from App.Page.basepage import BasePage


class ContactAddPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self,name, gender, phonenum):
        # 设置 姓名， 性别， 电话号码
        # editName = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        editName = self.find(MobileBy.XPATH,
                                            "// *[contains( @ text, '姓名')] /../ *[@text = '必填']").send_keys(name)
        # 点击性别按钮
        self.find(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            # 性别选择 --- 男
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        # 输入手机号码
        self.find(MobileBy.XPATH, "//*[contains(@text, '手机')]/../android.widget.EditText").send_keys(
            phonenum)
        # 点击保存
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from App.Page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)

    # def set_name(self):
    #     pass
    #
    # def set_gender(self):
    #     pass
    #
    # def set_phonenum(self):
    #     pass
