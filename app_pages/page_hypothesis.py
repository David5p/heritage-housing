import streamlit as st


def page_hypothesis_body():
    st.title("Project Hypotheses and Validation")

    st.write("""
    ## Hypothesis 1
    Houses with larger living area (GrLivArea) will have higher sale prices.

    **Validation:**  
    Correlation analysis shows GrLivArea is strongly positively correlated with SalePrice.

    ## Hypothesis 2
    Newer houses (YearBuilt) tend to sell for more.

    **Validation:**  
    YearBuilt shows a positive relationship with SalePrice.

    ## Hypothesis 3
    Houses with higher kitchen quality (KitchenQual) have a higher SalePrice.

    **Validation:**  
    Kitchen quality (KitchenQual) has one of the strongest correlations with SalePrice, confirming this hypothesis.
    """)
