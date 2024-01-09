from datetime import datetime
import pytest

from Pages.HomePage import HomePage

### SECOND LEVEL###


@pytest.mark.usefixtures("setup_browser")
class TestRegister:

    def test_register_with_mandatory_field(self):
        homepage = HomePage(self.driver)
        register_page = homepage.navigate_to_register_page()
        account_success_page = register_page.register_an_account('shyam','shine',self.generate_email_with_time_stamp(),'8889995546','abcd123456','abcd123456', 'no','select')
        expected_heading_text = 'Your Account Has Been Created!'
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_all_field(self):
        homepage = HomePage(self.driver)
        register_page = homepage.navigate_to_register_page()
        account_success_page = register_page.register_an_account('shyam','shine',self.generate_email_with_time_stamp(),'8889995546','abcd123456','abcd123456','yes','select')
        expected_heading_text = 'Your Account Has Been Created!'
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        homepage = HomePage(self.driver)
        register_page = homepage.navigate_to_register_page()
        register_page.register_an_account('shyam','shine','cooum@gmail.com','8889995546','abcd123456','abcd123456','yes','select')

        expected_warning_msg = 'Warning: E-Mail Address is already registered!'
        assert register_page.retrieve_mail_already_registered_warning().__eq__(expected_warning_msg)

    def test_register_without_entering_any_fields(self):
        homepage = HomePage(self.driver)
        register_page = homepage.navigate_to_register_page()
        register_page.register_an_account('','','','','','','no','')
        assert register_page.verify_all_warnings('Warning: You must agree to the Privacy Policy!','First Name must be between 1 and 32 characters!','Last Name must be between 1 and 32 characters!','E-Mail Address does not appear to be valid!', 'Telephone must be between 3 and 32 characters!','Password must be between 4 and 20 characters!')

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "ratna"+time_stamp+"@gmail.com"





















