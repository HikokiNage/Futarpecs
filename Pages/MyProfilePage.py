from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from selenium.webdriver.common.by import By


class MyProfilePagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # options

    myPackagesOption = (By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/ul/li[1]/a')
    periodicAccountingOption = (By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/ul/li[2]/a')
    invoicesOption = (By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/ul/li[3]/a')
    changingDataOption = (By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/ul/li[4]/a')
    changePasswordOption = (By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/ul/li[5]/a')

    # my packages

    filterInput = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/table/thead/tr[1]/td/table/tbody/tr[2]/td[1]/input')
    initialDateInput = (
        By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/table/thead/tr[1]/td/table/tbody/tr[2]/td[2]/div[1]/div/input')
    endDateInput = (
        By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/table/thead/tr[1]/td/table/tbody/tr[2]/td[3]/div[1]/div/input')
    searchBtn = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/table/thead/tr[1]/td/div/button')

    # periodic accounting

    periodicAccountH1Tag = (By.TAG_NAME, 'h1')

    # invoices

    invoicesH1Tag = (By.TAG_NAME, 'h1')

    # changing data

    # personal data

    nameInput = (By.ID, 'Name')
    emailInput = (By.ID, 'Email')
    phoneNumberInput = (By.ID, 'Phone')

    # invoice data

    invoiceNameInput = (By.ID, 'InvoiceName')
    invoiceZipInput = (By.ID, 'InvoiceZip')
    invoiceCityInput = (By.ID, 'InvoiceCity')
    invoiceAddressInput = (By.ID, 'InvoiceAddress')
    invoiceTaxCodeInput = (By.ID, 'InvoiceTaxCode')
    invoiceEmailInput = (By.ID, 'InvoiceEmail')

    # sender data

    senderNameInput = (By.ID, 'DefaultSenderName')
    senderZipInput = (By.ID, 'DefaultSenderZip')
    senderCityInput = (By.ID, 'DefaultSenderCity')
    senderAddressInput = (By.ID, 'DefaultSenderAddress')
    bankAccountNumberInput = (By.ID, 'BankAccountNumber')

    # save button

    saveDataChangesBtn = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/form/div/div[17]/div/button')

    # change password

    passwordInput = (By.ID, 'password')
    confirmPasswordInput = (By.ID, 'password1')
    submitBtn = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/form/div/div[3]/button')

    def logout(self):
        self.do_click(HomePage.logoutBtn)

    def change_password(self, newPassword, newPasswordConfirm):
        self.do_click(self.changePasswordOption)
        self.do_send_key(self.passwordInput, newPassword)
        self.do_send_key(self.confirmPasswordInput, newPasswordConfirm)
        self.do_click(self.submitBtn)

    # personal data changing methods

    def select_change_data_option(self):
        self.do_click(self.changingDataOption)

    def change_name(self, newName):
        self.clear_input(self.nameInput)
        self.do_send_key(self.nameInput, newName)

    def change_phone_number(self, newPhoneNumber):
        self.clear_input(self.phoneNumberInput)
        self.do_send_key(self.phoneNumberInput, newPhoneNumber)

    def change_email(self, newEmail):
        self.clear_input(self.emailInput)
        self.do_send_key(self.emailInput, newEmail)

    def change_invoice_name(self, newInvoiceName):
        self.clear_input(self.invoiceNameInput)
        self.do_send_key(self.invoiceNameInput, newInvoiceName)

    def change_invoice_zip(self, newInvoiceZip):
        self.clear_input(self.invoiceZipInput)
        self.do_send_key(self.invoiceZipInput, newInvoiceZip)

    def change_invoice_City(self, newInvoiceCity):
        self.clear_input(self.invoiceCityInput)
        self.do_send_key(self.invoiceCityInput, newInvoiceCity)

    def change_invoice_address(self, newInvoiceAddress):
        self.clear_input(self.invoiceAddressInput)
        self.do_send_key(self.invoiceAddressInput, newInvoiceAddress)

    def change_tax_code(self, newInvoiceTaxCode):
        self.clear_input(self.invoiceTaxCodeInput)
        self.do_send_key(self.invoiceTaxCodeInput, newInvoiceTaxCode)

    def change_invoice_email(self, newInvoiceEmail):
        self.clear_input(self.invoiceEmailInput)
        self.do_send_key(self.invoiceEmailInput, newInvoiceEmail)

    def change_sender_name(self, newSenderName):
        self.clear_input(self.senderNameInput)
        self.do_send_key(self.senderNameInput, newSenderName)

    def change_sender_zip(self, newSenderZip):
        self.clear_input(self.senderZipInput)
        self.do_send_key(self.senderZipInput, newSenderZip)

    def change_sender_city(self, newSenderCity):
        self.clear_input(self.senderCityInput)
        self.do_send_key(self.senderCityInput, newSenderCity)

    def change_sender_address(self, newSenderAddress):
        self.clear_input(self.senderAddressInput)
        self.do_send_key(self.senderAddressInput, newSenderAddress)

    def change_bank_account(self, newBankAccount):
        self.clear_input(self.bankAccountNumberInput)
        self.do_send_key(self.bankAccountNumberInput, newBankAccount)

    def submit_data_change(self):
        self.do_click(self.saveDataChangesBtn)
