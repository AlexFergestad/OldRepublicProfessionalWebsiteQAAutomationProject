"""
Homepage UI Tests
Test Cases: TC-001, TC-002, 
"""

import pytest
from playwright.sync_api import Page, expect


# """TC-001: Verify home page loads"""
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
# #     expect(description).to_be_visible()

# """TC-005: Verify all insurance type cards are visible"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_insurance_type_cards_and_links_visible(page: Page, base_url):


#     # Goes to the homepage fixture URL
#     page.goto(base_url)

#     # List of insurance card titles to check
#     insurance_types = [
#         "Public Companies",
#         "Private Companies",
#         "Law Firms",
#         "Financial Institutions",
#         "Commercial Crime"
#     ]

#     for insurance_type in insurance_types:

#         # Finds the card link that contains this text
#         card_link = page.locator(f"a.product-service-box:has-text('{insurance_type}')").first
#         expect(card_link).to_be_visible(timeout=5000)
        
#         # Verify it has an image
#         card_image = card_link.locator("img.product-service-box__icon__image").first
#         expect(card_image).to_be_visible(timeout=5000)
 
#         # Verify the title
#         card_title = card_link.locator("span.product-service-box__title").first
#         expect(card_title).to_have_text(insurance_type)

# """TC-006: Verify insurance type card titles and links are clickable"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_insurance_cards_clickable(page: Page, base_url):

    
#     insurance_types = [
#             "Public Companies",
#             "Private Companies",
#             "Law Firms",
#             "Financial Institutions",
#             "Commercial Crime"
#         ]

#     for insurance_type in insurance_types:
#         page.goto(base_url)
#         page.wait_for_load_state("networkidle")  # Waits for page to fully load

#         # Click each insurance type card title
#         title_link = page.locator(f"span.product-service-box__title:has-text('{insurance_type}')")
#         title_link.click()
#         page.wait_for_load_state("networkidle")  # Waits for page to fully load
#         title_click_url = page.url

#         # Go back to the main homepage and test clicking the image's link
#         page.goto(base_url)
#         page.wait_for_load_state("networkidle")  # Waits for page to fully load

#         # Click each insurance type card image
#         image_link= page.locator(f"a.product-service-box:has-text('{insurance_type}')").first \
#             .locator("img.product-service-box__icon__image").first
#         image_link.click()
#         page.wait_for_load_state("networkidle")  # Waits for page to fully load
#         image_click_url = page.url

#         # Verifies the links navigate to the same url/place
#         assert image_click_url == title_click_url, \
#             f"Different URLs: Image={image_click_url}, Title={title_click_url}"

# """TC-007: Verify Contact Us is visible and links correctly to the contact page"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_contact_us_link(page: Page, base_url):
    
#     # Goes to the homepage
#     page.goto(base_url)

#     # Look for the "Every great partnership starts with a conversation." text
#     contact_section = page.get_by_text("Every great partnership starts with a conversation.")
#     expect(contact_section).to_be_visible()
#     expect(contact_section).to_have_text("Every great partnership starts with a conversation.")

#     # Find by role (best practice - matches how screen readers find it)
#     contact_button = page.get_by_role("link", name="Contact Us").first

#     # Verify it's visible on the screen for a user
#     expect(contact_button).to_be_visible(timeout=5000)

#     # Verify the text is exactly "Contact Us"
#     expect(contact_button).to_have_text("Contact Us")

#     # Click and verify navigation
#     contact_button.click()
#     page.wait_for_load_state("networkidle")
    
#     # Verify we're on the contact page
#     current_url = page.url
#     assert "/contact" in current_url, f"Expected URL to contain '/contact', but got '{current_url}'"

# """TC-008: Verify Company Logo is Visible and Links to Homepage"""
# @pytest.mark.ui
# @pytest.mark.smoke
# def test_company_logo(page: Page, base_url):

#     # Start on contact page (not homepage)
#     page.goto(f"{base_url}/contact")
#     page.wait_for_load_state("networkidle")

