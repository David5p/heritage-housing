import streamlit as st
import pandas as pd
import joblib


# Cached loading functions

@st.cache_data
def load_training_data():
    return pd.read_csv("outputs/ml_pipeline/predict_saleprice/v1_gb_final/X_train.csv")


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


# Main Page Function

def page_predict_body():

    # Load assets
    model = load_model()
    feature_list = load_features()
    df_train = load_training_data()

    st.title("Predict House Price")
    st.write("Enter house details below:")

    # User Inputs
    gr_liv_area = st.number_input("GrLivArea", min_value=0)
    year_built = st.number_input("YearBuilt", min_value=1800, max_value=2025)
    garage_area = st.number_input("GarageArea", min_value=0)
    total_bsmt_sf = st.number_input("TotalBsmtSF", min_value=0)

    # Build input dataframe properly
    input_data = pd.DataFrame(columns=feature_list)

    # create empty row (no fake house)
    input_data.loc[0] = 0

    # overwrite only user-controlled features
    if "GrLivArea" in input_data.columns:
        input_data.at[0, "GrLivArea"] = gr_liv_area

    if "YearBuilt" in input_data.columns:
        input_data.at[0, "YearBuilt"] = year_built

    if "GarageArea" in input_data.columns:
        input_data.at[0, "GarageArea"] = garage_area

    if "TotalBsmtSF" in input_data.columns:
        input_data.at[0, "TotalBsmtSF"] = total_bsmt_sf

    # Ensure correct column order
    input_data = input_data[feature_list]

    # Prediction
    if st.button("Predict Price"):

        # Warning instead of hard rule
        min_area = df_train["GrLivArea"].quantile(0.01)

        if gr_liv_area < min_area:
            st.warning(
                f"Very small house compared to training data (typical min ~{min_area:.0f} sqft)."
            )

        prediction = model.predict(input_data)

        st.success(f"Estimated Price: ${prediction[0]:,.0f}")

        st.caption(
            "Prediction is based on a machine learning model trained on Ames housing data. "
            "Values are statistical estimates and not official valuations."
        )
