# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:41:39 2022

@author: Mustafa
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# reading excel or xlsx files
tdata = pd.read_excel('articles.xlsx')

#summary of the data
tdata.describe()

#summary of the columns
tdata.info()

#accounting the number of article per source
#format of groupby: df.(['column to group'])[column to count].count()
tdata.groupby(['source_id'])['article_id'].count()

#number of reactions per publisher
tdata.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column
tdata=tdata.drop('engagement_comment_plugin_count', axis=1)

# Functions in python
def thisFunction():
    print ('This is my first function')
    
thisFunction()

#This is a function with variables
def aboutMe(name, surname, location):
    print('This is '+ name+' My surname is '+surname+ ' I am from '+location)
    return name, surname, location

a = aboutMe('Dee', 'Naidoo', 'South Africa')

#Using for loops in function
def favfood(food):
    for x in food:
        print ('Top food is '+x)
        
fastfood = ['Salad', 'Water', 'Fruit']

favfood(fastfood)

#Creating a keyword flag

keyword = 'crash'

# Lets create a for loop to isolate each title row

length = len(tdata)
keyword_flag = []
for x in range(0, length):
    heading = tdata['title'][x]
    try:
        if keyword in heading:
            flag = 1
        else:
            flag = 0
    except:
        flag = 0
    keyword_flag.append(flag)
    
# creating a function

def keywordflag(keyword):
    length = len(tdata)
    keyword_flag = []
    for x in range(0, length):
        heading = tdata['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordflag('murder')

#creating a new column in tdata dataframe
tdata['keyword_flag'] = pd.Series(keywordflag)

#Sentiment Intent Analyzer

sent_int = SentimentIntensityAnalyzer()

text = tdata['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(tdata)

for x in range(0,length):
    try:
        text = tdata['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

tdata['title_neg_sentiment'] = title_neg_sentiment
tdata['title_pos_sentiment'] = title_pos_sentiment
tdata['title_neu_sentiment'] = title_neu_sentiment


