# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **educational tutorial repository** that teaches professional AI-assisted development workflow. It is not a runnable application — it contains documentation, sample data, and a PRD that students use to build an e-commerce Streamlit dashboard.

There are no build, test, or lint pipelines in this repository.

## Repository Structure

- `v1/` — Original multi-session tutorial format (reference material)
- `v2/` — Current format: async pre-work (`pre-work-setup.md`) + 3-hour live workshop (`workshop-build-deploy.md`)
- `prd/ecommerce-analytics.md` — Product Requirements Document that drives the workshop
- `data/sales-data.csv` — Sample e-commerce dataset (482 rows) used in the dashboard

## What Students Build

A Streamlit dashboard using:
- **Streamlit** — UI/web framework
- **Plotly** — Interactive charts
- **Pandas** — CSV loading and aggregation
- **Python 3.11+**
- **uv** — Package manager

Deployed to Streamlit Community Cloud, with code tracked in GitHub and tasks tracked in Jira.

## Workflow Being Taught

PRD (`prd/ecommerce-analytics.md`) → `spec-kit` CLI → Jira issues → Claude Code builds dashboard → Git commit with Jira reference (e.g., `ECOM-1`) → GitHub push → Streamlit Cloud deploy

## Content Maintenance Notes

- UI instructions in `v2/pre-work-setup.md` and `v2/workshop-build-deploy.md` frequently need updates as GitHub, Atlassian, Jira, Streamlit, and Claude UI evolve. Recent commits have been fixing these.
- Both v2 documents include a caveat about evolving UIs near the top.
- Jira project creation has a fallback manual link due to Atlassian's frequently changing onboarding flow.
- The PRD (`prd/ecommerce-analytics.md`) specifies expected output values (Total Sales: ~$116,500, Total Orders: 482) that should remain consistent with `data/sales-data.csv`.
