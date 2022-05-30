# -*- coding: UTF-8 -*-

import os
import time
import unittest

from appium import webdriver
from datetime import datetime


class WeTestAppiumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {

            # Appium native capabilities
            'platformName': 'iOS',  # Which mobile OS platform to use
            'deviceName': 'iPhone',  # The kind of mobile device to use
            'automationName': 'XCUITest',  # Which automation engine to use
            'newCommandTimeout': 300, # How long (in seconds) Appium will wait for a new command from the client before assuming the client quit and ending the session

            'bundleId': 'com.your.app.bundle.id',  # Replace with your app bundle id.

            # WeTest capabilities
            'wetest_secret_id': 'YourSecretId', # Replace with your secret id. This is available in the Accounts view.
            'wetest_secret_key': 'YourSecretKey', # Replace with your secret key. This is available in the Accounts view.
            'wetest_app_id': 'YourWetestAppId', # Replace with your app's WeTest app id. Specifies the Application file (.apk /.aab) to be installed on the device.
            'wetest_device_id': 1234,  # Replace with the WeTest device id you chosen.
            'wetest_project_id': 'YourProjectId',  # Replace with your WeTest project id.
            'wetest_test_timeout': 1200,  # The timeout for the whole test execution (in seconds)
        }

        # WeTest Appium WebDriver address
        # When running Appium locally, the web driver address is running on a localhost (http://localhost:4723/wd/hub).
        # When running the test from your local machine against a WeTest cloud device, you need to change the Appium server location.
        print("Waiting for response, the process includes WebDriver and Device initialization，App installation, this "
              "typically takes a few mins. Creating at", datetime.now())
        WeTestAppiumTest.driver = webdriver.Remote("https://pre.api.paas.wetest.net/wd/hub", desired_caps)
        print("Connecting to WeTest WebDriver successfully with Session ID:", WeTestAppiumTest.driver.session_id,
              ". Finished at ", datetime.now())

    @classmethod
    def tearDownClass(cls):
        print('Quiting')
        WeTestAppiumTest.driver.quit()

    def setUp(self):
        print('case setup')

    def tearDown(self):
        print('case tear down')

    # your test cases start here
    # this function is just a sample test case for com.tencent.wetestdemo package
    def test_login_success(self):
        print('test_login_success start.')
        username = self.driver.find_element_by_xpath("//XCUIElementTypeTextField")
        username.send_keys("WeTest@wetest.net")
        password = self.driver.find_element_by_xpath("//XCUIElementTypeSecureTextField")
        password.send_keys("123456")
        time.sleep(6)
        self.driver.find_element_by_name("Sign In").click()
        time.sleep(6)
        print('test_login_success end.')
    # your test cases end here


if __name__ == '__main__':
    unittest.main()

