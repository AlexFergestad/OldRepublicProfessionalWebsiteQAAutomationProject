# This file is for automating the testing of the employment-practices liability page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu

