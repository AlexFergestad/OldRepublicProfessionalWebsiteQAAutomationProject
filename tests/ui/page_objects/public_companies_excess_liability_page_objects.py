import re

from playwright.sync_api import Page, expect


class Public_Company_Excess_Liability:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
        self.excess_liability_page = self.header_nav.get_by_role("menuitem", name="Excess Liability")
        self.policy_features = page.locator("h2").first
        self.policy_features_bullet_point_top = page.locator()

        self.h1 = page.locator("h1").first
        self.h1_paragraph = page.locator("h1 + p")


    def navigate_to_excess_liability_page(self):
        self.excess_liability_page.click()
        self.page.wait_for_load_state("networkidle")

    def verify_excess_liability_h1(self):
        expect(self.h1).to_be_visible(timeout=5000)
        self.page.wait_for_load_state("networkidle")

    def verify_h1_paragraph(self):
        expect(self.h1_paragraph).to_be_visible(timeout=5000)
        self.page.wait_for_load_state("networkidle")

    def verify_policy_features(self):
        expect(self.policy_features).to_be_visible(timeout=5000)
        # Grab text once — used for both assertions and return value
        content = self.policy_features.text_content()
                
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
