import numpy as np
import pandas as pd

def generate_numeric_data(num_samples, num_features):
    data = np.random.randn(num_samples, num_features)  # Generate random normal data
    return pd.DataFrame(data, columns=[f'Feature_{i}' for i in range(num_features)])

synthetic_data = generate_numeric_data(1000, 5)
