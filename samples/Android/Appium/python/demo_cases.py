# -*- coding: UTF-8 -*-
import os
import time
import unittest

import xmlrunner as xmlrunner
from appium import webdriver


class WeTestAppiumTest(unittest.TestCase):
    def setUp(self):
        print('handle driver set up .')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '',  # match all platforms
            'deviceName': '<unknown>',
            'newCommandTimeout': 600,
            'automationName': 'UiAutomator1',
            'appPackage': os.getenv("CT_APP_PKG_NAME"),
            'appWaitPackage': os.getenv("CT_APP_PKG_NAME"),
            'appActivity': os.getenv("CT_APP_LAUNCH_ACTIVITY"),
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    # your test cases start here
    def test_login_failed(self):
        print('test login failed .')
        login = self.driver.find_element_by_id("com.tencent.wetestdemo:id/login")
        login.click()
        time.sleep(10)
        print('test login failed end.')

    def test_login_success(self):
        print('test login success .')
        username = self.driver.find_element_by_id("com.tencent.wetestdemo:id/username")
        username.send_keys("wetestname")
        pwd = self.driver.find_element_by_id("com.tencent.wetestdemo:id/password")
        pwd.send_keys("wetestpwd")
        login = self.driver.find_element_by_id("com.tencent.wetestdemo:id/login")
        login.click()
        time.sleep(10)
        print('test login success end.')

    def test_select_item(self):
        print('test select item .')
        self.test_login_success()
        item1 = self.driver.find_element_by_id("android:id/text1")
        item1.click()
        btn = self.driver.find_element_by_id("com.tencent.wetestdemo:id/submitbtn")
        btn.click()
        time.sleep(10)
        print('test select item end .')

    def test_failed(self):
        print('test failed .')
        assert 2 == 1 + 2
    
    # your test cases end here


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=os.getenv("UPLOADDIR")))
