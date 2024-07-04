import numpy as np
import pandas as pd

def generate_numeric_data(num_samples, num_features):
    """
    Generate synthetic numerical data.

    Parameters:
    - num_samples (int): Number of samples (rows) in the dataset.
    - num_features (int): Number of features (columns) in the dataset.

    Returns:
    - pd.DataFrame: DataFrame containing synthetic numerical data.
    """
    data = np.random.randn(num_samples, num_features)
    return pd.DataFrame(data, columns=[f'Feature_{i}' for i in range(num_features)])

def generate_categorical_data(num_samples, categories, proportions=None):
    """
    Generate synthetic categorical data.

    Parameters:
    - num_samples (int): Number of samples (rows) in the dataset.
    - categories (list): List of category labels.
    - proportions (list, optional): Proportions of each category. Default is None (equal proportions).

    Returns:
    - pd.DataFrame: DataFrame containing synthetic categorical data.
    """
    if proportions is None:
        proportions = [1 / len(categories)] * len(categories)
    data = np.random.choice(categories, size=num_samples, p=proportions)
    return pd.DataFrame({'Category': data})
