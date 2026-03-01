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

## TC-003: Verify the Careers Header is on the Careers page.
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

## TC-004: Verify LinkedIn Link Works as Intended
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the LinkedIn Link that says "inShare".
3. Verify that it opens up another window and asks for the user to sign in.

### Expected Result: 
- Career page loads without errors.
- LinkedIn Link is Visible.
- LinkedIn link opens up another window prompting a sign in to enter in username and password to LinkedIn. 

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_careers_page_linkedin_link`)

## TC-005: Verify the intern job listing link on the careers page.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Underwriting Analyst Intern" link.
3. Verify that it opens up another page with more information about the role. 

### Expected Result: 
- Career page loads without errors.
- "Underwriting Analyst Intern" link is visible.
- The role link brings the user to a new page.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_careers_page_intern_listing`)

## TC-006: Verify Job Description for Underwriting Analyst Intern.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Underwriting Analyst Intern" link.
3. Verify that it opens up another page with information such as "Job Description" and the paragraph below it. 

### Expected Result: 
- Career page loads without errors.
- The role link brings the user to a new page with more information about the role including a job description and the paragraph going into more detail right below it.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_careers_page_intern_job_description`)

## TC-007: Verify Job Requirements in the Intern Position
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Underwriting Analyst Intern" link.
3. Verify that it opens up another page displaying the job requirements for the intern role.

### Expected Result: 
- Career page loads without errors.
- The role link brings the user to a new page with more information about the role including the job requirements for the intern role.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_careers_page_intern_job_requirements`)

## TC-008: Verify About Old Republic Professional Section
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Underwriting Analyst Intern" link.
3. Verify that it opens up another page displaying the "About Old Republic Professional" heading and paragraph for the intern role.

### Expected Result: 
- Career page loads without errors.
- The role link brings the user to a new page with more information about the role including the about the company header and paragraph for the intern role.

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_homepage.py::test_about_orpro_section`)

## TC-009: Verify Culture Section
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Click on the "Underwriting Analyst Intern" link.
3. Verify that it opens up another page displaying the "Culture" heading and paragraph for the intern role.

### Expected Result: 
- Career page loads without errors.
- The role link brings the user to a new page with more information about the role and includes the "Culture" header and the paragraph underneath.
### Actual Result:
**Status**: ✅ Pas
**Automated**: Yes (`tests/test_homepage.py::test_culture_section`)