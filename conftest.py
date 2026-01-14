"""
Basic pytest configuration
"""
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://www.oldrepublicpro.com"