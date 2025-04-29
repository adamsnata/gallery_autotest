import allure
import pytest
from playwright.async_api import Page
from playwright.sync_api import expect

import config
from projekt_tests.utils.helper import open_site, open_menu


@allure.title('Menu')
@pytest.mark.health_check
def test_main_menu(page: Page):

    open_site(page)
    open_menu(page)
    with allure.step("Перевірити наявність пункту 'ГАЛЕРЕЯ' у меню"):
        expect(page.get_by_role("list")).to_contain_text("ГАЛЕРЕЯ")
    with allure.step("Перейти в розділ 'ГАЛЕРЕЯ'"):
        page.get_by_role("link", name="ГАЛЕРЕЯ").click()
        page.wait_for_url(f"{config.settings.base_url}artworks")
    with allure.step("Перевірити наявність пункту 'ГОЛОВНА' у меню"):
        expect(page.get_by_role("list")).to_contain_text("ГОЛОВНА")
    with allure.step("Повернутися на головну сторінку"):
        page.get_by_role("link", name="ГОЛОВНА").click()
        page.wait_for_url(config.settings.base_url)


@allure.title('Works')
@pytest.mark.health_check
def test_main_works(page: Page):

    open_site(page)
    open_menu(page)
    with allure.step("Перейти в розділ 'ГАЛЕРЕЯ'"):
        expect(page.get_by_role("list")).to_contain_text("ГАЛЕРЕЯ")
        page.get_by_role("link", name="ГАЛЕРЕЯ").click()
        page.wait_for_url(f"{config.settings.base_url}artworks")
    with allure.step("Натиснути на заголовок 'Works'"):
        page.get_by_text("Works").click()
        page.wait_for_url(config.settings.base_url)


@allure.title('Menus')
@pytest.mark.parametrize("menu, url",
                         [("ГАЛЕРЕЯ", "artworks"),
                          ("РЕФЕРЕНСИ", "reference"),
                          ("ПРО МЕНЕ", "about")],
                         ids=["artworks", "reference", "about"]
                         )
@pytest.mark.health_check
def test_menu(page: Page, menu, url):

    open_site(page)
    open_menu(page)
    with allure.step(f"Перевірити наявність пункту меню '{menu}'"):
        expect(page.get_by_role("list")).to_contain_text(menu)
    with allure.step(f"Перейти в розділ '{menu}'"):
        page.get_by_role("link", name=menu).click()
        page.wait_for_url(f"{config.settings.base_url}{url}")


@allure.title('Works')
@pytest.mark.health_check
def test_main_works(page: Page):

    open_site(page)
    open_menu(page)
    with allure.step("Перейти в розділ 'ГАЛЕРЕЯ'"):
        expect(page.get_by_role("list1")).to_contain_text("ГАЛЕРЕЯ")
        page.get_by_role("link", name="ГАЛЕРЕЯ").click()
        page.wait_for_url(f"{config.settings.base_url}artworks")
    with allure.step("Натиснути на заголовок 'Works'"):
        page.get_by_text("Works").click()
        page.wait_for_url(config.settings.base_url)


@allure.title('Works')
@pytest.mark.skip
def test_main_works2(page: Page):

    open_site(page)
    open_menu(page)
    with allure.step("Перейти в розділ 'ГАЛЕРЕЯ'"):
        expect(page.get_by_role("list")).to_contain_text("ГАЛЕРЕЯ")
        page.get_by_role("link", name="ГАЛЕРЕЯ").click()
        page.wait_for_url(f"{config.settings.base_url}artworks")
    with allure.step("Натиснути на заголовок 'Works'"):
        page.get_by_text("Works").click()
        page.wait_for_url(config.settings.base_url)
