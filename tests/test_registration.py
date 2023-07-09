from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from faker import Faker

faker = Faker()
class TestRegistration():
    def test_registr_user(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*L.NAME_INPUT).send_keys(faker.name())
        driver.find_element(*L.MAIL_INPUT).send_keys(faker.email())
        driver.find_element(*L.PASSWORD_INPUT).send_keys("qwerty12345")
        assert driver.find_element(*L.MAIL_INPUT).get_attribute("value") != None
        driver.find_element(*L.REGISTER_BUTTON).click()



    def test_registr_password_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*L.NAME_INPUT).send_keys(faker.name())
        driver.find_element(*L.MAIL_INPUT).send_keys(faker.email())
        driver.find_element(*L.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*L.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.REGISTER_PASSWORD_ERROR))
        assert driver.find_element(*L.REGISTER_PASSWORD_ERROR).text == "Некорректный пароль"