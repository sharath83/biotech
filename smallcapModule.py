# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:50:56 2015

@author: sharath
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stocks = pd.read_csv('/Users/homw/Documents/MSDS16/Python project/smallCap/smallcap2.csv')

num_plots = 2
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
labels = []
for i in stocks['EventNo'].unique():
    if stocks[stocks['EventNo']==i].Result[(i-1)*20] == 'N':    
        plt.plot(np.arange(1,21),stocks[stocks['EventNo']==i].Close[::-1]) #Reverse the array, Plot older prices first
        #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)  
        x = stocks[stocks['EventNo'] == i].Company_Name[(i-1)*20]
        
        labels.append(x.partition(' ')[0])   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=3, loc='upper center', 
           bbox_to_anchor=[0.5, 1.1], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
plt.xlabel('Days Around Results Announcement')
plt.ylabel('Daily Close Prices')
plt.show()

#Positive Small cap
num_plots = 4
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
labels = []
for i in stocks['EventNo'].unique():
    if stocks[stocks['EventNo']==i].Result[(i-1)*20] == 'P':    
        plt.plot(np.arange(1,21),stocks[stocks['EventNo']==i].Close[::-1]) #Reverse the array, Plot older prices first
        #Label it, ex: AMGN-1-P-3 (Event1, Positive, Phase 3)  
        x = stocks[stocks['EventNo'] == i].Company_Name[(i-1)*20]
        
        labels.append(x.partition(' ')[0])   
#stocks[stocks['EventNo']==1].Company_Code[(1-1)*17]
# Set labels on top of the graph
plt.legend(labels, ncol=3, loc='upper center', 
           bbox_to_anchor=[0.5, 1.1], 
           columnspacing=0.5, labelspacing=0.0,
           handletextpad=0, handlelength=1.5,
           fancybox=True, shadow=False)
plt.xlabel('Days around Results Announcement')
plt.ylabel('Daily Close Prices')
plt.show()


x = stocks[stocks['EventNo'] == 2]#.Company_Name[0]
x.partition(' ')[0]
stocks[stocks['EventNo']==1].Close[::-1]
