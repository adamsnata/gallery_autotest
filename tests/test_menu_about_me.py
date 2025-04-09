

import allure
import pytest
from playwright.async_api import Page
from playwright.sync_api import expect



@allure.title('Check About me')
@pytest.mark.health_check
def test_check_about_me(page: Page):
    page.goto("https://art-gallery-rina-34213.web.app/")
    page.get_by_role("navigation").locator("div").nth(2).click()
    page.get_by_role("link", name="ПРО МЕНЕ").click()
    expect(page.locator("h1")).to_contain_text("Про мене")


@allure.title('Check Briefly')
@pytest.mark.health_check
def test_check_briefly(page: Page):
    page.goto("https://art-gallery-rina-34213.web.app/")
    page.get_by_role("navigation").locator("div").nth(2).click()
    page.get_by_role("link", name="ПРО МЕНЕ").click()
    expect(page.locator("h2")).to_contain_text("Коротко")

@allure.title('Check the first part of the description ')
@pytest.mark.health_check
def test_description_part1(page: Page):
    page.goto("https://art-gallery-rina-34213.web.app/")
    page.get_by_role("navigation").locator("div").nth(2).click()
    page.get_by_role("link", name="ПРО МЕНЕ").click()
    expect(page.locator("#root")).to_contain_text(
        "Художниця, роботи якої представлені на цьому сайті,"
        " спеціалізується на живописі олією та цифровому мистецтві. "
        "Тут ви знайдете як її більш ранні роботи, виконані аквареллю та акрилом, так і пізніші твори."
        " Вона постійно експериментує з різними техніками та стилями. "
        "Після завершення художньої школи вона продовжила своє самостійне навчання, "
        "пройшовши безліч онлайн-курсів і практик. "
        "Тепер, накопичивши багатий досвід і знання, художниця готова поділитися своєю творчістю з усім світом.")


@allure.title('Check About me')
@pytest.mark.health_check
def test_description_part2(page: Page):
    page.goto("https://art-gallery-rina-34213.web.app/")
    page.get_by_role("navigation").locator("div").nth(2).click()
    page.get_by_role("link", name="ПРО МЕНЕ").click()
    expect(page.locator("#root")).to_contain_text(
        "Вона також захоплюється фотографією і використовує власні фотографії для створення своїх картин."
        " Оскільки кількість референсів в її арсеналі постійно зростає,"
        " виникла потреба у створенні місця для їх зберігання та сортування. Так і був створений цей сайт.")