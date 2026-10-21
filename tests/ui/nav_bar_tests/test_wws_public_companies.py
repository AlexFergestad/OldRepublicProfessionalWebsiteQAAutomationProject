import pytest
from playwright.sync_api import Page

from tests.ui.page_objects.wws_public_companies_page_objects import (
    WWS_Public_Companies,
)


"""TC-001: Verify the Who We Serve Public Companies page loads correctly."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_wws_public_companies_page_loads(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_page_loaded()


"""TC-002: Verify the two introductory paragraphs on the Public Companies page."""
@pytest.mark.ui
@pytest.mark.who_we_serve
def test_wws_public_companies_introductory_paragraphs(page: Page, base_url: str):
    public_companies = WWS_Public_Companies(page, base_url)
    public_companies.open_page()
    public_companies.verify_introductory_paragraphs()
