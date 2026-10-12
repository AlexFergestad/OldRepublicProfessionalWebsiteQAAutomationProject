
Automated UI test suite for the public [Old Republic Professional](https://www.oldrepublicpro.com/) website, built with **Python, Playwright, and Pytest**. The suite covers link validation, page performance, and accessibility (axe-core) across the site's navigation pages, using the **Page Object Model** for maintainable, reusable tests.

> **Status:** In progress. Navigation bar pages are covered first; additional pages and test types are being added.

## Highlights

- **60+ automated UI tests** across the navigation bar pages
- **Link validation**, **page performance checks**, and **axe-core accessibility scans** (WCAG)
- **Page Object Model:** one page object and one test file per page
- **Cross-browser execution:** Chromium, Firefox, and WebKit
- **Test documentation:** Markdown files record each test's expected result, actual result, and location in the repository
- **Debugging support:** Playwright traces and screenshots for failed tests





## Setup Instructions to Run Project

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright browsers: `python -m playwright install`
6. Run tests: 
   You can do:
   - python -m pytest
   - python -m pytest --headed (The UI version)
   - python -m pytest --headed --slowmo=1000 (Adds a 1-second delay between actions (1000 milliseconds))
   - python -m pytest --headed --slowmo=500 -s (The -s flag keeps output visible and can help with debugging)
   - python -m pytest --headed --browser firefox
   - python -m pytest --headed --browser webkit
   - python -m pytest --headed --browser chromium
   - python -m pytest --headed --browser chromium --browser firefox --browser webkit (Runs all browsers at once)

## List of Files and What They Do
Requirements.txt
- Lists all Python Packages your project needs.
- It's a shopping list for your project's dependencies.
- After you run "pip install -r requirements.txt", pip reads the file and installs all packages listed.
- Without it, you would have to manually install each package.

Conftest.py
- Shared pytest configuration and fixtures for all your tests.
- It's a toolbox that all your tests can access.
- Pytest automtically finds and loads the conftest.py file. 

__init__.py
- Marks a folder as a Python package.
- It's a sign that says "This folder contains Python code".

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