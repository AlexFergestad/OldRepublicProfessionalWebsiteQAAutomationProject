import re

from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect


class WWS_Financial_Institutions:
    PAGE_PATH = "/en/who-we-serve/private-companies"