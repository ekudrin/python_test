import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.page_load_strategy = 'eager'  # В обычном режиме сайт ждет ответ от апи >10 секунд,замедляет работу всех тестов
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()
