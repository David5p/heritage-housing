import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


def page_eda_body():
    """Displays exploratory data analysis (EDA) for the cleaned housing dataset."""

    st.title("Data Exploration")

    df = pd.read_csv("outputs/datasets/cleaned/CleanedData.csv")

    st.write("Dataset preview")
    st.dataframe(df.head())

    st.write("Shape of dataset")
    st.write(df.shape)

    st.write("Summary statistics")
    st.dataframe(df.describe())

    st.write("Distribution of SalePrice")
    plt.figure(figsize=(8, 5))
    sns.histplot(df["SalePrice"], kde=True)
    plt.title("SalePrice Distribution")
    st.pyplot(plt)

    st.write("""
    **Insight:** SalePrice is right-skewed, meaning there are more lower-priced houses 
    and fewer very expensive houses in the dataset.
    """)

    st.write("GrLivArea vs SalePrice")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="GrLivArea", y="SalePrice")
    plt.title("GrLivArea vs SalePrice")
    st.pyplot(plt)

    st.write("""
    **Insight:** Larger above-ground living area generally leads to higher sale price, 
    confirming that house size is a major price feature.
    """)

    st.write("YearBuilt vs SalePrice")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="YearBuilt", y="SalePrice")
    plt.title("YearBuilt vs SalePrice")
    st.pyplot(plt)

    st.write("""
    **Insight:** Newer houses have a tendancy to sell for more, but the relationship is weaker 
    than size-based features.
    """)
