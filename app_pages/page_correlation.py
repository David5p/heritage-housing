import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def page_correlation_body():
    st.title("Correlation Study - Sale Price Drivers")

    df = pd.read_csv("outputs/datasets/processed/TrainSet.csv")

    st.write("""
    This page explores which variables have the strongest relationship with **SalePrice**.
    """)

    # correlation calculation
    corr = df.corr(numeric_only=True)["SalePrice"].sort_values(ascending=False)

    st.write("## Top Correlated Features")
    st.dataframe(corr.head(15))

    st.write("## Correlation Bar Plot")
    plt.figure(figsize=(10, 6))
    corr.drop("SalePrice").head(10).plot(kind="bar")
    plt.title("Top 10 Features Correlated with SalePrice")
    plt.ylabel("Correlation")
    st.pyplot(plt)

    st.write("## Scatterplots of Key Variables")

    top_features = corr.drop("SalePrice").head(4).index

    for feature in top_features:
        st.write(f"### {feature} vs SalePrice")
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x=feature, y="SalePrice")
        st.pyplot(plt)
