import re

from playwright.sync_api import Page, expect


class Who_We_Serve:
    SECTIONS = {
        "Public Companies": {
            "tab": "tab1",
            "path": "/who-we-serve/public-companies",
            "description": "public companies",
        },
        "Private Companies": {
            "tab": "tab2",
            "path": "/en/who-we-serve/private-companies",
            "description": "private companies",
        },
        "Financial Institutions": {
            "tab": "tab3",
            "path": "/who-we-serve/financial-institutions",
            "description": "financial institutions",
        },
        "Not-for-Profit Entities": {
            "tab": "tab4",
            "path": "/who-we-serve/not-for-profit-entities",
            "description": "not-for-profit organizations",
        },
    }

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.connect_with_us_heading = page.get_by_role(
            "heading",
            name=re.compile(r"^Connect With Us$", re.IGNORECASE),
            level=2,
        )
        self.view_our_team_button = page.get_by_role(
            "button", name=re.compile(r"^View Our Team$", re.IGNORECASE)
        )
        self.who_we_serve_navbar_menu = page.get_by_role(
            "menuitem", name="Who We Serve", exact=True
        ).filter(visible=True).first
        self.who_we_serve_dropdown = page.locator(
            ".pwr-header-advanced-mm--is-active"
        )
        self.who_we_serve_navbar_links = {
            section_name: self.who_we_serve_dropdown.get_by_role(
                "link", name=section_name, exact=True
            )
            for section_name in self.SECTIONS
        }

    def section(self, section_name: str):
        if section_name not in self.SECTIONS:
            raise ValueError(f"Unknown Who We Serve section: {section_name}")

        return self.page.locator(".pwr-sec-mockup__content").filter(
            has=self.page.get_by_role("heading", name=section_name, exact=True)
        )

    def activate_section(self, section_name: str):
        if section_name not in self.SECTIONS:
            raise ValueError(f"Unknown Who We Serve section: {section_name}")

        tab = self.page.locator(
            f'.pwr-tabs__item[role="tab"][rel="{self.SECTIONS[section_name]["tab"]}"]'
        )
        expect(tab).to_contain_text(section_name)
        tab.click()
        expect(tab).to_have_attribute("aria-selected", "true")

    def verify_section(self, section_name: str):
        self.activate_section(section_name)
        section = self.section(section_name)
        expect(section.get_by_role("heading", name=section_name, exact=True)).to_be_visible()
        expect(section).to_contain_text(self.SECTIONS[section_name]["description"])

    def verify_connect_with_us_heading(self):
        expect(self.connect_with_us_heading).to_be_visible()
        expect(self.connect_with_us_heading).to_have_text(
            re.compile(r"^Connect With Us$", re.IGNORECASE)
        )

    def verify_view_our_team_button(self):
        expect(self.view_our_team_button).to_be_visible()
        expect(self.view_our_team_button).to_have_attribute(
            "href", re.compile(r"/team/?\?filter=underwriters(?:&|$)")
        )
        self.view_our_team_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(
            re.compile(r"/team/?\?filter=underwriters(?:&|$)")
        )

    def verify_who_we_serve_navbar_links(self):
        section_order = [
            "Public Companies",
            "Private Companies",
            "Financial Institutions",
            "Not-for-Profit Entities",
        ]

        for section_name in section_order:
            self.page.mouse.move(0, 0)
            self.who_we_serve_navbar_menu.hover()
            link = self.who_we_serve_navbar_links[section_name]
            section_path = self.SECTIONS[section_name]["path"]
            expect(link).to_be_visible()
            expect(link).to_have_attribute(
                "href", re.compile(re.escape(section_path) + r"/?$")
            )
            link.click()
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.page).to_have_url(
                re.compile(re.escape(section_path) + r"/?$")
            )

            if section_name in (
                "Public Companies",
                "Financial Institutions",
                "Not-for-Profit Entities",
            ):
                self.page.wait_for_timeout(1000)

    def verify_learn_more_buttons(self):
        for section_name, details in self.SECTIONS.items():
            learn_more = self.section(section_name).get_by_role(
                "button", name=re.compile(r"^learn more$", re.IGNORECASE)
            )
            expect(learn_more).to_be_visible()
            expect(learn_more).to_have_attribute(
                "href", re.compile(re.escape(details["path"]) + r"/?$")
            )

    def click_learn_more(self, section_name: str):
        self.activate_section(section_name)

        learn_more = self.section(section_name).get_by_role(
            "button", name=re.compile(r"^learn more$", re.IGNORECASE)
        )
        expect(learn_more).to_be_visible()
        learn_more.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(
            re.compile(
                re.escape(
                    self.page.evaluate("window.location.origin")
                    + self.SECTIONS[section_name]["path"]
                )
                + r"/?$"
            )
        )
        expect(self.page.locator("h1")).to_have_text(
            re.compile(rf"^{re.escape(section_name)}$", re.IGNORECASE)
        )

    def get_performance_metrics(self):
        self.page.evaluate("window.scrollBy(0, 100)")
        self.page.wait_for_timeout(500)

        return self.page.evaluate("""() => {
            const navigation = performance.getEntriesByType('navigation')[0];
            const paint = performance.getEntriesByType('paint');
            const fcp = paint.find(entry => entry.name === 'first-contentful-paint');
            const lcpEntries = performance.getEntriesByType('largest-contentful-paint');
            const lcp = lcpEntries.length ? lcpEntries[lcpEntries.length - 1] : null;
            const cls = performance.getEntriesByType('layout-shift')
                .reduce((total, entry) => total + (entry.hadRecentInput ? 0 : entry.value), 0);

            return {
                load_time: navigation ? navigation.loadEventEnd - navigation.startTime : null,
                first_contentful_paint: fcp ? fcp.startTime : null,
                largest_contentful_paint: lcp ? lcp.startTime : null,
                cumulative_layout_shift: cls
            };
        }""")
