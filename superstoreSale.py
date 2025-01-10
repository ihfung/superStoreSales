import pandas as pd

#first we need to get the data as a csv, excel or json file
#then look over the columns and understand the data 

#read the csv file 
df = pd.read_csv('super_store.csv', encoding='latin1') 

#explore the data 
#see the frist few rows
print(df.head())

#view the columns
print(df.columns)

#see the column with data types
print(df.info())

#check for any missing/ null values
print(df.isnull().sum())

#summary of the data which shows the count, mean, std, min, max, 25%, 50%, 75%
print(df.describe())

