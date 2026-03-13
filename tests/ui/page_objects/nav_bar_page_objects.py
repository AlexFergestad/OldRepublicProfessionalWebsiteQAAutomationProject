"""Page Object Model for Navigation Menu"""

from playwright.sync_api import Page, expect


class NavigationMenu:
    """Page Object for the main navigation menu"""
    
    def __init__(self, page: Page):
        self.page = page