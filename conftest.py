"""
Basic pytest configuration
"""
import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://www.oldrepublicpro.com"

@pytest.fixture(scope="function", autouse=True)
def context(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()

@pytest.fixture
def page(context):
    """Creates a new page with custom viewport size"""
    # ⬇️ Step 1: SETUP (before test)
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    
    # ⬇️ Step 2: Give page to test
    yield page

    # ⏸️ Test runs here...
    
    # ⬇️ Step 3: CLEANUP (after test)
    page.close()