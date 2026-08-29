from playwright.async_api import Page


class Public_Company_Lead_Side_A:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
        self.lead_side_a_page = self.header_nav.get_by_role("menuitem", name="Lead Side-A Only")

    def navigate_to_lead_side_a_page(self):
        self.lead_side_a_page.click()
        self.page.wait_for_load_state("networkidle")


