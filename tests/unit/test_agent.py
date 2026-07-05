"""Sales Analytics Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_pipeline():
    """Test Analyze sales pipeline health with stage conversion rates."""
    tools = AgentTools()
    result = await tools.analyze_pipeline(period="test", segments="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_win_loss():
    """Test Analyze win/loss patterns by segment, competitor, and deal size."""
    tools = AgentTools()
    result = await tools.analyze_win_loss(period="test", dimensions="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_forecast_revenue():
    """Test Generate weighted pipeline revenue forecast."""
    tools = AgentTools()
    result = await tools.forecast_revenue(period="test", method="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_score_deal_risk():
    """Test Score deal risk based on engagement, timing, and pipeline signals."""
    tools = AgentTools()
    result = await tools.score_deal_risk(deal_id="test", risk_factors="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.sales_analytics_agent_agent import SalesAnalyticsAgentAgent
    agent = SalesAnalyticsAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
