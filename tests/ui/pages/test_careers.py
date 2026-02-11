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

    # Goes to the home page first
    page.goto(base_url)
    
    # Clicks on the Careers menu item to navigate to the careers page
    page.get_by_role("menuitem", name="Careers").click()

    # Verifies that the URL is correct for the careers page
    expect(page).to_have_url(f"{base_url}/careers")

@pytest.mark.ui
@pytest.mark.careers
def test_careers_page_browser_tab(page: Page, base_url):


# Test the browser tab name 
# Test the h1 headin "Careers"
# Test the LinkedIn link
# Test the intern job listing and maybe more inside of it
# Test the About Us heading and content
# Test the Culture heading and content
# Test the Equal Employment Opportunity heading and content
# Test the contact us button and subheading to the right of it
# Test the three links above the footer
# Test navigation back to the home page via the logo in the header