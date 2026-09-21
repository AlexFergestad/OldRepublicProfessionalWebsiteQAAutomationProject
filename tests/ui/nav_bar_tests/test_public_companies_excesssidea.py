# This file is for automating the testing of the excess side a page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_excess_sidea_page_objects import Public_Company_Excess_Side_A

# Page Objects - relative import from same ui folder


"""

Public Companies Excess Side A Page UI Tests
Test Cases: TC-001, TC-002,

* This page verifies the Excess Side A page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""


"""TC-01: Verify that the public companies excess side a page loads correctly and has the correct URL when accessed from the home page."""
@pytest.mark.ui
@pytest.mark.public_companies_excess_side_a_page
def test_public_companies_excess_side_a_page_loads(page: Page, base_url):

    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the exccess side a page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Clicks on the Excess Side A link to navigate to the excess liability page
    Public_Company_Excess_Side_A(page, base_url).navigate_to_excess_side_a_page()

    # Verifies that the page has loaded correctly by checking the URL and the page title
    page.wait_for_load_state("networkidle")

"""TC-002: Verify that the public companies excess side a page has the correct title and headers."""



