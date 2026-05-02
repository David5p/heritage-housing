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
        Return a dataframe summarizing CV scores for all searched models, sorted by a chosen metric.
        """

        def row(key, scores, params):
            """
            Build a summary row of score statistics and hyperparameters for one estimator run.
            """
            d = {
                'estimator': key,
                'min_score': min(scores),
                'max_score': max(scores),
                'mean_score': np.mean(scores),
                'std_score': np.std(scores),
            }
            return pd.Series({**params, **d})

        rows = []
        for k in self.grid_searches:
            params = self.grid_searches[k].cv_results_['params']
            scores = []

            for i in range(self.grid_searches[k].cv):
                key = f"split{i}_test_score"
                r = self.grid_searches[k].cv_results_[key]
                scores.append(r.reshape(len(params), 1))

            all_scores = np.hstack(scores)

            for p, s in zip(params, all_scores):
                rows.append(row(k, s, p))

        df = pd.concat(rows, axis=1).T.sort_values([sort_by], ascending=False)

        columns = ['estimator', 'min_score',
                   'mean_score', 'max_score', 'std_score']
        columns = columns + [c for c in df.columns if c not in columns]

        return df[columns], self.grid_searches
