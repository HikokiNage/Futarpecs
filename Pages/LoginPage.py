from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    emailInput = (By.ID, 'email')
    passwordInput = (By.ID, 'password')
    loginBtn = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[3]/button')
    forgotPassword = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[3]/a')
    errorMessage = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[1]')

    def do_login(self, email, password):
        self.do_send_key(self.emailInput, email)
        self.do_send_key(self.passwordInput, password)
        self.do_click(self.loginBtn)

    def navigate_to_forgot_password_page(self):
        self.do_click(self.forgotPassword)