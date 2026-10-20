# This file is for automating the testing of the Who We Serve page in the nav bar.

import re

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.who_we_serve_page_objects import Who_We_Serve

"""

Who We Serve Main Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009

* This page verifies the Who We Serve page of the Old Republic Professional website loads correctly,
has the expected client segment sections, working Learn More buttons, performance, and accessibility.

"""


def open_who_we_serve(page: Page, base_url: str) -> Who_We_Serve:
    page.goto(base_url)
    NavigationMenu(page).navigate_to_nav_bar_item("Who We Serve")
    page.wait_for_load_state("networkidle")
    return Who_We_Serve(page, base_url)


# """TC-01: Verify that the Who We Serve page loads correctly and has the correct URL."""
# @pytest.mark.ui
# @pytest.mark.who_we_serve
# def test_who_we_serve_page_loads(page: Page, base_url):
#     open_who_we_serve(page, base_url)

#     expect(page).to_have_url(re.compile(r"/who-we-serve/?$"))
#     expect(page.locator("h1")).to_have_text("Who We Serve")
#     expect(page).to_have_title(re.compile(r"Who We Serve", re.IGNORECASE))


"""TC-02: Verify the 'Learn More' Button for the Public Companies Section."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_learn_more_button_for_public_companies(page: Page, base_url):
    who_we_serve = open_who_we_serve(page, base_url)
    who_we_serve.verify_section("Public Companies")
    who_we_serve.click_learn_more("Public Companies")


"""TC-03: Verify the Private Companies Section."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_private_companies_section(page: Page, base_url):
    who_we_serve = open_who_we_serve(page, base_url)
    who_we_serve.verify_section("Private Companies")
    who_we_serve.click_learn_more("Private Companies")


"""TC-04: Verify the Financial Institutions Section."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_financial_institutions_section(page: Page, base_url):
    who_we_serve = open_who_we_serve(page, base_url)
    who_we_serve.verify_section("Financial Institutions")
    who_we_serve.click_learn_more("Financial Institutions")


"""TC-05: Verify the Not-for-Profit Entities Section."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_not_for_profit_entities_section(page: Page, base_url):
    who_we_serve = open_who_we_serve(page, base_url)
    who_we_serve.verify_section("Not-for-Profit Entities")
    who_we_serve.click_learn_more("Not-for-Profit Entities")


"""TC-06: Verify the Connect With Us Heading and View Our Team Button."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_connect_with_us_heading_and_view_our_team_button(page: Page, base_url):
    who_we_serve = open_who_we_serve(page, base_url)
    who_we_serve.verify_connect_with_us_heading()
    who_we_serve.verify_view_our_team_button()


"""TC-07: Verify Links in the Who We Serve Navbar Dropdown."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_who_we_serve_navbar_dropdown_links(page: Page, base_url):
    who_we_serve = open_who_we_serve(page, base_url)
    who_we_serve.verify_who_we_serve_navbar_links()


"""TC-08: Verify the Who We Serve Page Performance Metrics."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_who_we_serve_page_performance_metrics(page: Page, base_url):
    who_we_serve = open_who_we_serve(page, base_url)
    performance_metrics = who_we_serve.get_performance_metrics()

    assert performance_metrics["load_time"] is not None
    assert performance_metrics["load_time"] < 3000, (
        f"Expected load time < 3000ms, got: {performance_metrics['load_time']}ms"
    )
    assert performance_metrics["first_contentful_paint"] is not None
    assert performance_metrics["first_contentful_paint"] < 2000, (
        "Expected first contentful paint < 2000ms, "
        f"got: {performance_metrics['first_contentful_paint']}ms"
    )
    if performance_metrics["largest_contentful_paint"] is not None:
        assert performance_metrics["largest_contentful_paint"] < 2500, (
            "Expected largest contentful paint < 2500ms, "
            f"got: {performance_metrics['largest_contentful_paint']}ms"
        )
    assert performance_metrics["cumulative_layout_shift"] < 0.1, (
        "Expected cumulative layout shift < 0.1, "
        f"got: {performance_metrics['cumulative_layout_shift']}"
    )


"""TC-09: Verify Accessibility Checks on the Who We Serve Page."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_who_we_serve_page_accessibility(page: Page, base_url):
    open_who_we_serve(page, base_url)

    results = Axe().run(page)
    violations = results.response["violations"]

    # Known existing violations on the site — documented but outside QA scope
    known_violations = {"color-contrast", "input-button-name", "link-name"}
    critical_violations = [
        violation
        for violation in violations
        if violation["impact"] in ("critical", "serious")
        and violation["id"] not in known_violations
    ]

    assert not critical_violations, (
        f"Found {len(critical_violations)} new critical/serious accessibility "
        "violation(s): "
        + "\n".join(
            f"  - {violation['id']}: {violation['description']}"
            for violation in critical_violations
        )
    )
