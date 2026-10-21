# TC-001: Verify the Who We Serve Public Companies page loads correctly
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.

### Expected Result:
- The page loads successfully at `/who-we-serve/public-companies`.
- The "Public Companies" page heading is visible.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_wws_public_companies_page_loads`)
