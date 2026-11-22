import re

from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect


class WWS_Financial_Institutions:
    PAGE_PATH = "/who-we-serve/financial-institutions"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.page_url = f"{base_url.rstrip('/')}{self.PAGE_PATH}"
        self.page_heading = page.get_by_role(
            "heading", name="Financial Institutions", exact=True
            )
        page_subheading = self.page.get_by_role(
            "heading", name="Protecting the financial institutions that protect our economy.", exact=True
            )

    def open_page(self):
        self.page.goto(self.page_url)
        self.page.wait_for_load_state("networkidle")


    def verify_page_loaded(self):
        expect(self.page).to_have_url(re.compile(re.escape(self.PAGE_PATH) + r"/?$"))
        expect(self.page_heading).to_be_visible()

    def verify_page_title(self):
        expect(self.page).to_have_title("Financial Institutions | Old Republic Professional")

    def verify_page_heading_and_subheading(self):
        expect(self.page_heading).to_be_visible()
        expect(self.page_heading).to_have_text("Financial Institutions")
        expect(self.page_subheading).to_be_visible()




