# -*- coding: UTF-8 -*-
import os
import time
import unittest
import xmlrunner as xmlrunner
import ctlog.logger
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *


class WeTestAirTestDemo(unittest.TestCase):
    def setUp(self):
        self.logger = ctlog.logger.get_log_instance()
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def tearDown(self):
        self.logger.info("end test")

    def test_demo_1(self):
        self.logger.info("test_demo_1")
        self.poco("com.tencent.wetestdemo:id/login").click()
        sleep(5)
        stop_app("com.tencent.wetestdemo")

    def test_demo_2(self):
        self.logger.info("test_demo_2")
        clear_app("com.tencent.wetestdemo")
        start_app("com.tencent.wetestdemo")
        self.poco("com.tencent.wetestdemo:id/username").click()
        sleep(3)
        text("wetest@wetest.net",enter=False)
        sleep(3)
        self.poco("com.tencent.wetestdemo:id/password").click()
        sleep(3)
        text("123456",enter=False)
        sleep(3)
        self.poco("com.tencent.wetestdemo:id/login").click()
        self.poco(text="Item3").swipe([0.0148, -0.2003])
        sleep(3)
        self.poco(text="Item6").click()
        sleep(3)
        self.poco(text="Item7").click()
        sleep(3)
        self.poco("com.tencent.wetestdemo:id/submitbtn").click()
        sleep(3)
        keyevent("HOME")


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=os.getenv("UPLOADDIR")))
