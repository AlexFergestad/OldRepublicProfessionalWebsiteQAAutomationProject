import re

from playwright.sync_api import Page, expect

class Public_Company_Products:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.url = f"{base_url}/business-insurance-public-company"
