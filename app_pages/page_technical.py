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

    st.write("### Model Evaluation Statement")

    if r2 >= 0.75:
        st.success(
            f"""
            The model demonstrates strong predictive performance on unseen data.

            - R² Score: {r2:.3f}
            - This indicates the model explains a large proportion of variance in house prices.
            - It is suitable for deployment for supporting pricing decisions.
            """
        )

    else:
        st.warning(
            f"""
            The model shows limited predictive performance.

            - R² Score: {r2:.3f}
            - This suggests the model may not generalise well to unseen data.
            - Further feature engineering or model tuning may be required.
            """
        )

    st.write("Pipeline Steps")
    st.code(model)
