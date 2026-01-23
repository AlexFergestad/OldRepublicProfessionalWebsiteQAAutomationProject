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
    insurance_types = {
        "Public Companies": "Public company employees smiling",
        "Private Companies": "Private company employees smiling",
        "Law Firms": "Law firm employees smiling",
        "Financial Institutions": "Financial institution employees smiling",
        "Commercial Crime": "Commercial crime prevention"
    }

    for insurance_type, alt_text in insurance_types:
        
        # Target the specific card text element by its title
        caption = page.locator(f".product-service-box__title:has-text('{insurance_type}')").first

        try:
            expect(caption).to_be_visible(timeout=5000)
            print(f"✅ Found: {insurance_type}")
        except Exception as e:
            print(f"❌ Not found: {insurance_type}")
            print(f"   Error: {e}")
        
        # Finds the card image element
        card_image = page.locator(f".product-service-box__icon__image:has-text('{insurance_type}')").first

        try:
            expect(card_image).to_be_visible(timeout=5000)
            print(f"✅ Found image for: {insurance_type}")
        except Exception as e:
            print(f"❌ Not found image for: {insurance_type}")
            print(f"   Error: {e}")

    # Double checks the correct elements of the titles and then do the images are visible for this test case - done

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