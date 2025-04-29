import allure
import pytest
from playwright.sync_api import Page, expect

from projekt_tests.utils.helper import open_site, open_menu


@allure.title('Check first image')
@pytest.mark.health_check
def test_check_img1(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Go to 'РЕФЕРЕНСИ' page"):
        page.get_by_role("link", name="РЕФЕРЕНСИ").click()

    with allure.step("Check first image is visible"):
        expect(page.locator("img").first).to_be_visible()


@allure.title('Check aria snapshot')
@pytest.mark.health_check
def test_check_aria_snapshot(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Go to 'РЕФЕРЕНСИ' page"):
        page.get_by_role("link", name="РЕФЕРЕНСИ").click()

    with allure.step("Check ARIA snapshot matches expected structure"):
        expect(page.locator("body")).to_match_aria_snapshot(
            "- navigation:\n  - listitem:\n    - link \"ArtWorks\"\n  - list:\n    - listitem:\n      - link \"ГОЛОВНА\"\n    - listitem:\n      - link \"ГАЛЕРЕЯ\"\n    - listitem:\n      - link \"РЕФЕРЕНСИ\"\n    - listitem:\n      - link \"ПРО МЕНЕ\"\n- textbox \"Add tags...\"\n- button \"ADD IMAGE\"\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img\n- img"
        )


def test_check_aria_snapshot2(page: Page):

    open_site(page)
    open_menu(page)

    with allure.step("Go to 'РЕФЕРЕНСИ' page"):
        page.get_by_role("link", name="РЕФЕРЕНСИ").click()

    with allure.step("Check ARIA snapshot"):
        expect(page.locator("body")).to_match_aria_snapshot(name="references-page")

    with allure.step("Check key elements are visible and functional"):
        expect(page.get_by_role("textbox", name="Add tags...")).to_be_visible()
        expect(page.get_by_role("button", name="ADD IMAGE")).to_be_enabled()
        expect(page.locator("img")).to_have_count(34)
