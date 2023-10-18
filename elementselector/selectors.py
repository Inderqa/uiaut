import os

fb_create_Signup_button = "//*[contains(text(),'Create new account')]"
fb_signup_text = "//div[@class='pvl _52lp _59d-']//div[contains(text(),'Sign Up')]"
fb_Signup_page_first_name = "//input[@name='firstname']"
fb_Signup_page_last_name = "//input[@name='lastname']"
fb_Signup_page_mobile_or_Email = "//input[@name='reg_email__']"
fb_Signup_page_re_enter_mobile_or_Email = "//input[@name='reg_email_confirmation__']"
fb_Signup_page_password = "//input[@name='reg_passwd__']"
fb_Signup_page_date = "//select[@id='day']"
fb_Signup_page_month = "//select[@id='month']"
fb_Signup_page_year = "//select[@id='year']"
fb_Signup_gender_checkbox = "//input[@type = 'radio']"
fb_Signup_button = "//div[@class='_1lch']//button[contains(text(),'Sign Up')]"
fb_send_Code_page_text= "//div[@class='rfloat _ohf']//h2[contains(text(),'Enter the code from your email')]"


## >>>>>>>>>>> Amazon Search <<<<<<<<<<<<##
amazon_search_placeholder = "//input[@placeholder='Search Amazon.in']"
amazon_Search_input_Dropdown = "//div[@class='s-suggestion-container']/div"
amazon_sensitivity = "//div/following-sibling::ul/span/li"



login_name = "//input[@id='signInName']"
auth0_intel_logo ="//img[@id='prompt-logo-center']"
auth0_login_error_message="//span[@id='error-element-password']"
# auth0_login_password_eye_button_hide_password = "//button[@class='ce7494284 ulp-button-icon c5bf19ed3 _button-icon']//span[@class='screen-reader-only password-toggle-label hide'][contains(text(),'Hide password')]"
auth0_login_password_eye_button_show_password = "//button[@type='button']"
auth0_login_validation_error_message = "//span[@id='error-element-password']"
auth0_forgot_password_button_through_login = "//*[contains(text(),'Forgot password?')]"
auth0_forgot_password_email_input = "//input[@id='email']"
auth0_forgot_password_page_continue_button= "//div[@class='c6d5cc3be']//button[contains(text(),'Continue')]"
auth0_forgot_password_page_back_to_idc_button = "//*[contains(text(),'Back to idc-client')]"
auth0_forgot_password_page_forgot_password_text = "//*[contains(text(),'Forgot Your Password?')]"
auth0_forgot_password_page_validation_error_invalid_email = "//span[@id='error-element-email']"
auth0_forgot_password_subheader_text="//*[contains(text(),'Enter your email address and we will send you instructions to reset your password.')]"
auth0_forgot_password_check_email_header_text = "//*[contains(text(),'Check Your Email')]"
auth0_forgot_password_email_logo="//div[@class='cbc698e37 cd2cfea10']"
auth0_login_welcome_text = "//*[contains(text(),'Welcome to Intel AI Cloud')]"
auth0_login_text = "//*[contains(text(),'Enter Email and password to log in')]"
auth0_login_email_input = "//input[@inputmode='email']"
auth0_login_password_input = "//input[@id='password']"
auth0_login_continue_button = "//div[@class='c00346576']//button[contains(text(),'Continue')]"