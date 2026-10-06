# This file is for automating the testing of the employment-practices liability page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_epl_page_objects import Employment_Practices_Liability

"""

Public Companies Employment-Practices Liability Page UI Tests
Test Cases: TC-001, TC-002

* This page verifies the Employment-Practices Liability page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

# """TC-01: Verify that the public companies employment-practices liability page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_employment_practices_liability_page
# def test_epl_page_loads(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Employment-Practices Liability card to navigate to the employment-practices liability page
#     Employment_Practices_Liability(page, base_url).navigate_to_epl_page()

#     # Verifies that the page has loaded correctly by checking the URL and the page title
#     page.wait_for_load_state("networkidle")


"""TC-002: Verify that the public companies employment-practices liability page has the correct title and headers."""
@pytest.mark.ui
@pytest.mark.public_companies_employment_practices_liability_page
def test_epl_page_title_and_headers(page: Page, base_url):
    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the public companies page

