"""
Homepage UI Tests
Test Cases: TC-001, TC-002, 
"""

import pytest
from playwright.sync_api import Page, expect


"""TC-001: Verify home page loads"""
@pytest.mark.ui
@pytest.mark.smoke
def test_homepage_loads(page: Page, base_url):
    page.goto(base_url)
    expect(page).to_have_title("Professional Liability Insurance | D&O | LPL | EPL | Old Republic Pro")

"""TC-002: Verify page title is correct"""
@pytest.mark.ui
@pytest.mark.smoke
def test_page_title(page: Page, base_url):
    page.goto(base_url)
    title = page.title()
    assert "Old Republic" in title or "Professional" in title
