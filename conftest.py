"""
Basic pytest configuration
"""
import pytest

@pytest.fixture
def base_url():
    """Base URL for the application"""
    return "https://www.oldrepublicpro.com"