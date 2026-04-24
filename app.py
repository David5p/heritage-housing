from app_pages.page_technical import page_technical_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_inherited_houses import page_inherited_houses_body
from app_pages.page_correlation import page_correlation_body
import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_eda import page_eda_body
from app_pages.page_predict import page_predict_body
from app_pages.page_correlation import page_correlation_body
from app_pages.page_inherited_houses import page_inherited_houses_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_technical import page_technical_body

app = MultiPage(app_name="House Price Predictor")

app.add_page("Project Summary", page_summary_body)
app.add_page("Data Exploration", page_eda_body)
app.add_page("Correlation Findings", page_correlation_body)
app.add_page("Inherited Houses", page_inherited_houses_body)
app.add_page("Predict House Price", page_predict_body)
app.add_page("Project Hypotheses", page_hypothesis_body)
app.add_page("Technical Information", page_technical_body)


app.run()
