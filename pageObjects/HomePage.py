from selenium.webdriver.common.by import By

from pageObjects.searchOutcome import SearchOutcome


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    topHun = (By.XPATH, "//a[normalize-space()='TOP 100']")


    def top100Item(self):
        self.driver.find_element(*HomePage.topHun).click()
        checkoutPage = SearchOutcome(self.driver)
        return checkoutPage


