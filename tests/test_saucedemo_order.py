import time

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage

def test_saucedemo_order(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_products_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_form("Vitalij", "Filipov", "12345")

    overview = CheckoutOverviewPage(driver)
    total = overview.get_total_price()

    print(f"🔥 Итоговая сумма: {total}")

    time.sleep(5)

    assert total == "Total: $58.29"
