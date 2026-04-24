import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def page_technical_body():
    st.title("Model Performance and Pipeline")

    model = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/model_pipeline.pkl"
    )

    X_test = pd.read_csv(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/X_test.csv"
    )

    y_test = pd.read_csv(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/y_test.csv"
    ).squeeze()

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    st.write("## Test Set Results")
    st.write(f"**MAE:** {mae:,.2f}")
    st.write(f"**RMSE:** {rmse:,.2f}")
    st.write(f"**R² Score:** {r2:.3f}")

    st.write("## Pipeline Steps")
    st.code(model)
