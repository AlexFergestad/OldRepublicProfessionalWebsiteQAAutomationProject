import re

from playwright.sync_api import Page, expect

class Public_Company_Products:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.productsPage = page.locator() 
        self.url = f"{base_url}/business-insurance-public-company/directors-and-officers-liability/products"

    def navigate_to_products_page(self):
        self.dAndOPage.click()
        self.page.wait_for_load_state("networkidle")