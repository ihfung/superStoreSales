import pandas as pd

#first we need to get the data as a csv, excel or json file
#then look over the columns and understand the data 

#read the csv file 
df = pd.read_csv('super_store.csv', encoding='latin1') 

#Explore the data 
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

#Data Cleaning

#option 1
#drop any rows with missing or null values
df.dropna(inplace=True)  #inplace=True means the changes will be pernament on the dataframe which is csv file

#option 2
#fill the missing / null values with values
#df['Order Date'].fillna('2020-03-19', inplace=True)

#fix data types

#date column convert to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

#remove duplicates

#find duplicates
df.duplicated()

#drop the duplicates
df.drop_duplicates(inplace=True)

#certain values in the columns will have to capitalize first letter
df['Category'] = df['Category'].str.capitalize() 

#Anaylsis 

#find the profit margin 
df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100

print(df.head())

#calculate discount impact 
discount_analysis = df.groupby('Discount')[['Sales', 'Profit']].mean() #group by discount and calculate the mean of sales column and profit column that have the same discount 

print(discount_analysis)

