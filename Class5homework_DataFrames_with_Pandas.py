"""
DataFrames with Pandas

Library meant to help with data analysis using two new data structures: Series and DataFrames.
At first it will resemble a lot like numpy Arrays, but the big difference is that we can assign labels to our
n dimensional, making it possible to create DataFrames, a table structure that can be used very similarly to
Excel or SQL tables.
Has many productivity functions to facilitate data visualization, manipulation and cleaning
Has many data loaders making it capable of integrating with many sources like csvs, xlsx, sql and html pages.
Let’s take a look together at pandas in the CEBD-1160-code project

"""

import pandas as pd

# 1. Load the insurance.csv in a DataFrame using pandas.
insurance_df = pd.read_csv(filepath_or_buffer='insurance.csv', sep=",", header=0)

# 2. Explore the DataSet using functions.
print(f"Printing an entire DataFrame: \n{insurance_df.to_string()}\n")
print(f"Show all the column names for a DataFrame: \n{insurance_df.columns}\n")
print(f"Show all the index for this DataFrame: {insurance_df.index}\n")
print(f"Show the data types for each column:\n{insurance_df.dtypes}\n")
print(f"This DataFrame's shape is: {insurance_df.shape}\n")
print("A concise summary of this DataFrame:\n")
insurance_df.info()
print(f"\nThe generate descriptive statistics of this DataFrame:\n{insurance_df.describe()}\n")

# Summary of Pandas DataFrame attributes/methods:
# - to_string(): Used to render a DataFrame to a console-friendly tabular output.
#   Using Print function won't show difference from print(df)
# - columns: Return the column labels of the DataFrame.
# - index: Return the index (row labels) of the DataFrame.
# - dtypes: Return the dtypes in the DataFrame.
# - shape: Return a tuple representing the dimensionality of the DataFrame.
# - info(): Print a concise summary of a DataFrame. So there is no need to add print() function.
# - describe(): Generate descriptive statistics.

# 3. Print only the column age
print(f"Show column[age]:\n{insurance_df['age']}\n")

# 4. Print only the columns age,children and charges
print(f"Show columns[age][children][charges]:\n{insurance_df[['age', 'children', 'charges']]}\n")

# 5. Print only the first 5 lines and only the columns age,children and charges
print(f"Show first 5 lines of columns[age][children][charges]:\n"
      f"{insurance_df.head()[['age', 'children', 'charges']]}\n")

# 6. What is the average, minimum and maximum charges ?
print(f"The average charges is about: {insurance_df['charges'].mean():.2f}")
print(f"The minimum charges is about: {insurance_df['charges'].min():.2f}")
print(f"The maximum charges is about: {insurance_df['charges'].max():.2f}\n")

# 7. What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
persons = insurance_df[insurance_df.charges == 10797.3362]
print(persons)  # Persons is returned as a DataFrame even there is only one result.

# Using for loop to iterate each row of DataFrame thus making each row becomes a Series.
# _ is a variable returned but not utilized.
for _, person in persons.iterrows():
    print(f"The person who paid 10797.3362 is {person['age']} years old and "
          f"{person['sex']} and if smoker: {person['smoker']}.\n")

# 8. What is the age of the person who paid the maximum charge?
mostPayer = insurance_df[insurance_df.charges == insurance_df['charges'].max()]
print(mostPayer)  # Return a DataFrame

# Use DataFrame.iloc to locate a single elements. (i: use integer index, loc is the label)
age = mostPayer.iloc[0]['age']
charge = mostPayer.iloc[0]['charges']
print(f"The person who paid most charges {charge} is {age} years old.\n")

# 9. How many insured people do we have for each region?
print(insurance_df.groupby('region')['region'].count())

# 10. How many insured people are children?
print(f"\nThe total insured children are: {insurance_df['children'].sum()}\n")

# 11. What do you expect to be the correlation between charges and age, bmi and children?
"""
BMI (Body mass index) definition: A key index for relating weight to height. Abbreviated BMI. 
BMI is a person's weight in kilograms (kg) divided by his or her height in meters squared.

I think by common sense, insurance premiums are positively related to age.
BMI is most related with weight and height as definition, so I don't think it is related to has children or not. 

"""

# 12. Using the method corr(), check if your assumptions were correct.
print(insurance_df.corr())

# DataFrame.at is also used to locate one singe element by using its index,column labels.
charges_corr_age = insurance_df.corr().at['age', 'charges']
bmi_corr_children = insurance_df.corr().at['bmi', 'children']

print(f"\nThe correlation between charges and age is : {charges_corr_age:.6f}")
print(f"The correlation between bmi and children is : {bmi_corr_children:.6f}")

# Output: 
# The correlation between charges and age is : 0.299008. Yes, it shows +correlation 
# The correlation between bmi and children is : 0.012759. No, it shows very low correlation