from locators.alerts_frame_windows_page_locators import BrowserWindowPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text
