from selenium.webdriver.support.ui import Select

class admin:

    def __init__(self, Driver):
        self.driver = Driver

    def System_users(self, username_system, Employee_name):
        self.driver.find_element_by_id('searchSystemUser_userName').send_keys(username_system)
        select_rol = Select(self.driver.find_element_by_id('searchSystemUser_userType'))
        select_rol.select_by_visible_text('ESS')
        self.driver.find_element_by_id('searchSystemUser_employeeName_empName').send_keys(Employee_name)
        Status = Select(self.driver.find_element_by_id('searchSystemUser_status'))
        Status.select_by_visible_text('Enabled')

    def click_boton_search(self):
        self.driver.find_element_by_id('searchBtn').click()

#Sub opcion "Job"

    def click_job(self):
        self.driver.find_element_by_id('menu_admin_Job').click()
