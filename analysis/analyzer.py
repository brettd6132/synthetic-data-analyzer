def analyze_data(dataframe):
    summary_stats = dataframe.describe()
    correlation_matrix = dataframe.corr()
    return summary_stats, correlation_matrix

summary, correlation = analyze_data(synthetic_data)
print(summary)
print(correlation)
