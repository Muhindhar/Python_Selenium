import pytest

from actions.OrderAction import OrderAction

@pytest.mark.usefixtures("setup_teardown")
class Test_Order():
    def test_order(self):
        ord= OrderAction(self.driver)
        ord.clk_myacc()
        ord.clk_login()
        ord.clck_mail()
        ord.clk_pass()
        ord.clk_loginbtn()
        ord.clk_searchbar()
        ord.clk_search()
        ord.clk_laptop()
        ord.clk_addtocart()
        ord.clk_shopcart()
        ord.clk_checkout()
        ord.clk_contbtn()
        ord.check_order()