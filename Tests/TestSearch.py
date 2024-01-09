import pytest
from Pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_browser")
class TestSearch:

    def test_search_for_a_valid(self):
        homepage = HomePage(self.driver)
        search_page = homepage.search_for_a_product('HP')
        assert search_page.display_status_of_valid_product()

    def test_search_for_an_invalid(self):
        homepage = HomePage(self.driver)
        search_page = homepage.search_for_a_product('Honda')
        expected_text = 'There is no product that matches the search criteria.'
        assert search_page.retrieve_no_product_message().__eq__(expected_text)






