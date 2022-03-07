from Tests.test_BaseTest import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


class TestLogin(BaseTest):

    def test_valid_logon(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_loginPage()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("validemail@teszt.hu", "Teszt123")
        assert self.homePage.get_element_text(self.homePage.profileBtn) == "Profilom"
        self.homePage.do_click(self.homePage.logoutBtn)

    def test_email_and_password_dont_add(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_loginPage()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("", "")
        assert self.homePage.is_visible(self.loginPage.errorMessage)

    def test_email_dont_add(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_loginPage()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("", "Teszt123")
        assert self.homePage.is_visible(self.loginPage.errorMessage)

    def test_password_dont_add(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_loginPage()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("validemail@teszt.hu", "")
        assert self.homePage.is_visible(self.loginPage.errorMessage)

    def test_invalid_email_add(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_loginPage()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("invalidemailteszt.hu", "Teszt123")
        assert self.homePage.is_visible(self.loginPage.errorMessage)