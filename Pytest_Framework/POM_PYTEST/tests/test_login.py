import pytest
from actions.loginAction import LoginActions
from utilities import excel_reader


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.parametrize("username,password,case",excel_reader.get_data(r"D:\Python_Selenium\Pytest_Framework\POM_PYTEST\utilities\Book1.xlsx", "Sheet1"),)
class TestLogin:
    def test_login(self, username, password, case):
        login = LoginActions(self.driver)
        login.click_myacc()
        login.click_login_link()
        login.enter_email(username)
        login.enter_password(str(password))
        login.click_login()

        if case.lower() == "valid":
            assert login.check_login()

        elif case.lower() == "invalid":
            assert login.invalid_login()
