package demo;

import com.tencent.wetest.WTBaseTest;
import io.appium.java_client.MobileElement;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class DemoAppTest extends WTBaseTest {

    @Test
    public void test_login_failed() throws InterruptedException {
        System.out.println("test_login_failed");
        MobileElement loginBtn = driver.findElementById("com.tencent.wetestdemo:id/login");
        loginBtn.click();
        MobileElement okBtn = driver.findElementById("android:id/button3");
        okBtn.click();
        Thread.sleep(10000);
    }

    @Test
    public void test_login_success() throws InterruptedException {
        System.out.println("test_login_success");
        MobileElement userNameText = driver.findElementById("com.tencent.wetestdemo:id/username");
        userNameText.sendKeys("wetestname");
        MobileElement pwdBtn = driver.findElementById("com.tencent.wetestdemo:id/password");
        pwdBtn.sendKeys("wetestpwd");
        MobileElement loginBtn = driver.findElementById("com.tencent.wetestdemo:id/login");
        loginBtn.click();
        Thread.sleep(10000);
    }

    @Test
    public void test_select_item() throws InterruptedException {
        MobileElement item1 = driver.findElementById("android:id/text1");
        item1.click();
        MobileElement btn = driver.findElementById("com.tencent.wetestdemo:id/submitbtn");
        btn.click();
        Thread.sleep(10000);
    }

    @Test
    public void test_failed(){
        System.out.println("test failed .");
        assert false;
    }

}
