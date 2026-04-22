import streamlit as st


def page_summary_body():
    """
    Displays the summary page for the House Price Predictor project.
    """
    st.title("House Price Predictor Project")

    st.write("""
    This application predicts house prices using a machine learning model trained on U.S. housing data.

    The model estimates property prices based on historical features such as area, quality, and living space.

    Project highlights:
    - Data exploration and cleaning
    - Feature engineering
    - Machine learning model training
    - Interactive price prediction interface
    """)
