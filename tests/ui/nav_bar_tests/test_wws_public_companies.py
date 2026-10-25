import pytest
from playwright.sync_api import Page

from tests.ui.page_objects.wws_public_companies_page_objects import (
    WWS_Public_Companies,
)


"""TC-001: Verify the Who We Serve Public Companies page loads correctly."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_wws_public_companies_page_loads(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_page_loaded()


"""TC-002: Verify the two introductory paragraphs on the Public Companies page."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_wws_public_companies_introductory_paragraphs(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_introductory_paragraphs()


"""TC-003: Verify the View D&O Coverage Details button and destination."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_view_d_and_o_coverage_details_button(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_d_and_o_coverage_details_button()


"""TC-004: Verify the four Directors & Officers coverage descriptions."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_public_companies_d_and_o_coverage_descriptions(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_d_and_o_coverage_descriptions()


"""TC-005: Verify Employment Practices Liability and its coverage details button."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_wws_public_companies_epl_coverage_details(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_epl_coverage_details()


"""TC-006: Verify Fiduciary Liability and its coverage details button."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_wws_public_companies_fiduciary_coverage_details(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_fiduciary_coverage_details()


"""TC-007: Verify Excess coverage and its coverage details button."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_wws_public_companies_excess_coverage_details(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_excess_coverage_details()


"""TC-008: Verify Crime/Fidelity coverage and its coverage details button."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_wws_public_companies_crime_fidelity_coverage_details(
    page: Page, base_url: str
):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_crime_fidelity_coverage_details()


"""TC-009: Verify Connect with Us and the View public company underwriters button."""
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_wws_public_companies_connect_with_us_underwriters_button(
    page: Page, base_url: str
):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_connect_with_us_underwriters_button()

"""TC-010: Verify "Other Segments We Serve" title and buttons underneath: "Public Companies", "Financial Institutions", "Not-for-Profit Entities" """
@pytest.mark.ui
@pytest.mark.wws_public_companies
def test_other_segments_we_serve_and_buttons_underneath(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_other_segments_we_serve_and_buttons_underneath()


"""TC-011: Verify Who We Serve Public Companies Page Performance Metrics."""
@pytest.mark.ui
@pytest.mark.wws_public_companies



