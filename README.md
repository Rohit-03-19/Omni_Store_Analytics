# Omni-Store: Hybrid Retail Analytics Platform 🚀

A professional-grade data analytics pipeline designed to bridge the gap between structured relational data (SQL) and flexible document metadata (NoSQL). This project demonstrates **Polyglot Persistence**, **Modular OOP Architecture**, and **Automated Testing**.

## 🏗️ Architecture Overview

This platform utilizes a "Decoupled Service" architecture:

- **Relational Data (PostgreSQL/Supabase):** Manages ACID-compliant transaction data (Orders, Payments).
- **Document Data (MongoDB Atlas):** Handles flexible product metadata and unstructured attributes (Tags, Categories).
- **Analytics Engine (Python/Pandas/NumPy):** Unifies these data sources in memory for high-performance statistical reporting.

## 🛠️ Tech Stack

- **Languages:** Python 3.12+
- **Databases:** Supabase (PostgreSQL), MongoDB Atlas
- **Data Science:** Pandas (Merging/Cleaning), NumPy (Statistical Analysis)
- **Visualization:** Matplotlib, Seaborn
- **Utilities:** Pytest (Unit Testing), python-dotenv (Security)

## 📁 Project Structure

```text
omni_store_analytics/
├── src/
│   ├── databases/     # SQL & NoSQL Client Wrappers
│   ├── analytics/     # Core Business Logic & NumPy Engines
│   ├── visualizations/# Automated Chart Generation
│   └── utils/         # Performance Decorators & Custom Exceptions
├── notebooks/         # Exploratory Data Analysis (EDA)
├── tests/             # Automated Unit & Integration Tests
└── main.py            # Unified Pipeline Entry Point
```

## 🚀 Key Features

- Hybrid Data Merging: Efficiently joins SQL and NoSQL datasets using standardized keys.

- Customer Loyalty Engine: Uses NumPy-based normalization to segment customers into Bronze, Silver, and Gold tiers.

- Automated Reporting: Generates revenue distribution charts and saves them directly to local storage.

- Production-Ready Utilities: Implements custom error handling and performance-monitoring decorators.

## 🚦 Getting Started

Clone the repository.

Create a virtual environment: python -m venv venv.

Install dependencies: pip install -r requirements.txt.

Configure your .env file with Supabase and MongoDB credentials.

Seed the database: python seed_data.py.

Run the pipeline: python main.py.

## 🧪 Testing

Run the automated test suite to verify math and processing logic:
python -m pytest
