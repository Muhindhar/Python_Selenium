import pytest
from actions.SearchAction import search

@pytest.mark.usefixtures("setup_teardown")
class TestSearch():
    def test_search_page(self):
        srch = search(self.driver)
        srch.click_bar()
        srch.clic_search()
        srch.check_search()
        
        