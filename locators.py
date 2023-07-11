from selenium.webdriver.common.by import By

class Locators:
    NAME_INPUT = [By.XPATH,'.//label[text()="Имя"]/following-sibling::input'] #Поле Имя при регистрации
    MAIL_INPUT = [By.XPATH,'.//label[text()="Email"]/following-sibling::input'] #Поле Email при регистрации
    PASSWORD_INPUT = [By.XPATH,'.//label[text()="Пароль"]/following-sibling::input'] #Поле Пароль при регистрации
    REGISTER_BUTTON = [By.XPATH,'.//button[text()="Зарегистрироваться"]'] #Кнопка Зарегистрироваться на странице Регистрация
    REGISTER_PASSWORD_ERROR = [By.XPATH,'.//p[text()="Некорректный пароль"]'] #Ошибка пароля при регистрации
    LOGIN_BUTTON = [By.XPATH,'.//button[text()="Войти"]'] #Кнопка Войти
    MAIN_LOGIN_BUTTON = [By.XPATH,'.//button[text()="Войти в аккаунт"]'] #Кнопка Войти в аккаунт на главной странице
    ORDER_BUTTON = [By.XPATH,'.//button[text()="Оформить заказ"]'] #Кнопка Оформить заказ
    PROFILE_BUTTON = [By.XPATH,'.//p[text()="Личный Кабинет"]'] #Кнопка Личный кабинет в хэдере
    AUTH_BUTTON = [By.XPATH,'.//a[@href="/login"]'] #Кнопка Войти на странице Регистрации
    CONSTRUCTOR_BUTTON = [By.XPATH,'.//a[@href="/"]'] #Кнопка Конструктор в хэдере
    CREATE_BURGER = [By.XPATH,'.//h1[text()="Соберите бургер"]'] #Текст Соберите бургер на главной странице
    LOGOUT_BUTTON = [By.XPATH,'.//button[text()="Выход"]'] #Кнопка Выход в Личном Кабинете
    BUNS_SWITCHER = [By.XPATH,'.//span[text()="Булки"]'] #Переключатель Булки
    SAUCES_SWITCHER = [By.XPATH,'.//span[text()="Соусы"]'] #Переключатель Соусы
    TOPPINGS_SWITCHER = [By.XPATH,'.//span[text()="Начинки"]'] #Переключатель Начинки
    BUNS_INGREDIENT = [By.XPATH,'.//p[text()="Флюоресцентная булка R2-D3"]'] #Ингредиент Булки
    SAUCES_INGREDIENT = [By.XPATH,'.//p[text()="Соус Spicy-X"]'] #Ингредиент Соусы
    TOPPINGS_INGREDIENT = [By.XPATH,'.//p[text()="Мясо бессмертных моллюсков Protostomia"]'] #Ингредиент Начинки
    LOGO_BUTTON = [By.XPATH,'.//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]'] #Логотип в Хэдере