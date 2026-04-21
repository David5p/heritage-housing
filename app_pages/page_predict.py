import streamlit as st
import pandas as pd


def page_predict_body():
    """
    Displays an interactive form to predict house prices using a trained ML model.
    """
    import joblib
    model = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/v1_gb_final/model_pipeline.pkl"
    )
    st.title("Predict House Price")

    st.write("Enter house details below:")

    gr_liv_area = st.number_input("GrLivArea")
    year_built = st.number_input("YearBuilt")
    garage_area = st.number_input("GarageArea")
    total_bsmt_sf = st.number_input("TotalBsmtSF")

    input_data = pd.DataFrame([{
        "GrLivArea": gr_liv_area,
        "YearBuilt": year_built,
        "GarageArea": garage_area,
        "TotalBsmtSF": total_bsmt_sf
    }])

    if st.button("Predict Price"):
        prediction = model.predict(input_data)
        st.success(f"Estimated Price: £{prediction[0]:,.0f}")
