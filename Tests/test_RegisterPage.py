import pytest
from Tests.test_BaseTest import BaseTest
from Pages.RegisterPage import RegisterPage
from Pages.HomePage import HomePage
from faker import Faker


class TestRegistration(BaseTest):
    fake = Faker()

    fakeName = fake.name()
    fakeEmail = fake.safe_email()

    def test_successful_registration(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_registerPage()
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.do_registration(self.fakeName, self.fakeEmail, "Teszt123")
        assert self.homePage.get_element_text(self.homePage.profileBtn) == "Profilom"
        self.homePage.do_click(self.homePage.logoutBtn)

    def test_name_dont_add(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_registerPage()
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.do_registration("", self.fakeEmail, "Teszt123")
        assert self.homePage.is_visible(self.registerPage.missingName)

    def test_email_dont_add(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_registerPage()
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.do_registration(self.fakeName, "", "Teszt123")
        assert self.homePage.is_visible(self.registerPage.missingEmail)

    def test_passwords_not_the_same(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_registerPage()
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.passwords_not_the_same(self.fakeName, self.fakeEmail, "Teszt123")
        assert self.homePage.is_visible(self.registerPage.notSamePassword)

    def test_privacy_dont_accept(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_registerPage()
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.privacy_dont_accept(self.fakeName, self.fakeEmail, "Teszt123")
        assert self.homePage.is_visible(self.registerPage.missingPrivacy)

    def test_term_dont_accept(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_registerPage()
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.term_dont_accept(self.fakeName, self.fakeEmail, "Teszt123")
        assert self.homePage.is_visible(self.registerPage.missingTerm)

    def test_email_already_registered(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_registerPage()
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.do_registration(self.fakeName, "teszt@teszt.hu", "Teszt123")
        assert self.homePage.is_visible(self.registerPage.emailExist)