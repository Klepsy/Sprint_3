from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L

def test_login_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*L.MAIN_LOGIN_BUTTON).click()
    driver.find_element(*L.MAIL_INPUT).send_keys("kunst_edvard1996@mail.ru")
    driver.find_element(*L.PASSWORD_INPUT).send_keys("qwerty123")
    driver.find_element(*L.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.ORDER_BUTTON))
    assert driver.find_element(*L.ORDER_BUTTON).text == "Оформить заказ"

def test_login_profile_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*L.PROFILE_BUTTON).click()
    driver.find_element(*L.MAIL_INPUT).send_keys("kunst_edvard1996@mail.ru")
    driver.find_element(*L.PASSWORD_INPUT).send_keys("qwerty123")
    driver.find_element(*L.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.ORDER_BUTTON))
    assert driver.find_element(*L.ORDER_BUTTON).text == "Оформить заказ"

def test_login_registr(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.AUTH_BUTTON))
    driver.find_element(*L.AUTH_BUTTON).click()
    driver.find_element(*L.MAIL_INPUT).send_keys("kunst_edvard1996@mail.ru")
    driver.find_element(*L.PASSWORD_INPUT).send_keys("qwerty123")
    driver.find_element(*L.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.ORDER_BUTTON))
    assert driver.find_element(*L.ORDER_BUTTON).text == "Оформить заказ"

def test_login_restore(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.AUTH_BUTTON))
    driver.find_element(*L.AUTH_BUTTON).click()
    driver.find_element(*L.MAIL_INPUT).send_keys("kunst_edvard1996@mail.ru")
    driver.find_element(*L.PASSWORD_INPUT).send_keys("qwerty123")
    driver.find_element(*L.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.ORDER_BUTTON))
    assert driver.find_element(*L.ORDER_BUTTON).text == "Оформить заказ"


