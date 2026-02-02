from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from metrics import calculate_metrics, evaluate_health
from ai_insights import generate_insights
from fastapi.middleware.cors import CORSMiddleware

from metrics import calculate_metrics

app = FastAPI(title="Financial Health Assessment API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    try:
        df = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid CSV file")

    required_columns = {
        "date",
        "revenue",
        "expense",
        "expense_category",
        "accounts_receivable",
        "accounts_payable",
        "loan_amount",
        "tax_paid",
    }

    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise HTTPException(
            status_code=400,
            detail=f"Missing required columns: {missing}",
        )

    metrics = calculate_metrics(df)

    # 🔴 Important: convert numpy types → native Python
    metrics = {k: float(v) for k, v in metrics.items()}

    health = evaluate_health(metrics, industry="services")
    ai_output = generate_insights(metrics, health, industry="services")

    return {
        "status": "success",
        "metrics": metrics,
        "health_assessment": health,
        "ai_insights": ai_output["insights"],
    }


