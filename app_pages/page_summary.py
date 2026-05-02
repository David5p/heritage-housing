import streamlit as st
import pandas as pd


def page_summary_body():
    st.title("Heritage Housing Issues - Project Summary")

    st.write("""
    ## Project Overview
    This dashboard supports a client who inherited four houses in Ames, Iowa (USA).

    The goal is to understand what factors influence sale price and to predict the sale
    price of the inherited properties.

    These insights directly support the business decision of whether to:
    - Sell the properties
    - Renovate to increase value
    - Or hold based on expected market value
    """)

    st.write("""
    ## Business Requirements
    1. Identify which house attributes are most strongly correlated with sale price.
    2. Predict the sale prices of the 4 inherited houses and estimate their combined value.
    3. Allow users to input different house attributes to generate predictions.
    """)

    st.write("## Dataset Summary")

    df = pd.read_csv("outputs/datasets/processed/TrainSet.csv")

    st.write(f"**Number of rows:** {df.shape[0]}")
    st.write(f"**Number of columns:** {df.shape[1]}")

    st.write("### Dataset Preview")
    st.dataframe(df.head(10))

    st.write("""
    ### Business Link
    This dataset forms the foundation of the analysis used throughout the project.
    It enables identification of key price drivers and supports valuation of the inherited properties.
    """)
