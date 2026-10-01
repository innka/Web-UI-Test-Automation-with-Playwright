#conftest.py
import pytest
from pages.login_page import LoginPage

url = "https://practicetestautomation.com/practice-test-login/"

@pytest.fixture
def login_page(page):
    page.goto(url)
    return LoginPage(page)