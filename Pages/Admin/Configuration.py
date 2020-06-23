from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class EmailConfiguration:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectMethod = (By.ID, 'emailConfigurationForm_cmbMailSendingMethod')


    def txt_mail(self, email):
        self.driver.find_element_by_id('emailConfigurationForm_txtMailAddress').send_keys(email)

    def drp_method(self, metodo):
        Select(self.driver.find_element_by_id(*self.selectMethod)).select_by_visible_text(metodo)


class Localization:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectLocalization = (By.ID, 'localization_dafault_language')
        self.selectFormat = (By.ID, 'localization_default_date_format')

    def drp_localization_language(self, localization):
        Select(self.driver.find_element_by_id(*self.selectLocalization)).select_by_visible_text(localization)

    def drp_date_format(self, format):
        Select(self.driver.find_element_by_id(*self.selectFormat)).select_by_visible_text(format)

