# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:10:45 2015

@author: sharath
"""
#Analyzing 24 clinical trial results and their impact on stock prices of those corresponding companies
# Phase wise Analysis- Phase 3, 2 and 1
# Analysis by Nature of the Result - Success OR Failure
# Values considered - Daily Close Price and Daily volume traded
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain

#Read Clinical trials stock prices data
stocks = pd.read_csv('/Users/homw/Documents/MSDS16/Python project/stocks.final.csv')

#look at all the columns of the df
stocks.ix[0]
#Remove columns that are not used
stocks.drop(['open','high','low','TrialID'], axis = 1, inplace = True)

stocks['EventNo'].unique()
# Normalize close price for every event
close_norm = [] #Initialize

#Normalize the close price = Price/max(prices of a particular event)
for i in stocks['EventNo'].unique():
    x = list(float(price)/max(stocks[stocks['EventNo'] == i].close) for price in stocks[stocks['EventNo'] == i].close)
    close_norm.append(x)

stocks['normalized_close'] = list(chain.from_iterable(close_norm))


#----------All Trials in one plot -------------------------
#Plot normalized close price 
num_plots = 24
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# Plot normalized closing price for every event against 17 days duration
# 8 days before and 8 days after
labels = []
for i in stocks['EventNo'].unique():
    plt.plot(np.arange(-8,9),stocks[stocks['EventNo']==i].normalized_close)
    #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)    
    labels.append(stocks[stocks['EventNo']==i].Company_Code[(i-1)*17]+'-'+ str(i)+stocks[stocks['EventNo']==i].Result[(i-1)*17]+'-'+
    str(stocks[stocks['EventNo']==i].Phase[(i-1)*17]))   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=8, loc='upper center', 
           bbox_to_anchor=[0.5, 1.1], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
plt.xlabel('Clinical Trial - Daily Standardized Close Price Analysis')
plt.ylabel('Standardized Daily Close Prices')

plt.show()
# This plot shows Normalized closing prices variations across 24 events

#---------------------Phase 3 Plots------------------
#len(stocks[stocks['Phase']==3])/17 - Set No of plots to Number of Phase 3 records
num_plots = len(stocks[stocks['Phase']==3])/17
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# Plot normalized closing price for every event against 17 days duration
# 8 days before and 8 days after
labels = []
for i in stocks['EventNo'].unique():
    if stocks[stocks['EventNo']==i].Phase[(i-1)*17] == 3:
        plt.plot(np.arange(-8,9),stocks[stocks['EventNo']==i].normalized_close)
        #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)    
        labels.append(stocks[stocks['EventNo']==i].Company_Code[(i-1)*17]+'-'+ str(i)+stocks[stocks['EventNo']==i].Result[(i-1)*17]+'-'+
        str(stocks[stocks['EventNo']==i].Phase[(i-1)*17]))   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=6, loc='upper center', 
           bbox_to_anchor=[0., 1.02, 1., .102], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
#plt.xlabel('8 Days Before and 8 days After the Trial')
plt.ylabel('Standardized Daily Close Prices')
plt.xlabel('Phase 3 - Trials - Standardized close prices')
plt.show()

#---------------------Phase 2 Plots------------------
num_plots = len(stocks[stocks['Phase']==2])/17
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# Plot normalized closing price for every event against 17 days duration
# 8 days before and 8 days after
labels = []
for i in stocks['EventNo'].unique():
    if stocks[stocks['EventNo']==i].Phase[(i-1)*17] == 2:
        plt.plot(np.arange(-8,9),stocks[stocks['EventNo']==i].normalized_close)
        #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)    
        labels.append(stocks[stocks['EventNo']==i].Company_Code[(i-1)*17]+'-'+ str(i)+stocks[stocks['EventNo']==i].Result[(i-1)*17]+'-'+
        str(stocks[stocks['EventNo']==i].Phase[(i-1)*17]))   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=8, loc='upper center', 
           bbox_to_anchor=[0., 1.02, 1., .102], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
#plt.xlabel('8 Days Before and 8 days After the Trial')
plt.ylabel('Standardized Daily Close Prices')
plt.xlabel('Phase 2 - Trials - Standardized close prices')
plt.show()

#---------------------Phase 1 Plots------------------
num_plots = len(stocks[stocks['Phase']==1])/17
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# Plot normalized closing price for every event against 17 days duration
# 8 days before and 8 days after
labels = []
for i in stocks['EventNo'].unique():
    if stocks[stocks['EventNo']==i].Phase[(i-1)*17] == 1:
        plt.plot(np.arange(-8,9),stocks[stocks['EventNo']==i].normalized_close)
        #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)    
        labels.append(stocks[stocks['EventNo']==i].Company_Code[(i-1)*17]+'-'+ str(i)+stocks[stocks['EventNo']==i].Result[(i-1)*17]+'-'+
        str(stocks[stocks['EventNo']==i].Phase[(i-1)*17]))   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=8, loc='upper center', 
           bbox_to_anchor=[0., 1.02, 1., .102], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
#plt.xlabel('8 Days Before and 8 days After the Trial')
plt.ylabel('Standardized Daily Close Prices')
plt.xlabel('Phase 1 - Trials - Standardized close prices')
plt.show()

#-----------------Trials with  Positive results-----
num_plots = len(stocks[stocks['Result']=='P'])/17
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])

labels = []
for i in stocks['EventNo'].unique():
    if stocks[stocks['EventNo']==i].Result[(i-1)*17] == 'P':
        plt.plot(np.arange(-8,9),stocks[stocks['EventNo']==i].normalized_close)
        #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)    
        labels.append(stocks[stocks['EventNo']==i].Company_Code[(i-1)*17]+'-'+ str(i)+stocks[stocks['EventNo']==i].Result[(i-1)*17]+'-'+
        str(stocks[stocks['EventNo']==i].Phase[(i-1)*17]))   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=6, loc='upper center', 
           bbox_to_anchor=[0., 1.02, 1., .102], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
#plt.xlabel('8 Days Before and 8 days After the Trial')
plt.ylabel('Standardized Daily Close Prices')
plt.xlabel('Trials With Positive Results - Standardized close prices')
plt.show()

#-----------------Trials with  Negative results-----
num_plots = len(stocks[stocks['Result']=='N'])/17
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])

labels = []
for i in stocks['EventNo'].unique():
    if stocks[stocks['EventNo']==i].Result[(i-1)*17] == 'N':
        plt.plot(np.arange(-8,9),stocks[stocks['EventNo']==i].normalized_close)
        #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)    
        labels.append(stocks[stocks['EventNo']==i].Company_Code[(i-1)*17]+'-'+ str(i)+stocks[stocks['EventNo']==i].Result[(i-1)*17]+'-'+
        str(stocks[stocks['EventNo']==i].Phase[(i-1)*17]))   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=6, loc='upper center', 
           bbox_to_anchor=[0., 1.02, 1., .102], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
#plt.xlabel('8 Days Before and 8 days After the Trial')
plt.ylabel('Standardized Daily Close Prices')
plt.xlabel('Trials With Negative Results - Standardized close prices')
plt.show()

