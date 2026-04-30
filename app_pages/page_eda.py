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
    **Insight:** GrLivArea shows a strong positive relationship with SalePrice, with correlation
    later confirmed at ~0.7, indicating it is one of the strongest predictors of housing value 
    in this dataset.”
    """)

    st.write("YearBuilt vs SalePrice")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="YearBuilt", y="SalePrice")
    plt.title("YearBuilt vs SalePrice")
    st.pyplot(plt)

    st.write("""
    **Insight:**YearBuilt shows a moderate positive relationship with SalePrice,
    suggesting newer properties tend to be more valuable. However, size remains a stronger
    indicator for sale price.”
    """)
