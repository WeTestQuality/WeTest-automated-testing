# -*- coding: UTF-8

import os
import unittest
import sys
from altunityrunner import *
import xmlrunner as xmlrunner
import time


class MyFirstTest(unittest.TestCase):

    altUnityDriver = None

    @classmethod
    def setUpClass(cls):
        AltUnityPortForwarding.forward_android()
        cls.altUnityDriver = AltUnityDriver(enable_logging=True)

    @classmethod
    def tearDownClass(cls):
        cls.altUnityDriver.stop()
        AltUnityPortForwarding.remove_forward_android()


    def test_open_store(self):
        print('test case open store start...')
        self.altUnityDriver.load_scene('Start')
        self.altUnityDriver.find_object(By.NAME, "StartButton").tap()
        time.sleep(10)
        self.altUnityDriver.find_object(By.NAME, "StoreButton").tap()
        time.sleep(10)
        store_button = self.altUnityDriver.wait_for_object(By.NAME,"StoreTitle")
        self.assertTrue(store_button.enabled)
        print('test case open store end...')

    def test_start_running(self):
        print('test case cat running start...')
        self.altUnityDriver.load_scene('Start')
        self.altUnityDriver.find_object(By.NAME, "StartButton").tap()
        time.sleep(10)
        self.altUnityDriver.wait_for_current_scene_to_be("Main")
        print('test case cat running end...')



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=os.getenv("UPLOADDIR")))