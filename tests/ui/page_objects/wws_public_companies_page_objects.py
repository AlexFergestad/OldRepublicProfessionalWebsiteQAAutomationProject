import re

from playwright.sync_api import Page, expect


class WWS_Public_Companies:
    PAGE_PATH = "/who-we-serve/public-companies"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.page_url = f"{base_url.rstrip('/')}{self.PAGE_PATH}"
        self.page_heading = page.get_by_role(
            "heading", name="Public Companies", exact=True
        )
        self.introductory_content = page.locator(
            ".pwr-sec-txt__content--top"
        ).filter(has_text="Public companies operate in a complex environment")
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
            "Public companies operate in a complex environment shaped by volatile "
            "financial markets, economic uncertainty, evolving regulations, "
            "technological disruption, and shifting social expectations."
        )
        expect(self.introductory_paragraph_right).to_have_text(
            "Executives must navigate heightened scrutiny from shareholders, "
            "regulators, customers, employees, and other stakeholders. Even "
            "well-managed organizations employing the most robust risk management "
            "practices may face allegations resulting in distraction, expense and "
            "reputational harm. Aligning with a stable Management Liability "
            "insurance provider plays a critical role in helping safeguard "
            "leadership against potential financial and reputational exposures."
        )
