# coding = utf-8

import time
from appium import webdriver

"""
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities()
capabilities.__setattr__('deviceName', 'SM-G955N')
capabilities.__setattr__('automationName', 'Appium')
capabilities.__setattr__('platformName', 'Android')
capabilities.__setattr__('platformVersion', '4.4.2')
capabilities.__setattr__('appPackage', 'com.youba.calculate')
capabilities.__setattr__('appActivity', 'com.youba.calculate.MainActivity')

diver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
"""
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'SM-G955N'
desired_caps['appPackage'] = 'com.youba.calculate'
desired_caps['appActivity'] = '.MainActivity'

diver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

diver.find_element_by_id('btn_eight').click()
diver.find_element_by_id('btn_plus').click()
diver.find_element_by_id('btn_nine').click()
diver.find_element_by_id('btn_equal').click()
#获取最终结果并输出
result = diver
time.sleep(10)

diver.quit()
