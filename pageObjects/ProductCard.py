from selenium.webdriver.common.by import By


class ProductCard:
    def __init__(self, driver):
        self.driver = driver

    details = (By.XPATH, "//span[@title='Dane szczegółowe']")
    addToCart = (By.XPATH, "//button[@data-title='Dodano do koszyka']")
    goToCheckout = (By.XPATH, "//button[contains(text(),'Przejdź do koszyka')]")

    def getCheckOut(self):

        #dodanie do koszyka dziala
        return self.driver.find_element(*ProductCard.addToCart)

    def goToCheckOut(self):
        return self.driver.find_element(*ProductCard.goToCheckout)
