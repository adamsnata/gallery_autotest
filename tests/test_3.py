
import allure
import pytest
import re
from playwright.sync_api import Page, expect

import path_dir


def test_main_page_screenshot(page: Page):

    page.goto("https://art-gallery-rina-34213.web.app/", timeout=60000)



    # Скриншот всей страницы
    page.screenshot(path=path_dir.screenshots("full_page.png"), full_page=True)

    # Пример: скриншот заголовка (если есть h1)
    try:
        h1 = page.locator("h1").first
        h1.screenshot(path="screenshots/header.png")
    except:
        print("Элемент h1 не найден")

    # Пример: скриншот галереи (если есть div.gallery)
    try:
        gallery = page.locator("div.gallery").first
        gallery.screenshot(path=path_dir.screenshots("gallery.png"))
    except:
        print("Элемент div.gallery не найден")