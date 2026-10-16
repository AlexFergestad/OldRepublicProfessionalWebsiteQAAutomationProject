import re

from playwright.sync_api import Page, expect

class Public_Company_Liability_Overview:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url



