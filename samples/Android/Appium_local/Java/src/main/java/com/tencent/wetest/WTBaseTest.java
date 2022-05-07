package com.tencent.wetest;

import java.net.URL;
import java.util.concurrent.TimeUnit;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.openqa.selenium.remote.DesiredCapabilities;

public abstract class WTBaseTest {
    protected static AppiumDriver<MobileElement> driver;
    private static String getServerUrl() {
        // WeTest Driver
        return "https://api.pass.wetest.net/wd/hub";
    }

    private static void initDriver() throws Exception {

        DesiredCapabilities capabilities = new DesiredCapabilities();

        // Appium native capabilities
        capabilities.setCapability("platformName", "Android");
        capabilities.setCapability("deviceName", "Android Phone");
        capabilities.setCapability("newCommandTimeout", 300);
        capabilities.setCapability("automationName", "UiAutomator2");

        // WeTest capabilities
        capabilities.setCapability("wetest_secret_id","YourSecretId"); //Token,this is available in the Accounts view
        capabilities.setCapability("wetest_secret_key","YourSecretKey"); //Token, this is available in the Accounts view
        capabilities.setCapability("wetest_app_id","YourAppId"); //Specifies the Application file (.app/.apk) to be installed on the device.
        capabilities.setCapability("wetest_device_id",0); // WeTest device id（For free-trial, you have access to any device in Android Trial Cloud.）
        capabilities.setCapability("wetest_project_id","YourProjectId"); // WeTest project id
        capabilities.setCapability("wetest_test_timeout",600); //The timeout for the whole test execution (in seconds)
        

        driver = new AndroidDriver<>(new URL(getServerUrl()), capabilities);
        driver.manage().timeouts().implicitlyWait(1800, TimeUnit.SECONDS);
    }

    @BeforeClass
    public static void setUp() throws Exception {
        initDriver();
    }

    @AfterClass
    public static void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
