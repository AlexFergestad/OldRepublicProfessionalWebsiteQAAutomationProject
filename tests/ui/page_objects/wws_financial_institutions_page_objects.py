import re

from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect


class WWS_Financial_Institutions:
    PAGE_PATH = "/who-we-serve/financial-institutions"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.page_url = f"{base_url.rstrip('/')}{self.PAGE_PATH}"
        self.page_heading = page.get_by_role("heading", name="Financial Institutions", level=1)
        self.page_subheading = page.locator("strong").filter(has_text="Specialized underwriting for financial institutions")
        self.intro_paragraph_left = page.locator("span").filter(
            has_text="Old Republic Professional's dedicated Financial Institutions team"
            ).last

        self.intro_paragraph_right = page.locator("div.pwr-sec-txt__right").filter(
            has_text="Backed by decades of underwriting expertise"

        # Tile locators
        self.investpro_paragraph = page.get_by_role("heading", name="InvestPRO", exact=True).locator("xpath=following-sibling::p[1]")
        self.view_investpro_coverage_details_button = page.get_by_role("button", name="View InvestPro Coverage Details", exact=True)
        self.do_paragraph = page.get_by_role("heading", name="Directors & Officers Liability", exact=True).locator("xpath=following-sibling::p[1]")
        self.view_do_coverage_details_button = page.get_by_role("button", name="View D&O Coverage Details", exact=True)
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

    def verify_intro_paragraphs(self):
        expect(self.intro_paragraph_left).to_be_visible()
        expect(self.intro_paragraph_right).to_be_visible()


    def verify_coverage_area_tiles(self):
        
        # InvestPRO Tile
        expect(self.investpro_paragraph).to_be_visible()
        expect(self.investpro_paragraph).to_contain_text("InvestPRO is a comprehensive management and professional liability solution")
        expect(self.investpro_paragraph).to_contain_text("InvestPRO serves investment advisers, asset managers, hedge funds")

        expect(self.view_investpro_coverage_details_button).to_be_visible()
        expect(self.view_investpro_coverage_details_button).to_have_text("View InvestPro Coverage Details")
        expect(self.view_investpro_coverage_details_button).to_have_attribute(
            "href", "https://www.orprofessional.com/coverages/solutions/investpro"
        )
        self.view_investpro_coverage_details_button.click()
        expect(self.page).to_have_url("https://www.orprofessional.com/coverages/solutions/investpro")
        self.page.go_back()

        # Directors & Officers Liability Tile
        expect(self.do_paragraph).to_be_visible()
        expect(self.do_paragraph).to_contain_text("provides D&O coverage for financial institutions on a primary and excess basis")
        expect(self.do_paragraph).to_contain_text("admitted and non-admitted paper")
        expect(self.do_paragraph).to_contain_text("standalone management liability placement")
        expect(self.view_do_coverage_details_button).to_be_visible()
        expect(self.view_do_coverage_details_button).to_have_text("View D&O Coverage Details")
        expect(self.view_do_coverage_details_button).to_have_attribute(
            "href", "https://www.orprofessional.com/coverages/directors-and-officers-liability"
        )

        self.view_do_coverage_details_button.click()
        expect(self.page).to_have_url("https://www.orprofessional.com/coverages/directors-and-officers-liability")
        self.page.go_back()

