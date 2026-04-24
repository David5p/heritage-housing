import streamlit as st
import pandas as pd
import joblib


def page_inherited_houses_body():
    """
    Displays the four inherited houses attributes, their predicted prices,
    and the total combined predicted sale price.
    """

    st.title("Inherited Houses - Predicted Sale Prices")

    # Load model + feature list
    model = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/model_pipeline.pkl"
    )

    feature_list = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/feature_list.pkl"
    )

    # Load inherited houses dataset
    df_inherited = pd.read_csv("inputs/inherited_houses.csv")

    st.write("## Inherited Houses Attributes")
    st.dataframe(df_inherited)

    # Create model-ready dataframe with ALL expected columns
    input_data = pd.DataFrame(columns=feature_list)
    input_data.loc[:] = 0

    for i in range(len(df_inherited)):
        row = pd.Series(0, index=feature_list)

        for col in df_inherited.columns:
            row[col] = df_inherited.loc[i, col]

        input_data.loc[i] = row

    # Predict
    predictions = model.predict(input_data)

    # Add predictions to table
    df_results = df_inherited.copy()
    df_results["PredictedSalePrice"] = predictions

    st.write("## Predicted Sale Prices")
    st.dataframe(df_results)

    # Total combined value
    total_value = df_results["PredictedSalePrice"].sum()

    st.success(
        f"Total Predicted Value of the 4 Houses combined: ${total_value:,.0f}")
