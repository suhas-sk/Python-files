# using isnull with csv file
import pandas as pd
import numpy as np

df = pd.read_csv("employees.csv")

# creating bool series True for Nan values
bool_series = pd.isnull(df["Gender"])

# displaing data with only Gender=Nan
print(df[bool_series])

# creating bool series False for Nan values
bool_series = pd.notnull(df["Gender"])

# displaing data with only Gender=Nan
print(df[bool_series])

