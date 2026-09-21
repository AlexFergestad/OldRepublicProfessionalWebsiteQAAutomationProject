from playwright.sync_api import Page, expect


class Public_Company_Excess_Side_A:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")

        self.excess_side_a_page = self.header_nav.get_by_role("menuitem", name="Excess Side-A Only")

    def navigate_to_excess_side_a_page(self):
        self.page.wait_for_timeout(1000)
        self.excess_side_a_page.hover()
        self.excess_side_a_page.click()
        self.page.wait_for_load_state("networkidle")

    def verify_page_title_and_headers(self):


