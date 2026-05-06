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

# """TC-02: Verify H1 Title and Who We Are Paragraph"""
# @pytest.mark.ui
# @pytest.mark.public_companies_directors_and_officers_liability_page
# def test_who_we_are_paragraph(page: Page, base_url):
#     # Goes to the home page
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks the D&O link from the Public Companies overview page object
#     public_companies_page = Public_Company_Liability_Overview(page, base_url)
#     public_companies_page.go_to_subpage(public_companies_page.directors_officers_link)

#     # Verifies the Title
#     Public_Company_Dando_Liability(page).verify_title()

#     # Verifies the "Who We Are" paragraph
#     Public_Company_Dando_Liability(page).verify_who_we_are()

# """TC-03: Verify What We Offer Section"""
# @pytest.mark.ui
# @pytest.mark.public_companies_directors_and_officers_liability_page
# def test_verify_what_we_offer_section(page: Page, base_url):
#     # Goes to the home page
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks the D&O link from the Public Companies overview page object
#     public_companies_page = Public_Company_Liability_Overview(page, base_url)
#     public_companies_page.go_to_subpage(public_companies_page.directors_officers_link)
    
#     # Verifies the What We Offer Paragraph
#     Public_Company_Dando_Liability(page).verify_what_we_offer()

"""TC-04: Verify Public Companies Section on the Right"""
@pytest.mark.ui
@pytest.mark.public_companies_first_page
def test_public_companies_right_section(page: Page, base_url):
    """Verify Public Companies Section on the Right"""
        
    # Navigate to the home page
    page.goto(base_url)

    # Click on the Public Companies menu item to navigate to the public companies page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Wait for the public companies page to load
    page.wait_for_load_state("networkidle")

    # Verify the right section of the public companies page
    public_companies = Public_Company_Liability_Overview(page, base_url)

    # Verify the links in the right section go to the correct pages and have the correct titles
    public_companies.verify_public_companies_right_section()
    

# Finished TC-04, do md file for it then verify performance and accessibility for the directors and officers public companies page.