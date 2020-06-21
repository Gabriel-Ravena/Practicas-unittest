from selenium.webdriver.support.ui import Select


class Users:

    def __init__(self, Driver):
        self.driver = Driver

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

    def drd_user_role(self, user_role):
        user_role = Select(self.driver.find_element_by_id('searchSystemUser_userType')).select_by_visible_text(user_role)


        #select_rol = Select(self.driver.find_element_by_id('searchSystemUser_userType'))
        #select_rol.select_by_visible_text('ESS')
        #self.driver.find_element_by_id('searchSystemUser_employeeName_empName').send_keys(Employee_name)
        #Status = Select(self.driver.find_element_by_id('searchSystemUser_status'))
        #Status.select_by_visible_text('Enabled')


##########Sub opcion "Job" ############
    def click_job(self):
        self.driver.find_element_by_id('menu_admin_Job').click()

    def click_job_titles(self):
        self.driver.find_element_by_id('menu_admin_viewJobTitleList').click()

    def click_Pay_Grades(self):
        self.driver.find_element_by_id('menu_admin_viewPayGrades').click()

    def click_Employment_status(self):
        self.driver.find_element_by_id('menu_admin_employmentStatus').click()

    def click_Job_Categories(self):
        self.driver.find_element_by_id('menu_admin_jobCategory').click()

    def click_Work_Shifts(self):
        self.driver.find_element_by_id('menu_admin_workShift').click()

#ADD Job Title

    def txt_titulo(self, titulo):
        self.driver.find_element_by_id('jobTitle_jobTitle').send_keys(titulo)

    def txt_descripcion(self, descripcion):
        self.driver.find_element_by_id('jobTitle_jobDescription').send_keys(descripcion)

    def txt_nota(self, nota):
        self.driver.find_element_by_id('jobTitle_note').send_keys(nota)

    def agregar_titulo(self, titulo, descripcion, nota):
        self.txt_titulo(titulo)
        self.txt_descripcion(descripcion)
        self.txt_nota(nota)
