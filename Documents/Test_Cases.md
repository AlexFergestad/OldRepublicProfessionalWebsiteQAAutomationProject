# Test Cases File

## TC-001: Homepage Loads Successfully
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Verify browser tab title is called "Professional Liability Insurance | D&O | LPL | EPL | Old Republic Pro"

### Expected Result: 
- Page loads without errors.
- Browser Tab Title is visible and correct.
- You are able to navigate and hover on the main webpage.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_homepage_loads`)


## TC-002: Verify Test Title says "Old Republic Professional"
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Top Right on the home page title says "Old Republic Professional"

### Expected Result: 
- Page loads without errors.
- H1 Title is visible and correct.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_page_title`)

## TC-003: Verify main header is visible and correct
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Verify on the middle of the page it exactly says "Industry leader of Management and Professional Liability, with 40 years of continuous experience."

### Expected Result: 
- Page loads without errors.
- Header is visible and exactly matches the intended text.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_main_header_visible_and_correct`)

## TC-004: Verify main header is visible and correct
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Verify on the middle of the page it exactly says "Industry leader of Management and Professional Liability, with 40 years of continuous experience."

### Expected Result: 
- Page loads without errors.
- Header is visible and exactly matches the intended text.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_main_header_visible_and_correct`)

