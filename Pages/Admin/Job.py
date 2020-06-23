from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class jobTitles:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectFromHours = (By.ID, 'workShift_workHours_from')
        self.selectToHours = (By.ID, 'workShift_workHours_to')
        self.selectEmployees = (By.ID, 'workShift_availableEmp')

    def click_job(self):
        """
        click en job dentro de admin
        :return:
        """
        self.driver.find_element_by_id('menu_admin_Job').click()

    def click_job_titles(self):
        """
        click en job titles dentro de la opcion job
        :return:
        """
        self.driver.find_element_by_id('menu_admin_viewJobTitleList').click()

    def click_Pay_Grades(self):
        """
        click en pay grades dentro de la opcion job
        :return:
        """
        self.driver.find_element_by_id('menu_admin_viewPayGrades').click()

    def click_Employment_status(self):
        """
        click en employment status dentro de la opcion job
        :return:
        """
        self.driver.find_element_by_id('menu_admin_employmentStatus').click()

    def click_Job_Categories(self):
        """
        click en job categories dentro de la opcion job
        :return:
        """
        self.driver.find_element_by_id('menu_admin_jobCategory').click()

    def click_Work_Shifts(self):
        """
        click en work shifts dentro de la opcion job
        :return:
        """
        self.driver.find_element_by_id('menu_admin_workShift').click()

    def txt_titulo(self, titulo):
        """
        campo de texto para poner un titulo
        :param titulo:
        :return:
        """
        return self.driver.find_element_by_id('jobTitle_jobTitle').send_keys(titulo)

    def txt_descripcion(self, descripcion):
        """
        campo de texto para agregar una descripcion
        :param descripcion:
        :return:
        """
        return self.driver.find_element_by_id('jobTitle_jobDescription').send_keys(descripcion)

    def txt_nota(self, nota):
        """
        campo de texto para agregar una nota
        :param nota:
        :return:
        """
        return self.driver.find_element_by_id('jobTitle_note').send_keys(nota)

    def add_job_title(self, titulo, descripcion, nota):
        """
        funcion que ingresa titulo, descripcion y nota en el menu add job titles
        :param titulo:
        :param descripcion:
        :param nota:
        :return:
        """
        self.txt_titulo(titulo)
        self.txt_descripcion(descripcion)
        self.txt_nota(nota)


class payGrades:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_pay_grades(self, pay):
        """
        campo de texto para agregar el pay grades
        :param paygrades:
        :return:
        """
        self.driver.find_element_by_id('payGrade_name').send_keys(pay)

    def agregar_pay_grades(self, pay):
        self.txt_pay_grades(pay)

class employmentStatus:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_employment_status(self, employment):
        self.driver.find_element_by_id('empStatus_name').send_keys(employment)

    def agregar_employment_status(self, employment):
        self.txt_employment_status(employment)


class jobCategories:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_job_categories(self, categoria):
        self.driver.find_element_by_id('jobCategory_name').send_keys(categoria)

    def agregar_categoria(self, categoria):
        self.txt_job_categories(categoria)

class worksShifts:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectFromHours = (By.ID, 'workShift_workHours_from')
        self.selectToHours = (By.ID, 'workShift_workHours_to')
        self.selectEmployees = (By.ID, 'workShift_availableEmp')

    def txt_shifts_name(self):
        self.driver.find_element_by_id('workShift_name').send_keys()

    def drp_from_work_hours(self, fromHours):
        Select(self.driver.find_element_by_id(*self.selectFromHours)).select_by_visible_text(fromHours)

    def drp_to_works_hours(self, ToHours):
        Select(self.driver.find_element_by_id(*self.selectToHours)).select_by_visible_text(ToHours)

    def drp_available_employees(self, employees):
        Select(self.driver.find_element_by_id(*self.selectEmployees)).select_by_visible_text(employees)

    def boton_assigne_employee(self):
        self.driver.find_element_by_id('btnAssignEmployee').click()

    def boton_remove(self):
        self.driver.find_element_by_id('btnRemoveEmployee').click()























