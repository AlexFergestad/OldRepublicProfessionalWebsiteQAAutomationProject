# Test Cases Public Companies Excess Side A File

# TC-001: Verify that the public companies excess side a page loads correctly and has the correct URL when accessed from the home page.
**Priority**: High
**Type**: Functional/Smoke
**Preconditions**: 
- Have a computer/laptop connected to the internet.
- Be on a common web browser such as Chrome, Edge, FireFox, Safari.

### Steps to Reproduce:
1. Navigate to https://www.oldrepublicpro.com/.
2. Hover over "Public Companies" in the nav bar and select the second option called "Excess Side A".
3. Wait for page to fully load.

### Expected Result:
- Page loads without any errors.
- You are able to hover over the public companies text in the nav bar and click on "Excess Side A".

### Actual Result:
**Status**: ✅ Pass
**Automated**: Yes (`tests/test_public_companies_excesssidea.py::test_public_companies_excess_side_a_page_loads`)