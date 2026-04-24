import streamlit as st


def page_hypothesis_body():
    st.title("Project Hypotheses and Validation")

    st.write("""
    ## Hypothesis 1
    Houses with larger living area (GrLivArea) will have higher sale prices.

    **Validation:**  
    GrLivArea shows a strong positive correlation with SalePrice, supporting this hypothesis.

    ## Hypothesis 2
    Newer houses (YearBuilt) tend to sell for more.

    **Validation:**  
    YearBuilt shows a moderate positive relationship with SalePrice, supporting the hypothesis.

    ## Hypothesis 3
    Houses with higher kitchen quality (KitchenQual) have higher sale prices.

    **Validation:**  
    Kitchen quality is among the more important categorical predictors of SalePrice and shows a clear positive relationship.  
    This hypothesis is supported, but it is not the strongest predictor compared to top-ranked features.
    """)
