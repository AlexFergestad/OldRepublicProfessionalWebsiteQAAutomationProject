# Test Cases Public Companies File

## TC-001: Homepage Loads Successfully
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Public Companies" in the nav bar.
3. Wait for page to fully load.

### Expected Result: 
- Page loads without any errors.
- You are able to navigate and hover on the public companies webpage.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_public_companies_page_loads`)

## TC-002: Verify Browser Tab is Correct
**Priority**: High
**Type**: Functional
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Public Companies" in the nav bar.
2. Wait for page to fully load.
3. Verify browser tab title is exactly called "Professional Liability Insurance | D&O | LPL | EPL | Old Republic Pro".

### Expected Result: 
- Page loads without any errors.
- Browser Tab Title is visible and correct.
- You are able to navigate and hover on the public companies webpage.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_public_companies_page_browser_title`)

## TC-003: Verify Header and Paragraphs
**Priority**: High
**Type**: Functional
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Public Companies" in the nav bar.
2. Wait for page to fully load.
3. View the Heading and Paragraphs.

### Expected Result: 
- Page loads without any errors.
- You are able to navigate and hover on the public companies webpage.
- The following is verified for the heading and paragraphs:
    - Grammar is correct ✓
    - Spelling is correct ✓
    - Tone is appropriate ✓
    - Information is accurate ✓

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_public_companies_page_heading_and_paragraph`)

## TC-004: Verify Top Image
**Priority**: High
**Type**: Functional
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Public Companies" in the nav bar.
2. Wait for page to fully load.
3. View the Top Image.

### Expected Result: 
- Page loads without any errors.
- You are able to navigate and hover on the public companies webpage.
- The Top Image looks correct.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_top_image_in_public_companies_page`)

## TC-005: Verify Public Companies Section on the Right
**Priority**: High
**Type**: Functional
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Public Companies" in the nav bar.
2. Wait for the page to fully load.
3. View the Links in the "Public Companies" section on the right.

### Expected Result: 
- Page loads without any errors.
- You are able to navigate and hover on the public companies webpage.
- The Right Section links go to the correct url and url itself is valid.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_public_companies_right_section`)

## TC-006: Verify Public Companies Page Performance Metrics
**Priority**: High
**Type**: Functional
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Public Companies" in the nav bar.
2. Record how long it takes for the public companies page to load.
4. Make sure the page loads in less than 4 seconds.

### Expected Result: 
- Page loads without any errors.
- You are able to navigate and hover on the public companies webpage.
- Page

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_public_companies_page_performance_metrics`)
