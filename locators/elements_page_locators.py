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


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    # add_person_form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class TestButtonsPageLocators:
    # buttons
    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button#rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    # result
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, "p#doubleClickMessage")
    SUCCESS_RIGHT = (By.CSS_SELECTOR, "p#rightClickMessage")
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, "p#dynamicClickMessage")


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a#simpleLink")
    BAD_REQUEST = (By.CSS_SELECTOR, "a#bad-request")


class UploadAndDownloadPageLocators:
    UPLOAD_FILE_INPUT = (By.CSS_SELECTOR, "input#uploadFile")
    UPLOADED_FILE = (By.CSS_SELECTOR, "p#uploadedFilePath")

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a#downloadButton')


class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button#colorChange")
    ENABLE_AFTER_BUTTON = (By.CSS_SELECTOR, "button#enableAfter")
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, "button#visibleAfter")
