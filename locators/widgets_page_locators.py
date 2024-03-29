from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div#section1Heading')
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, 'div#section1Content p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div#section2Heading')
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, 'div#section2Content p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div#section3Heading')
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, 'div#section3Content p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteMultipleInput')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div.css-1rhbuit-multiValue')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div.css-1rhbuit-multiValue svg path')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteSingleInput')


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input#datePickerMonthYearInput')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select.react-datepicker__month-select')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select.react-datepicker__year-select')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day-"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input#dateAndTimePickerInput')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input.range-slider')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input#sliderValue')


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button#startStopButton')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div.progress-bar')


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, 'a#demo-tab-what')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-what')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'a#demo-tab-origin')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-origin')
    TABS_USE = (By.CSS_SELECTOR, 'a#demo-tab-use')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-use')
    TABS_MORE = (By.CSS_SELECTOR, 'a#demo-tab-more')
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-more')


class ToolTipsPageLocators:
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button#toolTipButton')
    HOVER_TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'div#texFieldToolTopContainer input#toolTipTextField')
    HOVER_TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    TOOL_TIP_CONTRARY = (By.XPATH, '//*[.="Contrary"]')
    HOVER_TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    TOOL_TIP_SECTION = (By.XPATH, '//*[.="1.10.32"]')
    HOVER_TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    HOVER_TEXT = (By.CSS_SELECTOR, 'div.tooltip-inner')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul#nav li a')
