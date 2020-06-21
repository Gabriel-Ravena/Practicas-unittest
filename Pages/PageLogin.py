class PageLogin:

    def __init__(self, Driver):
        self.driver = Driver

    def username(self, username):
        """
        Campo de texto para ingresar el usuario con el que vamos a ingresar al sitio
        :param username:
        :return:
        """
        return self.driver.find_element_by_id('txtUsername').send_keys(username)

    def password(self, password):
        """
        Campo de texto para ingresar la contrasenia del usuario con el que vamos a ingresar al sitio
        :param password:
        :return:
        """
        return self.driver.find_element_by_id('txtPassword').send_keys(password)

    def boton_login(self):
        """
        Hace click en el boton LOGIN para ingresar al sitio
        :return:
        """
        self.driver.find_element_by_id('btnLogin').click()

    def login(self, username,  password):
        """
        Funcion que ingresa usuario, contrasenia, y hace click en LOGIN para ingresar al sitio
        :param username:
        :param password:
        :return:
        """
        self.username(username)
        self.password(password)
        self.boton_login()






