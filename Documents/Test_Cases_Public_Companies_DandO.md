# Test Cases Public Companies D and O File

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
**Automated**: Yes (`tests/test_public_companies_dando.py::test_public_companies_directors_and_officers_liability_page_loads`)