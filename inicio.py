import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pages.PageLogin import *
from Pages.admin import *
from Pages.Locators import *
import time

class test_logueo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.Page_Login = PageLogin(self.driver)
        self.Page_Admin = admin(self.driver)
        self.locators = Locator(self.driver)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.maximize_window()

    def test_login(self):
        self.Page_Login.login("Admin", "admin123")
        self.locators.click_admin()
        self.Page_Admin.System_users("robert.craig", "Robert Craig")
        self.Page_Admin.click_boton_search()
        time.sleep(2)
        self.Page_Admin.click_job()
        time.sleep(2)
        self.locators.click_pim()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
