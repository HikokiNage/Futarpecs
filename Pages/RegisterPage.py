from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # input fields
    nameInput = (By.ID, 'name')
    emailInput = (By.ID, 'email')
    passwordInput = (By.ID, 'password')
    passwordConfirmInput = (By.ID, 'password1')
    acceptPrivacyCheckbox = (By.ID, 'accept_privacy')
    acceptTermCheckbox = (By.ID, 'accept_term')
    registerBtn = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[7]/button')

    # error messages
    missingName = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[1]/div')
    missingEmail = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[2]/div')
    notSamePassword = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[3]/div')
    missingPrivacy = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[5]/div')
    missingTerm = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[6]/div')
    emailExist = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[2]/div')

    def do_registration(self, name, email, password):
        self.do_send_key(self.nameInput, name)
        self.do_send_key(self.emailInput, email)
        self.do_send_key(self.passwordInput, password)
        self.do_send_key(self.passwordConfirmInput, password)
        self.do_click(self.acceptPrivacyCheckbox)
        self.do_click(self.acceptTermCheckbox)
        self.do_click(self.registerBtn)

    def privacy_dont_accept(self, name, email, password):
        self.do_send_key(self.nameInput, name)
        self.do_send_key(self.emailInput, email)
        self.do_send_key(self.passwordInput, password)
        self.do_send_key(self.passwordConfirmInput, password)
        self.do_click(self.acceptPrivacyCheckbox)
        self.do_click(self.registerBtn)

    def term_dont_accept(self, name, email, password):
        self.do_send_key(self.nameInput, name)
        self.do_send_key(self.emailInput, email)
        self.do_send_key(self.passwordInput, password)
        self.do_send_key(self.passwordConfirmInput, password)
        self.do_click(self.acceptPrivacyCheckbox)
        self.do_click(self.registerBtn)

    def passwords_not_the_same(self, name, email, password):
        self.do_send_key(self.nameInput, name)
        self.do_send_key(self.emailInput, email)
        self.do_send_key(self.passwordInput, password)
        self.do_send_key(self.passwordConfirmInput, "")
        self.do_click(self.acceptPrivacyCheckbox)
        self.do_click(self.acceptTermCheckbox)
        self.do_click(self.registerBtn)

    def clear_all_input(self):
        self.clear_input(self.nameInput)
        self.clear_input(self.emailInput)
        self.clear_input(self.passwordInput)
        self.clear_input(self.passwordConfirmInput)
