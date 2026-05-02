from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def build_final_pipeline(best_params, numeric_features, categorical_features):
    """
    Builds the final machine learning pipeline.
    Combines preprocessing and the tuned Gradient Boosting model.
    """
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])

    final_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", GradientBoostingRegressor(
            random_state=42,
            learning_rate=best_params["model__learning_rate"],
            max_depth=best_params["model__max_depth"],
            n_estimators=best_params["model__n_estimators"]
        ))
    ])

    return final_pipeline
