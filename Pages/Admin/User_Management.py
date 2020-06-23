from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Users:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectUserRole = (By.ID, 'searchSystemUser_userType')

    def txt_username(self, username):
       """
       Campo de texto para introducir un usuario y buscarlo
       :param username: String
       :return:
       """
       return self.driver.find_element_by_id('searchSystemUser_userName').send_keys(username)

    def btn_search(self):
        """
        Hace click en el boton "Search" para realizar la busqueda del usuario
        :return:
        """
        return self.driver.find_element_by_id('searchBtn').click()

    def buscar_usuario_username(self, username):
        self.txt_username(username)
        self.btn_search()

    def drp_user_role(self, user_role):
        """
        selecciona un rol de usuario del dropdown
        :param user_role:
        :return:
        """
        return Select(self.driver.find_element_by_id(*self.selectUserRole)).select_by_visible_text(user_role)







