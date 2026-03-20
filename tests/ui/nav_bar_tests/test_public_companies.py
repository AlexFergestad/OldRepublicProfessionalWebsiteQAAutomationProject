# This file is for automating the testin of the public companies pages in the nav bar.

import pytest
from playwright.sync_api import Page, expect

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu

"""

Private Companies Nav Bar Section UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011

* This page verifies the homepage of the Old Republic Professional website loads correctly, 
has the correct title and main header, displays the company description, shows all insurance type cards 
with correct titles and links, has a working Contact Us link, displays the company logo that links to the 
homepage, has a functional search bar, and includes the expected links above the footer.

"""

import pytest
from playwright.sync_api import Page, expect

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage

"""TC-01: Verify that the public companies page loads correctly and has the correct URL when accessed from the home page."""
@pytest.mark.ui
@pytest.mark.careers
def test_public_companies_page_loads(page: Page, base_url):
    # Goes to the home page first
    page.goto(base_url)
    
    # Clicks on the Public Companies menu item to navigate to the public companies page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Waits for the public companies page to load
    page.wait_for_load_state("networkidle")

"""TC-002: Verify Browser Tab Name on Public Companies Page"""
@pytest.mark.ui
@pytest.mark.careers
def verify_public_companies_page_browser_title(page: Page, base_url):

    # Navigate to the home page
    page.goto(base_url)

    # Click on the Public Companies menu item to navigate to the public companies page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Wait for the public companies page to load
    page.wait_for_load_state("networkidle")

    # Verify that the browser tab title is correct
    ## Get the title
    title = page.title()
    
    # Verify it contains expected text
    assert "Old Republic Professional" in title, f"Expected 'Old Republic Professional' in title, got: {title}"

# """TC-003: Verify Public-Company Liability Overview Heading and Paragraph"""
@pytest.mark.ui
@pytest.mark.careers
    