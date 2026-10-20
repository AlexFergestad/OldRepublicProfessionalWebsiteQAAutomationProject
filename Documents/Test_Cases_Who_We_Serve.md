# Test Cases Who We Serve File

## TC-001: Verify that the Who We Serve page loads correctly and has the correct URL.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on "Who We Serve" link in the nav bar.
3. Wait for page to fully load.

### Expected Result: 
- Page loads without any errors.
- Url looks correct and matches: "https://www.orprofessional.com/who-we-serve".
- You are able to navigate and hover on the who we serve webpage in the nav bar.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_who_we_serve.py::test_who_we_serve_page_loads`)

# TC-002: Verify the "Learn More" button for the Public Companies section
**Priority**: High
**Type**: Functional
**Preconditions**:
- Have an internet-connected computer and a supported web browser.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Open "Who We Serve" from the navigation bar.
3. Click the "Learn More" button in the Public Companies section.

### Expected Result:
- The Public Companies section is displayed with its expected heading and description.
- The button opens the Public Companies page.
- The destination URL is `/who-we-serve/public-companies` and its H1 is "Public Companies".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/ui/nav_bar_tests/test_who_we_serve.py::test_learn_more_button_for_public_companies`)

