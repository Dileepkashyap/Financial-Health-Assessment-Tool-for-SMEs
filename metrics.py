import pandas as pd

def calculate_metrics(df: pd.DataFrame) -> dict:
    total_revenue = df["revenue"].sum()
    total_expense = df["expense"].sum()

    profit = total_revenue - total_expense
    profit_margin = profit / total_revenue if total_revenue else 0

    avg_receivable = df["accounts_receivable"].mean()
    avg_payable = df["accounts_payable"].mean()

    current_ratio = (
        avg_receivable / avg_payable
        if avg_payable else 0
    )

    total_loan = df["loan_amount"].iloc[-1]
    debt_to_income = (
        total_loan / total_revenue
        if total_revenue else 0
    )

    net_cash_flow = profit

    return {
        "total_revenue": round(total_revenue, 2),
        "total_expense": round(total_expense, 2),
        "profit": round(profit, 2),
        "profit_margin": round(profit_margin, 2),
        "current_ratio": round(current_ratio, 2),
        "debt_to_income": round(debt_to_income, 2),
        "net_cash_flow": round(net_cash_flow, 2),
    }
def evaluate_health(metrics: dict, industry: str = "services") -> dict:
    benchmarks = {
        "services": {
            "profit_margin": 0.15,
            "current_ratio": 1.5,
            "debt_to_income": 0.5,
        }
    }

    bm = benchmarks[industry]
    risks = {}
    score = 0

    # Profit Margin
    if metrics["profit_margin"] >= bm["profit_margin"]:
        risks["profitability"] = "Healthy"
        score += 1
    elif metrics["profit_margin"] >= bm["profit_margin"] * 0.7:
        risks["profitability"] = "Warning"
    else:
        risks["profitability"] = "Risk"

    # Liquidity
    if metrics["current_ratio"] >= bm["current_ratio"]:
        risks["liquidity"] = "Healthy"
        score += 1
    elif metrics["current_ratio"] >= 1.0:
        risks["liquidity"] = "Warning"
    else:
        risks["liquidity"] = "Risk"

    # Debt
    if metrics["debt_to_income"] <= bm["debt_to_income"]:
        risks["debt"] = "Healthy"
        score += 1
    elif metrics["debt_to_income"] <= bm["debt_to_income"] * 1.5:
        risks["debt"] = "Warning"
    else:
        risks["debt"] = "Risk"

    if score == 3:
        overall = "Financially Healthy"
    elif score == 2:
        overall = "Moderate Risk"
    else:
        overall = "High Risk"

    return {
        "overall_status": overall,
        "risk_breakdown": risks,
    }
