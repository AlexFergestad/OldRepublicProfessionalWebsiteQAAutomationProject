"""

Careers UI Tests
Test Cases: TC-001, TC-002

* This page verifies the career page of the Old Republic Professional website.

"""

import pytest
from playwright.sync_api import Page, expect

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.careers_job_details_page_object import JobDetailsPage

# Maybe try to add a fixture that marks these tests as career page tests, 
# so we can easily run them separately if needed.

# """TC-01: Verify that the careers page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.careers
# def test_careers_page_loads(page: Page, base_url):

#     # Goes to the home page first
#     page.goto(base_url)
    
#     # Clicks on the Careers menu item to navigate to the careers page
#     page.get_by_role("menuitem", name="Careers").click()

#     # Verifies that the URL is correct for the careers page
#     expect(page).to_have_url(f"{base_url}/careers")

# """TC-02:Verify that the browser tab name is correct when on the careers page."""
# @pytest.mark.ui
# @pytest.mark.careers
# def test_careers_page_browser_tab(page: Page, base_url):

#     # Goes to the careers page directly
#     page.goto(f"{base_url}/careers")
#     page.wait_for_load_state("networkidle")

#     # Verifies that the browser tab name is correct
#     expect(page).to_have_title("Careers at ORPRO")

# """TC-03: Verify the Careers Header is on the Careers page."""
# @pytest.mark.ui
# @pytest.mark.careers
# def test_careers_page_header(page: Page, base_url):

#     page.goto(f"{base_url}/careers")
#     page.wait_for_load_state("networkidle")

#     heading = page.locator("h1").first
    
#     # Verify it's visible
#     expect(heading).to_be_visible(timeout=5000)

#     # Verify exact text
#     expect(heading).to_have_text("Careers at ORPRO")

# """TC-004: Verify the LinkedIn link on the careers page."""
# @pytest.mark.ui
# @pytest.mark.careers
# def test_careers_page_linkedin_link(page: Page, base_url):
#     page.goto(f"{base_url}/careers")
#     page.wait_for_load_state("networkidle")

#     # Find the LinkedIn share button by text
#     linkedin_button = page.get_by_role("button", name="Share").first

#     # Verify it's visible
#     expect(linkedin_button).to_be_visible(timeout=5000)
    
#     # Click the button
#     linkedin_button.click()

#     # Wait a moment for LinkedIn popup/redirect
#     page.wait_for_timeout(2000)

# """TC-005: Verify the intern job listing on the careers page."""
# @pytest.mark.ui
# @pytest.mark.careers
# def test_careers_page_intern_listing(page: Page, base_url):
#     page.goto(f"{base_url}/careers")
#     page.wait_for_load_state("networkidle")

#     # Find the job posting link
#     job_link = page.get_by_role("link", name="Underwriting Analyst Intern")

#     # Verify it's visible
#     expect(job_link).to_be_visible(timeout=5000)

#     # Click the link
#     job_link.click()
#     page.wait_for_load_state("networkidle")

#     # Verify we navigated to the job details page
#     assert "/underwriting-analyst-intern" in page.url, \
#         f"Expected to navigate to job details, got: {page.url}"

# """TC-006: Verify Job Description for Underwriting Analyst Intern."""
# @pytest.mark.ui
# @pytest.mark.careers
# def test_careers_page_intern_job_description(page:Page, base_url):

#     page.goto(f"{base_url}/careers")
#     page.wait_for_load_state("networkidle")

#     # Click on the job listing for the Underwriting Analyst Intern
#     job_link = page.get_by_role("link", name="Underwriting Analyst Intern").first
#     expect(job_link).to_be_visible(timeout=5000)

#     # Clicks on the job listing for the Underwriting Analyst Intern and brings user to the page
#     job_link.click()

#     page.wait_for_load_state("networkidle")

#     # Verify the job description title is visible
#     job_description_heading = page.get_by_role("heading", level=3, name="Job Description")
#     expect(job_description_heading).to_be_visible(timeout=5000)

#     heading_text = job_description_heading.text_content().strip()
#     assert heading_text == "Job Description", \
#         f"Expected 'Job Description', got: {heading_text}"
#     print(f"✅ Job Description heading verified: {heading_text}")

#     # Verify the job description paragraph is visible
#     # The paragraph comes right after the h3
#     job_description_paragraph = page.locator("h3:has-text('Job Description') + p").first
#     expect(job_description_paragraph).to_be_visible(timeout=5000)

"""TC-007 Verify Job Requirements for Underwriting Analyst Intern Position."""
@pytest.mark.ui
@pytest.mark.careers
def test_careers_page_intern_job_requirements(page:Page, base_url):

    # Initialize page objects
    careers_page = CareersPage(page, base_url)
    job_details = JobDetailsPage(page)
    
    careers_page.navigate()
    careers_page.click_underwriting_analyst_intern_job()
    
    # One method verifies everything
    result = job_details.verify_job_requirements_section()
    
    print(f"\n✅ Job Requirements verified:")
    print(f"   - {result['paragraphs']} paragraphs")
    print(f"   - {result['list_items']} bullet points")

"""TC-008 Verify About Old Republic Professional Section"""
pytest.mark.ui


# Test the browser tab name --
# Test the h1 headin "Careers"
# Test the LinkedIn link
# Test the intern job listing and maybe more inside of it
# Test the inside of the Underwriting Analyst Intern job listing, including the description and the apply button
# Test the About Us heading and content
# Test the Culture heading and content
# Test the Equal Employment Opportunity heading and content
# Test the contact us button and subheading to the right of it
# Test the three links above the footer
# Test navigation back to the home page via the logo in the header