class Menu:

    def click_boton_add(self):
        """
        Click en el boton ADD para que aparezca el formulario que nos permita agregar un usuario nuevo
        :return:
        """
        self.driver.find_element_by_id('btnAdd').click()

    def click_boton_delete(self):
        """
        Click en el boton DELETE para eliminar un usuario de la tabla
        :return:
        """
        self.driver.find_element_by_id('btnDelete').click()

    def click_boton_Save(self):
        """
        Click en el boton SAVE  para guardar los datos agregados en el formulario
        :return:
        """
        self.driver.find_element_by_id('btnSave').click()

    def click_boton_cancel(self):
        """
        Click en el boton CANCEL para cancelar el envío de datos del formulario para agregar nuevo usuario
        :return:
        """
        self.driver.find_element_by_id('btnCancel').click()
