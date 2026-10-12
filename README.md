
Automated UI test suite for the public [Old Republic Professional](https://www.oldrepublicpro.com/) website, built with **Python, Playwright, and Pytest**. The suite covers link validation, page performance, and accessibility (axe-core) across the site's navigation pages, using the **Page Object Model** for maintainable, reusable tests.

> **Status:** In progress. Navigation bar pages are covered first; additional pages and test types are being added.

## Highlights

- **60+ automated UI tests** across the navigation bar pages
- **Link validation**, **page performance checks**, and **axe-core accessibility scans** (WCAG)
- **Image validation**, **text validation**, and **url validations** (WCAG)
- **Page Object Model:** one page object and one test file per page
- **Cross-browser execution:** Chromium, Firefox, and WebKit
- **Test documentation:** Markdown files record each test's expected result, actual result, and location in the repository
- **Debugging support:** Playwright traces and screenshots for failed tests


## Tech Stack

| Area | Tools |
| --- | --- |
| Language | Python |
| Automation | Playwright, Pytest |
| Accessibility | axe-core |
| Design pattern | Page Object Model |
| CI | GitHub Actions | (Soon)

## Project Structure

```
.
├── .github/
├── Documents/               # Test documentation: expected vs. actual results and test locations
├── screenshots/             # Screenshots captured during test runs
├── tests/
│   └── ui/
│       ├── page_objects/    # Page Object Model classes, one per page (locators and actions)
│       └── test_*.py        # UI test files, one per page (assertions and test scenarios)
├── conftest.py              # Shared Pytest fixtures
├── pytest.ini               # Pytest configuration and markers
├── playwright.config.ts     # Playwright configuration
├── package.json             # Node dependencies for Playwright tooling
└── requirements.txt         # Python dependencies
```

### How the pieces fit together

Each page of the website has two matching files:

| Layer | Location | Responsibility |
| --- | --- | --- |
| Page object | `tests/ui/page_objects/` | Holds the page's locators and actions (clicking, navigating, reading text) |
| Test file | `tests/ui/` | Holds the test scenarios and assertions that use the page object |

For example, a page's test file calls its page object to interact with the page, then asserts the result. When the page changes, only that page's page object needs updating, not every test.



## Test Coverage

| Category | What it checks |
| --- | --- |
| Smoke | Pages load without errors, correct titles, critical navigation works |
| Links | Navigation and in-page links resolve to the expected destinations |
| Performance | Page load timing checks for each navigation page |
| Accessibility | One axe-core scan per navigation page to detect WCAG violations |

Tests are prioritized in tiers, with smoke tests run first to confirm the site is stable enough for deeper testing.


### Prerequisites

- Python 3.x
- Git

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/AlexFergestad/OldRepublicProfessionalWebsiteQAAutomationProject.git
cd OldRepublicProfessionalWebsiteQAAutomationProject

# 2. Create a virtual environment
python -m venv venv

# 3. Activate it
.\venv\Scripts\activate          # Windows
source venv/bin/activate         # Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install Playwright browsers
python -m playwright install
```

## Running the Tests

```bash
# Run all tests (headless)
python -m pytest

# Run with the browser visible
python -m pytest --headed

# Slow down actions for easier viewing (milliseconds)
python -m pytest --headed --slowmo=500 -s

# Run in a specific browser
python -m pytest --browser chromium
python -m pytest --browser firefox
python -m pytest --browser webkit

# Run all three browsers
python -m pytest --browser chromium --browser firefox --browser webkit

# Run only UI-marked tests
python -m pytest -m ui --headed -s

# Run a single test with verbose output
python -m pytest path/to/test_file.py::test_name -s -v
```

## Test Documentation

Each test is documented in Markdown inside the `Documents/` folder, including:

- The test's purpose
- Expected result
- Actual result
- The location of the test in the repository

This keeps test cases traceable to the automated code that runs them.

## Design Approach

- **Page Object Model:** Each page has a dedicated page object that holds its locators and actions, and a matching test file that holds the assertions. If the page changes, only one page object needs updating.
- **Shared fixtures:** `conftest.py` provides setup shared across all tests.
- **Test the live site responsibly:** Tests run against a production website, so they avoid actions that create real data, such as submitting live forms.

## Roadmap

- [ ] Extend coverage beyond the navigation bar pages
- [ ] Add visual regression testing
- [ ] Expand accessibility checks
- [ ] Add test reporting to CI runs



## Command to debug in a UI

python -m playwright show-trace trace.zip

## Commands to Rum the Tests

# Show print statements
python -m pytest -s

# Or more verbose
python -m pytest -s -v

# For a specific test
python -m pytest {name of the test file}::{name of the test} -s -v

# Run all of the Mark.UI Tests
python -m pytest -m ui --headed -s

## What Each Method Does:

# to_be_visible()
"Is this actually on the screen and clickable?"

# to_have_text()
"Verify that this element has this text"
- Used when you already have an element and want to verify its text.

# get_by_text()
"Find me the element with this text"
- Used when you need to locate/find an element to interact with.

# Text verification methods
- to_have_text() = EXACT match (entire text must match exactly)
- to_contain_text() = PARTIAL match (text must contain this phrase)
- assert text == ... = EXACT match with custom error message

## Additional Testing Information

# Example of what exactly is in a test execution

expect(contact_button).to_be_visible()
  │         │              │
  │         │              └─ Assertion method (checks a condition)
  │         └─ Element to check
  └─ Function that creates an assertion object


## Author

**Alex Fergestad**
[GitHub](https://github.com/AlexFergestad)

