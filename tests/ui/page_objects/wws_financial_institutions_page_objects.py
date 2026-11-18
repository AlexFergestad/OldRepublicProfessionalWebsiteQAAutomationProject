import re

from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect


class WWS_Financial_Institutions:
    PAGE_PATH = "/en/who-we-serve/financial-institutions"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.page_url = f"{base_url.rstrip('/')}{self.PAGE_PATH}"
