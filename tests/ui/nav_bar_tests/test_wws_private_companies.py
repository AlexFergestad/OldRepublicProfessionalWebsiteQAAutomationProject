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
@pytest.mark.wws_public_companies
def test_wws_public_companies_page_loads(page: Page, base_url: str):
    private_companies = WWS_Private_Companies(page, base_url)





