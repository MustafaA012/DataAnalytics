# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:56:17 2022

@author: Mustafa
"""

import pandas as pd

# file_name pd.read_csv('file.csv')  ----This is the format for read csv

#tdata = pd.read_csv('transaction.csv')

tdata = pd.read_csv('transaction.csv', sep=';')

#Summary of tdata
#tdata.info()

#Playing around with variables

#var = {'name':'Dee','Location':'South Africa','Age':'23'}

#Working with calculations
#Defining variables

CostPerItem=11.73
SalesPerItem=21.11
NumberOfItemsPurchased=6

ProfitPerItem= SalesPerItem-CostPerItem
ProfitPerTran = ProfitPerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SalesPerTransaction = SalesPerItem * NumberOfItemsPurchased

#Cost Per Transaction column calculation
#variable = dataframe['column_name]

CostPerItem = tdata['CostPerItem']
NumberOfItemsPurchased = tdata['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

tdata['CostPerTransaction'] = CostPerTransaction
#We can also do it as the below;
# tdata['CostPerTransaction'] = tdata['CostPerItem'] * tdata['NumberOfItemsPurchased']

#Sales Per Transaction column calculation

#SalesPerItem = tdata['SellingPricePerItem']
#tdata['SalesPerTransaction'] = tdata['SellingPricePerItem'] * tdata['NumberOfItemsPurchased']
SalesPerTransaction = tdata['SellingPricePerItem'] * tdata['NumberOfItemsPurchased']
tdata['SalesPerTransaction'] = SalesPerTransaction
tdata['ProfitPerTransaction'] = SalesPerTransaction - CostPerTransaction
tdata['Markup'] = (tdata['ProfitPerTransaction']) / CostPerTransaction 

tdata['Markup'] = round(tdata['Markup'],2)

#checking colums data type
print(tdata['Day'].dtype)

#change columns type
day = tdata['Day'].astype(str)
year = tdata['Year'].astype(str)
print (day.dtype)
my_date = day+'-'+tdata['Month']+'-'+year
#print (my_date)
tdata['date'] = my_date

# using iloc to view specific columns/rows

tdata.iloc[0] #views the rows with index 0
tdata.iloc[0:3] #First 3 rows
tdata.iloc[-5] #last 5 rows

tdata.head(5) #brings in first 5 rows

tdata.iloc[:,2] #all rows but specific column, brings in all rows in 2nd column

tdata.iloc[4,2]   #brings in  4th row 2nd column


#Using split to split the  client_keywords field

split_col = tdata['ClientKeywords'].str.split(',' , expand=True)

#Creating new columns for the split columns in Client keyword

tdata['ClientAge'] = split_col[0]
tdata['ClientType'] = split_col[1]
tdata['LengthOfContract'] = split_col[2]

#Using the replace function

tdata['ClientAge'] = tdata['ClientAge'].str.replace('[', '')
tdata['LengthOfContract'] = tdata['LengthOfContract'].str.replace(']', '')

#Using the lower function to change item to lower case

tdata['ItemDescription'] = tdata['ItemDescription'].str.lower()

#how to merge files

#briging in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files: mergedf = pd.merge(df_old, df_new, on ='key')

tdata = pd.merge(tdata, seasons, on = 'Month')

#tdata.info()

#dropping columns
# df= df.drop(columnName, axis = 1)
# axis =1 cos its column. If its row, axis=0

tdata = tdata.drop('ClientKeywords', axis = 1)
tdata = tdata.drop(['Day', 'Month', 'Year'], axis = 1)

#Export into csv

tdata.to_csv('ValueInc_Cleaned.csv', index = False)

