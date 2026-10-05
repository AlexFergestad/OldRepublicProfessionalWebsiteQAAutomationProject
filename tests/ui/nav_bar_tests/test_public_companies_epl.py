# This file is for automating the testing of the employment-practices liability page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu

"""

Public Companies Employment-Practices Liability Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011

* This page verifies the Employment-Practices Liability page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

"""TC-01: Verify that the public companies employment-practices liability page loads correctly and has the correct URL when accessed from the home page."""
@pytest.mark.ui
@pytest.mark.public_companies_employment_practices_liability_page


