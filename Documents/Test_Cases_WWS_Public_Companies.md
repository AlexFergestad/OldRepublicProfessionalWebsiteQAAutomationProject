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

# TC-002: Verify the introductory paragraphs on the Public Companies page
**Priority**: High
**Type**: Functional/Content
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Read the two introductory paragraphs below the Public Companies page heading.

### Expected Result:
- The first paragraph reads: "Public companies operate in a complex environment shaped by volatile financial markets, economic uncertainty, evolving regulations, technological disruption, and shifting social expectations."
- The second paragraph reads: "Executives must navigate heightened scrutiny from shareholders, regulators, customers, employees, and other stakeholders. Even well-managed organizations employing the most robust risk management practices may face allegations resulting in distraction, expense and reputational harm. Aligning with a stable Management Liability insurance provider plays a critical role in helping safeguard leadership against potential financial and reputational exposures."

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_wws_public_companies_introductory_paragraphs`)

# TC-003: Verify the "View D&O Coverage Details" button
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Click "View D&O Coverage Details" in the Directors & Officers Liability section.

### Expected Result:
- The button is visible and links to `/coverages/directors-and-officers-liability`.
- Clicking the button navigates to the Directors & Officers Liability coverage page.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_view_d_and_o_coverage_details_button`)

# TC-004: Verify Public Primary D&O, Lead Side-A, Excess D&O, and Excess Side-A text
**Priority**: High
**Type**: Functional/Content
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Review the four coverage descriptions in the Directors & Officers Liability section.

### Expected Result:
- "Public Primary D&O" displays "First-layer D&O coverage for publicly traded companies."
- "Lead Side-A" displays "Dedicated Side-A coverage for non-indemnifiable loss."
- "Excess D&O" displays "Additional capacity above underlying public company D&O."
- "Excess Side-A" displays "Additional Side-A limits for layered public company programs."

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_public_companies_d_and_o_coverage_descriptions`)

# TC-005: Verify Employment Practices Liability and its coverage details button
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Verify the "Employment Practices Liability" section.
4. Click "View EPL Coverage Details".

### Expected Result:
- The Employment Practices Liability heading and button are visible.
- The button navigates to `/coverages/employment-practices-liability`.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_wws_public_companies_epl_coverage_details`)

# TC-006: Verify Fiduciary Liability and its coverage details button
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Verify the "Fiduciary Liability" section.
4. Click "View Fiduciary Coverage Details".

### Expected Result:
- The Fiduciary Liability heading and button are visible.
- The button navigates to `/coverages/fiduciary-liability`.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_wws_public_companies_fiduciary_coverage_details`)

# TC-007: Verify Excess coverage and its coverage details button
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Verify the "Excess" section.
4. Click "View Excess Coverage Details".

### Expected Result:
- The Excess heading and button are visible.
- The button navigates to `/coverages/solutions/excess`.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_wws_public_companies_excess_coverage_details`)

# TC-008: Verify Crime/Fidelity coverage and its coverage details button
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Verify the "Crime/Fidelity" section.
4. Click "View Crime/Fidelity Coverage Details".

### Expected Result:
- The Crime/Fidelity heading and button are visible.
- The button navigates to `/coverages/crime-and-fidelity`.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_wws_public_companies_crime_fidelity_coverage_details`)

# TC-009: Verify Connect with Us and the View public company underwriters button
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Verify the "Connect with Us" heading.
4. Click "View public company underwriters".

### Expected Result:
- The "Connect with Us" heading and button are visible.
- The button navigates to `/team?filter=public-company-underwriters`.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_wws_public_companies_connect_with_us_underwriters_button`)

## TC-010: Verify "Other Segments We Serve" title and buttons underneath: "Public Companies", "Financial Institutions", "Not-for-Profit Entities" 
**Priority**: High
**Type**: Functional/Navigation
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Verify the "Other Segments We Serve" title is correct.
4. Verify the buttons underneath function correctly and navigate to the correct url.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_other_segments_we_serve_and_buttons_underneath`)

# TC-011: Verify Public Companies page performance metrics
**Priority**: High
**Type**: Non-Functional/Performance
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to finish loading.
3. Measure the page's navigation and rendering performance metrics.

### Expected Result:
- Page load time is less than 3,000 ms.
- First Contentful Paint is less than 2,000 ms.
- Largest Contentful Paint is less than 2,500 ms when the browser provides the metric.
- Cumulative Layout Shift is less than 0.1.

### Actual Result:
**Status**: ❌ Fail — load time was 3,568 ms, exceeding the 3,000 ms threshold during validation.
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_who_we_serve_public_companies_page_performance_metrics`)

# TC-012: Verify accessibility checks on the Public Companies page
**Priority**: High
**Type**: Non-Functional/Accessibility
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/who-we-serve/public-companies.
2. Wait for the page to load.
3. Run axe accessibility checks on the page.

### Expected Result:
- The accessibility audit completes successfully.
- No new critical or serious accessibility violations are reported.
- Known existing violations (`color-contrast`, `input-button-name`, and `link-name`) are excluded from the failure criteria.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_wws_public_companies.py::test_who_we_serve_public_companies_accessibility`)
