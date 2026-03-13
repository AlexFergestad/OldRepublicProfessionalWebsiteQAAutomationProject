"""Page Object Model for Navigation Menu"""

from playwright.sync_api import Page, expect


class NavigationMenu:
    """Page Object for the main navigation menu"""
    
    def __init__(self, page: Page):
        self.page = page

        # Main navigation item locators
        self.public_companies_link = page.get_by_role("menuitem", name="Public Companies").first
        self.private_companies_link = page.get_by_role("menuitem", name="Private Companies").first
        self.law_firms_link = page.get_by_role("menuitem", name="Law Firms").first
        self.financial_institutions_link = page.get_by_role("menuitem", name="Financial Institutions").first
        self.commercial_crime_link = page.get_by_role("menuitem", name="Commercial Crime").first