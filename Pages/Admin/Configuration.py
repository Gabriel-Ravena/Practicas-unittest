from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class EmailConfiguration:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectMethod = (By.ID, 'emailConfigurationForm_cmbMailSendingMethod')


    def txt_mail(self, email):
        """
        campo de texzto para ingresar un email
        :param email:
        :return:
        """
        return self.driver.find_element_by_id('emailConfigurationForm_txtMailAddress').send_keys(email)

    def drp_method(self, metodo):
        """
        dropdown para seleccionar un metodo
        :param metodo:
        :return:
        """
        return Select(self.driver.find_element_by_id(*self.selectMethod)).select_by_visible_text(metodo)


class Localization:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectLocalization = (By.ID, 'localization_dafault_language')
        self.selectFormat = (By.ID, 'localization_default_date_format')

    def drp_localization_language(self, localization):
        """
        dropdown para seleccionar una localizacion y un lenguaje
        :param localization:
        :return:
        """
        return Select(self.driver.find_element_by_id(*self.selectLocalization)).select_by_visible_text(localization)

    def drp_date_format(self, format):
        """
        dropdown para seleccionar el formato de la fecha
        :param format:
        :return:
        """
        return Select(self.driver.find_element_by_id(*self.selectFormat)).select_by_visible_text(format)

class socialMediaAuthentication:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectType = (By.ID, 'openIdProvider_type')

    def drp_type(self, type):
        """
        dropdown para seleccionar un type
        :param type:
        :return:
        """
        return Select(self.driver.find_element_by_id(*self.selectType)).select_by_visible_text(type)

    def txt_name(self, name):
        """
        campo de texto para ingresar un name
        :param name:
        :return:
        """
        return self.driver.find_element_by_id('openIdProvider_name').send_keys(name)

    def txt_url(self, url):
        """
        campo de texto para ingresar una url
        :param url:
        :return:
        """
        return self.driver.find_element_by_id('openIdProvider_url').send_keys(url)



