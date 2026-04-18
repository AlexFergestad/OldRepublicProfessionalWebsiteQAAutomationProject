from playwright.sync_api import Page, expect

from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_page_objects import Public_Company_Liability_Overview

class Public_Company_Dando_Liability:
    def __init__(self, page: Page):
        self.page = page

        self.page_title_locator = page.locator("h1")
        self.page_url = "/business-insurance-public-company/directors-and-officers-liability"
        self.dAndOPage = page.get_by_role("menuitem", name="Directors and Officers Liability")
    
    def navigate_to_directors_and_officers_liability_page(self):
        self.dAndOPage.click()
        self.page.wait_for_load_state("networkidle")