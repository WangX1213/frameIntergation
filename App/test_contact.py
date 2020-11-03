from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:

    def setup_class(self):
        # 定义一个字典
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = "launch.WwMainActivity"
        #noReset 保留缓存 ， 比如登录状态
        caps["noReset"] = "True"
        #不停止应用， 直接运行测试用例
        #caps["dontStopAppOnReset"] = "True"
        caps["skipDeviceInitialization"] = "True"
        caps["skipServerInstallation"] = "True"
        #caps["settings[waitForIdleTimeout]"] = 0
        caps["ensureWebviewsHavePages"] = True

        # 关键 localhost:4723  本机ip : server端口
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        name = "hogwarts_003"
        gender = "男"
        phonenum = "13500000004"
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH, "// *[@text='通讯录']").click()
        #点击添加成员 -- 使用页面滑动方式
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        #点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, "// *[@text='手动输入添加']").click()
        #输入姓名
        #editName = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        editName = self.driver.find_element(MobileBy.XPATH, "// *[contains( @ text, '姓名')] /../ *[@text = '必填']").send_keys(name)
        #点击性别按钮
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self.driver,10).until(lambda x:x.find_element(MobileBy.XPATH,"//*[@text='女']"))
            #性别选择 --- 男
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        #输入手机号码
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/../android.widget.EditText").send_keys(phonenum)
        #点击保存
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(2)
        print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        assert result == "添加成功"