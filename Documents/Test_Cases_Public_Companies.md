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
- Page loads without errors.
- You are able to navigate and hover on the public companies webpage.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_public_companies_page_loads`)

## TC-002: Verify Browser Tab is named "
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Public Companies" in the nav bar.
2. Wait for page to fully load.
3. Verify browser tab title is exactly called "Professional Liability Insurance | D&O | LPL | EPL | Old Republic Pro".

### Expected Result: 
- Page loads without errors.
- Browser Tab Title is visible and correct.
- You are able to navigate and hover on the public companies webpage.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::verify_public_companies_page_browser_title`)