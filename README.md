# Old Republic Professional Website QA Automation Project
I'm creating a project that will test the Old Republic Professional's main website in different ways by creating test cases and automation scripts in an organized and ordered way.

## Project Overview
Automated UI testing suite for the Old Republic Professional insurance website (https://www.oldrepublicpro.com/)


## Setup Instructions to Run Project

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright browsers: `python -m playwright install`
6. Run tests: `pytest`

## List of Files and What They Do
Requirements.txt
- Lists all Python Packages your project needs.
- It's a shopping list for your project's dependencies.
- After you run "pip install -r requirements.txt", pip reads the file and installs all packages listed.
- Without it, you would have to manually install each package.

Conftest.py
- Shared pytest configuration and fixtures for all your test.
- It's a toolbox that all your tests can access.
- Pytest automatically finds and loads the conftest.py file. 

__init__.py
- Marks a folder as a Python package.
- It's a sign that says "This folder contains Python code".

