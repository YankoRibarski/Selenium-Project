import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demo_element_state():
    def demo_enable_desable(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        demo_state = driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state)
        driver.find_element_by_xpath("//input[@id='user_name']").send_keys("username")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='user_pass']").send_keys("passwloed358")
        time.sleep(2)
        demo_state1 = driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state1)

demostate = Demo_element_state()
demostate.demo_enable_desable()
