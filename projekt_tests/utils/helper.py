import allure

import config


@allure.step("Open site: {base_url}")
def open_site(page, base_url=config.settings.base_url):
    page.goto(base_url)


@allure.step("Click on menu trigger")
def open_menu(page):
    page.locator(".menuTrigger").click()