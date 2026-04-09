# This file is for automating the testin of the public companies pages in the nav bar.

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_page_objects import Public_Company_Liability_Overview

"""

Private Companies Nav Bar Section UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005

* This page verifies the homepage of the Old Republic Professional website loads correctly, 
has the correct title and main header, displays the company description, shows all insurance type cards 
with correct titles and links, has a working Contact Us link, displays the company logo that links to the 
homepage, has a functional search bar, and includes the expected links above the footer.

"""

import pytest
from playwright.sync_api import Page, expect

# """TC-01: Verify that the public companies page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_first_page
# def test_public_companies_page_loads(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)
    
#     # Clicks on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Waits for the public companies page to load
#     page.wait_for_load_state("networkidle")

# """TC-002: Verify Browser Tab Name on Public Companies Page"""
# @pytest.mark.ui
# @pytest.mark.public_companies_first_page
# def test_public_companies_page_browser_title(page: Page, base_url):

#     # Navigate to the home page
#     page.goto(base_url)

#     # Click on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Wait for the public companies page to load
#     page.wait_for_load_state("networkidle")

#     # Verify that the browser tab title is correct
#     ## Get the title
#     title = page.title()
    
#     # Verify it contains expected text
#     assert "Old Republic Professional" in title, f"Expected 'Old Republic Professional' in title, got: {title}"

# """TC-003: Verify Public-Company Liability Overview Heading and Paragraph"""
# @pytest.mark.ui
# @pytest.mark.public_companies_first_page
# def test_public_companies_page_heading_and_paragraph(page: Page, base_url):
#     """Verify Public Companies page heading and paragraphs"""
    
#     # Navigate to the home page
#     page.goto(base_url)
#     page.wait_for_load_state("networkidle")
    
#     # Click on the Public Companies menu item
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")
#     page.wait_for_load_state("networkidle")
    
#     # Verify the heading and paragraph
#     public_companies = Public_Company_Liability_Overview(page, base_url)  
#     public_companies.verify_heading_and_paragraphs()

# """TC-004: Verify Top Image in Public Companies Page"""
# @pytest.mark.ui
# @pytest.mark.public_companies_first_page
# def test_top_image_in_public_companies_page(page: Page, base_url):
#     """Verify Top Image in Public Companies page"""
    
#     # Navigate to the home page
#     page.goto(base_url)

#     # Click on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Wait for the public companies page to load
#     page.wait_for_load_state("networkidle")

#     # Verify the top image is correct
#     public_companies = Public_Company_Liability_Overview(page, base_url)
#     public_companies.verify_top_image()

# """TC-005: Verify Public Companies Section on the Right"""
# @pytest.mark.ui
# @pytest.mark.public_companies_first_page
# def test_public_companies_right_section(page: Page, base_url):
#     """Verify Public Companies Section on the Right"""
    
#     # Navigate to the home page
#     page.goto(base_url)

#     # Click on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Wait for the public companies page to load
#     page.wait_for_load_state("networkidle")

#     # Verify the right section of the public companies page
#     public_companies = Public_Company_Liability_Overview(page, base_url)

#     # Verify the links in the right section go to the correct pages and have the correct titles
#     public_companies.verify_public_companies_right_section()

# """TC-006: Verify Public Companies Page Performance Metrics"""
# @pytest.mark.ui
# @pytest.mark.public_companies_first_page
# def test_public_companies_page_performance_metrics(page: Page, base_url):
#     """Verify Public Companies Page Performance Metrics"""
    
#     # Navigate to the home page
#     page.goto(base_url)

#     # Click on the Public Companies menu item to navigate to the public companies page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Wait for the public companies page to load
#     page.wait_for_load_state("networkidle")

#     # Gets the performance metrics for the public companies page
#     public_companies = Public_Company_Liability_Overview(page, base_url)
#     performance_metrics = public_companies.get_performance_metrics()

#     # Verify the performance metrics meet expected thresholds (these thresholds can be adjusted based on requirements)
#     assert performance_metrics["load_time"] < 3000, f"Expected load time < 3000ms, got: {performance_metrics['load_time']}ms"
#     assert performance_metrics["first_contentful_paint"] < 2000, f"Expected first contentful paint < 2000ms, got: {performance_metrics['first_contentful_paint']}ms"
#     assert performance_metrics["largest_contentful_paint"] < 2500, f"Expected largest contentful paint < 2500ms, got: {performance_metrics['largest_contentful_paint']}ms"
#     assert performance_metrics["cumulative_layout_shift"] < 0.1, f"Expected cumulative layout shift < 0.1, got: {performance_metrics['cumulative_layout_shift']}"

"""TC-007: Verify Public Companies Page Accessibility with axe-core"""
@pytest.mark.ui
@pytest.mark.public_companies_first_page
def test_public_companies_page_accessibility(page: Page, base_url):
    """Verify Public Companies Page Accessibility with axe-core"""
    
    # Navigate to the public companies page
    page.goto(base_url)
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")
    page.wait_for_load_state("networkidle")

    # Run axe-core accessibility checks
    results = Axe().run(page)

    violations = results.response["violations"]
    passes = results.response["passes"]
    incomplete = results.response.get("incomplete", [])

    # Print summary
    print(f"\n♿ Accessibility Results — Public Companies Page")
    print(f"   Violations:  {len(violations)}")
    print(f"   Passes:      {len(passes)}")
    print(f"   Incomplete:  {len(incomplete)}")

    # Print each violation with details
    for v in violations:
        print(f"\n   ❌ {v['id']} — {v['description']}")
        print(f"      Impact: {v['impact']}")
        print(f"      Help:   {v['helpUrl']}")

    # Known existing violations on the site — documented but outside QA scope
    known_violations = {"color-contrast", "input-button-name", "link-name"}
    skipped = [v for v in violations if v["id"] in known_violations]
    print(f"\n   ⚠️  Known existing violations skipped ({len(skipped)}):")
    for v in skipped:
        print(f"      - {v['id']} ({v['impact']})")

    # Only fail on NEW critical/serious violations not already known
    critical_violations = [
        v for v in violations
        if v["impact"] in ("critical", "serious")
        and v["id"] not in known_violations
    ]

    assert len(critical_violations) == 0, (
        f"\nFound {len(critical_violations)} new critical/serious violation(s):\n"
        + "\n".join(f"  - {v['id']} ({v['impact']}): {v['description']}" for v in critical_violations)
    )

    print(f"\n✅ Accessibility check passed — no new critical/serious violations found")


# The Following next tests -> then Done
# - Top Image -- Done
# - Public Companies Section on the Right -- Done
# - Add page performance metrics (in claude text) to this and careers test -- Done
# - Add axe-core accessibility checks to this and careers test
# - Add test for the links in the right section of the public companies page (and careers page) to verify they go to the correct pages and have the correct titles.

    