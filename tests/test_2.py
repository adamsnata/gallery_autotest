

import allure
import pytest
import re
from playwright.sync_api import Page, expect




@allure.title('Check first image')
@pytest.mark.health_check
def test_check_img1(page: Page):
    page.goto("https://art-gallery-rina-34213.web.app/")
    page.locator("span").nth(1).click()
    page.get_by_role("link", name="РЕФЕРЕНСИ").click()
    expect(page.locator("img").first).to_be_visible()



@allure.title('Check aria snapshot')
@pytest.mark.health_check
def test_check_aria_snapshot(page: Page):
    page.goto("https://art-gallery-rina-34213.web.app/")
    page.locator("span").nth(1).click()
    page.get_by_role("link", name="РЕФЕРЕНСИ").click()
    expect(page.locator("body")).to_match_aria_snapshot(
        "- navigation:\n  - listitem:\n    - link \"ArtWorks\"\n  - list:\n    - listitem:\n      - link \"ГОЛОВНА\"\n    - listitem:\n      - link \"ГАЛЕРЕЯ\"\n    - listitem:\n      - link \"РЕФЕРЕНСИ\"\n    - listitem:\n      - link \"ПРО МЕНЕ\"\n- textbox \"Add tags...\"\n- button \"ADD IMAGE\"\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img")



def test_check_aria_snapshot2(page: Page):
    with allure.step("Go to main page"):
        page.goto("https://art-gallery-rina-34213.web.app/")

    with allure.step("Click 'РЕФЕРЕНСИ' link"):
        page.locator("span").nth(1).click()
        page.get_by_role("link", name="РЕФЕРЕНСИ").click()
        expect(page).to_have_url(re.compile(".*РЕФЕРЕНСИ"))

    with allure.step("Check ARIA snapshot"):
        expect(page.locator("body")).to_match_aria_snapshot(name="references-page")

    with allure.step("Check key elements are visible and functional"):
        expect(page.get_by_role("textbox", name="Add tags...")).to_be_visible()
        expect(page.get_by_role("button", name="ADD IMAGE")).to_be_enabled()
        expect(page.locator("img")).to_have_count(34)


# Что такое to_match_aria_snapshot?
# Это метод Playwright, который проверяет доступность страницы, как она воспринимается скринридерами (читателями экрана). Вместо DOM-структуры сравнивается логическая доступность компонентов.


# Зачем это используется?
# Такой тест помогает:
#
# Проверить, что нужные элементы действительно видимы и доступны (в том числе с клавиатуры или скринридером).
#
# Проверить, что страница не изменилась неожиданно (например, после изменений в коде).
#
# Убедиться, что важные элементы, такие как ссылки и кнопки, находятся на своих местах.

# ARIA (от англ. Accessible Rich Internet Applications) — это набор атрибутов, разработанных для улучшения доступности веб-приложений, особенно для людей с ограниченными возможностями, которые используют скринридеры или другие вспомогательные технологии.

# Скринридеры (от англ. screen readers) — это программы, которые читают вслух содержимое экрана с помощью синтеза речи или выводят текст на брайлевский дисплей, чтобы люди с нарушениями зрения могли взаимодействовать с компьютером, веб-сайтами и приложениями.