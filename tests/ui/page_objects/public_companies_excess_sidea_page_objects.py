from playwright.sync_api import Page, expect


class Public_Company_Excess_Side_A:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")

        self.excess_side_a_page = self.header_nav.get_by_role("menuitem", name="Excess Side-A Only")
