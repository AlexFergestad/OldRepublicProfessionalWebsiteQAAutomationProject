import pytest
from playwright.sync_api import Page

from tests.ui.page_objects.wws_financial_institutions_page_objects import (
    WWS_Financial_Institutions,
)

"""

Who We Serve Financial Institutions Page UI Tests
Test Cases: TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009

* This page verifies the Who We Serve Financial Institutions page of the Old Republic Professional website loads correctly,
has the expected , performance, and accessibility.

"""

"""TC-001: Verify the Who We Serve Financial Institutions page loads correctly."""
@pytest.mark.ui
@pytest.mark.wws_financial_institutions
def test_wws_financial_institutions_page_loads(page: Page, base_url: str):
    financial_institutions = WWS_Financial_Institutions(page, base_url)
    financial_institutions.open_page()
    financial_institutions.verify_page_loaded()


""""TC-002: Verify the Who We Serve Financial Institutions page has the expected title."""
@pytest.mark.ui
