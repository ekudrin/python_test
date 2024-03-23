from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button#tabButton')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')

    NEW_TAB_TITLE = (By.CSS_SELECTOR, 'h1#sampleHeading')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#alertButton')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button#timerAlertButton')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#confirmButton')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span#confirmResult')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#promtButton')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span#promptResult')


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe#frame1')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe#frame2')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1#sampleHeading')


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe#frame1')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button#showSmallModal')
    CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button#closeSmallModal')
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div.modal-body')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-sm')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button#showLargeModal')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, 'div.modal-body p')
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-lg')
