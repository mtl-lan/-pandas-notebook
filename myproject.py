import pandas as pd

"""
DataSet title: Title: Wine Quality
This project is going to predict the quality of the wine before a wine taster gives his/her evaluation.
It may help wine manufacturers to develop new wine.

Step 1: load and organize the data in a pandas data frame format.
"""
redwine_link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
whitewine_link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

# Loading datasets (red wine and white wine)
redwine_table = pd.read_csv(redwine_link, ";", header=0)
whitewine_table = pd.read_csv(whitewine_link, ";", header=0)

# Concatenate two datasets vertically (red wine has the same columns as white wine)
wine = pd.concat([redwine_table, whitewine_table])

# Check and make sure the concatenation is correct
assert redwine_table.shape[0] + whitewine_table.shape[0] == wine.shape[0], 'merge error'
assert redwine_table.shape[1] == whitewine_table.shape[1] == wine.shape[1], 'merge error'

"""
Step 2: compute and print information and summary statistics on the combined wine DataFrame
"""

# Check how the data is distributed
print(f"First 5 rows:\n{wine.head()}")

# Show Information about wine dataFrame (columns and indexes)
# ==> All the data type are numeric numbers. No missing data.
print("\nA concise summary of this DataFrame:\n")
wine.info()

# Show a summary statistics information
# ==> mean quality is 5.818378, so we can think the quality over 7 is high quality wine.
print(f"\nThe generate descriptive statistics of whole dataset:\n{wine.describe()}\n")

# Sort out the wine's quality > 7,8,9 to evaluate their statistics and compare with the whole dataset.
# ==> with the quality is getting higher, the alcohol is higher.
print(f"Statistics for Wine quality 7:\n{wine[wine.quality == 7].describe()}")
print(f"Statistics for Wine quality 8:\n{wine[wine.quality == 8].describe()}")
print(f"Statistics for Wine quality 9:\n{wine[wine.quality == 9].describe()}")

# Show best wine (quality =9)
print(f"Wine quality is 9:\n{wine[wine.quality == 9]}")

"""
Step 3: compute and print correlations on the dataset
"""
# ==> correlation between quality and alcohol is 0.444319.
# ==> correlation between quality and density is -0.305858.
# ==> correlation between density and residual sugar is 0.552517.
# ==> correlation between alcohol and density is -0.686745.

# Set it to None to display all columns in the dataFrame
# pd.set_option('display.max_columns', None)  # to display all the columns in order to show all the correlations.
print("correlation matrix is:\n", wine.corr())
