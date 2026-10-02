# This file is for automating the testing of the excess side a page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_excess_liability_page_objects import Public_Company_Excess_Liability
from tests.ui.page_objects.public_companies_excess_sidea_page_objects import Public_Company_Excess_Side_A

# Page Objects - relative import from same ui folder


"""

Public Companies Excess Side A Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006

* This page verifies the Excess Side A page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""


# """TC-01: Verify that the public companies excess side a page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_side_a_page
# def test_public_companies_excess_side_a_page_loads(page: Page, base_url):

#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the exccess side a page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Side A link to navigate to the excess liability page
#     Public_Company_Excess_Side_A(page, base_url).navigate_to_excess_side_a_page()

#     # Verifies that the page has loaded correctly by checking the URL and the page title
#     page.wait_for_load_state("networkidle")

"""TC-002: Verify that the public companies excess side a page has the correct title and headers."""
@pytest.mark.ui
@pytest.mark.public_companies_excess_side_a_page
def test_public_companies_excess_side_a_page_title_and_headers(page: Page, base_url):

    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the exccess side a page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Clicks on the Excess Side A link to navigate to the excess liability page
    Public_Company_Excess_Side_A(page, base_url).navigate_to_excess_side_a_page()

    # Verifies that the page has the correct title and header
    Public_Company_Excess_Side_A(page, base_url).verify_page_title_and_header()

"""TC-03: Verify Policy features bullet point list, the capactiy, and the eligibility text are correct."""
@pytest.mark.ui
@pytest.mark.public_companies_excess_side_a_page
def test_public_companies_excess_side_a_page_policy_features(page: Page, base_url):
    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the exccess side a page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Clicks on the Excess Side A link to navigate to the excess liability page
    Public_Company_Excess_Side_A(page, base_url).navigate_to_excess_side_a_page()

    # Verifies that the page has the correct policy features bullet point list, capacity, and eligibility text
    Public_Company_Excess_Side_A(page, base_url).verify_policy_features_bullet_points()

"""TC-04: Verify that the public companies excess side a page has the correct download buttons and that they are functional."""
@pytest.mark.ui
@pytest.mark.public_companies_excess_side_a_page
def test_public_companies_excess_side_a_page_download_buttons(page: Page, base_url: str):
    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the exccess side a page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Clicks on the Excess Side A link to navigate to the excess liability page
    Public_Company_Excess_Side_A(page, base_url).navigate_to_excess_side_a_page()

    # Verifies that the page has the correct download buttons and that they are functional
    Public_Company_Excess_Side_A(page, base_url).verify_download_buttons()

"""TC-05: Verify Performance of the public companies excess side a page."""
@pytest.mark.ui
@pytest.mark.public_companies_excess_side_a_page
def test_public_companies_excess_side_a_page_performance(page: Page, base_url: str):
    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the exccess side a page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Clicks on the Excess Side A link to navigate to the excess liability page
    Public_Company_Excess_Side_A(page, base_url).navigate_to_excess_side_a_page()

    # Verifies that the page has the correct performance metrics
    Public_Company_Excess_Side_A(page, base_url).verify_performance_metrics()

"""TC-06: Verify Accessibility of the public companies excess side a page."""
@pytest.mark.ui
@pytest.mark.public_companies_excess_side_a_page
def test_public_companies_excess_side_a_page_accessibility(page: Page, base_url: str):
    # Goes to the home page first
    page.goto(base_url)

    # Clicks on the Public Companies menu item to navigate to the exccess side a page
    NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

    # Clicks on the Excess Side A link to navigate to the excess liability page
    Public_Company_Excess_Side_A(page, base_url).navigate_to_excess_side_a_page()

    # Verifies that the page has the correct accessibility metrics
    excess_side_a_page = Public_Company_Excess_Side_A(page, base_url)
    page.wait_for_load_state("networkidle")
    
    # Run axe-core accessibility checks
    results = Axe().run(page)
    
    violations = results.response["violations"]
    passes = results.response["passes"]
    incomplete = results.response.get("incomplete", [])
    
    # Print summary
    print(f"\n♿ Accessibility Results — Public Companies Excess Side A Page")
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