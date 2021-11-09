# WeTest Jenkins Plugin

### 1. About WeTest 

WeTest is a full-scale testing platform for each stage of your development and operations lifecycle.By using WeTest platform, your team members are able to ensure complete digital confidence in your application's behavior and performance on any mobile device, regardless of complicated user environments(OS,Device...etc). 

For more details, please visit  [WeTest Official Website](https://www.wetest.net/)

### 2. About WeTest Automated Testing

Automated testing can increase the depth and scope of tests and significantly improve software quality.Depending on the size of the project and the application, test automation will always provide a good return on investment. Once tests have been created, automated tests can be run over and over again at no additional cost. Test automation typically reduces the time required to run repetitive tests from weeks to hours. 

WeTest provides a professional cloud-based mobile app testing platform that allows you to perform automated testing in popular framework against real Android and iOS devices, so you can troubleshoot issues in your development and operations lifecycle before being reported by your customers.The infrastructure is build to support unlimited number of simultaneous test runs, meaning that you can choose any number of devices for your test run.

### 3. WeTest Jenkins Integration
Integration with the Jenkins to trigger Automated Tests with each build action. Once you build an app, the system can automatically push it for testing on devices on cloud. This saves a lot of time, produces instant results and developers can fix any issues instantly.

#### Step1. Install the Plugin

Install the WeTest plugin locally

* Download the plugin from our GitHub repository
* Install the plugin in Jenkins Plugin Management

#### Step2. Credential Settings

1. Go to **Manage Jenkins > Configure System**
2. Fill in the necessary information in the **WeTest Automated Testing** section. 
3. Click the  **Save** button to validate account details

**Secret id**: you can find it in your user settings

**Secret Key:** you can find it in your user settings

**WeTest URL**：pre.api.paas.wetest.net

**ToolPath**：cloudtest

**Protocol**：https:// 

#### Step3. Build Step

Open an existing Jenkins job or create a new one. From the job configuration, add a new build step. (**Configure-Build--Add build step--WeTest Automated Testing**) 

To run automated tests , select a target project, and fill in the necessary information.

**Project**: Target project name for automated testing.

**Target OS Type**: OS, Android or iOS

**Application**: 

* Local absolute path required
* eg:
  * Windows: C:\Users\jenkins\test.apk
  * Mac: /Users/jenkins/test.apk

**Test Script**

* Local absolute path required
* eg:
  * Windows: C:\Users\jenkins\test.zip 
  * Mac: /Users/jenkins/test.zip

**Framework**：Testing Framework

**Device group**：A set of devices which is chosen by user and used for test running. If you do not have a device group yet, please create one on our website first.

**Advanced Setting**

* Device time-out period
  * The timeout of the each device running in your test. The default value is 10 minutes. 
* Test time-out period
  * The timeout of the this test run. The default value is 30 minutes. 

#### Step4. Build your Job

Build your Job and you will see the log information in console.
