from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div#section1Heading')
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, 'div#section1Content p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div#section2Heading')
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, 'div#section2Content p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div#section3Heading')
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, 'div#section3Content p')
