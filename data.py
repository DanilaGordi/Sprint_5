import random


class EnterSite:
    name = 'Daniil'
    email = 'danila.gordi@yandex.ru'
    password = '1233121223'
    invalid_password = '11111'

    @staticmethod
    def random_email():
        user = ""
        domen = random.choice(['gmail.com', 'yandex.ru', 'mail.com', 'kek.ru'])

        for i in range(8):
            user += random.choice('abcdefgHIJKLMNOP-!._123')

        email = f"{user}@{domen}"
        return email

    @staticmethod
    def random_password():
        password = ""

        for i in range(8):
            digit = str(random.randint(0, 9))
            password += digit

        return password


class Site:
    main_site = 'https://stellarburgers.nomoreparties.site/'
    login_site = 'https://stellarburgers.nomoreparties.site/login'
    registration_site = 'https://stellarburgers.nomoreparties.site/register'
    forgot_pass_site = 'https://stellarburgers.nomoreparties.site/forgot-password'
    profile_site = 'https://stellarburgers.nomoreparties.site/account/profile'