#     # Find and verify logo is visible
#     logo = page.get_by_alt_text("Old Republic Professional")
#     expect(logo).to_be_visible(timeout=5000)

#     # Click logo to go home
#     logo.click()
#     page.wait_for_load_state("networkidle")

#     # Verify we're on homepage
#     current_url = page.url.rstrip('/')
#     expected_url = base_url.rstrip('/')
#     assert current_url == expected_url, \
#         f"Expected homepage '{expected_url}', got '{current_url}'"

# """TC-009: Verify Search Bar Functionality on Homepage"""
# @pytest.mark.ui
# def test_search_bar(page: Page, base_url):

#     # Test multiple search queries
#     search_queries = [
#         "Directors and Officers",
#         "Liability Insurance",
#         "Contact"
#     ]
    
#     for query in search_queries:

#         # Goes back to homepage for each search
#         page.goto(base_url)
#         page.wait_for_load_state("networkidle")
        
#         # Find search input
#         search_input = page.get_by_placeholder("Search")
#         expect(search_input).to_be_visible(timeout=5000)
        
#         # Enter query
#         search_input.fill(query)
        
#         # Submit search (press Enter)
#         search_input.press("Enter")
#         page.wait_for_load_state("networkidle")
        
#         # Verify navigation
#         current_url = page.url
#         assert current_url != base_url, f"Search '{query}' did not navigate"

# """TC-010: Verify ORPRO Above the Footer, "Old Republic Insurance Group" Link, "Privacy" Link, and "Terms of Use" Link"""
# @pytest.mark.ui
# def test_above_footer(page: Page, base_url):
     
#     # Goes to the homepage
#     page.goto(base_url)
#     page.wait_for_load_state("networkidle")

#     # Scroll to the bottom of the page to reveal footer
#     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#     page.wait_for_timeout(500)  # Give it a moment to settle

#     # Verify Old Republic Insuranced Group Link
#     orig_link = page.get_by_role("menuitem", name="Old Republic Insurance Group")
#     expect(orig_link).to_be_visible(timeout=5000)

#     orig_href = orig_link.get_attribute("href")
#     assert orig_href, "Old Republic Insurance Group link has no href"

#     # Test orig link
#     orig_link.click()
#     page.wait_for_load_state("networkidle")
#     page.goto(base_url) # Goes back to homepage

#     # Verify Privacy Link
#     privacy_link = page.get_by_role("menuitem", name="Privacy")
#     expect(privacy_link).to_be_visible(timeout=5000)
    
#     privacy_href = privacy_link.get_attribute("href")
#     assert privacy_href, "Privacy link has no href"
#     print(f"✅ Privacy link: {privacy_href}")

#     # Test privacy link
#     privacy_link.click()
#     page.wait_for_load_state("networkidle")
#     page.goto(base_url) # Goes back to homepage

#     # Verify Terms of Use Link
#     terms_link = page.get_by_role("menuitem", name="Terms of Use")
#     expect(terms_link).to_be_visible(timeout=5000)
    
#     terms_href = terms_link.get_attribute("href")

#     # Test terms of use link
#     terms_link.click()
#     page.wait_for_load_state("networkidle")
#     page.goto(base_url) # Goes back to homepage

#     assert terms_href, "Terms of Use link has no href"

    

"""TC-011: Verify Main Center Image"""
def test_main_center_image(page: Page, base_url):

    # Starts at the homepage
    page.goto(base_url)

    # Look for the main center image (assuming it has an alt text we can use)
    billboard_image = page.locator("div.billboard__underlay").first

    # Verify the element is visible
    expect(billboard_image).to_be_visible(timeout=5000)

# Tests that I want done:
# - Don't do TC8 from Claude
# - Contact and careers in separate files
# - search bar functionality on homepage
# - company description (subheading)
# - contact us on homepage
# - old republic insurance group link, privacy link, and terms of use link all in a test case on homepage
# - old republic professional logo validation test case on homepage
# - home icon link validation test case on homepage do in nav_bar page
# - old republic professional top left link is validated and works on homepage
# - footer, nav bar, cards, test cases on separate folders
# - Also finish the other test cases in Claude