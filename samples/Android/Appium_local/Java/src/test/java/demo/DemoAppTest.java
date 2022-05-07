package demo;

import com.tencent.wetest.WTBaseTest;
import io.appium.java_client.MobileElement;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class DemoAppTest extends WTBaseTest {

    // your test cases start here
    //this function is just a sample test case for com.tencent.wetestdemo package
    @Test
    public void test_login_success() throws InterruptedException {
        System.out.println("test_login_success");
        MobileElement userNameText = driver.findElementById("com.tencent.wetestdemo:id/username");
        userNameText.sendKeys("wetestname");
        MobileElement pwdBtn = driver.findElementById("com.tencent.wetestdemo:id/password");
        pwdBtn.sendKeys("wetestpwd");
        Thread.sleep(10000);
        MobileElement loginBtn = driver.findElementById("com.tencent.wetestdemo:id/login");
        loginBtn.click();
    }

    // your test cases end here

}
