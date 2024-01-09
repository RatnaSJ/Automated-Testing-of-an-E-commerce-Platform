from selenium.webdriver.common.by import By

from Pages.AccountSuccessPage import AccountSuccessPage


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    first_name_xpath =  '//input[@id="input-firstname"]'
    last_name_xpath = '//input[@id="input-lastname"]'
    email_field_xpath = '//input[@id="input-email"]'
    telephone_xpath = '//input[@id="input-telephone"]'
    password_xpath = '//input[@id="input-password"]'
    confirm_password_xpath = '//input[@id="input-confirm"]'
    agree_check_box_xpath = '//input[@name="agree"]'
    continue_button_xpath = '//input[@value="Continue"]'
    yes_radio_button_xpath = '//input[@name="newsletter"][@value="1"]'
    duplicate_email_xpath = '//div[@id="account-register"]/div[1]'
    private_policy_warning_xpath = '//div[@class="alert alert-danger alert-dismissible"]'
    first_name_warning_msg_xpath =  '//input[@id="input-firstname"]/following-sibling::div'
    last_name_warning_msg = '//input[@id="input-lastname"]/following-sibling::div'
    email_warning_msg = '//input[@id="input-email"]/following-sibling::div'
    telephone_warning_msg = '//input[@id="input-telephone"]/following-sibling::div'
    password_warning_msg = '//div[text()="Password must be between 4 and 20 characters!"]'
    register_continue_button = '//input[@type="submit"]'

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.first_name_xpath).click()
        self.driver.find_element(By.XPATH, self.first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.last_name_xpath).click()
        self.driver.find_element(By.XPATH, self.last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(last_name)

    def enter_email_field(self, email_address):
        self.driver.find_element(By.XPATH, self.email_field_xpath).click()
        self.driver.find_element(By.XPATH, self.email_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(email_address)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.XPATH, self.telephone_xpath).click()
        self.driver.find_element(By.XPATH, self.telephone_xpath).clear()
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).click()
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).click()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirm_password)

    def click_on_agree_checkbox(self):
        self.driver.find_element(By.XPATH, self.agree_check_box_xpath).click()

    def click_on_yes_redio_button(self):
        self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def click_on_register_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def register_an_account(self,first_name,last_name,email_address,telephone,password,confirm_password, yes_or_no, privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_field(email_address)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if yes_or_no.__eq__('yes'):
            self.click_on_yes_redio_button()

        if privacy_policy.__eq__('select'):
            self.click_on_agree_checkbox()

        self.click_on_register_continue_button()
        return AccountSuccessPage(self.driver)

    def retrieve_mail_already_registered_warning(self):
        return self.driver.find_element(By.XPATH, self.duplicate_email_xpath).text

    def retrieve_private_policy_warning_msg(self):
        return self.driver.find_element(By.XPATH, self.private_policy_warning_xpath).text

    def retrieve_first_name_warning_msg(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_msg_xpath).text

    def retrieve_last_name_warning_msg(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_msg).text

    def retrieve_email_warning_msg(self):
        return self.driver.find_element(By.XPATH, self.email_warning_msg).text

    def retrieve_telephone_warning_msg(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_msg).text

    def retrieve_password_warning_msg(self):
        return self.driver.find_element(By.XPATH, self.password_warning_msg).text

    def verify_all_warnings(self, expected_privacy_policy_warning_msg,expected_first_name_warning_msg,expected_last_name_warning_msg,expected_email_warning_msg,expected_telephone_warning_msg,expected_password_warning_msg):
        actual_privacy_policy_warning_msg = self.retrieve_private_policy_warning_msg()
        actual_first_name_warning_msg = self.retrieve_first_name_warning_msg()
        actual_last_name_warning_msg = self.retrieve_last_name_warning_msg()
        actual_email_warning_msg = self.retrieve_email_warning_msg()
        actual_telephone_warning_msg = self.retrieve_telephone_warning_msg()
        actual_password_warning_msg = self.retrieve_password_warning_msg()

        status = False

        if expected_privacy_policy_warning_msg.__contains__(actual_privacy_policy_warning_msg):
            if expected_first_name_warning_msg.__eq__(actual_first_name_warning_msg):
                if expected_last_name_warning_msg.__eq__(actual_last_name_warning_msg):
                    if expected_email_warning_msg.__eq__(actual_email_warning_msg):
                        if expected_telephone_warning_msg.__eq__(actual_telephone_warning_msg):
                            if expected_password_warning_msg.__eq__(actual_password_warning_msg):
                                status = True
        return status



