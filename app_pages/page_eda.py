import streamlit as st
import pandas as pd


def page_eda_body():
    """Displays exploratory data analysis (EDA) for the cleaned housing dataset."""

    st.title("Data Exploration")

    df = pd.read_csv("outputs/datasets/cleaned/CleanedData.csv")

    st.write("Dataset preview:")
    st.dataframe(df.head())

    st.write("Shape:", df.shape)

    st.write("Summary statistics:")
    st.dataframe(df.describe())
