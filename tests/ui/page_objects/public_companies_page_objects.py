from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

class Public_Company_Liability_Overview:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.page_heading = page.locator("h1").first
    
    def 