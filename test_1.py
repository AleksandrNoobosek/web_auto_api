from testpage import OperationsHelper
import pytest
import logging


def test_step1(browser, send_report):  
    logging.info("Test1 Starting")  
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
    logging.info("Test1 completed")

if __name__  == "__main__":
    pytest.main(['-v'])