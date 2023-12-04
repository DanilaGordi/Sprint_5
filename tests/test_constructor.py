from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import Site
from locators import TestLocators


class TestConstructorSections:

    def test_bread_section(self, driver):
        driver.get(Site.main_site)
        driver.find_element(*TestLocators.SAUCE_BTN).click()
        driver.find_element(*TestLocators.BREAD_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BREAD_SECTION))
        assert driver.find_element(*TestLocators.ACTIVE_BTN).text == 'Булки'

    def test_sauce_section(self, driver):
        driver.get(Site.main_site)
        driver.find_element(*TestLocators.SAUCE_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SAUCE_SECTION))
        assert driver.find_element(*TestLocators.ACTIVE_BTN).text == 'Соусы'

    def test_topping_section(self, driver):
        driver.get(Site.main_site)
        driver.find_element(*TestLocators.TOPPING_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TOPPING_SECTION))
        assert driver.find_element(*TestLocators.ACTIVE_BTN).text == 'Начинки'
