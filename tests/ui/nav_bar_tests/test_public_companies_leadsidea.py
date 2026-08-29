# This file is for automating the testing of the lead side a page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_dando_liability_page_objects import Public_Company_Dando_Liability
from tests.ui.page_objects.public_companies_excess_liability_page_objects import Public_Company_Excess_Liability

"""

Public Companies Lead Side A Page UI Tests
Test Cases: TC-001, TC-002,

* This page verifies the Lead Side A page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

"""TC-01:"""