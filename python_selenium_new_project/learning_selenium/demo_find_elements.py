import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demofind_elements_by_id():
    def locate_by_id(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.udemy.com/")
        driver.maximize_window()
        list_1 = driver.find_elements_by_tag_name('input')
        print(len(list_1))
        for i in list_1:
            print(i.text)
        time.sleep(4)
findbyid = Demofind_elements_by_id()
findbyid.locate_by_id()


