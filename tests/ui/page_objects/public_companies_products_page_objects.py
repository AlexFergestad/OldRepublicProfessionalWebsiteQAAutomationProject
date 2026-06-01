import re

from playwright.sync_api import Page, expect

class Public_Company_Products:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.productsPage = page.get_by_role("menuitem", name="Products") 
        self.url = f"{base_url}/business-insurance-public-company/directors-and-officers-liability/products"
        self.products_h1 = page.locator("h1")

    def navigate_to_products_page(self):
        self.productsPage.click()
        self.page.wait_for_load_state("networkidle")

    def verify_products_h1(self):
        expect(self.products_h1).to_have_text("Public Company Directors & Officers Liability Underwriting Products")
        expect(self.products_h1).to_be_visible()