# Test Cases Careers File

## TC-001: Career Page Loads Successfully
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Careers" button to the left of the search bar on the top left of the screen.

### Expected Result: 
- Career page loads without errors.
- The browser navigates to the correct page.
- At the end of the url, it includes "/careers".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_careers_page_loads`)

## TC-002: Browser Tab Title is Correct
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Careers" button to the left of the search bar on the top left of the screen.

### Expected Result: 
- Career page loads without errors.
- The browser navigates to the correct page.
- The browser tab title is called "Careers at ORPRO".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_careers_page_browser_tab`)

## TC-003: Verify H1 Heading is Visible
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Careers" button to the left of the search bar on the top left of the screen.

### Expected Result: 
- Career page loads without errors.
- The browser navigates to the correct page.
- The careers page displays a h1 heading named "Careers at ORPRO".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_careers_page_header`)
