import re

from playwright.sync_api import Page, expect


class WWS_Public_Companies:
    PAGE_PATH = "/who-we-serve/public-companies"
    OTHER_SEGMENTS = {
        "Private Companies": "/en/who-we-serve/private-companies",
        "Financial Institutions": "/who-we-serve/financial-institutions",
        "Not-for-Profit Entities": "/who-we-serve/not-for-profit-entities",
    }
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
        self.connect_with_us_heading = page.get_by_role(
            "heading",
            name=re.compile(r"^Connect with Us$", re.IGNORECASE),
            level=2,
        )
        self.view_public_company_underwriters_button = page.get_by_role(
            "button",
            name=re.compile(r"^View public company underwriters$", re.IGNORECASE),
        )
        self.other_segments_heading = page.get_by_role(
            "heading", name="Other Segments We Serve", exact=True
        )
        self.other_segment_links = {
            name: page.get_by_role(
                "link",
                name=re.compile(
                    rf"^{re.escape(name)}.*View Segment$", re.IGNORECASE
                ),
            )
            for name in self.OTHER_SEGMENTS
        }

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

    def verify_connect_with_us_underwriters_button(self):
        underwriters_path = r"/team/?\?filter=public-company-underwriters(?:&|$)"
        expect(self.connect_with_us_heading).to_be_visible()
        expect(self.connect_with_us_heading).to_have_text(
            re.compile(r"^Connect with Us$", re.IGNORECASE)
        )
        expect(self.view_public_company_underwriters_button).to_be_visible()
        expect(self.view_public_company_underwriters_button).to_have_text(
            re.compile(r"^View public company underwriters$", re.IGNORECASE)
        )
        expect(self.view_public_company_underwriters_button).to_have_attribute(
            "href", re.compile(underwriters_path)
        )
        self.view_public_company_underwriters_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(underwriters_path))

    def verify_other_segments_we_serve_and_buttons_underneath(self):
        expect(self.other_segments_heading).to_be_visible()
        expect(self.other_segments_heading).to_have_text("Other Segments We Serve")

        for index, (name, path) in enumerate(self.OTHER_SEGMENTS.items()):
            segment_link = self.other_segment_links[name]
            segment_path = re.escape(path) + r"/?$"

            expect(segment_link).to_be_visible()
            expect(segment_link).to_contain_text(name)
            expect(segment_link).to_contain_text(
                re.compile(r"View Segment", re.IGNORECASE)
            )
            expect(segment_link).to_have_attribute("href", re.compile(segment_path))
            segment_link.click()
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.page).to_have_url(re.compile(segment_path))

            if index < len(self.OTHER_SEGMENTS) - 1:
                self.open_page()
