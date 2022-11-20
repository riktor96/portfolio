from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductCard import ProductCard
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        #inicjowanie loggera
        log = self.getLogger()
        #tworzenie obiektów
        homePage = HomePage(self.driver)
        checkoutPage = homePage.top100Item()
        log.info("Getting all product cards")
        productCard = ProductCard(self.driver)
        log.info("Getting checkout")
        goToDeliveryMethod = CheckOutPage(self.driver)

        #klikanie
        # karty w bestsellerach na listingu
        cards = checkoutPage.getCardTitle()
        # wejście w pierwszy wynik w bestsellerach
        log.info("Wejście w karty")
        log.info(cards[0])
        cards[0].click()
        productCard.getCheckOut().click()
        productCard.goToCheckOut()
        #przejscie do checkout
        log.info("Wejście w checkout")
        productCard.goToCheckOut().click()
        #dodaj proponowany produkt do koszyka
        self.driver.execute_script("window.scrollTo(0, 600)")
        goToDeliveryMethod.addPromotedProductToCart()
        #przejdz do wpisania adresu
        goToDeliveryMethod.getMethodOfDelivery().click()

        goToDeliveryMethod.chooseDeliveryMethod()
