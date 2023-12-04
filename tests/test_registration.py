from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import EnterSite, Site
from locators import TestLocators


class TestRegistration:
    def test_registration_correct(self, driver):
        driver.get(Site.registration_site)
        driver.find_element(*TestLocators.NANE_FIELD_FIRST).send_keys(EnterSite.name)
        driver.find_element(*TestLocators.EMAIL_FIELD_FIRST).send_keys(EnterSite.random_email())
        driver.find_element(*TestLocators.PASSWORD_FIELD_FIRST).send_keys(EnterSite.random_password())
        driver.find_element(*TestLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains("site/login"))
        assert driver.current_url == Site.login_site

    def test_registration_short_pass(self, driver):
        driver.get(Site.registration_site)
        driver.find_element(*TestLocators.NANE_FIELD_FIRST).send_keys(EnterSite.name)
        driver.find_element(*TestLocators.EMAIL_FIELD_FIRST).send_keys(EnterSite.email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_FIRST).send_keys(EnterSite.invalid_password)
        driver.find_element(*TestLocators.REGISTRATION_BTN).click()
        assert driver.find_element(*TestLocators.PASSWORD_ERROR).text == 'Некорректный пароль'