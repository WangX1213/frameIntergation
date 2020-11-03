from appium import webdriver
import time

desired_caps={}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '6.0'

desired_caps['deviceName'] = '127.0.0.1:7555'

desired_caps['appPackage'] = 'com.xueqiu.android'

desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'

desired_caps['noSet'] = "true"

desired_caps['dontStopAppOnReset'] = "true"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.implicitly_wait(10)

driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()

driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')

time.sleep(3)
driver.back()
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