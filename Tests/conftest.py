import pytest
from selenium import webdriver
import settings
import sys
import os

# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(settings.URL)

    yield driver

    driver.quit()
#