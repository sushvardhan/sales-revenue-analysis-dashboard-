# Sales & Revenue Analysis Dashboard

An interactive dashboard built with **Python, Streamlit, Pandas, and Plotly** to explore sales performance using a sample retail dataset.

> **Dataset note:** The included records are synthetic and generated for this portfolio project. They do not represent a real company or internship employer.

## Dashboard features
- KPI cards: revenue, profit, order count, units sold, and profit margin
- Date, region, product, and sales-channel filters
- Monthly revenue and profit trend
- Revenue breakdown by region and product
- Sales-channel revenue share
- Filtered order-level table and CSV export

## Run locally

1. Install Python 3.10 or newer.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

The app opens in your browser. The data file is loaded from `data/sales_data.csv`.

## Repository structure

```text
sales-revenue-analysis-dashboard/
├── app.py
├── data/
│   └── sales_data.csv
├── requirements.txt
└── README.md
```

## Metrics
- **Revenue:** Quantity × Unit Price × (1 − Discount)
- **Profit:** Revenue − Cost
- **Profit margin:** Profit ÷ Revenue × 100

## Suggested next improvements
- Connect a database or live sales API
- Add year-over-year and month-over-month comparisons
- Add product-level profitability and average order value
- Add authentication and deployment

## Portfolio description
Created an interactive sales analytics dashboard to monitor revenue, profitability, order volume, and product/region/channel performance. Implemented dynamic filters, time-series and categorical visualizations, and CSV export using Python, Streamlit, Pandas, and Plotly.
