# This file is for automating the testing of the excess side a page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder


"""

Public Companies Excess Side A Page UI Tests
Test Cases: TC-001, TC-002,

* This page verifies the Excess Side A page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""