import re

from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect

class WWS_Private_Companies:
    PAGE_PATH = "en/who-we-serve/private-companies"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.page_url = f"{base_url.rstrip('/')}{self.PAGE_PATH}"
        self.page_heading = page.get_by_role(
            "heading", name="Private Companies", exact=True
        )


    def open_page(self):
        self.page.goto(self.page_url)
        self.page.wait_for_load_state("networkidle")


    def verify_page_loaded(self):
        expect(self.page).to_have_url(re.compile(re.escape(self.PAGE_PATH) + r"/?$"))
        expect(self.page_heading).to_be_visible()
        

