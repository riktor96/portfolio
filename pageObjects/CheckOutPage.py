import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    elementInCarouselBtn = (By.XPATH, "//div[@id='more-products']//button[@type='submit']")
    deliveryBtn = (By.XPATH, "//a[text()='Wybierz sposób dostawy']")
    nonRegisteredBtn = (By.XPATH, "//a[text()='ZAMÓW BEZ REJESTRACJI']")
    emailInput = (By.XPATH, "//input[@type='email']")
    addEmailBtn = (By.XPATH, "//button[@type='submit']")
    methodOfDeliveryStore = (By.XPATH, "//div[data-ta='STORE']")

    #dodaj do koszyka element z polecanych
    def addPromotedProductToCart(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*CheckOutPage.elementInCarouselBtn).click()

    #przejdz do sposobów dostawy
    def getMethodOfDelivery(self):
        #klikniecie w wybierz sposob dostawy
        self.driver.find_element(*CheckOutPage.deliveryBtn).click()
        #zamow bez rejestracji
        self.driver.find_element(*CheckOutPage.nonRegisteredBtn).click()
        self.driver.find_element(*CheckOutPage.emailInput).send_keys("wiktor@testEmaW.com")
        return self.driver.find_element(*CheckOutPage.addEmailBtn)

    def test_fillData(self):
        # WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Testowy")
        self.driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Czeslaw")
        self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("589777999")
        self.driver.find_element(By.XPATH, "//input[@name='street']").send_keys("Testowa")
        self.driver.find_element(By.XPATH, "//input[@name='buildingNumber']").send_keys("5")
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='__-___']").click()
        self.driver.find_element(By.XPATH, "//input[@name='zipCode']").send_keys("25-028")



    def chooseDeliveryMethod(self):
        self.driver.find_element(By.XPATH, "//div[text()='odbiór w punkcie - Empik']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Wpisz miejscowość lub kod pocztowy']").send_keys('Kielce')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//p[normalize-space()='Kielce Echo (SP)']").click()
        #uzupelnienie danych
        CheckOutPage.test_fillData(self)
        self.driver.execute_script("window.scrollTo(0, 800)")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

