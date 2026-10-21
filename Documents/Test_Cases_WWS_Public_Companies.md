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
