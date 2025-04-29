import time

import allure
from playwright.sync_api import Page

from projekt_tests.utils import path_dir
from projekt_tests.utils.helper import open_site, open_menu
from projekt_tests.utils.image import compare_images


@allure.title("Full-page screenshot comparison on 'ПРО МЕНЕ'")
def test_about_full_screenshot(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Navigate to 'ПРО МЕНЕ' page"):
        page.get_by_role("link", name="ПРО МЕНЕ").click()
    with allure.step("Wait for content to load"):
        time.sleep(10)  # Лучше заменить на ожидание элемента, если можно

    with allure.step("Take full-page screenshot"):
        diff_img = path_dir.screenshots("about_diff.png")
        img2_path = path_dir.screenshots("about_test.png")
        page.screenshot(path=img2_path, full_page=True)

    with allure.step("Compare screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("about.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'ПРО МЕНЕ' отличаются! Diff сохранён в {diff_img}"


@allure.title("Logo screenshot comparison on 'ПРО МЕНЕ'")
def test_about_logo_screenshot(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Navigate to 'ПРО МЕНЕ' page"):
        page.get_by_role("link", name="ПРО МЕНЕ").click()
    with allure.step("Wait for content to load"):
        page.wait_for_timeout(3000)

    with allure.step("Take clipped screenshot of logo area"):
        diff_img = path_dir.screenshots("about_logo_diff.png")
        img2_path = path_dir.screenshots("about_logo_test.png")
        page.screenshot(
            path=img2_path,
            clip={"x": 150, "y": 250, "width": 450, "height": 450}
        )

    with allure.step("Compare logo screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("about_logo.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'ПРО МЕНЕ' отличаются! Diff сохранён в {diff_img}"