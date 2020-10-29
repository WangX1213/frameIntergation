from appium import webdriver

desired_caps={}

desired_caps['platformName']='Android'

desired_caps['platformVersion']='6.0'

desired_caps['deviceName']='emulator-5554'

desired_caps['appPackage']='com.android.settings'

desired_caps['appActivity']='com.android.settings.Settings'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.quit()
# from appium import webdriver
# # from time import sleep
# # sumsung_note8 = {
# #     'platformName': 'Android',
# #     'deviceName': '127.0.0.1:7555',
# #     'platformVersion': '6.0.1',
# #     'appPackage': 'com.taobao.taobao',
# #     'appActivity': 'com.taobao.tao.welcome.Welcome',
# #     'unicodeKeyboard': 'True',  # 使用unicode输入法
# #     'resetKeyboard': "True",    # 重置输入法到初始状态
# #     'noReset': "True"  # 启动app时不要清除app里的原有的数据
# # }
# # driver =webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities = sumsung_note8,keep_alive=True)