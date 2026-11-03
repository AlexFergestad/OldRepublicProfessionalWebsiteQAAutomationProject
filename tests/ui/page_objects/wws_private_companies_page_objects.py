import re

from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect

class WWS_Private_Companies:
    PAGE_PATH = "/en/who-we-serve/private-companies"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.page_url = f"{base_url.rstrip('/')}{self.PAGE_PATH}"
        self.page_heading = page.get_by_role(
            "heading", name="Private Companies", exact=True
        )
        self.introductory_content = page.locator(
            ".pwr-sec-txt__content--top"
        ).filter(has_text="Old Republic Professional’s dedicated private company team")
        self.introductory_paragraph_left = self.introductory_content.locator(
            ".pwr-sec-txt__left"
        )
        self.introductory_paragraph_right = self.introductory_content.locator(
            ".pwr-sec-txt__right"
        )

    def open_page(self):
        self.page.goto(self.page_url)
        self.page.wait_for_load_state("networkidle")


    def verify_page_loaded(self):
        expect(self.page).to_have_url(re.compile(re.escape(self.PAGE_PATH) + r"/?$"))
        expect(self.page_heading).to_be_visible()
        
    def verify_introductory_paragraphs(self):
        expect(self.introductory_paragraph_left).to_have_text(
            "Old Republic Professional’s dedicated private company team focuses on "
            "the management liability exposures facing private companies with different "
            "ownership structures and business needs."
        )
        expect(self.introductory_paragraph_right).to_have_text(
            "Backed by deep underwriting expertise and claims "
            "experience, we provide management liability coverage with the flexibility "
            "to structure protection for each organization’s needs."
        )
    
    def verify_orprotect_coverage_details(self):



        