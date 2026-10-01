#logged_in_success_page.py
import re
from playwright.sync_api import expect

class LoggedInSuccessPage:
    def __init__(self, page):
        self.page = page
        self.login_success = self.page.get_by_role("heading", name="Logged In Successfully")
        self.success_text = page.get_by_text("Congratulations student. You successfully logged in!")
        self.button_logout = page.get_by_role("link", name="Log out")
    
    #verifier l'affichage des éléments de la page
    def verify_login_success_visible(self):
        expect(self.login_success).to_be_visible()
    
    def verify_success_text_visible(self):
        expect(self.success_text).to_be_visible()

    def verify_logout_button_visible(self):
        expect(self.button_logout).to_be_visible()

    #verifier l'url de la page
    def verify_page_url(self):
        expect(self.page).to_have_url(re.compile(r"/logged-in-successfully/"))

    