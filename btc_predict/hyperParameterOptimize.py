from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def hyperParameterOptimize(X_train, y_train):
    """
    Performs hyperparameter optimization for a Random Forest classifier using grid search cross-validation.

    Args:
        X_train (numpy.ndarray): The training data to use for hyperparameter optimization.
        y_train (numpy.ndarray): The training labels to use for hyperparameter optimization.

    Returns:
        None
    """

    isOptimized = True

    # If hyperparameters have already been optimized, skip this step
    if isOptimized is True:
        return

    # Define the range of hyperparameters to tune
    param_grid = {
        'n_estimators': [50, 100, 200, 500],
        'max_depth': [3, 5, 10, 20, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2']
    }

    # Create a Random Forest classifier
    rf = RandomForestClassifier()

    # Use grid search cross-validation to find the optimal hyperparameters
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=14)
    grid_search.fit(X_train, y_train)

    # Print the best hyperparameters
    print("Best hyperparameters: ", grid_search.best_params_)

    # Train the model with the best hyperparameters
    best_rf = RandomForestClassifier(**grid_search.best_params_)
    best_rf.fit(X_train, y_train)

    # Evaluate the model
    accuracy = best_rf.score(X_test, y_test)
    print("Accuracy:", accuracy)
