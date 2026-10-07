
from playwright.async_api import Page, expect


class Employment_Practices_Liability:
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

        def verify_page_title_and_headers(self):
                # Verifies that the page has the correct title and headers
                expect(self.page).to_have_title("EPL | Employment-Practices | Old Republic Professional")
                expect(self.page.locator("h1")).to_have_text("Employment-Practices Liability")     