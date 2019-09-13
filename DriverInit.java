package ru.yandex;

import org.junit.After;
import org.junit.Before;
import org.openqa.selenium.chrome.ChromeDriver;

public class DriverInit {
    public ChromeDriver driver;
    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "/Program Files/chromedriver.exe");
        driver = new ChromeDriver();
    }
    @After
    public void close() {
        driver.quit();
    }
}
