from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # header buttons
    registerBtn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/nav/div[2]/a[4]')
    loginBtn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/nav/div[2]/a[3]')
    trackingBtn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/nav/div[2]/a[2]')
    courierOrderBtn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/nav/div[2]/a[1]')
    profileBtn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/nav/div[2]/a[3]')
    logoutBtn = (By.XPATH,  '//*[@id="root"]/div[1]/div[1]/div/div[1]/nav/div[2]/a[4]')

    def navigate_to_registerPage(self):
        self.do_click(self.registerBtn)

    def navigate_to_loginPage(self):
        self.do_click(self.loginBtn)

    def navigate_to_trackingPage(self):
        self.do_click(self.trackingBtn)

    def navigate_to_courierOrderPage(self):
        self.do_click(self.courierOrderBtn)
