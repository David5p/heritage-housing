import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_regression(x, y, pipeline):
    """
    Evaluates a trained regression model using common performance metrics.
    """
    y_pred = pipeline.predict(x)

    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)

    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2:", r2)

    return mae, rmse, r2


def plot_predictions(x, y, pipeline):
    """
    Plots actual vs predicted values for regression model evaluation.
    """
    y_pred = pipeline.predict(x)

    plt.figure(figsize=(6, 6))
    plt.scatter(y, y_pred)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted")
    plt.show()


def plot_residuals(x, y, pipeline):
    """
    Plots residuals (errors) of a regression model to assess model fit.
    Residuals are calculated as: actual - predicted.
    """
    y_pred = pipeline.predict(x)
    residuals = y - y_pred

    plt.figure(figsize=(6, 4))
    sns.histplot(residuals, kde=True)
    plt.xlabel("Residuals (Actual - Predicted)")
    plt.title("Residual Distribution")
    plt.show()
