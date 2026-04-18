import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load(
    "outputs/ml_pipeline/predict_saleprice/v1_gb_final/model_pipeline.pkl")
