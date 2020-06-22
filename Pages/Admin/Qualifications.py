class skills:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_name(self, name):
        self.driver.find_element_by_id('skill_name').send_keys(name)

    def txt_description(self, description):
        self.driver.find_element_by_id('skill_description').send_keys(description)

class education:

    def txt_level(self, level):
        self.driver.find_element_by_id('education_name')

class licenses:

    def txt_license_name(self, license):
        self.driver.find_element_by_id('license_name').send_keys(license)

class languages:

    def txt_languages(self, language):
        self.driver.find_element_by_id('language_name').send_keys(language)

class membership:

    def txt_membership(self, member):
        self.driver.find_element_by_id('membership_name').send_keys(member)