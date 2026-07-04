# This file is for automating the testing of the products page in the public companies section in the nav bar.

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe

# Page Objects - relative import from same ui folder
from tests.ui.page_objects.careers_page_object import CareersPage
from tests.ui.page_objects.nav_bar_page_objects import NavigationMenu
from tests.ui.page_objects.public_companies_page_objects import Public_Company_Liability_Overview
from tests.ui.page_objects.public_companies_products_page_objects import Public_Company_Products

"""

Public Companies Products Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006

* This page verifies the Products page of the Old Republic Professional website loads correctly, 
has the correct title and headers, performanced checks the page, and accessibility checks the page.

"""

# """TC-01: Verify that the public companies products page loads correctly and has the correct URL when accessed from the home page."""
# @pytest.mark.ui
# @pytest.mark.public_companies_products_page
# def test_public_companies_products_page_loads(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Public Companies menu item to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Products link to navigate to the products page
#     Public_Company_Products(page, base_url).navigate_to_products_page()

#     # Verifies that the products page loads correctly and has the correct URL
#     page.wait_for_load_state("networkidle")

# """TC-02: Verify H1 Title in Products Page"""
# @pytest.mark.ui
# @pytest.mark.public_companies_products_page
# def test_h1_title_in_products_page(page: Page, base_url): 
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Products link to navigate to the products page
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Products link to navigate to the products page
#     Public_Company_Products(page, base_url).navigate_to_products_page()

#     # Verifies that the H1 title is correct
#     Public_Company_Products(page, base_url).verify_products_h1()

# """TC-03: Verify Primary Traditional D&O Bullet Point"""
# @pytest.mark.ui
# @pytest.mark.public_companies_products_page
# def test_primary_traditional_d_and_o_bullet_point(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Products link to navigate to the public companies nav bar dropdown
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Products link to navigate to the products page
#     Public_Company_Products(page, base_url).navigate_to_products_page()

#     # Clicks on the Primary, Traditional D&O bullet point to verify it is clickable and navigates to the correct page
#     Public_Company_Products(page, base_url).verify_primary_traditional_d_and_o_bullet_point()


# """TC-04: Verify Excess Liability Bullet Point"""
# @pytest.mark.ui
# @pytest.mark.public_companies_products_page
# def test_excess_liability_bullet_point(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Products link to navigate to the public companies nav bar dropdown
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Products link to navigate to the products page  
#     Public_Company_Products(page, base_url).navigate_to_products_page()

#     # Clicks on the Excess Liability bullet point to verify it is clickable and navigates to the correct page
#     Public_Company_Products(page, base_url).verify_excess_liability_bullet_point()

# """TC-05: Verify Lead Side A Bullet Point"""
# @pytest.mark.ui
# @pytest.mark.public_companies_products_page
# def test_lead_side_a_bullet_point(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Products link to navigate to the public companies nav bar dropdown
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")
    
#     # Clicks on the Products link to navigate to the products page
#     Public_Company_Products(page, base_url).navigate_to_products_page()

#     # Clicks on the Lead Side A bullet point to verify it is clickable and navigates to the correct page
#     Public_Company_Products(page, base_url).verify_lead_side_a_bullet_point()

# """TC-06: Verify Excess Side A Bullet Point"""
# @pytest.mark.ui
# @pytest.mark.public_companies_products_page
# def test_excess_side_a_bullet_point(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Products link to navigate to the public companies nav bar dropdown
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Products link to navigate to the products page
#     Public_Company_Products(page, base_url).navigate_to_products_page()

#     # Clicks on the Excess Side A bullet point to verify it is clickable and navigates to the correct page
#     Public_Company_Products(page, base_url).verify_excess_side_a_bullet_point()

# """TC-07: Verify Contact Us Button"""
# @pytest.mark.ui
# @pytest.mark.public_companies_products_page
# def test_contact_us_button(page: Page, base_url):
#     # Goes to the home page first
#     page.goto(base_url)

#     # Clicks on the Products link to navigate to the public companies nav bar dropdown
#     NavigationMenu(page).navigate_to_nav_bar_item("Public Companies")

#     # Clicks on the Products link to navigate to the products page
#     Public_Company_Products(page, base_url).navigate_to_products_page()

#     # Clicks on the Contact Us button to verify it is clickable and navigates to the correct page
#     Public_Company_Products(page, base_url).verify_contact_us_button()


"""TC-08: Verify Performance Metrics"""
@pytest.mark.ui
@pytest.mark.public_companies_products_page
def test_performance_metrics_products_page(page: Page, base_url):
    # Goes to the home page first
    

# """TC-09: Verify Accessibility Checks"""