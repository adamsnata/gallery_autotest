import pytest

from projekt_tests.utils import path_dir


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):

    # iphone_11 = playwright.devices['iPhone 11 Pro']
    downloads_path = path_dir.reports()
    return {
        **browser_context_args,
        # **iphone_11,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1536, # 1920
            "height": 864, # 1080
        },
        # "accept_downloads": True,
        # "downloads_path": downloads_path
        # "locale": "de-DE",
        # "timezone_id" : "Europe/Berlin",
    }





# @pytest.fixture(scope="function", autouse=True)
# def screenshot_on_failure(page, request):
#     yield
#     save_all_screenshots = True
#
#     if save_all_screenshots or request.node.rep_call.failed:
#         test_name = request.node.name
#         screenshot_path = path_dir.screenshots(f'{test_name}.png')
#
#         page.screenshot(path=screenshot_path)
#
#         with open(screenshot_path, "rb") as image_file:
#             allure.attach(
#                 image_file.read(),
#                 name=f"{test_name}_screenshot",
#                 attachment_type=allure.attachment_type.PNG
#             )
#
#
# @pytest.fixture(scope="function", autouse=True)
# def capture_browser_logs_and_html(page, request):
#     """
#     Pytest fixture for capturing browser logs and page source automatically.
#     Attaches data to Allure after test execution.
#     """
#     console_logs = []
#
#     # Collect browser console logs using the 'console' event
#     def log_message(msg):
#         console_logs.append(f"{msg.type}: {msg.text}")
#
#     page.on("console", log_message)
#
#     # Yield control to the test
#     yield
#
#     # After the test is done, attach the logs and page source to Allure
#     if console_logs:
#         log_text = "\n".join(console_logs)
#         allure.attach(log_text, name="browser_logs", attachment_type=AttachmentType.TEXT, extension=".log")
#
#     try:
#         html_source = page.content()
#         allure.attach(html_source, name="page_source", attachment_type=AttachmentType.HTML, extension=".html")
#     except Exception as e:
#         allure.attach(str(e), name="Error capturing page source", attachment_type=AttachmentType.TEXT)
#
#
