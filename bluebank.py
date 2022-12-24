# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# Method 1 to read json data
json_file = open('loan_data_json.json')
tdata = json.load(json_file)

# Method 2 to read json data
with open('loan_data_json.json') as json_file:
    tdata = json.load(json_file)
    
# transform to data frame
loandata = pd.DataFrame(tdata)

# Finding unique value for the purpose column
print (loandata['purpose'].unique())

#describe the data
loandata.describe()

#describe the data for a specific column
print(loandata['int.rate'].describe())
loandata['fico'].describe()
loandata['dti'].describe()

# Using EXP to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income

# for loops
fruits = ['apple', 'pear', 'banana']

for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)
    
for x in range(0,3):
    y= fruits[x] + ' for sale'
    print (y)
    
# applying for loops to loan data

length = len(loandata)
ficocat = []
for x in range(0, length):
     category = loandata['fico'][x]
     if category >=300 and category < 400:
         cat = 'Very Poor'
     elif category >=400 and category < 600:
         cat = 'Poor'
     elif category >=610 and category < 660:
         cat = 'Fair'
     elif category >=660 and category < 700:
         cat = 'Good'
     elif category >= 700:
         cat='Excellent'
     else:
             cat = 'Unknown'
     ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
    
loandata['fico_category'] = ficocat
    
    
# #while loop
# i=1
# while i < 10:
#     print (i)
#     i = i+1

# Try and except exceptions handling
# =============================================================================
# lengths = len(loandata)
# ficocats = []
# for x in range(0, lengths):
#      categorys = 'red'#loandata['fico'][x]
#      
#      try:
#          
#          if categorys >=300 and categorys < 400:
#              cats = 'Very Poor'
#          elif categorys >=400 and categorys < 600:
#              cats = 'Poor'
#          elif categorys >=610 and categorys < 660:
#              cats = 'Fair'
#          elif categorys >=660 and categorys < 700:
#              cats = 'Good'
#          elif categorys >= 700:
#              cats ='Excellent'
#          else:
#                  cats = 'Unknown'
#      except:
#         cats = 'Error - Unknown'
#         
#         
#      ficocats.append(cats)
#     
# ficocats = pd.Series(ficocats)
#     
# loandata['fico_categorys'] = ficocats
# =============================================================================

#df.loc as conditional statements
#df.loc[df[columnname] condition, newcolumn] = 'value if the condition is met'

# for interest rates, a new column is wanted. rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# number of loans/rows by fico_category

catplot = loandata.groupby(['fico_category']).size()
catplot.plot.bar(color = 'green', width = 0.2)
plt.show()


purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='pink')
plt.show()


# scatter plot. with this u need x y values or variables9
#here we want to check debt to income ratio

xpoint = loandata['annual income']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

# Writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)
