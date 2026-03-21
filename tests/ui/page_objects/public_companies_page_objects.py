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
        # Verify the heading text
        expect(self.page_heading).to_have_text("Public Company Liability Overview")

        # Verify the first paragraph contains expected text
        expect(self.overview_paragraphs.nth(0)).to_contain_text("Old Republic Professional has provided Directors and Officers liability insurance without interruption for 40 years on both a primary and an excess basis, and currently ranks among the nation's top 20 underwriters of D&O insurance. The company serves all industry sectors, and is a leader "
        "in technology, biotechnology, and life science firms, currently insuring 50 percent of the NASDAQ 100 Index and 60 percent of the NASDAQ Biotechnology Index.")