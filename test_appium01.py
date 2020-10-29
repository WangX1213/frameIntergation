from appium import webdriver

desire_cap = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias"
}

driver = webdriver.Remote("http://127.0.0.1:9555", desire_cap)

el1 = driver.find_element_by_id("com.xueqiu.android:id/input_text")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView[1]")
el3.click()
