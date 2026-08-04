import re

from playwright.sync_api import Page, expect


class Public_Company_Excess_Liability:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
        self.excess_liability_page = self.header_nav.get_by_role("menuitem", name="Excess Liability")
        self.policy_features = page.locator("h2").filter(has_text="Policy features")
        self.policy_features_list = page.locator("h2").filter(has_text="Policy features").locator("xpath=following-sibling::ul[1]")

        self.h1 = page.locator("h1").first
        self.h1_paragraph = page.locator("h1 + p")
        self.capacity = page.locator("p").filter(has_text="Capacity:")
        self.attachment = page.locator("p").filter(has_text="Attachment:")
        self.eligibility = page.locator("p").filter(has_text="Eligibility:")
        self.download_excess_do_sell_sheet = page.get_by_role("link", name="Download Excess D&O Sell Sheet")

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

        bullet_point_texts = [
            "One-page",
            "Market-leading erosion language",
            "Shareholder Derivative Demand Investigations",
            "Excess Flex™"
        ]

        for text in bullet_point_texts:
            expect(self.policy_features_list).to_contain_text(text)


    def verify_capacity_attachment_eligibility_and_download_button(self):
        expect(self.capacity).to_be_visible(timeout=5000)
        expect(self.attachment).to_be_visible(timeout=5000)
        expect(self.eligibility).to_be_visible(timeout=5000)
        expect(self.download_excess_do_sell_sheet).to_be_visible(timeout=5000)
        self.download_excess_do_sell_sheet.click()
        self.page.wait_for_timeout(5000)

        
