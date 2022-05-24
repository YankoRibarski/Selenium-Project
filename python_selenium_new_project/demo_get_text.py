import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demo_get_text():
    def demo_get_text(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.bbc.com/news")
        driver.maximize_window()
        text = driver.find_element_by_xpath("//p[contains(text(),'A Ukrainian commander at the Azovstal plant says h')]").text
        text1 = driver.find_element_by_xpath("//li[@class='gs-o-list-ui__item--flush gel-long-primer gs-u-display-block gs-u-float-left nw-c-nav__wide-menuitem-container']//span[contains(text(),'Business')]").text
        print(text)
        print(text1)
        time.sleep(4)
findbyid = Demo_get_text()
findbyid.demo_get_text()
