from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Sender Data

    senderName = (By.ID, 'sender_name')
    senderZip = (By.ID, 'sender_zip')
    senderCity = (By.ID, 'sender_city')
    senderAddress = (By.ID, 'sender_address')
    senderEmail = (By.ID, 'sender_email')
    senderPhone = (By.ID, 'sender_phone')

    # Recipient Data

    recipientName = (By.ID, 'recipient_name')
    recipientContactName = (By.ID, 'recipient_contact_name')
    recipientZip = (By.ID, 'recipient_zip')
    recipientCity = (By.ID, 'recipient_city')
    recipientAddress = (By.ID, 'recipient_address')
    recipientPhone = (By.ID, 'recipient_phone')
    recipientEmail = (By.ID, 'recipient_email')

    # Package Data

    isBrittle = (By.ID, 'is_brittle')
    packageNumber = (By.ID, 'package_number')
    allPackageSame = (By.ID, 'all_package_same')
    deliveryAmount = (By.ID, 'cash_on_delivery_amount')
    packageValue = (By.ID, 'package_value')
    bankAccountNumber = (By.ID, 'bank_account_number')
    payer = (By.ID, 'payer')
    documentReturn = (By.ID, 'document_return')
    publicComment = (By.ID, 'public_comment')
    privateComment = (By.ID, 'private_comment')

    # Price Calculator

    priceCalculatorBtn = (By.XPATH, '//*[@id="root"]/div[2]/form/div[3]/div[3]/div[2]/div/div[1]/span')

    # Invoice

    differentInvoiceAddress = (By.ID, 'different_invoice_address')

    # Accept Terms

    acceptTerms = (By.ID, 'accept_terms')