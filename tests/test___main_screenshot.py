import time

import allure
from playwright.sync_api import Page

from projekt_tests.utils import path_dir
from projekt_tests.utils.helper import open_site
from projekt_tests.utils.image import compare_images


@allure.title("Full-page screenshot comparison on main page")
def test_main_full_screenshot(page: Page):

    open_site(page)
    time.sleep(15)  # Лучше заменить на явное ожидание элемента

    with allure.step("Take full-page screenshot"):
        diff_img = path_dir.screenshots("main_diff.png")
        img2_path = path_dir.screenshots("main_test.png")
        page.screenshot(path=img2_path, full_page=True)

    with allure.step("Compare screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("main.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'ПРО МЕНЕ' отличаются! Diff сохранён в {diff_img}"


@allure.title("Logo screenshot comparison on main page")
def test_main_logo_screenshot(page: Page):

    open_site(page)
    page.wait_for_timeout(3000)

    with allure.step("Take clipped screenshot of logo area"):
        diff_img = path_dir.screenshots("main_logo_diff.png")
        img2_path = path_dir.screenshots("main_logo_test.png")
        page.screenshot(
            path=img2_path,
            clip={"x": 700, "y": 550, "width": 130, "height": 150}
        )

    with allure.step("Compare logo screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("main_logo.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'ПРО МЕНЕ' отличаются! Diff сохранён в {diff_img}"