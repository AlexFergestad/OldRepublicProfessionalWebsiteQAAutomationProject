# This file is for automating the testing of the lead side a page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_dando_liability_page_objects import Public_Company_Dando_Liability
from tests.ui.page_objects.public_companies_leadsidea_page_objects import Public_Company_Lead_Side_A

"""

Public Companies Lead Side A Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006

* This page verifies the Lead Side A page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

# """TC-01: Verify that the public companies lead side a page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_lead_side_a_page
# def test_public_companies_lead_side_a_page_loads(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Lead_Side_A(page, base_url).navigate_to_lead_side_a_page()

#     # Verifies that the page has loaded correctly by checking the URL and the page title
#     page.wait_for_load_state("networkidle")

# """TC-02: Verify that the public companies lead side a page has the correct title and headers."""
# @pytest.mark.ui
# @pytest.mark.public_companies_lead_side_a_page
# def test_public_companies_lead_side_a_page_title_and_headers(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Lead_Side_A(page, base_url).navigate_to_lead_side_a_page()

#     # Verifies that the page has loaded correctly by checking the URL and the page title    
#     Public_Company_Lead_Side_A(page, base_url).verify_lead_side_a_page_title_and_headers()

# """TC-03: Verify the paragraph underneath 'Lead Side-A D&O: "A-Sure'"""
# @pytest.mark.ui
# @pytest.mark.public_companies_lead_side_a_page
# def test_public_companies_lead_side_a_h1_paragraph(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Lead Side-A link to navigate to the lead side a page
#     Public_Company_Lead_Side_A(page, base_url).navigate_to_lead_side_a_page()

#     # Verifies that the paragraph underneath 'Lead Side-A D&O: "A-Sure' is visible
#     Public_Company_Lead_Side_A(page, base_url).verify_lead_side_a_h1_paragraph()


# """TC-04: Verify the download buttonns."""
# @pytest.mark.ui
# @pytest.mark.public_companies_lead_side_a_page
# def test_public_companies_lead_side_a_download_buttons(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")
    
#     # Clicks on the Lead Side-A link to navigate to the lead side a page
#     Public_Company_Lead_Side_A(page, base_url).navigate_to_lead_side_a_page()

#     # Verifies that the download buttons are visible
#     Public_Company_Lead_Side_A(page, base_url).verify_download_buttons()

"""TC-05: Verify the Performance of the public companies lead side a page."""
@pytest.mark.ui
@pytest.mark.public_companies_lead_side_a_page
def test_public_companies_lead_side_a_page_performance(page: Page, base_url):
    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the products page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Clicks on the Lead Side-A link to navigate to the lead side a page
    Public_Company_Lead_Side_A(page, base_url).navigate_to_lead_side_a_page()

    # Verifies the Performance Metrics section is visible and contains the expected content
    # Now instantiate the lead side a page object and get metrics
    leadsidea_page = Public_Company_Lead_Side_A(page, base_url)
    performance_metrics = leadsidea_page.get_performance_metrics()
    
    assert performance_metrics["load_time"] < 3000, f"Expected load time < 3000ms, got: {performance_metrics['load_time']}ms"
    assert performance_metrics["first_contentful_paint"] < 2000, f"Expected FCP < 2000ms, got: {performance_metrics['first_contentful_paint']}ms"
    if performance_metrics["largest_contentful_paint"] is not None:
        assert performance_metrics["largest_contentful_paint"] < 2500, f"Expected LCP < 2500ms, got: {performance_metrics['largest_contentful_paint']}ms"
    else:
        print("Warning: LCP metric not available in headless mode")
    assert performance_metrics["cumulative_layout_shift"] < 0.1, f"Expected CLS < 0.1, got: {performance_metrics['cumulative_layout_shift']}"

