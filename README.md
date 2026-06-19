# Boat Sales Analytics — Performance & Customer Intelligence Dashboard

> End-to-end data analytics portfolio project covering Python, SQL, and Power BI.

---

## 📌 Project Overview

This project analyses five interconnected datasets from a boat/audio electronics sales business to uncover actionable insights across revenue trends, customer behaviour, channel performance, and delivery operations.

The analysis is structured across **three phases** — Python-based data cleaning & EDA, SQL querying, and Power BI dashboard development — demonstrating a complete modern data analyst workflow.

---

## 🔑 Key Insights

| # | Insight |
|---|---------|
| 1 | Online channel drives **57% of revenue** but delivers lower profit margin than offline channels |
| 2 | Gold-tier customers (41% of base) contribute **54% of total profit** |
| 3 | Festival periods generate **2.3× the average order value** vs non-festival periods |
| 4 | Top delivery partner achieves **2.10 avg delivery days** with a 4.1/5 customer rating |
| 5 | Wired earphones record the **highest profit margin at 20.86%** across all product categories |

---

## 🗂️ Datasets

| Dataset | Description |
|--------|-------------|
| `salesdata` | Core fact table — order ID, dates, amounts, discounts, status, delivery days |
| `saleschannel` | Channel dimension — online, offline, marketplace types |
| `productdetails` | Product dimension — category, MRP, cost, margin data |
| `customerdetails` | Customer dimension — tier, segment, city, state, signup date |
| `deliverypartnerdata` | Delivery dimension — partner name, avg days, rating, region |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python (Pandas, NumPy)** | Data loading, cleaning, merging, EDA |
| **Matplotlib & Seaborn** | Trend visualisations and comparisons |
| **SQLAlchemy / MySQL** | Relational database setup and business SQL queries |
| **Power BI Desktop** | 4-page interactive dashboard with 15+ DAX measures |
| **Jupyter Notebooks** | Iterative analysis and documentation |

---

## 📁 Project Structure

```
BoatSalesProject/
├── data/
│   ├── raw/              ← Original CSVs (never modified)
│   └── cleaned/          ← Cleaned & transformed versions
├── notebooks/            ← Jupyter Notebooks (EDA, SQL, cleaning)
├── sql/                  ← SQL scripts (.sql files)
├── powerbi/              ← Power BI .pbix file
├── outputs/              ← Charts and PNG exports
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/PB-Pranav/boat-sales-analytics.git
cd boat-sales-analytics
```

### 2. Install Python dependencies

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy openpyxl jupyter plotly
```

### 3. Run the notebooks

Launch Jupyter and open the notebooks in order:

```bash
jupyter notebook
```

| Notebook | Description |
|----------|-------------|
| `01_data_cleaning.ipynb` | Data loading, cleaning, and transformation |
| `02_eda.ipynb` | Exploratory data analysis and visualisations |
| `03_sql_queries.ipynb` | Database setup and business SQL queries |

---

## 🔍 Analysis Phases

### Phase 1 — Project Setup & Planning
Organised project structure with clean separation of raw data, cleaned data, notebooks, SQL scripts, and outputs.

### Phase 2 — Python: Data Cleaning & EDA
- Parsed dates, extracted Year/Month/Quarter columns
- Handled nulls in cancellation and return reason fields
- Removed duplicate records; validated business logic (no negative NetSales)
- Explored revenue trends, channel performance, customer tiers, festival impact, cancellations, and delivery partner metrics
- Merged all five datasets into a single `master_sales.csv`

### Phase 3 — SQL: Database & Business Queries
- Loaded all tables into a relational database via SQLAlchemy
- Wrote 10+ business queries covering monthly trends, channel performance, top products, customer tiers, festival comparison, cancellation rates, delivery rankings, and YoY growth
- Applied advanced SQL: window functions (`LAG`, `RANK`, `ROW_NUMBER`), CTEs, and `CASE WHEN` for RFM scoring

### Phase 4 — Power BI Dashboard
A 4-page interactive dashboard built on a star schema data model with 15+ DAX measures.

| Page | Focus |
|------|-------|
| Executive Summary | KPI cards, monthly revenue trend, channel split, category breakdown |
| Channel & Product Analysis | Channel × category matrix, waterfall chart, scatter plot, top products |
| Customer Intelligence | Tier breakdown, geographic map, new vs returning customers, top 20 table |
| Operations & Delivery | Delivery partner rankings, cancellation gauge, treemap of cancellation reasons |

---

## 📊 DAX Measures (Selected)

| Measure | Logic |
|---------|-------|
| Total Revenue | `SUM(salesdata[NetSales])` |
| Profit Margin % | `DIVIDE([Total Profit], [Total Revenue], 0) * 100` |
| Cancellation Rate % | Orders with status = 'Cancelled' ÷ Total Orders |
| Revenue MoM Growth % | Current month vs previous month using `DATEADD` |
| Revenue YoY Growth % | Current year vs prior year using `SAMEPERIODLASTYEAR()` |

---

## 💡 Business Recommendations

- **Online channel**: Review discount strategy — high revenue but lower margin than offline
- **Gold-tier customers**: Launch a loyalty programme; personalise outreach and offers
- **Festival season**: Prepare inventory 3–4 weeks ahead; run targeted campaigns
- **Delivery partners**: Increase order share to the top performer; review contract with the slowest partner
- **Hero products**: Maintain stock for top 3 products (>34% of revenue); build cross-sell bundles

---

## 👤 PRANAV PB

**Data Analyst Portfolio Project**  
Year: 2025  
Status: ✅ Completed

---

## 📄 License

This project is for portfolio and educational purposes.

