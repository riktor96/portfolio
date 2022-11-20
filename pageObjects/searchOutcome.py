from selenium.webdriver.common.by import By


class SearchOutcome:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".search-content > .search-list-item")
    #  > .search-list-item:first-child

    def getCardTitle(self):
        # print(self.driver.find_elements(CheckoutPage.cardTitle))
        return self.driver.find_elements(*SearchOutcome.cardTitle)