class Locator:

    def __init__(self, Driver):
        self.driver = Driver

    def click_admin(self):
        self.driver.find_element_by_id('menu_admin_viewAdminModule').click()

    def click_pim(self):
        self.driver.find_element_by_id('menu_pim_viewPimModule').click()

