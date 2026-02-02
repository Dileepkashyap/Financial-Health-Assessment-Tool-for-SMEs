# Financial Health Assessment Tool for SMEs

## Overview

The Financial Health Assessment Tool is an AI-powered web application designed to help **Small and Medium Enterprises (SMEs)** understand, monitor, and improve their financial health.

Many SMEs struggle with:

* Understanding financial statements
* Identifying hidden financial risks
* Making informed decisions on expenses, debt, and growth
* Accessing clear, simple insights without financial expertise

This platform solves these challenges by combining **data analysis, AI-driven insights, and intuitive visualizations** into a single easy-to-use system.

---

## Problem Statement

Small and Medium Enterprises often lack access to advanced financial analysis tools due to:

* High cost of professional financial services
* Lack of financial literacy
* Complex financial data that is difficult to interpret

As a result, business owners fail to:

* Detect financial risks early
* Optimize costs and working capital
* Prepare investor-ready financial reports
* Make informed decisions for sustainable growth

---

##  Solution

This platform provides a **comprehensive financial health assessment** by:

* Analyzing uploaded financial data (CSV format)
* Calculating key financial metrics
* Evaluating creditworthiness and risk
* Generating AI-powered insights and recommendations
* Displaying results using simple and clear visualizations
* Supporting multiple languages for regional business owners

---

##  Key Features

### Financial Metrics Calculation

The system automatically computes:

* **Total Revenue**
* **Total Expenses**
* **Profit**
* **Profit Margin**
* **Current Ratio (Liquidity)**
* **Debt-to-Income Ratio**
* **Net Cash Flow**

These metrics form the foundation for financial risk analysis.

---

### Data Visualization

To ensure clarity for non-finance users:

* Visual bar charts compare **Revenue vs Expense**
* Color indicators highlight financial conditions
* Simple layout improves readability

**Visual comparison of income and expenditure for quick financial understanding.**

---

### Financial Risk Assessment

The platform evaluates:

* **Overall Financial Risk Status**

  * Low Risk
  * Moderate Risk
  * High Risk

* **Risk Breakdown**:

  * Profitability Risk
  * Liquidity Risk
  * Debt Risk

---

### AI-Powered Insights

Using an AI narrative layer, the system provides:

* Business financial summary
* Identification of major financial risks
* Actionable recommendations such as:

  * Cost optimization strategies
  * Debt restructuring suggestions
  * Working capital improvements

These insights are written in **simple language**, suitable for non-finance business owners.

---

### Multilingual Support

To support regional SME owners:

* English
* Hindi

The UI dynamically switches language without reloading.

---

### Security & Compliance

* No permanent storage of financial data
* Secure API communication
* Input validation on uploaded files
* Separation of frontend and backend layers
* Designed with data privacy and regulatory awareness

---

## System Architecture

```
Frontend (React)
   ↓
FastAPI Backend
   ↓
Financial Metrics Engine (Pandas)
   ↓
AI Insight Generator
```

---

## Technology Stack

### Frontend

* React.js
* JavaScript
* Inline CSS for simplicity
* Responsive UI

### Backend

* Python
* FastAPI
* Pandas (data processing)

### AI Layer

* OpenAI API (narrative & recommendations)

---

##  Project Structure

```
financial-health/
│
├── backend/
│   ├── main.py               # API endpoints
│   ├── metrics.py            # Financial calculations
│   ├── ai_insights.py        # AI-generated insights
│   ├── requirements.txt
│
├── frontend/
│   └── src/
│       └── App.js            # React UI
│
├── data/
│   └── sample_financials.csv
│
└── README.md
```

---

## How to Run the Project

###  Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

##  Sample Input

The application accepts:

* CSV files containing financial data
* Required fields include revenue, expenses, loans, and cash flow

A sample file is provided in:

```
/data/sample_financials.csv
```

---

## Application Screenshots

### Dashboard & File Upload

(Add screenshot here)

###  Financial Visualization

(Add revenue vs expense bar chart screenshot)

###  Risk Assessment & Metrics

(Add metrics and risk breakdown screenshot)

###  AI Insights Section

(Add AI insights screenshot)

---

##  Future Enhancements

* XLSX and PDF support
* Industry-specific benchmarking
* GST data integration
* Banking API integrations
* Financial forecasting module
* Investor-ready report generation
* Role-based access control
* Cloud deployment

---

##  Hackathon Readiness

✔ Meets all problem statement requirements
✔ End-to-end working solution
✔ Clean and intuitive UI
✔ AI-driven decision support
✔ Multilingual support
✔ Scalable architecture

This solution is **production-aligned and hackathon-ready**.

---

##  Author

**Dileep Kashyap L**
Financial Health Assessment Tool
GUVI × HCL Hackathon 2026

---

 *Thank you for reviewing this project.*

---
<img width="1920" height="856" alt="Screenshot (139)" src="https://github.com/user-attachments/assets/2566570e-8b55-44f6-a1ab-4f3954d0d80b" />
<img width="1920" height="877" alt="Screenshot (141)" src="https://github.com/user-attachments/assets/d9aa2fe1-ff2f-4836-b665-322c6faa02c7" />
<img width="1920" height="910" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/cecb90aa-3e52-4b15-8d73-c0460809ae17" />
<img width="1920" height="851" alt="Screenshot (149)" src="https://github.com/user-attachments/assets/37247e8c-6a42-4715-afd3-b4ce7dcef1e0" />
<img width="1920" height="861" alt="Screenshot (150)" src="https://github.com/user-attachments/assets/212dbcc9-a834-45fd-b4cb-ecd635be0c6c" />




