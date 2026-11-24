# TC-001: Verify the Who We Serve Financial Institutions page loads correctly.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/financial-institutions.
2. Wait for the page to load.

### Expected Result:
- The page loads successfully at `who-we-serve/financial-institutions`.
- The "Financial Institutions" page heading is visible.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_financial_institutions::test_wws_financial_institutions_page_loads`)


# TC-002: Verify the Who We Serve Financial Institutions page has the expected title.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/financial-institutions.
2. Wait for the page to load.

### Expected Result:
- The page loads successfully at `who-we-serve/financial-institutions`.
- The browser tab title says "Financial Institutions | Old Republic Professional".


### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_financial_institutions.py::test_wws_financial_institutions_page_title`)


# TC-003: Verify the Who We Serve Financial Institutions page heading and sub-heading.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/financial-institutions.
2. Wait for the page to load.

### Expected Result:
- The page loads.
- The heading says "Financial Institutions".
- The subheading says "Specialized underwriting for financial institutions".


### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_financial_institutions.py::test_wws_financial_institutions_page_heading`)


# TC-004: Verify top introductory paragraph content on the Who We Serve Financial Institutions page.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/financial-institutions.
2. Wait for the page to load.

### Expected Result:
- The page loads.
- The left paragraph says "Old Republic Professional's dedicated Financial Institutions team".
- The right paragraph says "".


### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_financial_institutions.py::test_wws_financial_institutions_page_intro_paragraphs`)