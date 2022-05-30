# -*- coding: UTF-8 -*-
import os
import time
import unittest

from appium import webdriver


class WeTestAppiumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {

            # Appium native capabilities
            'platformName': 'Android',  # Which mobile OS platform to use
            'deviceName': 'Android Phone',  # The kind of mobile device or emulator to use
            'automationName': 'UiAutomator2',  # Which automation engine to use
            'newCommandTimeout': 300,
            # How long (in seconds) Appium will wait for a new command from the client before assuming the client quit and ending the session

            # WeTest capabilities
            'wetest_secret_id': 'YourSecretId',  # Replace with your secret id. This is available in the Accounts view.
            'wetest_secret_key': 'YourSecretKey',  # Replace with your secret key. This is available in the Accounts view.
            'wetest_app_id': 'YourWetestAppId',  # Replace with your app's WeTest app id. Specifies the Application file (.apk /.aab) to be installed on the device.
            'wetest_device_id': 0,  # WeTest device id (For free-trial, you have access to any device in Android Trial Cloud.)  Replace it with the WeTest device id you chosen.
            'wetest_project_id': 'YourProjectId',  # Replace with your WeTest project id.
            'wetest_test_timeout': 1200,  # The timeout for the whole test execution (in seconds)
        }

        # WeTest Appium WebDriver address
        # When running Appium locally, the web driver address is running on a localhost (http://localhost:4723/wd/hub).
        # When running the test from your local machine against a WeTest cloud device, you need to change the Appium server location.
        print("Waiting for response, the process includes WebDriver and Device initialization，App installation, this "
              "typically takes a few mins. Creating at", datetime.now())
        WeTestAppiumTest.driver = webdriver.Remote("https://api.paas.wetest.net/wd/hub", desired_caps)
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
        username = self.driver.find_element_by_id("com.tencent.wetestdemo:id/username")
        username.send_keys("wetestname")
        pwd = self.driver.find_element_by_id("com.tencent.wetestdemo:id/password")
        pwd.send_keys("wetestpwd")
        time.sleep(5)
        login = self.driver.find_element_by_id("com.tencent.wetestdemo:id/login")
        login.click()
        time.sleep(5)
        print('test_login_success end.')
    # your test cases end here


if __name__ == '__main__':
    unittest.main()
