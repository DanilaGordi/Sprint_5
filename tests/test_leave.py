from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import EnterSite, Site
from locators import TestLocators


class TestLogout:
    def test_leave(self, driver):
        driver.get(Site.login_site)
        driver.find_element(*TestLocators.EMAIL_FIELD_SECOND).send_keys(EnterSite.email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SECOND).send_keys(EnterSite.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BTN))
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.LEAVE_BTN))
        driver.find_element(*TestLocators.LEAVE_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Site.login_site))
        assert driver.current_url == Site.login_site
