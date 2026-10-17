# This file is for automating the testing of the public companies pages in the nav bar.

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.who_we_serve_page_objects import Who_We_Serve

"""

Who We Serve Main Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007

* This page verifies the Wo We Serve page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

"""TC-01: Verify that the Who We Serve page loads correctly and has the correct URL when accessed from the home page."""
@pytest.mark.ui
@pytest.mark.who_we_serve_main_page
def test_who_we_serve_page_loads(page: Page, base_url):
    # Goes to the home page first
    page.goto(base_url)
    
    # Clicks on the Public Companies menu item to navigate to the public companies page
    NavigationMenu(page).navigate_to_nav_bar_item("Who We Serve")

    # Waits for the public companies page to load
    page.wait_for_load_state("networkidle")


"""TC-02: Verify the 'Learn More' Button for the Public Companies Section."""
@pytest.mark.ui
@pytest.mark.who_we_serve_main_page
def test_learn_more_button_for_public_companies(page: Page, base_url):