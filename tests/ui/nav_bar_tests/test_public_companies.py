# This file is for automating the testin of the public companies pages in the nav bar.

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