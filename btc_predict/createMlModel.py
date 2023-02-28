from sklearn.ensemble import RandomForestClassifier

def createMlModel():
    # Create the machine learning model
    model = RandomForestClassifier(n_estimators=400, max_depth=30, random_state=42,min_samples_split=10, n_jobs=14, max_features='log2')
    return model