from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Users:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectUserRole = (By.ID, 'searchSystemUser_userType')
        self.selectStatus = (By.ID, 'searchSystemUser_status')

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
        Select(self.driver.find_element(*self.selectUserRole)).select_by_visible_text(user_role)

    def select_user_role(self, user_role):
        self.drp_user_role(user_role)
        self.btn_search()

    def txt_employee_name(self, employee):
        """
        Campo de texto para ingresar un employee name
        :param employee:
        :return:
        """
        return self.driver.find_element_by_id('searchSystemUser_employeeName_empName').send_keys(employee)

    def buscar_usuario_employee_name(self, employee):
        self.txt_employee_name(employee)
        self.btn_search()

    def select_status(self, status):
        Select(self.driver.find_element(*self.selectStatus)).select_by_visible_text(status)

    def filtrar_usuarios_por_status(self, status):
        self.select_status(status)




