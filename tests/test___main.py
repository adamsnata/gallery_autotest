import allure
import pytest
from playwright.async_api import Page
from playwright.sync_api import expect

from projekt_tests.utils.helper import open_site


@allure.title('Перевірка заголовка "Галерея Напрацювань" на головній сторінці')
@pytest.mark.health_check
def test_main_page_contains_gallery_title(page: Page):

    open_site(page)
    with allure.step('Перевірити наявність тексту "Галерея Напрацювань"'):
        expect(page.locator("#root")).to_contain_text("Галерея Напрацювань")


@allure.title('Перевірка опису художниці (олійний та цифровий живопис)')
@pytest.mark.health_check
def test_about_me_contains_painting_description(page: Page):

    open_site(page)
    with allure.step("Перевірити наявність опису художниці"):
        expect(page.locator("#root")).to_contain_text(
            "Працюю з олійним та цифровим живописом. "
            "Мій стиль поєднує елементи імпресіонізму та реалізму,"
            " з акцентом на впізнаваність і яскравість образів у мрійливій атмосфері."
        )


@allure.title('Перевірка інформації про Clip Studio Paint та техніки')
@pytest.mark.health_check
def test_about_me_contains_clip_studio_info(page: Page):

    open_site(page)
    with allure.step("Перевірити згадку про Clip Studio Paint та техніки"):
        expect(page.locator("#root")).to_contain_text(
            "У своїй цифровій роботі я використовую Clip Studio Paint, "
            "поєднуючи традиційні техніки з сучасними — і навпаки."
            " Вірю, що кожна техніка збагачує іншу та відкриває нові творчі можливості."
        )


@allure.title('Перевірка вітального тексту та опису галереї')
@pytest.mark.health_check
def test_about_me_contains_gallery_welcome_text(page: Page):

    open_site(page)
    with allure.step("Перевірити вітальний текст"):
        expect(page.locator("#root")).to_contain_text(
            "Ласкаво просимо до Галереї! "
            "Тут ви знайдете різноманітні роботи в різних техніках, "
            "а також фотографії,"
            " які можна використовувати як референси для створення мистецтва."
        )


@allure.title('Перевірка наявності заголовка "Роботи"')
@pytest.mark.health_check
def test_main_page_contains_works_header(page: Page):

    open_site(page)
    with allure.step('Перевірити наявність заголовка "Роботи"'):
        expect(page.locator("#root")).to_contain_text("Роботи")


@allure.title('Перевірка наявності підпису "Олія & Цифровий живопис"')
@pytest.mark.health_check
def test_main_page_contains_oil_and_digital_painting_label(page: Page):

    open_site(page)
    with allure.step('Перевірити наявність підпису "Олія & Цифровий живопис"'):
        expect(page.locator("#root")).to_contain_text("Олія & Цифровий живопис")