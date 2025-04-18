import time

import allure
from playwright.sync_api import Page

from projekt_tests.utils import path_dir
from projekt_tests.utils.helper import open_site, open_menu
from projekt_tests.utils.image import compare_images


@allure.title("Full-page screenshot comparison on 'ГАЛЕРЕЯ'")
def test_artwoks(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Navigate to 'ГАЛЕРЕЯ' page"):
        page.get_by_role("link", name="ГАЛЕРЕЯ").click()
    with allure.step("Wait for content to load"):
        time.sleep(10)

    with allure.step("Take full-page screenshot"):
        diff_img = path_dir.screenshots("artworks_diff.png")
        img2_path = path_dir.screenshots("artworks_test.png")
        page.screenshot(path=img2_path, full_page=True)

    with allure.step("Compare screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("artworks.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'ГАЛЕРЕЯ' отличаются! Diff сохранён в {diff_img}"


@allure.title("Filtered screenshot comparison on 'ГАЛЕРЕЯ' with tag 'cats'")
def test_artwoks_filter(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Navigate to 'ГАЛЕРЕЯ' page"):
        page.get_by_role("link", name="ГАЛЕРЕЯ").click()
    with allure.step("Wait for content to load"):
        time.sleep(10)

    with allure.step("Apply filter: 'cats'"):
        textbox = page.get_by_role("textbox", name="Add tags...")
        textbox.click()
        textbox.fill("cats")
        textbox.press("Enter")

    with allure.step("Wait for filtered results to load"):
        time.sleep(1)

    with allure.step("Take filtered full-page screenshot"):
        diff_img = path_dir.screenshots("artworks_cats_diff.png")
        img2_path = path_dir.screenshots("artworks_cats_test.png")
        page.screenshot(path=img2_path, full_page=True)

    with allure.step("Compare filtered screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("artworks_cats.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'ГАЛЕРЕЯ' отличаются! Diff сохранён в {diff_img}"