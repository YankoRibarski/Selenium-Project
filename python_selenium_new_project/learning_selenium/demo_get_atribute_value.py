import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demo_get_atribute_value():
    def demo_get_value(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.booking.com/")
        value = driver.find_element_by_xpath("//a[@class='bui-button bui-button--light bui-traveller-header__product-action']").get_attribute("class")
        print(value)



        time.sleep(2)
findbyid = Demo_get_atribute_value()
findbyid.demo_get_value()
