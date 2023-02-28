from sklearn.ensemble import RandomForestClassifier

def createMlModel():
    """
    Creates a new instance of a Random Forest classifier with default hyperparameters.

    Returns:
        sklearn.ensemble.RandomForestClassifier: The new Random Forest classifier instance.
    """

    # Set the hyperparameters for the new Random Forest classifier
    n_estimators = 400
    max_depth = 30
    random_state = 42
    min_samples_split = 10
    n_jobs = 14
    max_features = 'log2'

    # Create the new Random Forest classifier instance with the specified hyperparameters
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state,
                                    min_samples_split=min_samples_split, n_jobs=n_jobs, max_features=max_features)

    return model
