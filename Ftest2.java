package ru.yandex;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.List;

public class Ftest2 {
    public ChromeDriver driver;

    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "/Program Files/chromedriver.exe");
         driver = new ChromeDriver();
    }

    @Test
    public void firsttest() {
            driver.get("https://www.yandex.ru/");
            List<WebElement> a=driver.findElements(By.cssSelector("a"));
            for(int i=0;i<a.size();i++) {
                String b=a.get(i).getAttribute("href");
                System.out.println(b);
                if (b !=null ) {
                    a.get(i).click();
                    driver.navigate().back();
                }
                a = driver.findElements(By.cssSelector("a"));
            }
        }

    @After
    public void close() {
        driver.quit();
    }
    }

