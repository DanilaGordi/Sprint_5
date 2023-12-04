from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import EnterSite, Site
from locators import TestLocators


class TestLogin:
    def test_enter_main_site(self, driver):
        driver.get(Site.main_site)
        driver.find_element(*TestLocators.LOGIN_IN_ACC_BTN).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_SECOND).send_keys(EnterSite.email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SECOND).send_keys(EnterSite.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Site.main_site))
        assert driver.current_url == Site.main_site

    def test_enter_cabinet(self, driver):
        driver.get(Site.main_site)
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_SECOND).send_keys(EnterSite.email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SECOND).send_keys(EnterSite.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Site.main_site))
        assert driver.current_url == Site.main_site

    def test_enter_registration(self, driver):
        driver.get(Site.registration_site)
        driver.find_element(*TestLocators.LOGIN_LINK_BTN).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_SECOND).send_keys(EnterSite.email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SECOND).send_keys(EnterSite.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Site.main_site))
        assert driver.current_url == Site.main_site

    def test_enter_forgot_password(self, driver):
        driver.get(Site.forgot_pass_site)
        driver.find_element(*TestLocators.LOGIN_LINK_BTN).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_SECOND).send_keys(EnterSite.email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SECOND).send_keys(EnterSite.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Site.main_site))
        assert driver.current_url == Site.main_site
