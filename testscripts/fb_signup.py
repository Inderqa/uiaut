import string
import time
from random import random
import random

import requests
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from elementselector.selectors import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC




class CommonHelper:
    @classmethod
    def signup_facebook(cls):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")
        create_signup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, fb_create_Signup_button)))
        create_signup.click()

        signup_text = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,fb_signup_text),'Sign Up'))
        # assert "Sign Up" in signup_text
        alphabets = string.ascii_letters
        random_first_user = 'dan' + ''.join(random.choices(string.ascii_lowercase, k=2))
        random_last_user = 'jac' + ''.join(random.choices(string.ascii_lowercase , k=2))
        firstname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,fb_Signup_page_first_name)))
        firstname.send_keys(random_first_user)
        lastname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,fb_Signup_page_last_name)))
        lastname.send_keys(random_last_user)
        random_email = '' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        email = f"{random_email}@mailinator.com"
        enter_Email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,fb_Signup_page_mobile_or_Email)))
        enter_Email.send_keys(email)
        reenter_Email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,fb_Signup_page_re_enter_mobile_or_Email)))
        reenter_Email.send_keys(email)
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,fb_Signup_page_password)))
        password.send_keys("New@123$$$$")
        # elements = driver.find_elements(By.XPATH,fb_Signup_page_date)
        dropdown = Select(driver.find_element(By.XPATH,fb_Signup_page_date))
        desired_value = '15'
        for option in dropdown.options:
            if option.get_attribute('value') == desired_value:
                option.click()
                break  # Exit the loop after clicking the desired option
        month_dropdown = Select(driver.find_element(By.XPATH,fb_Signup_page_month))
        desired_value = 'Nov'
        for option in month_dropdown.options:
            if option.get_attribute('value') == desired_value:
                option.click()
                break
        year_dropdown = Select(driver.find_element(By.XPATH,fb_Signup_page_year))
        desired_value = '1982'
        for option in year_dropdown.options:
            if option.get_attribute('value') == desired_value:
                option.click()
                break
        gender_checkbox = driver.find_elements(By.XPATH,fb_Signup_gender_checkbox)
        desired_value = '2'
        for option in gender_checkbox:
            if option.get_attribute('value') == desired_value:
                option.click()
                break
        signup_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,fb_Signup_button)))
        signup_button.click()
        code_page_text = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,fb_send_Code_page_text)))
        assert "Enter the code from your email" in code_page_text.text
        assert "https://www.facebook.com/confirmemail.php" in driver.current_url
        # signup= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, fb_Signup_button)))

    @classmethod
    def amazon_search(cls):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        time.sleep(2)
        # element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, amazon_search_placeholder)))
        search = driver.find_element(By.XPATH, amazon_search_placeholder)
        placeholder_text = search.get_attribute("placeholder")
        assert "Search Amazon.in" in placeholder_text
        search.send_keys("air")
        try:
            wait = WebDriverWait(driver, 10)
            dropdown_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, amazon_Search_input_Dropdown)))
            desired_aria_label = "airpods"
            for option in dropdown_options:
                try:
                    if option.get_attribute("aria-label") == desired_aria_label:
                        option.click()
                        assert f"https://www.amazon.in/s?k={desired_aria_label}" in driver.current_url
                        break
                except StaleElementReferenceException:
                    continue
        finally:
            print("Element Found")

        element = driver.find_element(By.XPATH,amazon_sensitivity)
        x_coordinate = element.location['x']
        y_coordinate = element.location['y']
        x = print(x_coordinate)
        y = print(y_coordinate)
        # driver.execute_script("window.scrollTo(0, 2600)")
        wait = WebDriverWait(driver, 10)
        filter = wait.until(EC.visibility_of_all_elements_located((By.XPATH, amazon_sensitivity)))
        desired_label = "Up to 1.9"
        for option in filter:
            if option.get_attribute("aria-label") == desired_label:
                driver.execute_script("arguments[0].scrollIntoView();", option)
                time.sleep(5)
                driver.execute_script("arguments[0].click();", option)
                break
        import pdb
        pdb.set_trace()
        # select = Select(input_dropdown)
        # option_text = "airpods pro 2"
        # select.select_by_visible_text(option_text)


