import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def page_correlation_body():
    st.title("Correlation Study - Key Drivers of House Prices")

    df = pd.read_csv("outputs/datasets/processed/TrainSet.csv")

    st.write("""
    ## Business Context
    The client has inherited four properties in Ames, Iowa and needs to understand
    which property characteristics most strongly influence market value.

    This analysis identifies the features most strongly associated with **SalePrice**.
    These insights help inform:
    - Property valuation decisions
    - Investment or renovation priorities
    - Understanding what drives higher market value
    """)

    st.success("""
    Executive Summary:
    House prices in this dataset are primarily driven by property size (living area and basement space),
    garage capacity, and overall property age/quality.
    """)

    # Correlation calculation
    corr = df.corr(numeric_only=True)["SalePrice"].sort_values(ascending=False)
    corr = corr.drop("SalePrice")

    st.write("## Top Features Influencing Sale Price")

    st.write("""
    The features below have the strongest statistical relationship with house price.
    Higher values (positive or negative) indicate a stronger influence on property value.
    """)

    st.dataframe(corr.head(15))

    st.write("""
    ### Business Insight
    The analysis shows that **GrLivArea, GarageArea, TotalBsmtSF, and YearBuilt**
    are the strongest features associated with sale price.

    In practical terms, this suggests that property size, usable space, and age
    are the main factors influencing value in this market.
    """)

    # Correlation bar plot
    st.write("## Top 10 Price Drivers")

    fig, ax = plt.subplots(figsize=(10, 6))
    corr.head(10).plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Features Influencing Sale Price")
    ax.set_ylabel("Correlation with Sale Price")
    ax.set_xlabel("Feature")

    st.pyplot(fig)

    st.write("""
    ### Interpretation for the Client
    Features with stronger correlations are the most strongly associated with house value.

    This means that when evaluating or improving a property, priority should be given to
    these factors, as changes here are more likely to impact market price.
    """)

    # Scatterplots
    st.write("## How Key Features Affect Sale Price")

    top_features = corr.head(4).index

    st.write("""
    The following charts show how the most influential features relate directly to
    house prices. This helps visualise why these features matter in real estate valuation.
    """)

    for feature in top_features:
        st.write(f"### {feature} vs Sale Price")

        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=df, x=feature, y="SalePrice", ax=ax)

        ax.set_title(f"{feature} vs Sale Price")
        ax.set_xlabel(feature)
        ax.set_ylabel("Sale Price")

        st.pyplot(fig)

    st.write("""
    ### What this means for the client
    To maximise the value of the inherited properties, priority should be given to:

    - Increasing usable living space (e.g. extensions or conversions)
    - Improving or upgrading garage facilities
    - Modernising older properties where feasible

    These actions are more likely to increase market value than cosmetic improvements alone.
    """)
