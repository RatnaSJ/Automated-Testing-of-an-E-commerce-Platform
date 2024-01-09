from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.SearchPage import SearchPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = 'search'
    search_button_xpath = '//button[@class="btn btn-default btn-lg"]'
    my_account_drop_menu_xpath = '//span[text()="My Account"]'
    login_option_link_text = 'Login'
    register_option_link_text = 'Register'

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.click_on_login_option()

    def click_on_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.click_on_register_option()

    ##this method is call to enter_product_into_search_box_field() and click_on_search_button() internally
    def search_for_a_product(self,product_name):
        self.enter_product_into_search_box_field(product_name)
        self.click_on_search_button()
        return SearchPage(self.driver)



##### NEXT LEVEL CODE ##
    #
    # search_box_field_name = "search"
    # search_button_xpath = "//button[contains(@class,'btn-default')]"
    # my_account_drop_menu_xpath = '//span[text()="My Account"]'
    # login_option_xpath = '//a[text()="Login"]'
    # register_option_xpath = '//a[text()="Register"]'
    #
    # def enter_product_into_search_box_field_1(self, product_name):
    #     self.type_into_element(product_name,"search_box_field_name", self.search_box_field_name)
    #
    # def click_on_search_button_1(self):
    #     self.element_click("search_button_xpath",self.search_button_xpath)
    #     return SearchPage(self.driver)
    #
    # def click_on_my_account_drop_menu_1(self):
    #     self.element_click("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath)
    #
    # def select_login_option_1(self):
    #     self.element_click("login_option_xpath", self.login_option_xpath)
    #     return LoginPage(self.driver)
    #
    # def navigate_to_login_page2(self):
    #     self.click_on_my_account_drop_menu()
    #     return self.select_login_option()
    #
    # def click_on_register_option(self):
    #     self.element_click("register_option_xpath",self.register_option_xpath)
    #
    # def navigate_to_register_page(self):
    #     self.click_on_my_account_drop_menu()
    #     return self.click_on_register_option()
    #
    # def search_for_a_product(self,product_name):
    #     self.enter_product_into_search_box_field(product_name)
    #     return self.click_on_search_button()
