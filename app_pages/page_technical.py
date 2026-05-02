import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def page_technical_body():
    st.title("Model Performance and Pipeline")

    # Load model + data
    model = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/model_pipeline.pkl"
    )

    X_test = pd.read_csv(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/X_test.csv"
    )

    y_test = pd.read_csv(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/y_test.csv"
    ).squeeze()

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    st.write("## Model Performance (Test Set)")

    st.write(f"**MAE:** {mae:,.2f}")
    st.write(f"**RMSE:** {rmse:,.2f}")
    st.write(f"**R² Score:** {r2:.3f}")

    st.write("""
    ## Business Case Relevance
    This model is used to support the client’s decision-making process for the inherited properties.

    A reliable model ensures that estimated house prices reflect real market behaviour,
    enabling better decisions around selling or investing in renovations.
    """)

    st.write("### Model Evaluation Statement")

    if r2 >= 0.75:
        st.success(f"""
        The model demonstrates strong predictive performance.

        - R² Score: {r2:.3f}
        - The model explains a large proportion of variation in house prices.
        - It is suitable for supporting real estate valuation decisions.
        """)
    else:
        st.warning(f"""
        The model shows limited predictive performance.

        - R² Score: {r2:.3f}
        - This suggests the model may not generalise well to unseen data.
        - Further tuning or feature engineering may be required.
        """)

    st.write("## Pipeline Object")

    st.code(str(model))
