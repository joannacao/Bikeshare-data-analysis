# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 00:06:25 2018

@author: joann
"""
import numpy as np
import pandas as pd
from scipy import stats
from datetime import datetime as dt
#Display or graph 3 metrics or trends from the data set that are interesting to you.
#Which start/stop stations are most popular?
#What is the average distance traveled
#How many riders include bike sharing as a regular part of their commute?

#3 trends: Duration, plan duration, Passholder

#Regular user -> monthly user 

#Duration unit: seconds

#average distance: using latitude and longitude?

#below is for testing comparing dates
#a = dt.strptime('2016-07-07','%Y-%m-%d')
#b = dt.strptime('2016-07-08', '%Y-%m-%d')
#print(a < b)

df = pd.read_csv('metro-bike-share-trip-data.csv')
#check if bike riders have taken rides twice in the same day
counter = 0
for i in df['Start Time']:
    date = df['Start Time'][i][:10]
    specificDate = df[['Start Time'] == date]
    #still trying to determine how to increment date
    for p in specificDate['Bike ID']: #I'm aware this is inefficient, but if I had more time
        #I would try to figure out a more efficient method
        for p2 in range(1,len(specificDate['Bike ID'])):
            if p == p2:
                counter = counter + 1 #increment counter


#print(df['Starting Station ID'].describe())
print(df['Duration'].describe()) #figure out how to neatly display information
#box plot for the above currently looks very messy
startStationMode = stats.mode(df['Starting Station ID'])
endStationMode = stats.mode(df['Ending Station ID'])
print('Most popular start station: ', startStationMode)
print('Most popular end station: ', endStationMode)

