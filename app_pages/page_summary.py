import streamlit as st


def page_summary_body():
    """
    Displays the summary page for the House Price Predictor project.
    """
    st.title("House Price Predictor Project")

    st.write("""
    This app predicts house prices using a machine learning model trained on housing data.

    It includes:
    - Data exploration
    - Feature engineering
    - Machine learning model
    - Interactive price prediction
    """)
