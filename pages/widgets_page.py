import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPagePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_FIRST_CONTENT},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_SECOND_CONTENT},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_THIRD_CONTENT},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        if accordian_num != 'first':
            section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
            input_multi.click()
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.RETURN)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.RETURN)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.select_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.select_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.select_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        time.sleep(1)
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(10, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        time.sleep(3)
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_present(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self):
        time.sleep(2)
        what_button = self.element_is_visible(self.locators.TABS_WHAT)
        origin_button = self.element_is_visible(self.locators.TABS_ORIGIN)
        use_button = self.element_is_visible(self.locators.TABS_USE)
        # more_button = self.element_is_visible(self.locators.TABS_MORE)
        what_button.click()
        what_content = self.element_is_visible(self.locators.TABS_WHAT_CONTENT).text
        origin_button.click()
        origin_content = self.element_is_visible(self.locators.TABS_ORIGIN_CONTENT).text
        use_button.click()
        use_content = self.element_is_visible(self.locators.TABS_USE_CONTENT).text
        # more_button.click()
        # more_content = self.element_is_visible(self.locators.TABS_WHAT_CONTENT)
        return what_button.text, len(what_content), origin_button.text, len(origin_content), use_button.text, len(
            use_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPagePageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.HOVER_TEXT)
        time.sleep(2)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        time.sleep(5)
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.TOOL_TIP_BUTTON,
                                                            self.locators.HOVER_TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.TOOL_TIP_FIELD,
                                                           self.locators.HOVER_TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.TOOL_TIP_CONTRARY,
                                                              self.locators.HOVER_TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.TOOL_TIP_SECTION,
                                                             self.locators.HOVER_TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
