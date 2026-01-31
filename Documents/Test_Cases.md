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

## TC-004: Verify company description/subheading is visible and correct
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Verify on the middle of the page it exactly says "Old Republic Professional underwrites insurance" at the start of the subheading.

### Expected Result: 
- Page loads without errors.
- Subheading is visible and exactly matches the intended text.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_company_description_visible`)

## TC-005: Verify the Insurance Type Card Images and their Titles Are Visible
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Verify on the middle of the page the insurance type cards and their titles are visible on the page.

### Expected Result: 
- Page loads without errors.
- Card images and their titles are visible and exactly matches the intended text.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_insurance_type_cards_and_links_visible`)

## TC-006: Verify when clicking the Insurance Type Card Images and Titles, it brings a User to a new page 
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Click on an image title.
4. Verify that it brings you to the correct next page.
5. Click the back arrow or type the address "https://www.oldrepublicpro.com/" into the url.
6. Click the image itself and verify that it brings you to the correct next page.
7. Rinse and repeat for each insurance type card title and image.


### Expected Result: 
- Each insurance type card image and their title bring the user to the next/correct page.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_insurance_cards_clickable`)

## TC-007: Verify Contact Us is visible and links correctly to the contact page
**Priority**: Medium
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Wait for page to fully load.
3. Click on the "Contact" button in the nav bar. 
4. Verify that it brings you to the contact page.
5. Click on the Old Republic Professional image on the top left.
6. Verify that the user was brought to the homepage.
7. Verify that the image itself is visible and displays correct.


### Expected Result: 
- User will go from the contac page to the home page and the Old Republic Professional Logo will display correct.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_contact_us_link`)

