# Test Cases Public Companies Excess Liability File

# TC-001: Verify that the public companies excess liability page loads correctly and has the correct URL when accessed from the home page
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Liability".
3. Wait for page to fully load.

### Expected Result:
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Excess Liability".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excess_liabilit.py::test_public_companies_excess_liability_page_loads_correctly`)

# TC-002: Verify that the public companies excess liability page has the correct title
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Liability".
3. Wait for page to fully load.
4. Verify that the h1 says "Excess D&O and Excess Plus™".

### Expected Result:
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Excess Liability".
- The H1 title says "Excess D&O and Excess Plus™".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excess_liabilit.py::test_public_companies_excess_liability_page_title`)



# TC-003: Verify the H1 paragraph underneath has the correct text
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Liability".
3. Wait for page to fully load.
4. Verify that the h1 paragraph says "Intended to follow the underlying policy(s) in a layered program, excess policies are the building blocks that make up the towers of D&O and other Management Liability protection. ORUG-91 is our excess policy form for public company and private company policyholders".

### Expected Result:
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Excess Liability".
- The H1 title says "Intended to follow the underlying policy(s) in a layered program, excess policies are the building blocks that make up the towers of D&O and other Management Liability protection. ORUG-91 is our excess policy form for public company and private company policyholders".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excess_liabilit.py::test_public_companies_excess_liability_page_title_paragraph`)


# TC-004: Verify policy features and bullet points underneath
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Liability".
3. Wait for page to fully load.
4. Verify that the  policy features title is correct and the bullet points underneath include:
    -  "One-page".
    - "Market-leading erosion language".
    - "Shareholder Derivative Demand Investigations".
    - "Excess Flex™".

### Expected Result:
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Excess Liability".
- The Policy Features title is correct and the following accept criteria text is included in the paragraph underneath. 

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excess_liability.py::test_policy_features_and_bullet_points_underneath`)


# TC-005: Verify Capacity, Attachment, Eligibility, are correct and that the 'Download Excess D&O Sell Sheet' button is clickable/navigates to the correct page.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:  
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Liability".
3. Wait for page to fully load.

## Expected Result:
- Verify "Capacity", "Attachment", "Eligibility" sections display correct.
- Verify the 'Download Excess D&O Sell Sheet' button is clickable/navigates to the correct page.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excess_liability.py:: test_capacity_attachment_eligibility_and_download_excess_sell_sheet_button`)

# TC-006: Verify Our Excess Plus™ Endorsement Link and Paragraph Underneath.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:  
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Liability".
3. Wait for page to fully load.


## Expected Result:
- Verify "Capacity", "Attachment", "Eligibility" sections display correct.
- Verify the 'Excess Plus™ Endorsement' Link and the Paragraph underneath work as expected.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excess_liability.py:: test_our_excess_plus_endorsement_link_and_paragraph_underneath`)

# TC-007: Verify How Excess Plus™ Works and Bullet Points Underneath.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**:  
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Liability".
3. Wait for page to fully load.

## Expected Result:
- Verify "Capacity", "Attachment", "Eligibility" sections display correct.
- Verify the 'Excess Plus™ Endorsement' Link and the Paragraph underneath work as expected.