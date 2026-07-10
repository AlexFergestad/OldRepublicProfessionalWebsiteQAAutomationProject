import re

from playwright.sync_api import Page, expect


class Public_Company_Excess_Liability:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        

    def navigate_to_excess_liability_page(self):
        self.excess_liability_page.click()
        self.page.wait_for_load_state("networkidle")
