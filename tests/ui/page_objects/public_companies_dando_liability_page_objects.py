
from playwright.sync_api import Page, expect

from conftest import page

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_page_objects import Public_Company_Liability_Overview

class Public_Company_Dando_Liability_Page:
    def __init__(self):
        # Locators for the Directors and Officers Liability page
        self.page_title_locator = "h1"
        self.page_url = "/public-companies/directors-and-officers-liability"
        self.dAndOPage = page.locatorpage.locator("a[href='/business-insurance-public-company/directors-and-officers-liability'][role='menuitem']")
    
    def navigate_to_directors_and_officers_liability_page(self, page: Page):

        # Clicks on the Directors and Officers Liability card to navigate to the directors and officers liability page
        