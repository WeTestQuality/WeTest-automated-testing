# -*- coding: UTF-8 -*-
import os
import time
import unittest

import xmlrunner as xmlrunner
import ctlog.logger
from poco.drivers.unity3d import UnityPoco


class WeTestAirTestDemo(unittest.TestCase):
    def setUp(self):
        self.logger = ctlog.logger.get_log_instance()
        self.poco = UnityPoco()

    def tearDown(self):
        self.logger.info("end test")

    def click_start(self,btn_name):
        for i in range(15):
            self.poco('btn_start').click()
            time.sleep(1.5)
            if self.poco(btn_name).exists():
                self.logger.info("click start ok in %d times", i)
                break
            else:
                self.logger.info("click start failed in %d times,continue", i)

    def select_drop(self):
        for i in range(3):
            self.poco('drag_and_drop').click()
            time.sleep(1.5)
            if self.poco('shell').exists():
                self.logger.info("select drop ok in %d times", i)
                break

    def test_demo_1(self):
        self.click_start('drag_and_drop')
        self.select_drop()

    def test_demo_2(self):
        shell = self.poco('shell').focus('center')
        for star in self.poco('star'):
            star.drag_to(shell)
        time.sleep(3)
        # assert self.poco('scoreVal').get_text() == "100", "score correct."
        self.poco('btn_back', type='Button').click()
        time.sleep(3)
        self.logger.info("back to the screen")


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=os.getenv("UPLOADDIR")))
