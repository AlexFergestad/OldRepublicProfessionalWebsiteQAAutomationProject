"""
Homepage UI Tests
Test Cases: TC-001, TC-002, 
"""

import pytest
from playwright.sync_api import Page, expect


"""TC-001: Verify home page loads"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_homepage_loads(page: Page, base_url):
#     page.goto(base_url)
#     expect(page).to_have_title("Professional Liability Insurance | D&O | LPL | EPL | Old Republic Pro")

# """TC-002: Verify page title is correct"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_page_title(page: Page, base_url):
#     page.goto(base_url)
#     title = page.title()
#     assert "Old Republic" in title or "Professional" in title

# """TC-003: Verify main header is visible and correct"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_main_header_visible_and_correct(page: Page, base_url):
#     page.goto(base_url)
    
#     # The main header on the homepage
#     heading = page.locator("h1").first
#     expect(heading).to_be_visible()

#     # Verify it contains correct text
#     heading_text = heading.text_content()
#     assert "Industry leader of Management and Professional Liability, with 40 years of continuous experience." in heading_text

# """TC-004: Verify company description/subheading is visible and correct"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_company_description_visible(page: Page, base_url):
#     page.goto(base_url)
    
#     # Look for the description/subheading text
#     description = page.locator("text=/Old Republic Professional underwrites/i")
#     expect(description).to_be_visible()

"""TC-005: Verify all insurance type cards are visible"""
@pytest.mark.ui
@pytest.mark.smoke
def test_insurance_type_cards_and_links_visible(page: Page, base_url):
    
    # Sets a larger viewport to ensure all elements are visible
    page.set_viewport_size({"width": 1920, "height": 1080})

    # Goes to the homepage fixture URL
    page.goto(base_url)

    # List of insurance card titles to check
    insurance_types = [
        "Public Companies",
        "Private Companies",
        "Law Firms",
        "Financial Institutions",
        "Commercial Crime"
    ]

    for insurance_type in insurance_types:

        # Finds the card link that contains this text
        card_link = page.locator(f"a.product-service-box:has-text('{insurance_type}')").first
        expect(card_link).to_be_visible(timeout=5000)
        
        # Verify it has an image
        card_image = card_link.locator("img.product-service-box__icon__image").first
        expect(card_image).to_be_visible(timeout=5000)
 
        # Verify the title
        card_title = card_link.locator("span.product-service-box__title").first
        expect(card_title).to_have_text(insurance_type)


# Tests that I want done:
# - Contact and careers in separate files
# - search bar functionality on homepage
# - company description (subheading)
# - contact us on homepage
# - old republic insurance group link, privacy link, and terms of use link all in a test case on homepage
# - old republic professional logo validation test case on homepage
# - home icon link validation test case on homepage
# - old republic professional top left link is validated and works on homepage
# - footer, nav bar, cards, test cases on separate folders
# - Also finish the other test cases in Claude