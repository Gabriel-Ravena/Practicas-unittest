class skills:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_name(self, name):
        """
        campo de texto para ingresar un nombre
        :param name:
        :return:
        """
        return self.driver.find_element_by_id('skill_name').send_keys(name)

    def txt_description(self, description):
        """
        campo de texto para ingresar una descripcion
        :param description:
        :return:
        """
        return self.driver.find_element_by_id('skill_description').send_keys(description)

class education:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_level(self, level):
        """
        campo de texto para ingresar el nivel
        :param level:
        :return:
        """
        return self.driver.find_element_by_id('education_name').send_keys(level)

class licenses:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_license_name(self, license):
        """
        campo de texto para ingresar una licencia
        :param license:
        :return:
        """
        return self.driver.find_element_by_id('license_name').send_keys(license)

class languages:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_languages(self, language):
        """
        campo de texto para ingresar un lenguaje
        :param language:
        :return:
        """
        return self.driver.find_element_by_id('language_name').send_keys(language)

class membership:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_membership(self, member):
        """
        campo de texto para ingresar un member
        :param member:
        :return:
        """
        return self.driver.find_element_by_id('membership_name').send_keys(member)