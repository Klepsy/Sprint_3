from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L

class TestConstructor():
    def test_switch_to_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*L.SAUCES_SWITCHER).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.SAUCES_INGREDIENT))
        assert driver.find_element(*L.SAUCES_INGREDIENT).text == "Соус Spicy-X"

    def test_switch_to_toppings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*L.TOPPINGS_SWITCHER).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.TOPPINGS_INGREDIENT))
        assert driver.find_element(*L.TOPPINGS_INGREDIENT).text == "Мясо бессмертных моллюсков Protostomia"

    def test_switch_to_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*L.SAUCES_SWITCHER).click()
        driver.find_element(*L.BUNS_SWITCHER).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(L.BUNS_INGREDIENT))
        assert driver.find_element(*L.BUNS_INGREDIENT).text == "Флюоресцентная булка R2-D3"
