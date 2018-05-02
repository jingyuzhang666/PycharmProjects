# coding = utf-8
from appium import webdriver
import time
import os
import sys
#from mobile import get_serialno

#device_id = get_serialno()
#os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()
#print (os_version)
#print (device_id)

desired_caps = {}
# desired_caps = {'platformName': 'android'}
# desired_caps = {'platformVersion': '4.4.2'}
# desired_caps = {'deviceName': 'SM-G955N'}
# desired_caps = {'appPackage': 'cn.com.gtmc.wsi'}
# desired_caps = {'appActivity': 'cn.com.gtmc.wsi.MainActivity'}


desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'SM-G955N'
desired_caps['appPackage'] = 'cn.com.gtmc.wsi'
desired_caps['appActivity'] = '.MainActivity'


# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '7.0'
# desired_caps['deviceName'] = 'Samsung Galaxy S7 edge'
# desired_caps['appPackage'] = 'cn.com.gtmc.wsi'
# desired_caps['appActivity'] = 'cn.com.gtmc.wsi.MainActivity'

diver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)

#diver.find_element_by_name("1").click()
#diver.find_element_by_name("5").click()
#diver.find_element_by_name("9").click()
#diver.find_element_by_name("delete").click()
#diver.find_element_by_name("9").click()
#diver.find_element_by_name("5").click()
#diver.find_element_by_name("+").click()
#diver.find_element_by_name("6").click()
#diver.find_element_by_name("=").click()
diver.quit()

