"""
Homepage UI Tests
Test Cases: TC-001, 
"""

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_homepage_title(page: Page, base_url):
    page.goto(base_url)
    expect(page).to_have_title("Old Republic Professional")
