!pip install pandas
import pandas as pd

data_path = 'data/titanic.csv'
raw_data = pd.read_csv(data_path)
raw_data.head()

#search for missing values
raw_data.isna().sum()

# Making Male/ Female to integer numbers calles Label Encoding
raw_data["Sex"].replace("male", 1, inplace = True)
raw_data["Sex"].replace("female", 0, inplace = True)
raw_data.head()

raw_data.to_csv('data/data_features.csv', index=False, float_format='%g')
