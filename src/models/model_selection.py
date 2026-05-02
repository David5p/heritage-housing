from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import GridSearchCV

import numpy as np
import pandas as pd


def PipelineReg(model):
    """
    Create a regression pipeline with scaling, feature selection, and the given model.
    """
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("feat_selection", SelectFromModel(model)),
        ("model", model),
    ])
    return pipeline


class HyperparameterOptimizationSearch:
    """
    Run GridSearchCV across multiple models and summarize cross-validation results.
    """

    def __init__(self, models, params):
        """
        Initialize with model dictionary and corresponding parameter grids.
        """
        self.models = models
        self.params = params
        self.keys = models.keys()
        self.grid_searches = {}

    def fit(self, x, y, cv, n_jobs, verbose=1, scoring=None):
        """
        Fit GridSearchCV pipelines for all models using the given CV and scoring settings.
        """
        for key in self.keys:
            print(f"\nRunning GridSearchCV for {key}\n")

            model = PipelineReg(self.models[key])
            params = self.params[key]

            gs = GridSearchCV(
                estimator=model,
                param_grid=params,
                cv=cv,
                n_jobs=n_jobs,
                verbose=verbose,
                scoring=scoring
            )

            gs.fit(x, y)
            self.grid_searches[key] = gs

    def score_summary(self, sort_by='mean_score'):
        """
        Return a dataframe summarizing CV scores for all searched models.
        """

        rows = []

        for k in self.grid_searches:
            cv_results = self.grid_searches[k].cv_results_

            for i in range(len(cv_results["params"])):
                rows.append({
                    "estimator": k,
                    "min_score": cv_results["mean_test_score"][i] - cv_results["std_test_score"][i],
                    "mean_score": cv_results["mean_test_score"][i],
                    "max_score": cv_results["mean_test_score"][i] + cv_results["std_test_score"][i],
                    "std_score": cv_results["std_test_score"][i],
                    **cv_results["params"][i]
                })

        df = pd.DataFrame(rows).sort_values(sort_by, ascending=False)

        columns = ['estimator', 'min_score',
                   'mean_score', 'max_score', 'std_score']
        columns = columns + [c for c in df.columns if c not in columns]

        return df[columns], self.grid_searches
