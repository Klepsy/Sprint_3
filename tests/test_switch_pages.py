from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L

class TestSwitchPages():
    def test_switch_profile_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*L.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.LOGIN_BUTTON))
        assert driver.find_element(*L.LOGIN_BUTTON).text == "Войти"

    def test_switch_profile_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*L.PROFILE_BUTTON).click()
        driver.find_element(*L.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.CREATE_BURGER))
        assert driver.find_element(*L.CREATE_BURGER).text == "Соберите бургер"

    def test_switch_to_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*L.LOGO_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.CREATE_BURGER))
        assert driver.find_element(*L.CREATE_BURGER).text == "Соберите бургер"

    def test_logout_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*L.MAIL_INPUT).send_keys("kunst_edvard1996@mail.ru")
        driver.find_element(*L.PASSWORD_INPUT).send_keys("qwerty123")
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.PROFILE_BUTTON))
        driver.find_element(*L.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.LOGOUT_BUTTON))
        driver.find_element(*L.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.LOGIN_BUTTON))
        assert driver.find_element(*L.LOGIN_BUTTON).text == "Войти"


