

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
- The four sub titles in the tiles are correct.
- The "View Orprotect Coverage Details" button navigates to the correct url.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_private_companies.py::test_wws_private_companies_orprotect_coverage_details`)


# TC-004: Verify Side-A DIC Tile
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/en/who-we-serve/private-companies.
2. Wait for the page to load.
3. Test the Side-A DIC Tile and click on the tile's corresponding button.

### Expected Result:
- The Text in the Side-A title is correct.
- The "Lead Side-A" and "Excess Side-A" paragraphs are correct.
- The "View Side-A Coverage Details" button navigates to the correct url.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_private_companies.py::test_wws_private_companies_side_a_dic_tile`)

# TC-005: Verify Excess Tile
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/en/who-we-serve/private-companies.
2. Wait for the page to load.
3. Test the Excess Tile and click on the tile's corresponding button.

### Expected Result:
- The Text in the Excess title is correct.
- The "View Excess Coverage Details" button navigates to the correct url.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_private_companies.py::test_wws_private_companies_excess_tile`)

# TC-006: Verify Connect With Us Section
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/en/who-we-serve/private-companies.
2. Wait for the page to load.
3. Scroll Down to the "Connect With Us" section.

### Expected Result:
- The Connect With Us Header and Paragraph are correct.
- The "View Private Company Underwriters" button correctly navigfates to the expected url and functions properly.


### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_private_companies.py::test_connect_with_us_section`)


# TC-007: Verify the Other Segments We Serve Section
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/en/who-we-serve/private-companies.
2. Wait for the page to load.
3. Scroll Down to the "Other Segments We Serve" section.

### Expected Result:
- The "Other Segments We Serve" text is correct.
- The "Public Companies" tile is correct and navigates to the correct page/url.
- The "Public Companies" tile is correct and navigates to the correct page/url.
- The "Public Companies" tile is correct and navigates to the correct page/url.
