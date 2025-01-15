import pandas as pd
import matplotlib.pyplot as plt

#first we need to get the data as a csv, excel or json file
#then look over the columns and understand the data 

#read the csv file 
data = pd.read_csv('super_store.csv', encoding='latin1') 

#Explore the data 
#see the frist few rows
print(data.head())

#view the columns
print(data.columns)

#see the column with data types
print(data.info())

#check for any missing/ null values
print(data.isnull().sum())

#summary of the data which shows the count, mean, std, min, max, 25%, 50%, 75%
print(data.describe())

#Data Cleaning

#option 1
#drop any rows with missing or null values
data.dropna(inplace=True)  #inplace=True means the changes will be pernament on the dataframe which is csv file

#option 2
#fill the missing / null values with values
#data['Order Date'].fillna('2020-03-19', inplace=True)

#fix data types

#date column convert to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

#remove duplicates

#find duplicates
data.duplicated()

#drop the duplicates
data.drop_duplicates(inplace=True)

#certain values in the columns will have to capitalize first letter
data['Category'] = data['Category'].str.capitalize() 

#Anaylsis 

#find the profit margin 
data["Profit Margin %"] = (data["Profit"] / data["Sales"]) * 100 #data["profit margin"] is the name of the column that will be created

print(data.head())

#calculate discount impact 
discountAnalysis = data.groupby('Discount')[['Sales', 'Profit']].mean() #group by discount and calculate the mean of sales column and profit column that have the same discount 

print(discountAnalysis)

#how well is a product performing 
#top product by sales
topProduct = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print(topProduct)

#top products by profit
topProfit = data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)

print(topProfit)

#determine trends by the performance of the category or sub category

categoryTrend = data.groupby('Category')['Sales'].sum()
subCategoryTrend = data.groupby('Sub-Category')['Sales'].sum()

print(categoryTrend)
print(subCategoryTrend)

#region revenue
regionRevenue = data.groupby('Region')['Sales'].sum()
print(regionRevenue)

#region profit
regionProfit = data.groupby('Region')['Profit'].sum()
print(regionProfit)

#state profit and sales
stateProfitSales = data.groupby('State')[['Sales', 'Profit']].sum().sort_values('Sales', ascending=False).head(10) #['sales, profit'] calculate sum of each column which are sales and profit

print(stateProfitSales)

# Customer and Segment Analysis

#segment Performance
segmentPerformance = data.groupby('Segment')[['Sales', 'Profit']].sum()
#top Customers by Sales:
topCustomers = data.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(topCustomers)

#Temporal Analysis

# monthly sales trends
data['Month'] = data['Order Date'].dt.month
monthlySales = data.groupby('Month')['Sales'].sum()
print(monthlySales)

# yearly trends
# extract year from Order Date
data['Year'] = data['Order Date'].dt.year
yearlySales = data.groupby('Year')['Sales'].sum()
print(yearlySales)


# shipping times
# calculate shipping times to evaluate logistical efficiency
data['Shipping Time (days)'] = (data['Ship Date'] - data['Order Date']).dt.days
shippingTimes = data.groupby('Ship Mode')['Shipping Time (days)'].mean()
print(shippingTimes)



# discount against profit 

#find the relationship between discount and profit:
discountProfit = data.groupby('Discount')['Profit'].mean()
print(discountProfit)


#Visualize
#top profit product in a bar graph
topProfit = data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
topProfit.plot(kind='bar', figsize=(10, 6), title='Top 10 Products by Sales and Profit')
plt.ylabel('Amount')
plt.xlabel('Product Name')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# totalSales = data['Sales'].sum()
# print(totalSales)

# totalProfit = data['Profit'].sum()
# print(totalProfit)

#overall profit margin
overallProfitMargin = (data['Profit'].sum() / data['Sales'].sum()) * 100
print(overallProfitMargin)

#Line Plot: Monthly Sales Trends
data['Month'] = data['Order Date'].dt.month #this will get the month from order date column and make as a month column with extract months
topSales = data.groupby('Month')['Sales'].sum()

topSales.plot(kind='line', figsize=(10, 6), title='Monthly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Months')
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid()
plt.tight_layout()
plt.show()
