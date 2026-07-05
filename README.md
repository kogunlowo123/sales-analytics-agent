# Sales Analytics Agent

[![CI](https://github.com/kogunlowo123/sales-analytics-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/sales-analytics-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Business Intelligence | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Sales analytics agent that tracks pipeline health, analyzes win/loss patterns, forecasts revenue, identifies deal risks, and provides rep performance benchmarking with coaching insights.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_pipeline` | Analyze sales pipeline health with stage conversion rates |
| `analyze_win_loss` | Analyze win/loss patterns by segment, competitor, and deal size |
| `forecast_revenue` | Generate weighted pipeline revenue forecast |
| `score_deal_risk` | Score deal risk based on engagement, timing, and pipeline signals |
| `benchmark_reps` | Benchmark sales rep performance against team and top performers |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/sales/pipeline` | Analyze pipeline |
| `POST` | `/api/v1/sales/win-loss` | Analyze win/loss |
| `POST` | `/api/v1/sales/forecast` | Forecast revenue |
| `POST` | `/api/v1/sales/deal-risk` | Score deal risk |
| `GET` | `/api/v1/sales/benchmark` | Benchmark reps |

## Features

- Pipeline Analysis
- Win Loss Analysis
- Revenue Forecasting
- Deal Risk Scoring
- Rep Benchmarking

## Integrations

- Salesforce
- Hubspot
- Pipedrive
- Snowflake
- Looker

## Architecture

```
sales-analytics-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── sales_analytics_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Data Warehouse + BI Platform**

---

Built as part of the Enterprise AI Agent Platform.
