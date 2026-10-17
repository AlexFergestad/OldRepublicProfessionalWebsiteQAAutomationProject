import re

from playwright.sync_api import Page, expect

class Who_We_Serve:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

        self.learn_more_public_companies = page.get_by_role("button", name="Learn More")

    def verify_learn_more_button(self, locator):
        locator.click()
