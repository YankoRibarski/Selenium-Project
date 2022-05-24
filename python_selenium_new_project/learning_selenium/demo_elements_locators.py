import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demofind_elements_by_id():
    def locate_by_id(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://passport.abv.bg/app/profiles/lostpass")
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys("user1234")
        time.sleep(10)
findbyid = Demofind_elements_by_id()
findbyid.locate_by_id()


