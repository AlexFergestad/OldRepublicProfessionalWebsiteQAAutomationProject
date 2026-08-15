# This file is for automating the testing of the excess liability page in the public companies section in the nav bar.

import playwright
import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_dando_liability_page_objects import Public_Company_Dando_Liability
from tests.ui.page_objects.public_companies_excess_liability_page_objects import Public_Company_Excess_Liability

"""

Public Companies Excess Liability Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005

* This page verifies the Excess Liability page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

# """TC-01: Verify that the public companies excess liability page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_liability
# def test_public_companies_excess_liability_page_loads_correctly(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Excess_Liability(page, base_url).navigate_to_excess_liability_page()

#     # Verifies that the page has loaded correctly by checking the URL and the page title
#     page.wait_for_load_state("networkidle")


# """TC-02: Verify that the public companies excess liability page has the correct title."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_liability
# def test_public_companies_excess_liability_page_title(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Excess_Liability(page, base_url).navigate_to_excess_liability_page()

#     # Verifies the title of the page is correct
#     Public_Company_Excess_Liability(page, base_url).verify_excess_liability_h1()

# """TC-03: Verify the H1 paragraph underneath has the correct text."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_liability
# def test_public_companies_excess_liability_page_title_paragraph(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Excess_Liability(page, base_url).navigate_to_excess_liability_page()

#     # Verifies the h1 paragraph
#     Public_Company_Excess_Liability(page, base_url).verify_h1_paragraph()

# """TC-04: Verify policy features and bullet points underneath."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_liability
# def test_policy_features_and_bullet_points_underneath(page: Page, base_url):
    
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Excess_Liability(page, base_url).navigate_to_excess_liability_page()

#     # Verifies policy features and the bullet points undereath
#     Public_Company_Excess_Liability(page, base_url).verify_policy_features()


# """TC-05: Verify Capacity, Attachment, Eligibility, are correct and that the 'Download Excess D&O Sell Sheet' button is clickable/navigates to the correct page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_liability
# def test_capacity_attachment_eligibility_and_download_excess_sell_sheet_button(page: Page, base_url):

#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Excess_Liability(page, base_url).navigate_to_excess_liability_page()

#     # Clicks on Capacity, Attachment, Eligibility, and the 'Download Excess D&O Sell Sheet' button
#     Public_Company_Excess_Liability(page, base_url).verify_capacity_attachment_eligibility_and_download_button()

# """TC-06: Verify Our Excess Plus™ Endorsement Link and Paragraph Underneath."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_liability
# def test_our_excess_plus_endorsement_link_and_paragraph_underneath(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Excess_Liability(page, base_url).navigate_to_excess_liability_page()

#     # Verifies the Our Excess Plus™ Endorsement link and paragraph underneath
#     Public_Company_Excess_Liability(page, base_url).verify_our_eccess_plus_endorsement_link_and_paragraph()

# """TC-07: Verify How Excess Plus™ Works and Bullet Points Underneath."""
# @pytest.mark.ui
# @pytest.mark.public_companies_excess_liability
# def test_how_excess_plus_works_and_bullet_points_underneath(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Excess Liability link to navigate to the excess liability page
#     Public_Company_Excess_Liability(page, base_url).navigate_to_excess_liability_page()

#     # Verifies the How Excess Plus™ Works and Bullet Points Underneath
#     Public_Company_Excess_Liability(page, base_url).verify_how_excess_plus_works_and_bullet_points()

"""TC-08: Verify the Excess Plus Benefits and Bullet Points Underneath."""
@pytest.mark.ui
@pytest.mark.public_companies_excess_liability
def test_
