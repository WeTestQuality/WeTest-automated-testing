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
        return "http://localhost:4723/wd/hub";
    }

    private static void initDriver() throws Exception {

        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("platformVersion", "");
        capabilities.setCapability("platformName", "Android");
        capabilities.setCapability("deviceName", "<unknown>");
        capabilities.setCapability("newCommandTimeout", 600);
        capabilities.setCapability("automationName", "UiAutomator1");
        capabilities.setCapability("appPackage", System.getenv("CT_APP_PKG_NAME"));
        capabilities.setCapability("appWaitPackage", System.getenv("CT_APP_PKG_NAME"));
        capabilities.setCapability("appActivity", System.getenv("CT_APP_LAUNCH_ACTIVITY"));

        driver = new AndroidDriver<>(new URL(getServerUrl()), capabilities);
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
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
