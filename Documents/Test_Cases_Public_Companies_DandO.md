# Test Cases Public Companies D and O File

## TC-001: Homepage Loads Successfully
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the first option called "Directors and Officers Liability".
3. Wait for page to fully load.

### Expected Result: 
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Directors and Officers Liability".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_dando.py::test_public_companies_directors_and_officers_liability_page_loads`)

## TC-002: Verify H1 Title and Who We Are Paragraph
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the first option called "Directors and Officers Liability".
3. Verify that the title says "Directors & Officers Liability".
4. Verify the "Who We Are Paragraph" says "Old Republic Professional...New York".

### Expected Result: 
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Directors and Officers Liability".
- The title says "Directors & Officers Liability".
- The "Who We Are Paragraph" says "Old Republic Professional...New York".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_dando.py::test_who_we_are_paragraph`)

## TC-003: Verify What We Offer Section
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the first option called "Directors and Officers Liability".
3. Verify that the title says "What We Offer: ".
4. Verify the consistency, experienced underwriting, and experienced in house claims staff lists.

### Expected Result: 
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Directors and Officers Liability".
- The title says "What We Offer: ".
- The consistency, experienced underwriting, and experienced in house claims staff lists have correct text.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_dando.py::test_verify_what_we_offer_section`)

## TC-004: Verify Public Companies Section on the Right
**Priority**: High
**Type**: Functional
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Directors and Officers Liability" inside the "Public Companies" section in the nav bar.
2. Wait for the page to fully load.
3. View the Links in the "Public Companies" section on the right.

### Expected Result: 
- Page loads without any errors.
- You are able to navigate and hover on the public companies webpage.
- The Right Section links go to the correct url and url itself is valid.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_dando.py::test_public_companies_right_section`)

## TC-005: Verify D&O Products Link
**Priority**: High
**Type**: Functional
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Directors and Officers Liability" inside the "Public Companies" section in the nav bar.
3. Wait for the page to fully load.
4. Click on the "D&O Products" link.

### Expected Result: 
- Page loads without any errors.
- You are able to navigate and hover on the public companies webpage.
- After clicking the "D&O Products" link, it correctly brings you to the correct page. 

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_dando.py::test_verify_dando_products_link`)
