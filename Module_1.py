import pandas as pd
import numpy as np

# Q1. Version of NumPy
np_version=np.__version__
print(np_version)

# There is 1.23.2 version of NumPy installed.

# Getting the data
data=pd.read_csv('data.csv')

# Q2. How many records?
print(data.shape)

# There are 11 914 records in this dataset.

# Q3. TOP-3 the most frequent manufacturers
freq_make=data.groupby(['Make']).count().sort_values(by='Model', ascending=False).iloc[:3,0].reset_index()
print(freq_make.Make)

# TOP-3 most frequent manufactures: Chevrolet, Ford, Toyota.

# Q4. Number of uniaque Audi
freq_audi=data[data.Make=='Audi'].Model.nunique()
#print(freq_audi)

# There are 12 unique Audi  models.

# Q5. Cols with missing values
print(data.isnull().any().count())

# There are 16 cols with values missing.

# Q6.
cyl_median=data['Engine Cylinders'].median()
print("The median is: " + str(cyl_median)) # 6.0
cyl_mode=data['Engine Cylinders'].mode()
print("The mode is: {}".format(cyl_mode)) # 4.0

cyl_median_new=data['Engine Cylinders'].fillna(cyl_mode).median()
print("The new median is: {}".format(cyl_median_new))

# The median is the same.

# Q7.
data_lotus=data[data.Make=='Honda']
print(data_lotus)

# ??????