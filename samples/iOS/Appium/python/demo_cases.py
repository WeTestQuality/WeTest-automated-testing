# -*- coding: UTF-8 -*-
import os
import time
import unittest

import xmlrunner as xmlrunner
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


class WeTestAppiumTest(unittest.TestCase):
    def setUp(self):
        print('handle driver set up .')
        desired_caps = {
            'platformName': 'iOS',
            'automationName': 'XCUITest',
            'deviceName': 'iOS',
            'newCommandTimeout': 600,
            'bundleId': 'com.wetest.demo.db',
            'udid': os.getenv("IOS_SERIAL"),
            'webDriverAgentUrl': "http://%s:%s/" % (os.getenv("WDA_SERVER_IP"), os.getenv("WDA_SERVER_PORT")),
            'webviewConnectTimeout': 10000,
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        print('tear down')
        self.driver.quit()

    def check_exists_by_name(self, name):
        try:
            self.driver.find_element_by_name(name)
        except NoSuchElementException:
            return False
        return True

    # demo login success
    def test_login_success(self):
        print('test_login_success')
        self.driver.launch_app()
        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"WeTest Demo\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField")
        el1.send_keys("WeTest@wetest.net")
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"WeTest Demo\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField")
        el2.send_keys("123456")
        self.driver.find_element_by_name("Sign In").click()
        if self.check_exists_by_name("Submit"):
            time.sleep(5)
            assert True
        else:
            assert False

        # demo login success
    def test_select_item_failed(self):
        print('test_select_item_failed')
        self.driver.launch_app()
        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"WeTest Demo\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField")
        el1.send_keys("WeTest@wetest.net")
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"WeTest Demo\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField")
        el2.send_keys("123456")
        self.driver.find_element_by_name("Sign In").click()
        self.driver.find_element_by_name("Submit").click()
        if self.check_exists_by_name("No Item Selected"):
            time.sleep(5)
            assert True
        else:
            assert False
    
    def test_select_item_sucess(self):
        print('test_login_success')
        self.driver.launch_app()
        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"WeTest Demo\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField")
        el1.send_keys("WeTest@wetest.com")
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"WeTest Demo\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField")
        el2.send_keys("123456")
        self.driver.find_element_by_name("Sign In").click()
        self.driver.find_element_by_accessibility_id("Item1").click()
        self.driver.find_element_by_accessibility_id("Item3").click()
        self.driver.find_element_by_name("Submit").click()
        if self.check_exists_by_name("Order Detail"):
            time.sleep(5)
            assert True
        else:
            assert False

    def test_failed(self):
        print('test failed .')
        assert 2 == 1 + 2

    def test_success2(self):
        print('test success.')
        assert 'test' == 'test'

    # def test_select_failed(self):
    #     print('test_select_failed')
    #     self.driver.launch_app()

    # def test_select_success(self):
    #     print('test_select_success')
    #     self.driver.launch_app()

    # # demo select item failed

    # # your test cases 1
    # def test_open_alarm(self):
    #     print('Clicking Alarm tab')
    #     self.driver.launch_app()
    #     if self.check_exists_by_name("Alarm"):
    #         self.driver.find_element_by_name("Alarm").click()
    #         time.sleep(5)
    #         assert True
    #     elif self.check_exists_by_name("闹钟"):
    #         self.driver.find_element_by_name("闹钟").click()
    #         time.sleep(5)
    #         assert True
    #     else:
    #         assert False

    # # your test cases 2
    # def test_open_world_clock(self):
    #     print('Clicking World Clock tab')
    #     self.driver.launch_app()
    #     if self.check_exists_by_name("World Clock"):
    #         self.driver.find_element_by_name("World Clock").click()
    #         time.sleep(5)
    #         assert True
    #     elif self.check_exists_by_name("世界时钟"):
    #         self.driver.find_element_by_name("世界时钟").click()
    #         time.sleep(5)
    #         assert True
    #     else:
    #         assert False

    # # your test cases 3
    # def test_open_nonexistent_thing(self):
    #     print('Clicking a non-existent object.')
    #     if self.check_exists_by_name("non-existent"):
    #         self.driver.find_element_by_name("non-existent").click()
    #         assert True
    #     else:
    #         assert False
    


    # your test cases end here


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=os.getenv("UPLOADDIR")))
