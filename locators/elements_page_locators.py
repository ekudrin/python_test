from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "button#submit")

    # created form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "p#name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "p#email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p#currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p#permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title = 'Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class ='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class ='text-success']")

