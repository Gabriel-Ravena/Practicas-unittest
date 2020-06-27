class Locator:
    """
    En esta clase se encuentran todas acciones del menú
    """
    def __init__(self, Driver):
        self.driver = Driver

#Menú
    def click_admin(self):
        """
        click en la opcion admin del menu principal
        :return:
        """
        self.driver.find_element_by_id('menu_admin_viewAdminModule').click()

    def click_pim(self):
        """
        click en la opcion pim del menu principal
        :return:
        """
        self.driver.find_element_by_id('menu_pim_viewPimModule').click()

#Botones

    def click_add(self):
        self.driver.find_element_by_id('btnAdd').click()


