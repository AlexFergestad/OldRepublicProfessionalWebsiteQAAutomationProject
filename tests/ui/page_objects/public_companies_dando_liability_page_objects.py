from playwright.sync_api import Page, expect

from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_page_objects import Public_Company_Liability_Overview

class Public_Company_Dando_Liability:
    def __init__(self, page: Page):
        self.page = page

        self.page_title_locator = page.locator("h1")
        self.page_url = "/business-insurance-public-company/directors-and-officers-liability"
        self.dAndOPage = page.locator("#hs_menu_wrapper_module_1527184808535133_mjfm_header_main_menu").get_by_role("menuitem", name="Directors and Officers Liability")
        self.who_we_are_paragraph = page.locator("p").filter(has_text="established in December 1983")
    
    def navigate_to_directors_and_officers_liability_page(self):
        self.dAndOPage.click()
        self.page.wait_for_load_state("networkidle")
    
    def verify_title(self):
        expect(self.page_title_locator).to_have_text("Directors and Officers Liability")

    def verify_who_we_are(self):
        expect(self.who_we_are_paragraph).to_be_visible()