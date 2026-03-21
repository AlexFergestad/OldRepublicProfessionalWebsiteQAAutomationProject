# Old Republic Professional Website QA Automation Project
I'm creating a project that will test the Old Republic Professional's main website in different ways by creating test cases and automation scripts in an organized and ordered way.

## Project Overview
Automated UI testing suite for the Old Republic Professional insurance website (https://www.oldrepublicpro.com/)

## Order of the Testing
Tier 1: Smoke Tests (Test FIRST) 🔥
Goal: Verify the app is stable enough to test further
Start with the most critical, basic functionality:

1. Page Loads ← You just did this!

- Does the homepage load?
- Does it load without errors?
- Is the title correct?

2. Critical Navigation

- Can users access main pages?
- Do primary menu items work?

3. Critical Forms/Actions

- Can users submit the contact form?
- Do essential user actions work?


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