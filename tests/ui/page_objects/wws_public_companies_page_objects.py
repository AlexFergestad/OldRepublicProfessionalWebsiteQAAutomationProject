import re

from playwright.sync_api import Page, expect


class WWS_Public_Companies:
    PAGE_PATH = "/who-we-serve/public-companies"
    D_AND_O_COVERAGE_DESCRIPTIONS = {
        "Public Primary D&O": "First-layer D&O coverage for publicly traded companies.",
        "Lead Side-A": "Dedicated Side-A coverage for non-indemnifiable loss.",
        "Excess D&O": "Additional capacity above underlying public company D&O.",
        "Excess Side-A": "Additional Side-A limits for layered public company programs.",
    }

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
        self.d_and_o_coverage_details_button = page.locator(
            "a.cta_button"
        ).filter(has_text=re.compile(r"^VIEW D&O COVERAGE DETAILS$", re.IGNORECASE))
        self.d_and_o_coverage_cards = {
            name: page.get_by_role("heading", name=name, exact=True).locator("xpath=..")
            for name in self.D_AND_O_COVERAGE_DESCRIPTIONS
        }
        self.epl_coverage_card = self.coverage_card("Employment Practices Liability")
        self.epl_coverage_details_button = self.epl_coverage_card.locator(
            "a.cta_button"
        )
        self.fiduciary_coverage_card = self.coverage_card("Fiduciary Liability")
        self.fiduciary_coverage_details_button = (
            self.fiduciary_coverage_card.locator("a.cta_button")
        )
        self.excess_coverage_card = self.coverage_card("Excess")
        self.excess_coverage_details_button = self.excess_coverage_card.locator(
            "a.cta_button"
        )
        self.crime_fidelity_coverage_card = self.coverage_card("Crime/Fidelity")
        self.crime_fidelity_coverage_details_button = (
            self.crime_fidelity_coverage_card.locator("a.cta_button")
        )

    def coverage_card(self, heading: str):
        return self.page.get_by_role(
            "heading", name=heading, exact=True
        ).locator(
            "xpath=ancestor::div[contains(@class, 'pwr-adc__content-wrapper')][1]"
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

    def verify_d_and_o_coverage_details_button(self):
        coverage_path = "/coverages/directors-and-officers-liability"
        expect(self.d_and_o_coverage_details_button).to_be_visible()
        expect(self.d_and_o_coverage_details_button).to_have_attribute(
            "href", re.compile(re.escape(coverage_path) + r"/?$")
        )
        self.d_and_o_coverage_details_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(
            re.compile(re.escape(coverage_path) + r"/?$")
        )

    def verify_d_and_o_coverage_descriptions(self):
        for name, description in self.D_AND_O_COVERAGE_DESCRIPTIONS.items():
            card = self.d_and_o_coverage_cards[name]
            expect(card.get_by_role("heading", name=name, exact=True)).to_be_visible()
            expect(card).to_contain_text(description)

    def verify_epl_coverage_details(self):
        coverage_path = "/coverages/employment-practices-liability"
        expect(
            self.epl_coverage_card.get_by_role(
                "heading", name="Employment Practices Liability", exact=True
            )
        ).to_be_visible()
        expect(self.epl_coverage_details_button).to_be_visible()
        expect(self.epl_coverage_details_button).to_have_text(
            re.compile(r"^VIEW EPL COVERAGE DETAILS$", re.IGNORECASE)
        )
        expect(self.epl_coverage_details_button).to_have_attribute(
            "href", re.compile(re.escape(coverage_path) + r"/?$")
        )
        self.epl_coverage_details_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(re.escape(coverage_path) + r"/?$"))

    def verify_fiduciary_coverage_details(self):
        coverage_path = "/coverages/fiduciary-liability"
        expect(
            self.fiduciary_coverage_card.get_by_role(
                "heading", name="Fiduciary Liability", exact=True
            )
        ).to_be_visible()
        expect(self.fiduciary_coverage_details_button).to_be_visible()
        expect(self.fiduciary_coverage_details_button).to_have_text(
            re.compile(r"^VIEW FIDUCIARY COVERAGE DETAILS$", re.IGNORECASE)
        )
        expect(self.fiduciary_coverage_details_button).to_have_attribute(
            "href", re.compile(re.escape(coverage_path) + r"/?$")
        )
        self.fiduciary_coverage_details_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(re.escape(coverage_path) + r"/?$"))

    def verify_excess_coverage_details(self):
        coverage_path = "/coverages/solutions/excess"
        expect(
            self.excess_coverage_card.get_by_role(
                "heading", name="Excess", exact=True
            )
        ).to_be_visible()
        expect(self.excess_coverage_details_button).to_be_visible()
        expect(self.excess_coverage_details_button).to_have_text(
            re.compile(r"^VIEW EXCESS COVERAGE DETAILS$", re.IGNORECASE)
        )
        expect(self.excess_coverage_details_button).to_have_attribute(
            "href", re.compile(re.escape(coverage_path) + r"/?$")
        )
        self.excess_coverage_details_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(re.escape(coverage_path) + r"/?$"))

    def verify_crime_fidelity_coverage_details(self):
        coverage_path = "/coverages/crime-and-fidelity"
        expect(
            self.crime_fidelity_coverage_card.get_by_role(
                "heading", name="Crime/Fidelity", exact=True
            )
        ).to_be_visible()
        expect(self.crime_fidelity_coverage_details_button).to_be_visible()
        expect(self.crime_fidelity_coverage_details_button).to_have_text(
            re.compile(r"^VIEW CRIME/FIDELITY COVERAGE DETAILS$", re.IGNORECASE)
        )
        expect(self.crime_fidelity_coverage_details_button).to_have_attribute(
            "href", re.compile(re.escape(coverage_path) + r"/?$")
        )
        self.crime_fidelity_coverage_details_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(re.escape(coverage_path) + r"/?$"))
