import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_eda import page_eda_body
from app_pages.page_predict import page_predict_body

app = MultiPage(app_name="House Price Predictor")

app.add_page("Project Summary", page_summary_body)
app.add_page("Data Exploration", page_eda_body)
app.add_page("Predict House Price", page_predict_body)

app.run()
