import pytest
from playwright.sync_api import Page

from tests.ui.page_objects.wws_private_companies_page_objects import (
    WWS_Private_Companies,
)


"""

Who We Serve Private Companies Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004 

* This page verifies the Who We Serve Public Companies page of the Old Republic Professional website loads correctly,
has the expected , performance, and accessibility.

"""

"""TC-001: Verify the Who We Serve Private Companies page loads correctly."""
@pytest.mark.ui
@pytest.mark.wws_private_companies
def test_wws_private_companies_page_loads(page: Page, base_url: str):
    private_companies = WWS_Private_Companies(page, base_url)
    private_companies.open_page()
    private_companies.verify_page_loaded()


"""TC-002: Verify the two introductory paragraphs on the Private Companies page. """
@pytest.mark.ui
@pytest.mark.wws_private_companies
def test_wws_private_companies_introductory_paragraphs(page: Page, base_url: str):
    private_companies = WWS_Private_Companies(page, base_url)
    private_companies.open_page()
    private_companies.verify_introductory_paragraphs()


"""TC-003: Verify the ORPROtect coverage details button and text tiles beneath. """
@pytest.mark.ui
@pytest.mark.wws_private_companies
def test_wws_private_companies_orprotect_coverage_details(page: Page, base_url: str):
    private_companies = WWS_Private_Companies(page, base_url)
    private_companies.open_page()
    private_companies.verify_orprotect_coverage_details()


"""TC-004: Verify Side-A DIC Tile"""
@pytest.mark.ui
@pytest.mark.wws_private_companies
def test_wws_private_companies_side_a_dic_tile(page: Page, base_url: str):
    private_companies = WWS_Private_Companies(page, base_url)
    private_companies.open_page()
    private_companies.verify_side_a_dic_tile()


"""TC-005: Verify Excess Tile"""
@pytest.mark.ui
@pytest.mark.wws_private_companies
def test_wws_private_companies_excess_tile(page: Page, base_url: str):
    private_companies = WWS_Private_Companies(page, base_url)
    private_companies.open_page()
    private_companies.verify_excess_tile()


"""TC-006: Verify Connect With Us Section"""
@pytest.mark.ui
