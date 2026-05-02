from sklearn.model_selection import train_test_split


def split_data(df, target="SalePrice", test_size=0.2, random_state=42):
    """
    Splits dataset into train and test sets.
    Returns X_train, X_test, y_train, y_test.
    """

    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test
