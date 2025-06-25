from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_price(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text