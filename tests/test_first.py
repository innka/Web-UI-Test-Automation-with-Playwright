#smoke test pour verifier que playwright fonctionne correctement
from playwright.sync_api import sync_playwright

url = "https://practicetestautomation.com/practice-test-login/"

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    assert page.title() == "Test Login | Practice Test Automation"
    browser.close()

