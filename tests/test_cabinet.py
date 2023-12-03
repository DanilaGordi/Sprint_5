from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import EnterSite, Site
from locators import TestLocators


class TestCabinetPage:
    def test_cabinet_registered_profile(self, driver):
        driver.get(Site.login_site)
        driver.find_element(*TestLocators.EMAIL_FIELD_SECOND).send_keys(EnterSite.email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SECOND).send_keys(EnterSite.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BTN))
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Site.profile_site))
        assert driver.current_url == Site.profile_site
