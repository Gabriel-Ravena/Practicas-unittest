from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class GeneralInformation:

    def __init__(self, Driver):
        self.driver = Driver
        self.selectCountry = (By.ID, 'organization_country')
        self.selectCountryLocation = (By.ID, 'searchLocation_city')

    def boton_edit(self):
        self.driver.find_element_by_id('btnSaveGenInfo').click()

    def txt_organization_name(self, organization):
        self.driver.find_element_by_id('organization_name').send_keys(organization)

    def txt_tax_id(self, tax):
        self.driver.find_element_by_id('organization_taxId').send_keys(tax)

    def txt_registration_number(self, number):
        self.driver.find_element_by_id('organization_registraionNumber').send_keys(number)

    def txt_phone(self):
        self.driver.find_element_by_id('organization_phone').send_keys()

    def txt_fax(self, fax):
        self.driver.find_element_by_id('organization_fax').send_keys(fax)

    def txt_email(self):
        self.driver.find_element_by_id('organization_email').send_keys()

    def txt_address_street(self, address):
        self.driver.find_element_by_id('organization_street1').send_keys(address)

    def txt_city(self, city):
        self.driver.find_element_by_id('organization_city').send_keys(city)

    def txt_province(self, province):
        self.driver.find_element_by_id('organization_province').send_keys(province)

    def select_country(self, country):
        Select(self.driver.find_element_by_id(*self.selectCountry)).select_by_visible_text(country)

    def txt_note(self, note):
        self.driver.find_element_by_id('organization_note').send_keys(note)

    def btn_save(self):
        self.driver.find_element_by_id('btnSaveGenInfo').click()

class Locations:

    def txt_location_name(self, name):
        self.driver.find_element_by_id('searchLocation_name').send_keys(name)

    def txt_city(self, city):
        self.driver.find_element_by_id('searchLocation_city').send_keys(city)

    def select_country(self, country):
        Select(self.driver.find_element_by_id(*self.selectCountryLocation)).select_by_visible_text(country)