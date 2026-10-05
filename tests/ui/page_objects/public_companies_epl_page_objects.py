
from playwright.async_api import Page


def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.header_nav = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu")
        self.epl_page = self.header_nav.get_by_role("menuitem", name="Employment-Practices Liability")

def navigate_to_epl_page(self):
        self.page.wait_for_timeout(1000)
        self.epl_page.hover()
        self.epl_page.click()
        self.page.wait_for_load_state("networkidle")