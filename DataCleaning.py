# Saffron Livaccari
# Email saffron.livaccari@gmail.com for inquiries.

import pandas as pd  # pandas
import numpy as np

"""
##### This script is meant to clean up a CSV data sheet

Written by Saffron Livaccari
April 14th, 2022
"""

# CSV File
file_path = "/Users/saffron/Documents/Application Things/KoBold Metals Assignment/MN_geochem_ads.csv"  # Change this to your file path!
df = pd.read_csv(file_path)

# First, I want to see the dataset
print(df.columns) # column names
print(len(df.columns.values.tolist())) # number of columns
print(df.head) # first and last rows of the dataset


# Function for looking at what is in the CSV file
def checking_values(column_name):
    column_df = df[column_name].dropna()  # Drop any blanks just for this
    column_list = column_df.tolist()
    print("\n Column: ", column_name) # name of the column we are looking at
    # print("\nThe original column: ")
    # print(column_list)
    # print("\n All of the unique values in the list: ")
    # print(column_df.unique().tolist()) # Gets all of the unique values in each column
    print("\n The top 5 occurences per column: ")
    print(column_df.value_counts().nlargest(5))  # Gets the 5 top occurances per column
    print("\n The lowest 5 occurences per column: ")
    print(column_df.value_counts().nsmallest(5))  # Gets the 5 lowest occurances per column
    sort_list = sorted(column_list)
    print("\nThe highest five values in the list:")
    print(sort_list[-5:])
    print("\nThe lowest five values in the list:")
    print(sort_list[0:5])
    print("\n")


def check_outliers(column_name):
    print("For Column: ",column_name)
    upper_quantile = (df[column_name] > df[column_name].quantile(0.99)) # finds the index of the values out of 99% percentile
    lower_quantile = (df[column_name] < df[column_name].quantile(0.01)) # finds the index of the values out of 1% percentile
    upper_index = np.concatenate(np.where(upper_quantile)).tolist()  # turn these indexes into a list
    lower_index = np.concatenate(np.where(lower_quantile)).tolist()  # turn these indexes into a list
    list = df[column_name].tolist()
    upper_values = [list[i] for i in upper_index]  # turns the actual values from the index into an list
    lower_values = [list[i] for i in lower_index]  # turns the actual values from the index into an list
    print("Upper Outliers: ", upper_values)
    print("Lower Outliers: ", lower_values)
    outliers = upper_values + lower_values
    print("\n")
    return outliers # returns a list of all the outlier values

def replace_outliers(column_name):
    outlier_list = check_outliers(column_name) # runs the function "check_outliers_ to get the list of outliers
    for i in outlier_list:  df[column_name] = df[column_name].replace(i, np.NaN) #replaces any outliers with NaN
    return df[column_name]

def clean_data_columns(*args): # variable number of arguements
    data_columns = df[[*args]].copy() # turns the columns into a new dataframe
    for i in data_columns: data_columns[i] = data_columns[i].apply(pd.to_numeric,errors='coerce')
    # The above like applies the function to_numeric which attempts to turn the value into an integer.
    # If it cannot be turned into an integer, the value is turned into NaN
    return data_columns

# First, I want to review all of the data in every column
for i in (df.columns.values.tolist()): checking_values(i)

## I assume that 'sample' is supposed to be a unique key ID
# Here's a line that finds duplicates:
ID_list = df['sample'].tolist() # puts all of the sample data points into a list
duplicate = [ID_list[i] for i in range(len(ID_list)) if ID_list[i] in ID_list[:i]]
# The above line will return the ID_list value if that value is in the whole list
# (as in there are two or more of that value)
print("Duplicate IDs: ",duplicate)
# There are duplicate values. The ID's could be updated or the duplicate rows could be dropped.
# This would have to be determined by someone who knows the data better.

# I noticed that some of the words in columns 'lithology' and 'structure' was incorrect,
# so I wanted to create a dictionary that replaces these words
# I like using dictionaries for this because:
# 1. The words I want to replace are VERY specific,
# 2. I would not replace any values unintentionally.
# 3. someone could alter these values to values that might be MORE CORRECT
# 4. quickly see that I have replaced these values
misspellings = {"basalt.": "basalt",  # THESE ARE IN THE 'lithology' COLUMN
               "Basalt": "basalt",
               "basaltt": "basalt",
               "DACITE": "dacite",
               "GABBRO": "gabbro",
               "gabro": "gabbro",
               "bassalt": "basalt",
               "CHERT": "chert",
               "GRAYWACKE": "graywacke",
               "none":"",

               "plug/pipe": "plug; pipe",  # THESE ARE IN THE 'structure' COLUMN
               "sill/laccolith": "sill; laccolith"}

# replaces any values in the misspelling dictionary with
# the corresponding value in the key:value pair
df['lithology'] = df['lithology'].replace(dict(misspellings))
df['structure'] = df['structure'].replace(dict(misspellings))


# There are issues with specifically the columns that whole the data.
# One is Ni_ppm is a column of strings rather than integers.
# Ni_ppm column has '<1.5', which is not a good value to have since it is not a numeric value.
# This could be replaced another value or dropped.
# I chose to drop this value (turn into NaN), but someone who knows this data better could make a better decision.
# df['Ni_ppm'] = pd.to_numeric(df['Ni_ppm'].replace('<1.5', np.NaN)) # This line would drop any <1.5 values,
# But I made a function to make it more transferable

data = ["Co_ppm","Cu_ppm","Ni_ppm"]
print("\n")
for i in data: df[i] = clean_data_columns(i) # Removes any strings in the data columns
for i in data: replace_outliers(i) # Removes any OUTLIERS in the data columns
# These outliers may not be outliers and will have to be reviewed by someone who knows the data better!!


# replace these column names so it is easier to input into QGIS
df.rename(columns={'easting_wgs84': 'longitude',
                   'northing_wgs84': 'latitude'}, inplace=True) # replace these column names

# Then, check the data in every column again!
for i in (df.columns.values.tolist()): checking_values(i)

### CHANGE THIS TO NAME
file_name = '/Users/saffron/Documents/Application Things/KoBold Metals Assignment/csvFile_CLEANED.csv'

# saving the new csv
df.to_csv(file_name)
print('\nDataFrame is written to  csv File successfully.')
