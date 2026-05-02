import numpy as np
from sklearn.preprocessing import PowerTransformer
from feature_engine.encoding import OneHotEncoder
from feature_engine.selection import SmartCorrelatedSelection
from feature_engine.outliers import Winsorizer


def feature_engineering_pipeline(X_train, X_test):
    """
    Applies feature engineering steps and returns transformed dataset
    """
    ohe = OneHotEncoder(variables=None, drop_last=False)
    X_train = ohe.fit_transform(X_train)
    X_test = ohe.transform(X_test)

    corr_sel = SmartCorrelatedSelection(
        variables=None,
        method="spearman",
        threshold=0.6,
        selection_method="variance"
    )
    X_train = corr_sel.fit_transform(X_train)
    X_test = corr_sel.transform(X_test)

    boxcox_vars = ['GrLivArea', '1stFlrSF']
    boxcox_vars = [c for c in boxcox_vars if c in X_train.columns]
    # Remove non-positive columns
    boxcox_vars = [
        c for c in boxcox_vars
        if (X_train[c] > 0).all()
    ]
    pt_boxcox = PowerTransformer(method="box-cox")
    X_train[boxcox_vars] = pt_boxcox.fit_transform(X_train[boxcox_vars])
    X_test[boxcox_vars] = pt_boxcox.transform(X_test[boxcox_vars])

    yeojohnson_vars = ['LotArea', 'TotalBsmtSF', 'BsmtFinSF1']
    yeojohnson_vars = [c for c in yeojohnson_vars if c in X_train.columns]
    pt_yeo = PowerTransformer(method="yeo-johnson")
    X_train[yeojohnson_vars] = pt_yeo.fit_transform(X_train[yeojohnson_vars])
    X_test[yeojohnson_vars] = pt_yeo.transform(X_test[yeojohnson_vars])

    winsor_vars = ['GrLivArea', 'LotArea', 'TotalBsmtSF']
    winsor_vars = [c for c in winsor_vars if c in X_train.columns]

    winsor = Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=winsor_vars
    )

    if winsor_vars:
        X_train = winsor.fit_transform(X_train)
        X_test = winsor.transform(X_test)

    return X_train, X_test, {
        "boxcox_vars": boxcox_vars,
        "yeojohnson_vars": yeojohnson_vars,
        "winsor_vars": winsor_vars,
        "dropped_features": corr_sel.features_to_drop_
    }
