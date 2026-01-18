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