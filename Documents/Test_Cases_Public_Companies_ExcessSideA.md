# Test Cases Public Companies Excess Side A File

# TC-001: Verify that the public companies excess side a page loads correctly and has the correct URL when accessed from the home page.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Side A-Only".
3. Wait for page to fully load.

### Expected Result:
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Excess Side A-Only".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excesssidea.py::test_public_companies_excess_side_a_page_loads`)

# TC-002: Verify that the public companies excess side a page has the correct title and headers.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Side A-Only".
3. Wait for page to fully load.

### Expected Result:
- Page loads without any errors.
- The browser title exactly says "Excess Side-A D&O | Public Company D & O | Old Republic Professional".
- The header exactly says "Excess Side-A D&O".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excesssidea.py::test_public_companies_excess_side_a_page_title_and_headers`)

# TC-003: Verify Policy features bullet point list, the capacity, and the eligibility text are correct.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Side A-Only".
3. Wait for page to fully load.

### Expected Result:
- Page loads without any errors.
- The policy features sub title says "Policy features (ORUG-92):".
- There are 4 bulleted points underneath.
- The capacity line says "Capacity: Up to $25,000,000 per Claim / $50,000,000 Aggregate in a single layer or split over more than one layer.".
- The Eligibility line says "Eligibility: All U.S. public and private companies.".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excesssidea.py::test_public_companies_excess_side_a_page_policy_features`)

# TC-004: Verify that the public companies excess side a page has the correct download buttons and that they are functional.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Side A-Only".
3. Wait for page to fully load.

### Expected Result:
- Page loads without any errors.
- Clicking the "Download Excess Side-A Sell Sheet" button navigates to the correct page.
- The header exactly says "Excess Side-A D&O".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excesssidea.py::test_public_companies_excess_side_a_page_download_buttons`)


