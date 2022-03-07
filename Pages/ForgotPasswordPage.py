from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    emailInput = (By.ID, 'email')
    newPasswordBtn = (By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/div[3]/button')