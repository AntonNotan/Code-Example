package ru.yandex;

import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import java.util.List;

public class Autotest extends DriverInit {

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

    }

