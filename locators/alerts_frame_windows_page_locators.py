from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button#tabButton')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')

    NEW_TAB_TITLE = (By.CSS_SELECTOR, 'h1#sampleHeading')
