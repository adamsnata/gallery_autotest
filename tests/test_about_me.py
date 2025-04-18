import allure
import pytest
from playwright.async_api import Page
from playwright.sync_api import expect

from projekt_tests.utils.helper import open_site, open_menu


@allure.title('Check About me')
@pytest.mark.health_check
def test_check_about_me(page: Page):
    open_site(page)
    open_menu(page)
    with allure.step("Click on 'ПРО МЕНЕ' link"):
        page.get_by_role("link", name="ПРО МЕНЕ").click()
    with allure.step("Check  'Про мене'"):
        expect(page.locator("h1")).to_contain_text("Про мене")


@allure.title('Check Briefly')
@pytest.mark.health_check
def test_check_briefly(page: Page):
    open_site(page)
    open_menu(page)
    with allure.step("Click on 'ПРО МЕНЕ' link"):
        page.get_by_role("link", name="ПРО МЕНЕ").click()
    with allure.step("Check 'Коротко'"):
        expect(page.locator("h2")).to_contain_text("Коротко")


@allure.title('Check the first part of the description')
@pytest.mark.health_check
def test_description_part1(page: Page):
    open_site(page)
    open_menu(page)
    with allure.step("Click on 'ПРО МЕНЕ' link"):
        page.get_by_role("link", name="ПРО МЕНЕ").click()
    with allure.step("Check that page contains the first part of the description"):
        expect(page.locator("#root")).to_contain_text(
            "Художниця, роботи якої представлені на цьому сайті,"
            " спеціалізується на живописі олією та цифровому мистецтві. "
            "Тут ви знайдете як її більш ранні роботи, виконані аквареллю та акрилом, так і пізніші твори."
            " Вона постійно експериментує з різними техніками та стилями. "
            "Після завершення художньої школи вона продовжила своє самостійне навчання, "
            "пройшовши безліч онлайн-курсів і практик. "
            "Тепер, накопичивши багатий досвід і знання, художниця готова поділитися своєю творчістю з усім світом."
        )


@allure.title('Check the second part of the description')
@pytest.mark.health_check
def test_description_part2(page: Page):
    open_site(page)
    open_menu(page)
    with allure.step("Click on 'ПРО МЕНЕ' link"):
        page.get_by_role("link", name="ПРО МЕНЕ").click()
    with allure.step("Check that page contains the second part of the description"):
        expect(page.locator("#root")).to_contain_text(
            "Вона також захоплюється фотографією і використовує власні фотографії для створення своїх картин."
            " Оскільки кількість референсів в її арсеналі постійно зростає,"
            " виникла потреба у створенні місця для їх зберігання та сортування. Так і був створений цей сайт."
        )