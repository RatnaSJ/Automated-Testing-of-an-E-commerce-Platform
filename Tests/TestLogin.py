from datetime import datetime
import pytest
from Pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_browser")
class TestLogin:
    def test_login_with_valid_credentials(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        account_page = login_page.login_to_application('cooum@gmail.com', 'shya@12345')
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_invalid_email_and_valid_password(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(), 'shya@12345')
        expected_warning_msg = 'Warning: No match for E-Mail Address and/or Password.'
        assert login_page.retrieve_warning_message_text().__eq__(expected_warning_msg)

    def test_login_with_valid_email_invalid_password(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        login_page.login_to_application('cooum@gmail.com', '2345')

        expected_warning_msg = 'Warning: No match for E-Mail Address and/or Password.'
        assert login_page.retrieve_warning_message_text().__contains__(expected_warning_msg)

    def test_login_without_entering_credentials(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        login_page.login_to_application('', '')

        expected_warning_msg = 'Warning: No match for E-Mail Address and/or Password.'
        assert login_page.retrieve_warning_message_text().__contains__(expected_warning_msg)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "ratna"+time_stamp+"@gmail.com"





