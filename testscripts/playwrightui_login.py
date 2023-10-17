import string
import time
from random import random
import random

import requests
# from selenium import webdriver
# from selenium.common import StaleElementReferenceException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from elementselector.selectors import *
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from pytest_steps import step
from allure_commons._allure import step
from playwright.sync_api import *

from playwright.sync_api import Page


class CommonHelper_UI:
    @classmethod
    def launchWeb(cls, page=None, logged_in='False'):
        with step("Launch the browser and web page"):
            page.goto("https://console.dev.intelcloud.cnvrg.io", timeout=120000)
            time.sleep(5)
            if logged_in == 'False':
                page.locator(login_name).is_visible(timeout=20000)
            else:
                page.wait_for_url(url=os.environ.get('DEFAULT_URL') + "/overview", timeout=20000)

    # @classmethod
    # def launchpage(cls, page=None):
    #     with sync_playwright() as p:
    #         browser = p.chromium.launch()
    #         context = browser.new_context()
    #         page = context.new_page()
    #         # Navigate to a URL
    #         return page.goto('https://console.dev.intelcloud.cnvrg.io')

    @classmethod
    def auth0_signin_Validation(cls, details=None, page=None):
        with step("Verify New Auth0 LOGIN UI"):
            expect(page.locator(auth0_intel_logo)).to_be_visible(timeout=20000)
            expect(page.locator(auth0_login_welcome_text)).to_be_visible(timeout=20000)
            expect(page.locator(auth0_login_welcome_text)).to_contain_text("Welcome to Intel AI Cloud")
            expect(page.locator(auth0_login_text)).to_be_visible(timeout=20000)
            expect(page.locator(auth0_login_text)).to_contain_text("Enter Email and password to log in")
            expect(page.locator(auth0_login_email_input)).to_be_visible(timeout=20000)
            expect(page.locator(auth0_login_password_input)).to_be_visible(timeout=20000)
            expect(page.locator(auth0_login_password_eye_button_show_password)).to_be_visible(timeout=20000)
            expect(page.locator(auth0_forgot_password_button_through_login)).to_be_visible(timeout=20000)
            expect(page.locator(auth0_login_continue_button)).to_be_visible(timeout=20000)
            if "dev" in os.environ.get('DEFAULT_URL'):
                assert "https://idc-dev.us.auth0.com/u/login?" in page.url
            else:
                assert "https://idc-stg.us.auth0.com/u/login?" in page.url