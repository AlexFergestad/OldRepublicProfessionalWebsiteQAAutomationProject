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
    
    def navigate_to_nav_bar_item(self, item_name: str):
        """Navigate to a specific navigation item by name"""
        item_name = item_name.lower()
        if item_name == "public companies":
            self.public_companies_link.click()
        elif item_name == "private companies":
            self.private_companies_link.click()
        elif item_name == "law firms":
            self.law_firms_link.click()
        elif item_name == "financial institutions":
            self.financial_institutions_link.click()
        elif item_name == "commercial crime":
            self.commercial_crime_link.click()
        else:
            raise ValueError(f"Navigation item '{item_name}' not found in the navigation menu.")
        
        self.page.wait_for_load_state("networkidle")

    def open_dropdown(self, dropdown_option: str, option: str):
        """Open a dropdown menu by name"""
        
        self.page.wait_for_timeout(500)  # Wait for the dropdown to be interactable

        # To highliht the dropdown option, we can use the get_by_role method to find the dropdown menu item and click it
        dropdown_option.click()

        self.page.wait_for_timeout(500)  # Wait for the dropdown to open