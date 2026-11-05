

# TC-001: Verify the Who We Serve Private Companies page loads correctly
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/en/who-we-serve/private-companies.
2. Wait for the page to load.

### Expected Result:
- The page loads successfully at `/who-we-serve/private-companies`.
- The "Private Companies" page heading is visible.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_private_companies.py::test_wws_private_companies_page_loads`)

# TC-002: Verify the two introductory paragraphs on the Private Companies page.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/en/who-we-serve/private-companies.
2. Wait for the page to load.

### Expected Result:
- The two introductory paragrah text are correct and visible.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_private_companies.py::test_wws_private_companies_introductory_paragraphs`)


# TC-003: Verify the ORPROtect coverage details button and text tiles beneath. 
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/en/who-we-serve/private-companies.
2. Wait for the page to load.

### Expected Result:
- The two introductory paragrah text are correct and visible.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_private_companies.py::test_wws_private_companies_orprotect_coverage_details`)


