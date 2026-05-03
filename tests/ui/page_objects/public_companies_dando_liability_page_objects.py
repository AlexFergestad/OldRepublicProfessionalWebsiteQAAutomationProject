from playwright.sync_api import Page, expect

from conftest import page
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
        self.who_we_are = page.locator("h2").first
        self.what_we_offer = page.locator("h2").nth(1)
        self.consistency_heading = page.locator("h3").filter(has_text="Consistency:")
        self.consistency_list = page.locator("ul").filter(has_text="40 years of D&O underwriting")
        self.experienced_underwriting_staff = page.locator("h3").filter(has_text="Experienced:")
        self.experienced_underwriting_list = page.locator("ul").filter(has_text="Empowered to be decisional")

    
    def navigate_to_directors_and_officers_liability_page(self):
        self.dAndOPage.click()
        self.page.wait_for_load_state("networkidle")
    
    def verify_title(self):
        expect(self.page_title_locator).to_have_text("Directors & Officers Liability")

    def verify_who_we_are(self):
        expect(self.who_we_are).to_have_text("Who We Are:")
        expect(self.who_we_are_paragraph).to_be_visible()

    def verify_what_we_offer(self):
        expect(self.what_we_offer).to_have_text("What We Offer:")
        expect(self.consistency_heading).to_be_visible()
        expect(self.consistency_list).to_be_visible()
        expect(self.experienced_underwriting_staff).to_have_text("Experienced:")
        expect(self.experienced_underwriting_staff).to_be_visible()
        
