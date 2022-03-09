import time

from Tests.test_BaseTest import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MyProfilePage import MyProfilePagePage
from Config.Config import TestData
from faker import Faker


class TestMyProfilePage(BaseTest):
    fake = Faker(['hu_HU'])

    fakeName = fake.name()
    fakeInvoiceName = fake.name()
    fakeSenderName = fake.name()
    fakeEmail = fake.free_email()
    fakePhoneNumber = fake.phone_number()
    fakeZip = fake.postcode()
    fakeCity = fake.real_city_name()
    fakeAddress = fake.street_address()
    fakeBankAccount = fake.iban()
    fakeTaxCode = fake.isbn13()

    def test_change_personal_data(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_loginPage()

        time.sleep(10)

        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.validUsername, TestData.password)
        self.homePage.do_click(self.homePage.profileBtn)

        self.myProfilePage = MyProfilePagePage(self.driver)
        self.myProfilePage.select_change_data_option()

        time.sleep(10)

        self.myProfilePage.change_phone_number(self.fakePhoneNumber)
        self.myProfilePage.change_invoice_name(self.fakeInvoiceName)
        self.myProfilePage.change_invoice_zip(self.fakeZip)
        self.myProfilePage.change_invoice_City(self.fakeCity)
        self.myProfilePage.change_invoice_address(self.fakeAddress)
        self.myProfilePage.change_tax_code(self.fakeTaxCode)
        self.myProfilePage.change_invoice_email(self.fakeEmail)
        self.myProfilePage.change_sender_name(self.fakeSenderName)
        self.myProfilePage.change_sender_zip(self.fakeZip)
        self.myProfilePage.change_sender_city(self.fakeCity)
        self.myProfilePage.change_sender_address(self.fakeAddress)
        self.myProfilePage.change_bank_account(self.fakeBankAccount)

        self.myProfilePage.submit_data_change()
        self.homePage.alert_is_present()