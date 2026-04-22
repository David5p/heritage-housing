import streamlit as st
import pandas as pd
import joblib


def page_predict_body():
    """
    Displays an interactive form to predict house prices using a trained ML model.
    """

    # Load model
    model = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/model_pipeline.pkl"
    )

    # Load feature list (match training features)
    feature_list = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/feature_list.pkl"
    )

    st.title("Predict House Price")
    st.write("Enter house details below:")

    gr_liv_area = st.number_input("GrLivArea", min_value=0)
    year_built = st.number_input("YearBuilt", min_value=1800, max_value=2025)
    garage_area = st.number_input("GarageArea", min_value=0)
    total_bsmt_sf = st.number_input("TotalBsmtSF", min_value=0)

    # Create input dataframe with ALL expected columns
    input_data = pd.DataFrame(columns=feature_list)
    input_data.loc[0] = 0

    # Fill in user inputs
    input_data.at[0, "GrLivArea"] = gr_liv_area
    input_data.at[0, "YearBuilt"] = year_built
    input_data.at[0, "GarageArea"] = garage_area
    input_data.at[0, "TotalBsmtSF"] = total_bsmt_sf

    if st.button("Predict Price"):
        prediction = model.predict(input_data)
        st.success(f"Estimated Price: ${prediction[0]:,.0f}")
