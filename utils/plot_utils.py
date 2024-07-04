import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column):
    """
    Plot histogram of a specific column in a DataFrame.

    Parameters:
    - data (pd.DataFrame): Input DataFrame containing the data.
    - column (str): Column name to plot the histogram.

    Returns:
    - None
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], kde=False, bins=20, color='blue')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_correlation_heatmap(data):
    """
    Plot heatmap of correlations between numerical columns in a DataFrame.

    Parameters:
    - data (pd.DataFrame): Input DataFrame containing numerical data.

    Returns:
    - None
    """
    corr_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    plt.title('Correlation Heatmap')
    plt.show()
