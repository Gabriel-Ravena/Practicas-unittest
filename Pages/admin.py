from selenium.webdriver.support.ui import Select

class admin:

    def __init__(self, Driver):
        self.driver = Driver

    def click_admin(self):
        self.driver.find_element_by_id('menu_admin_viewAdminModule').click()

    def System_users(self):
        username_system = self.driver.find_element_by_id('searchSystemUser_userName')
        username_system.send_keys('robert craig')
        select_rol = Select(self.driver.find_element_by_id('searchSystemUser_userType'))
        select_rol.select_by_visible_text('ESS')
        Employee_name = self.driver.find_element_by_id('searchSystemUser_employeeName_empName')
        Employee_name.send_keys('Robert Craig')
        Status = Select(self.driver.find_element_by_id('searchSystemUser_status'))
        Status.select_by_visible_text('Enabled')


