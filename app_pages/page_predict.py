import streamlit as st
import pandas as pd
import joblib


# Cached model + features load
@st.cache_resource
def load_model():
    return joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/model_pipeline.pkl"
    )


@st.cache_resource
def load_features():
    return joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/feature_list.pkl"
    )


def page_predict_body():
    """
    Displays an interactive form to predict house prices using a trained ML model.
    """

    # Load model and features
    model = load_model()
    feature_list = load_features()

    st.title("Predict House Price")
    st.write("Enter house details below:")

    # Inputs
    gr_liv_area = st.number_input("GrLivArea", min_value=0)
    year_built = st.number_input("YearBuilt", min_value=1800, max_value=2025)
    garage_area = st.number_input("GarageArea", min_value=0)
    total_bsmt_sf = st.number_input("TotalBsmtSF", min_value=0)

    # Build input dataframe
    input_data = pd.DataFrame(columns=feature_list)
    input_data.loc[0] = 0

    input_data.at[0, "GrLivArea"] = gr_liv_area
    input_data.at[0, "YearBuilt"] = year_built
    input_data.at[0, "GarageArea"] = garage_area
    input_data.at[0, "TotalBsmtSF"] = total_bsmt_sf

    # Prediction button + validation
    if st.button("Predict Price"):

        # validation
        if gr_liv_area == 0 or garage_area == 0 or total_bsmt_sf == 0:
            st.warning("Please enter realistic values before predicting.")
        else:
            prediction = model.predict(input_data)

            st.success(f"Estimated Price: ${prediction[0]:,.0f}")

            st.caption(
                "Note: This model is trained on U.S. housing data and provides estimates based on historical patterns for houses in Ames, Iowa. "
                "It is not intended for real-world property valuation."
            )
