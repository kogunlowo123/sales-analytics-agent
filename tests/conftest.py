"""Test configuration for Sales Analytics Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "sales-analytics-agent", "category": "Business Intelligence"}
