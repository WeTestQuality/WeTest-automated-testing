# -*- coding: UTF-8 -*-
import os
import time
import unittest
import xmlrunner as xmlrunner
import ctlog.logger
from airtest.core.api import *
#from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
init_device()
app_package = "com.tencent.wetestdemo"


class WeTestAirTestDemo(unittest.TestCase):
    def setUp(self):
        self.logger = ctlog.logger.get_log_instance()
        self.logger.info("=======start task=======")
        #self.poco = UnityPoco()

    def tearDown(self):
        self.logger.info("=======end task=======")

    def setup_method(self, method):
        self.logger.info("=======start App=======")
        clear_app(app_package)
        time.sleep(3)
        start_app(app_package)
        #self.poco("com.oohoo.videocollection:id/welcome_btn").click()

    def teardown_method(self, method):
        self.logger.info("=======stop App=======")
        time.sleep(3)
        #stop_app(app_package)

    def test_login_failed(self):
        touch(Template(r"tpl1660630233595.png", record_pos=(0.005, 0.071), resolution=(1080, 2340)))
        time.sleep(5)

    def test_login(self):
        touch(Template(r"tpl1660630659309.png", record_pos=(-0.262, -0.437), resolution=(1080, 2340)))
        time.sleep(5)
        text("wetest",enter=False)
        touch(Template(r"tpl1660630669822.png", record_pos=(-0.253, -0.284), resolution=(1080, 2340)))
        time.sleep(5)
        text("123456",enter=False)
        time.sleep(5)
        touch(Template(r"tpl1660630233595.png", record_pos=(0.005, 0.071), resolution=(1080, 2340)))
        # swipe(Template(r"tpl1660630354970.png", record_pos=(-0.093, 0.447), resolution=(1080, 2340)), vector=[-0.3391, -0.2707])
        # touch(Template(r"tpl1660630618215.png", record_pos=(-0.317, 0.152), resolution=(1080, 2340)))
        # touch(Template(r"tpl1660630629370.png", record_pos=(-0.291, 0.29), resolution=(1080, 2340)))
        # touch(Template(r"tpl1660630602461.png", record_pos=(-0.351, -0.698), resolution=(1080, 2340)))
        print("test_login success")


    def test_success(self):
        self.logger.info('test sucess .')
        assert 2 == 2


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=os.getenv("UPLOADDIR")))
