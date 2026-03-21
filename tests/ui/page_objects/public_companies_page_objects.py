from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

class Public_Company_Liability_Overview:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.page_heading = page.locator("h1").first
        
         # All paragraphs in the header section
        self.overview_paragraphs = page.locator("div.constrain > p")
    
    def verify_heading_and_paragraph(self):
        """Verify the heading and paragraph on the public company liability overview page"""
        expect(self.page_heading).to_have_text("Public Company Liability Overview")