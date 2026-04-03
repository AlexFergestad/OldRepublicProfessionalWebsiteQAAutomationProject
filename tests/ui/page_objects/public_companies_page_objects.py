import re

from playwright.sync_api import Page, expect

class Public_Company_Liability_Overview:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.url = f"{base_url}/business-insurance-public-company"
        
        # Text Locators
        self.page_heading = page.locator("h1").first
        self.overview_paragraphs = page.locator("div.constrain > p")

        # Scope to header nav first — must come before any locators that depend on it
        self.header_nav = self.page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")

        self.public_companies_menu = self.header_nav.locator("a[aria-haspopup='true'][href*='business-insurance-public-company']").first

        # Public Companies submenu items
        self.directors_officers_link = self.header_nav.get_by_role("menuitem", name="Directors and Officers Liability").first
        self.products_link = self.header_nav.get_by_role("menuitem", name="Products").first
        self.excess_liability_link = self.header_nav.get_by_role("menuitem", name="Excess Liability").first
        self.lead_side_a_link = self.header_nav.get_by_role("menuitem", name="Lead Side-A Only").first
        self.excess_side_a_link = self.header_nav.get_by_role("menuitem", name="Excess Side-A Only").first
        self.epl_link = self.header_nav.get_by_role("menuitem", name="Employment-Practices Liability").first
        self.epl_loss_prevention_link = self.header_nav.get_by_role("menuitem", name="EPL Loss Prevention").first
        self.fiduciary_liability_link = self.header_nav.get_by_role("menuitem", name="Fiduciary Liability").first
        self.public_companies_underwriters_link = self.header_nav.get_by_role("menuitem", name="Public Companies Underwriters").first

        # Image locator
        self.billboard = self.page.locator(".billboard__underlay")

    
    def navigate(self):
        """Navigate to the Public Companies page"""
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
    
    def verify_page_heading(self):
        """Verify the main page heading"""
        expect(self.page_heading).to_be_visible(timeout=5000)
        expect(self.page_heading).to_have_text("Public-Company Liability Overview")
        
        heading_text = self.page_heading.text_content()
        print(f"✅ Heading: {heading_text}")
        
        return heading_text
    
    def verify_overview_paragraph1(self):
        """Verify overview section paragraphs contain key information"""
        # Verify we have paragraphs
        paragraphs = self.overview_paragraphs.all()
        assert len(paragraphs) >= 4, f"Expected at least 4 paragraphs, found {len(paragraphs)}"
        
        # Get first paragraph
        first_para = self.overview_paragraphs.nth(0)
        expect(first_para).to_be_visible(timeout=5000)

        # Grab text once — used for both assertions and return value
        content = first_para.text_content()
        
        # Verify key facts in first paragraph
        key_facts = [
            "Directors and Officers liability insurance",
            "40 years",
            "NASDAQ 100 Index",
            "60 percent of the NASDAQ Biotechnology Index"
        ]
        
        for fact in key_facts:
            assert fact in content, (
                f"\nKey fact not found: '{fact}'\n"
                f"Content says instead:\n  '{content[:200]}...'"
            )
        
        print(f"✅ Overview paragraphs verified ({len(paragraphs)} paragraphs, {len(key_facts)} key facts)")
        
        return paragraphs

    def verify_overview_paragraph2(self):
        """Verify the second overview paragraph contains key information"""
        second_para = self.overview_paragraphs.nth(1)
        expect(second_para).to_be_visible(timeout=5000)
        
        # Grab text once — used for both assertions and return value
        content = second_para.text_content()

        # Checks for key concepts, not exact wording, this is best practice
        key_facts = [
            "Corporate directors and officers",
            "ever-expanding array of risk",
            "insurance carrier partner"
        ]

        for fact in key_facts:
            assert fact in content, (
                f"\nKey fact not found: '{fact}'\n"
                f"Content says instead:\n  '{content[:200]}...'"
            )

        print(f"✅ Second overview paragraph verified with key facts")
        
        return second_para.text_content()

    def verify_overview_paragraph3(self):
        """Verify the third overview paragraph contains key information"""
        third_para = self.overview_paragraphs.nth(2)
        expect(third_para).to_be_visible(timeout=5000)
        
        # Grab text once — used for both assertions and return value
        content = third_para.text_content()

        # Checks for key concepts, not exact wording, this is best practice
        # Key facts: short, meaningful phrases
        key_facts = [
            "20 years' experience",
            "D&O underwriting",
            "initial public offerings",
            "bankruptcies",
            "turnarounds",
            "public and private company risks"
        ]

        for fact in key_facts:
            assert fact in content, (
                f"\nKey fact not found: '{fact}'\n"
                f"Content says instead:\n  '{content[:200]}...'"
            )


        print(f"✅ Third overview paragraph verified with key facts")
        
        return third_para.text_content()

    def verify_last_part_of_paragraph(self):
        """Verify the last part of the overview section contains key information"""
        section = self.page.get_by_text("Click through to learn more about").locator("..")
        expect(section).to_be_visible(timeout=5000)

        full_content = section.text_content()
        
        # Slice from "Click through" onward — ignore everything above it
        start = full_content.find("Click through")
        content = full_content[start:]

        key_facts = [
            "Click through to learn more about",
            "Public company D&O solutions",
            "Public company\u00a0EPL solutions",
            "Public company\u00a0Fiduciary solutions",
            "Information shown is subject to change",
        ]

        for fact in key_facts:
            assert fact in content, (
                f"\nKey fact not found: '{fact}'\n"
                f"Content says instead:\n  '{content[:200]}...'"
            )

        print(f"✅ Last overview paragraph verified with key facts")
        return content
    
    def verify_heading_and_paragraphs(self):
        """Verify both heading and paragraphs"""
        self.verify_page_heading()
        self.verify_overview_paragraph1()
        self.verify_overview_paragraph2()
        self.verify_overview_paragraph3()
        self.verify_last_part_of_paragraph()
        
        return True

    def verify_top_image(self):
        """Verify the billboard background image is correct"""
        expect(self.billboard).to_be_visible(timeout=5000)

        style = self.billboard.get_attribute("style")
        expected_url = "public-companies-1200x320.jpg"

        assert expected_url in style, (
            f"\nBillboard image not found: '{expected_url}'\n"
            f"Style attribute says instead:\n  '{style}'"
        )

        print(f"✅ Billboard background image verified")
        return style

    def verify_public_companies_right_section(self):
        """Verify the right section of the public companies page contains key information"""

        # Each tuple is (locator, expected URL snippet)
        nav_links = [
            (self.directors_officers_link, "/directors-and-officers-liability"),
            (self.products_link, "/directors-and-officers-liability/products"),
            (self.excess_liability_link, "/excess-liability"),
            (self.lead_side_a_link, "/lead-side-a-only"),
            (self.excess_side_a_link, "/excess-side-a-only"),
            (self.epl_link, "/employment-practices-liability"),
            (self.fiduciary_liability_link, "/fiduciary-liability"),
            (self.public_companies_underwriters_link, "/directors-and-officers-liability/underwriters"),
        ]

        # For each link, hover over the main menu to reveal it, click it, verify URL, then go back
        for link, expected_url in nav_links:
            self.public_companies_menu.hover()
            link.click()
            self.page.wait_for_load_state("networkidle")
            expect(self.page).to_have_url(re.compile(expected_url))
            print(f"✅ Verified navigation to: {expected_url}")
            self.page.go_back()
            self.page.wait_for_load_state("networkidle")
    
    def

    