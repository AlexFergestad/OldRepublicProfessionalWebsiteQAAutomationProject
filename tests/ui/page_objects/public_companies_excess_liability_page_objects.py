import re

from playwright.sync_api import Page, expect


class Public_Company_Excess_Liability:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
        self.excess_liability_page = self.header_nav.get_by_role("menuitem", name="Excess Liability")

        self.h1 = page.locator("h1").first


    def navigate_to_excess_liability_page(self):
        self.excess_liability_page.click()
        self.page.wait_for_load_state("networkidle")

    def verify_excess_liability_h1(self):
        expect(self.h1).to_be_visible(timeout=5000)
        self.page.wait_for_load_state("networkidle")

    def 
