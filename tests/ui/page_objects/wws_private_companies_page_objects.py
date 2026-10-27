import re

from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect

class WWS_Private_Companies:
    PAGE_PATH = "/who-we-serve/public-companies"
    OTHER_SEGMENTS = {
        "Private Companies": "/en/who-we-serve/private-companies",
        "Financial Institutions": "/who-we-serve/financial-institutions",
        "Not-for-Profit Entities": "/who-we-serve/not-for-profit-entities",
    }
    D_AND_O_COVERAGE_DESCRIPTIONS = {
        "Public Primary D&O": "First-layer D&O coverage for publicly traded companies.",
        "Lead Side-A": "Dedicated Side-A coverage for non-indemnifiable loss.",
        "Excess D&O": "Additional capacity above underlying public company D&O.",
        "Excess Side-A": "Additional Side-A limits for layered public company programs.",
    }

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.page_url = f"{base_url.rstrip('/')}{self.PAGE_PATH}"
        self.page_heading = page.get_by_role(
            "heading", name="Public Companies", exact=True
        )