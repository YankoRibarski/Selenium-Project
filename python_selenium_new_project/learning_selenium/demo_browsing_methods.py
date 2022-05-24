import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class demo_selenium_learning():
    def demo_browser_methods(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://training.rcvacademy.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element_by_link_text("ALL COURSES").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.minimize_window()

        time.sleep(4)
        driver.quit()

demobrowser = demo_selenium_learning()
demobrowser.demo_browser_methods()