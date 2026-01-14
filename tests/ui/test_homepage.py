"""
Homepage UI Tests
Test Cases: TC-001, 
"""

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_browser_page__title(page: Page, base_url):
    page.goto(base_url)
    expect(page).to_have_title("Professional Liability Insurance | D&O | LPL | EPL | Old Republic Pro")


