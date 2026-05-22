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

# """TC-04: Verify Public Companies Section on the Right"""
# @pytest.mark.ui
# @pytest.mark.public_companies_first_page
# def test_public_companies_right_section(page: Page, base_url):
#     """Verify Public Companies Section on the Right"""
        
#     # Navigate to the home page
#     page.goto(base_url)

#     # Click on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Wait for the public companies page to load
#     page.wait_for_load_state("networkidle")

#     # Verify the right section of the public companies page
#     public_companies = Public_Company_Liability_Overview(page, base_url)

#     # Verify the links in the right section go to the correct pages and have the correct titles
#     public_companies.verify_public_companies_right_section()

# """TC-05: Verify D&O Products Link"""
# @pytest.mark.ui
# @pytest.mark.public_companies_directors_and_officers_liability_page
# def test_verify_dando_products_link(page: Page, base_url):
#     # Goes to the home page
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks the D&O link from the Public Companies overview page object
#     public_companies_page = Public_Company_Liability_Overview(page, base_url)
#     public_companies_page.go_to_subpage(public_companies_page.directors_officers_link)

#     # Verifies the D&O Products link in the right section goes to the correct page and has the correct title
#     Public_Company_Dando_Liability(page).verify_dando_products_link()

"""TC-06: Verify Performance of Directors and Officers Liability Page"""
@pytest.mark.ui
@pytest.mark.public_companies_directors_and_officers_liability_page
def test_performance_of_dando_page(page: Page, base_url):
    page.goto(base_url)

    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    overview = Public_Company_Liability_Overview(page, base_url)
    overview.go_to_subpage(overview.directors_officers_link)

    # # Now instantiate the D&O page object and get metrics
    # dando_page = Public_Company_Dando_Liability(page)
    # performance_metrics = dando_page.get_performance_metrics()

    # assert performance_metrics["load_time"] < 3000, f"Expected load time < 3000ms, got: {performance_metrics['load_time']}ms"
    # assert performance_metrics["first_contentful_paint"] < 2000, f"Expected FCP < 2000ms, got: {performance_metrics['first_contentful_paint']}ms"
    # if performance_metrics["largest_contentful_paint"] is not None:
    #     assert performance_metrics["largest_contentful_paint"] < 2500, f"Expected LCP < 2500ms, got: {performance_metrics['largest_contentful_paint']}ms"
    # else:
    #     print("Warning: LCP metric not available in headless mode")
    # assert performance_metrics["cumulative_layout_shift"] < 0.1, f"Expected CLS < 0.1, got: {performance_metrics['cumulative_layout_shift']}"



# Finished TC-04, do md file for it then verify performance and accessibility for the directors and officers public companies page.