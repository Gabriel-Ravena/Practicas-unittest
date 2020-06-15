class PageLogin:

    def __init__(self, Driver):
        self.driver = Driver

    def login(self, username, password):
        self.driver.find_element_by_id('txtUsername').send_keys(username)
        self.driver.find_element_by_id('txtPassword').send_keys(password)
        self.driver.find_element_by_id('btnLogin').click()



