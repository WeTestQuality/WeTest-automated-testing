# Appium Python Samples

This folder contains a sample test case with Appium and Unittest. In order to know more details of using Appium to run your test
in WeTest Automation, please view our online doc `https://iwiki.woa.com/pages/viewpage.action?pageId=162053150`.

## Environment

* Operating   System	:    Ubuntu 20.04.2 LTS
* Python  Version	 	 :    Python  3.8.10 
* Appium   Version	   :    Appium 1.19.1
* Java   Version               :   openjdk version "1.8.0_292" 

## Folder Content

This folder contains the following files:

* `demo_cases.py` is the actual test cases written in Python with Unittest framework. This is just a template, you can download and insert your cases into it.
* `runTest.sh`  is environment specific shell scripts which will be executed by WeTest Cloud when the test is started on some device. It is not necessary to change it.
* `create-zip.sh` is a shell script used to package your test files into a zip file, then you are able to upload the zip file to WeTest Cloud and run your test.

