import unittest
from selenium import webdriver
from Pages.PageLogin import *
from Pages.Admin.User_Management import *
from Pages.Common import *
import time


class TestLogueo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.Page_Login = PageLogin(self.driver)
        self.Page_Admin = Users(self.driver)
        self.locators = Locator(self.driver)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.maximize_window()

    def test_login(self):
        self.Page_Login.login("Admin", "admin123")
        self.assertEqual(self.driver.title, "OrangeHRM", "No se encontro el titulo")
        self.assertEqual(self.driver.current_url, "https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        titulo = self.driver.find_element_by_xpath('//div[@class="head"]//h1').text
        self.assertEqual(titulo, "Dashboard")

    def test_buscar_usuario_by_username(self):
        self.Page_Login.login("Admin", "admin123")
        self.locators.click_admin()
        self.Page_Admin.buscar_usuario_username("robert.craig")



    #def tearDown(self):
        #self.driver.quit()

if __name__ == '__main__':
    unittest.main()
