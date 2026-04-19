# This file is for automating the testin of the public companies pages in the nav bar.

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_page_objects import Public_Company_Liability_Overview
from tests.ui.page_objects.public_companies_dando_liability_page_objects import Public_Company_Dando_Liability


# """TC-01: Verify that the public companies directors and officers liability page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_directors_and_officers_liability_page
# def test_public_companies_directors_and_officers_liability_page_loads(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")
    
#     # Clicks on the Directors and Officers Liability card to navigate to the directors and officers liability page
#     Public_Company_Dando_Liability(page).navigate_to_directors_and_officers_liability_page()

#     # Waits for the directors and officers liability page to load
#     page.wait_for_load_state("networkidle")

"""Verify H1 Title and Who We Are Paragraph"""
@pytest.mark.ui