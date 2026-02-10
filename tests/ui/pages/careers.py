"""

Careers UI Tests
Test Cases: TC-

* This page verifies the career page of the Old Republic Professional website.

"""

import pytest
from playwright.sync_api import Page, expect

# Maybe try to add a fixture that marks these tests as career page tests, 
# so we can easily run them separately if needed.

@pytest.mark.ui
@pytest.mark.careers
def test_careers_page_loads(page: Page, base_url):
    """Test that the careers page loads successfully."""
    page.goto(base_url)
    
    page.get_by_role("link", name="Careers").click()

    expect(page).to_have_url(f"{base_url}/careers")