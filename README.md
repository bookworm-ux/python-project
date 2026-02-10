🚢 Vessel Profitability & TCE Automation Tool
Project Overview

This project is a high-speed data product designed to automate asset management processes for a container ship fleet. It calculates the Time Charter Equivalent (TCE)—a core maritime financial KPI—to help stakeholders monitor profitability against market volatility in real-time.

Key Features

Automated TCE Calculation: Dynamically calculates daily net profit for 59+ vessel assets.

Sensitivity Analysis: Interactive "What-If" scenarios for fuel price (Bunker) fluctuations and charter rate changes.

Profitability Guardrails: Visual flagging of underperforming assets based on a configurable USD/Day benchmark.

Clean Code Architecture: Built with Python using functional programming principles and type hinting for maintainability.

Tech Stack

Language: Python 3.x

Data Logic: Pandas, NumPy

Visualization: Streamlit (UI), Matplotlib (Financial Charting)

Data Structure: Designed for integration with Azure SQL / MS SQL Server

Business Impact

In a "Fast Growth" environment like MPC, manual Excel-based fleet tracking is a bottleneck. This tool:

Speeds up development of financial reporting.

Establishes best practices for data validation and master data integrity.

Boosts profitability by providing instant visibility into which ships require operational review.

How to Run

Clone the repository.

Install dependencies: pip install streamlit pandas matplotlib

Launch the app: streamlit run mpc_dashboard.py
