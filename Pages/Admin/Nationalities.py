class nationalities:

    def __init__(self, Driver):
        self.driver = Driver

    def txt_nacionalities(self, nation):
        self.driver.find_element_by_id('nationality_name').send_keys(nation)