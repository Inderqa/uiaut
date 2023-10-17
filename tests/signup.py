# from selenium.webdriver.common.devtools.v117 import page
import page

from testscripts.fb_signup import CommonHelper
from testscripts.playwrightui_login import CommonHelper_UI
from playwright.sync_api import Page


# CommonHelper.signup_facebook()

# CommonHelper.amazon_search()
# def Verify_signup_through_mail_change_password_redirection_after_setting_new_password(browser_fixture):
#     browser, context, page = browser_fixture
#     CommonHelper.launchWeb(page=page)
#     details = CommonHelper.create_organization()
#     CommonHelper.sign_up(details=details, page=page)
#     CommonHelper.delete_org(details=details, page=page)

def test_verify_auth0ui_login_page(browser_fixture):
     browser, context, page = browser_fixture
     CommonHelper_UI.launchWeb(page=page)
     CommonHelper_UI.auth0_signin_Validation(page=page)