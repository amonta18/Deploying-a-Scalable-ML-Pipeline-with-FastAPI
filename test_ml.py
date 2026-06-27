
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.model import (
    train_model,
    inference,
    compute_model_metrics,
)

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # Test that train_model returns a RandomForestClassifier.
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0])
    
    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)

# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    Test that inference returns the correct number of predictions.
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0])

    model = train_model(X_train, y_train)
    preds = inference(model, X_train)

    assert len(preds) == len(y_train)

# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test that the metric values are between 0 and 1.
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])
    
    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
