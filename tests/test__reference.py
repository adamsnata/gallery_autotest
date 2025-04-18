import time

import allure
from playwright.sync_api import Page

from projekt_tests.utils import path_dir
from projekt_tests.utils.helper import open_menu, open_site
from projekt_tests.utils.image import compare_images


@allure.title("Full-page screenshot comparison on 'РЕФЕРЕНСИ'")
def test_reference(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Navigate to 'РЕФЕРЕНСИ' page"):
        page.get_by_role("link", name="РЕФЕРЕНСИ").click()
    with allure.step("Wait for content to load"):
        time.sleep(15)  # Желательно заменить на явное ожидание

    with allure.step("Take full-page screenshot"):
        diff_img = path_dir.screenshots("reference_diff.png")
        img2_path = path_dir.screenshots("reference_test.png")
        page.screenshot(path=img2_path, full_page=True)

    with allure.step("Compare screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("reference.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'РЕФЕРЕНСИ' отличаются! Diff сохранён в {diff_img}"


@allure.title("Filtered screenshot comparison on 'РЕФЕРЕНСИ' with tags 'sky' and 'road'")
def test_reference_filter(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Navigate to 'РЕФЕРЕНСИ' page"):
        page.get_by_role("link", name="РЕФЕРЕНСИ").click()
    with allure.step("Wait for content to load"):
        time.sleep(15)

    with allure.step("Apply filters: 'sky' and 'road'"):
        textbox = page.get_by_role("textbox", name="Add tags...")
        textbox.click()
        textbox.fill("sky")
        textbox.press("Enter")
        textbox.fill("road")
        textbox.press("Enter")

    with allure.step("Wait for filtered content to render"):
        time.sleep(10)

    with allure.step("Take filtered full-page screenshot"):
        diff_img = path_dir.screenshots("reference_sky_road_diff.png")
        img2_path = path_dir.screenshots("reference_sky_road_test.png")
        page.screenshot(path=img2_path, full_page=True)

    with allure.step("Compare filtered screenshots and save diff if needed"):
        assert compare_images(
            img1_path=path_dir.screenshots_expected("reference_sky_road.png"),
            img2_path=img2_path,
            diff_output_path=diff_img
        ), f"Скриншоты 'РЕФЕРЕНСИ' отличаются! Diff сохранён в {diff_img}"