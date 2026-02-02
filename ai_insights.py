def generate_insights(metrics: dict, health: dict, industry: str) -> dict:
    return {
        "insights": (
            "Summary:\n"
            "The business shows strong profitability but faces high financial risk "
            "due to a heavy debt burden.\n\n"
            "Key Risks:\n"
            "- High debt-to-income ratio affecting financial flexibility\n"
            "- Moderate liquidity risk impacting short-term obligations\n\n"
            "Recommendations:\n"
            "1. Restructure or reduce outstanding loans to lower debt exposure.\n"
            "2. Improve working capital management to strengthen liquidity.\n"
            "3. Maintain cost discipline while sustaining revenue growth."
        )
    }
