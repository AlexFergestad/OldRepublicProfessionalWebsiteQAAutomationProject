# Test Cases Who We Serve File

## TC-001: Verify that the Who We Serve page loads correctly and has the correct URL.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Who We Serve" link in the nav bar.
3. Wait for page to fully load.

### Expected Result: 
- Page loads without any errors.
- Url looks correct and matches: "https://www.orprofessional.com/who-we-serve".
- You are able to navigate and hover on the who we serve webpage in the nav bar.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_who_we_serve.py::test_who_we_serve_page_loads`)

# TC-002: Verify the "Learn More" button for the Public Companies section
**Priority**: High
**Type**: Functional
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Open "Who We Serve" from the navigation bar.
3. Click the "Learn More" button in the Public Companies section.

### Expected Result:
- The Public Companies section is displayed with its expected heading and description.
- The button opens the Public Companies page.
- The destination URL is `/who-we-serve/public-companies` and its H1 is "Public Companies".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_who_we_serve.py::test_learn_more_button_for_public_companies`)

# TC-003: Verify the Private Companies section and "Learn More" button
**Priority**: High
**Type**: Functional
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Open "Who We Serve" from the navigation bar.
3. Select the Private Companies tab.
4. Verify the section heading and description.
5. Click the "Learn More" button.

### Expected Result:
- The Private Companies tab is selected and its section heading and description are displayed.
- The button opens the Private Companies page.
- The destination URL is `/en/who-we-serve/private-companies` and its H1 is "Private Companies".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_who_we_serve.py::test_private_companies_section`)

# TC-004: Verify the Financial Institutions section and "Learn More" button
**Priority**: High
**Type**: Functional
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Open "Who We Serve" from the navigation bar.
3. Select the Financial Institutions tab.
4. Verify the section heading and description.
5. Click the "Learn More" button.

### Expected Result:
- The Financial Institutions tab is selected and its section heading and description are displayed.
- The button opens the Financial Institutions page.
- The destination URL is `/who-we-serve/financial-institutions` and its H1 is "Financial Institutions".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_who_we_serve.py::test_financial_institutions_section`)

# TC-005: Verify the Not-for-Profit Entities section and "Learn More" button
**Priority**: High
**Type**: Functional
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Open "Who We Serve" from the navigation bar.
3. Select the Not-for-Profit Entities tab.
4. Verify the section heading and description.
5. Click the "Learn More" button.

### Expected Result:
- The Not-for-Profit Entities tab is selected and its section heading and description are displayed.
- The button opens the Not-for-Profit Entities page.
- The destination URL is `/who-we-serve/not-for-profit-entities` and its H1 is "Not-for-Profit Entities".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_who_we_serve.py::test_not_for_profit_entities_section`)

# TC-006: Verify the "Connect With Us" heading and "View Our Team" button
**Priority**: High
**Type**: Functional
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Open "Who We Serve" from the navigation bar.
3. Scroll to the "Connect With Us" section.
4. Verify the H2 heading and click "View Our Team".

### Expected Result:
- The H2 heading "Connect With Us" is visible.
- The "View Our Team" button navigates to `/team?filter=underwriters`.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_who_we_serve.py::test_connect_with_us_heading_and_view_our_team_button`)

# TC-007: Verify links in the Who We Serve navigation dropdown
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported desktop web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/ and open "Who We Serve".
2. Hover over "Who We Serve" in the navigation bar.
3. Click "Public Companies" and wait one second.
4. Return to the page's navigation bar and click "Private Companies".
5. Return to the navigation bar, click "Financial Institutions", and wait one second.
6. Return to the navigation bar, click "Not-for-Profit Entities", and wait one second.

### Expected Result:
- Each dropdown link is visible and points to its corresponding Who We Serve page.
- Each click navigates to the matching URL in the requested order.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_who_we_serve.py::test_who_we_serve_navbar_dropdown_links`)
