from selenium.webdriver.common.by import By


class TestLocators:
    # Для первичного окна регистрации
    NANE_FIELD_FIRST = (By.XPATH, "(//input[@name= 'name'])[1]") # Поле ввода имени
    EMAIL_FIELD_FIRST = (By.XPATH, "(//input[@name= 'name'])[2]")  # Поле ввода email
    PASSWORD_FIELD_FIRST = (By.XPATH, "//input[@name= 'Пароль']")  # Поле ввода пароля
    REGISTRATION_BTN = (By.XPATH, "//button[text()='Зарегистрироваться']")   # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об некорректном пароле

    # Для последующего входа
    EMAIL_FIELD_SECOND = (By.XPATH, ".//input[@name='name']")  # Поле ввода email
    PASSWORD_FIELD_SECOND = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввода пароля
    LOGIN_IN_ACC_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт
    ACCOUNT_BTN = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    LOGIN_BTN = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"
    LOGIN_LINK_BTN = (By.XPATH, ".//a[@href='/login']")  # Кнопка Уже зарегистрированы? "Войти"

    # Для проверки перехода в конструктор
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок страницы Конструктор
    LOGO_BTN = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Лого страницы сайта

    # Для проверки выхода
    LEAVE_BTN = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход"

    # Для тестирования конструктора
    BREAD_BTN = (By.XPATH, ".//span[text()='Булки']")  # Кнопка "Булки"
    BREAD_SECTION = (By.XPATH, ".//h2[text()='Булки']")  # Раздел "Булки"
    SAUCE_BTN = (By.XPATH, ".//span[text()='Соусы']")  # Кнопка "Соус"
    SAUCE_SECTION = (By.XPATH, ".//h2[text()='Соусы']")  # Раздел "Соус"
    TOPPING_BTN = (By.XPATH, ".//span[text()='Начинки']")  # Кнопка "Начинки"
    TOPPING_SECTION = (By.XPATH, ".//h2[text()='Начинки']")  # Раздел "Начинки"
    ACTIVE_BTN = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # Текущая кнопка конструктора
