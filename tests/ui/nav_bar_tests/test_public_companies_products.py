# This file is for automating the testing of the products page in the public companies section in the nav bar.

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_page_objects import Public_Company_Liability_Overview
from tests.ui.page_objects.public_companies_products_page_objects import Public_Company_Products

"""

Public Companies Products Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007

* This page verifies the Products page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

"""TC-01: Verify that the public companies products page loads correctly and has the correct URL when accessed from the home page."""
@pytest.mark.ui
@pytest.mark.public_companies_products_page