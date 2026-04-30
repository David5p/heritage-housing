import streamlit as st
import pandas as pd
import joblib


# Cached training data model + features load

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


def page_predict_body():
    """
    Displays an interactive form to predict house prices using a trained ML model.
    """

    # Load model, features and training dataset
    model = load_model()
    feature_list = load_features()
    df_train = load_training_data()

    baseline_values = df_train.median(numeric_only=True)

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

    # Fill numeric columns with median baseline values
    for col in baseline_values.index:
        if col in input_data.columns:
            input_data.at[0, col] = baseline_values[col]

    input_data.at[0, "GrLivArea"] = gr_liv_area
    input_data.at[0, "YearBuilt"] = year_built
    input_data.at[0, "GarageArea"] = garage_area
    input_data.at[0, "TotalBsmtSF"] = total_bsmt_sf

    # Prediction button + validation
    if st.button("Predict Price"):
        if gr_liv_area < 300:
            st.warning(
                "GrLivArea seems too low. Please enter a realistic value.")
        else:
            prediction = model.predict(input_data)
            st.success(f"Estimated Price: ${prediction[0]:,.0f}")

            st.caption(
                "Note: The prediction is based on the values you entered. "
                "All other missing variables are automatically set to typical (median) values "
                "from the training dataset. The model is trained on housing data from "
                "Ames, Iowa and provides statistical estimates, not real-world valuations."
            )
