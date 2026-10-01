#login_page.py
from playwright.sync_api import expect
from pages.logged_in_success_page import LoggedInSuccessPage

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.submit_button = page.locator('#submit')
        self.error_message = page.locator('#error')

    #username
    def verify_username_visible(self):
        expect(self.username_input).to_be_visible()

    def set_username_input(self, username):
        self.username_input.fill(username)

    #password
    def verify_password_visible(self):
        expect(self.password_input).to_be_visible()

    def set_password_input(self, password):
        self.password_input.fill(password)

    #button submit
    def verify_submit_button_visible(self):
        expect(self.submit_button).to_be_visible()

    def click_submit_button(self):
        self.submit_button.click()

    #login method that returns LoggedInSuccessPage if login is successful, otherwise returns self
    def login(self, username, password):
        self.set_username_input(username)
        self.set_password_input(password)
        self.click_submit_button()
        if "/logged-in-successfully/" in self.page.url:
            return LoggedInSuccessPage(self.page)
        return self
    
    #error message for incorrect username
    def error_message_incorrect_username(self):
        expect(self.error_message).to_have_text("Your username is invalid!")

    #error message for incorrect password
    def error_message_incorrect_password(self):
        expect(self.error_message).to_have_text("Your password is invalid!")
    

        
