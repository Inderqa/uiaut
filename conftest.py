import pytest
import os
import json
import re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="function", autouse=True)
# def browser_fixture():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
#         page = context.new_page()
#         yield browser, context, page
#         browser.close()
