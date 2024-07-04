import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(dataframe):
    plt.figure(figsize=(10, 6))
    sns.pairplot(dataframe)
    plt.title('Pairplot of Synthetic Data')
    plt.show()

visualize_data(synthetic_data)
