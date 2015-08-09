__author__ = 'Jason'

import pandas as pd
import numpy as np
import pandas.io.date_converters as conv
import datetime
from pandas.tseries.offsets import *
import platform
# the stocks in the csv file include AMGN, GILD, LLY, BIIB, PFE, GILD, BMS, and MRK

# below are the dates of interest, the company, and the expected sign(postive or negative)

list = {'Event1': 'AMGN, 2013-03-19', 'Event2': 'GILD, 2013-03-05', 'Event3': 'LLY, 2013-02-07', 'Event4': 'BIIB, 2013-01-24',
        'Event5': 'BIIB, 2013-01-03', 'Event6': 'PFE, 2012-12-05', 'Event7': 'GILD, 2012-11-10', 'Event8': 'PFE, 2012-10-11',
        'Event9': 'BIIB, 2012-09-26', 'Event10': 'AMGN, 2012-08-08', 'Event11': 'PFE, 2012-08-06', 'Event12': 'BMS, 2012-08-02',
        'Event13': 'LLY, 2012-07-11', 'Event14': 'BMS, 2012-07-02', 'Event15': 'LLY, 2012-05-22', 'Event16': 'AMGN, 2012-05-16',
        'Event17': 'AMGN, 2012-03-28', 'Event18': 'LLY, 2012-03-28', 'Event19': 'AMGN, 2012-03-25', 'Event20': 'MRK, 2012-03-05',
        'Event21': 'GILD, 2012-02-03', 'Event22': 'BMS, 2011-12-22', 'Event23': 'BIIB, 2011-08-09', 'Event24': 'BMS, 2011-02-02'}

# retrieving stock values for this key date 3/19/2013 for AMGN
# first is to the retrieve the 10 days prior to the event and the 10 days after the event, including event date


def stockhunter(eventnumber, event_date, symbol):
    stocksdf = pd.read_csv('/Users/analyticsmachine/Desktop/MyLife/SchoolWork/UVA/CS_5010/project/stocks_historical.csv', names = ['symbol', 'date', 'open', 'high', 'low', 'close', 'volume'],
                       parse_dates = 'date',
                       infer_datetime_format = True,
                       keep_date_col = True,
                       index_col = 1)
    # converting the string event_date into a datetime character
    a = pd.Series([pd.to_datetime(event_date)])
    # utilizing Pandas dateoffset which will look at the 10 days prior to the event_date
    startdate = a[0] + DateOffset(days=-10)
    # utilizing Pandas dateoffset which will look at the 10 days following the event_date
    enddate = a[0] + DateOffset(days=10)
    # converting back into a string so pandas locate feature can select between the range of dates
    startdate1 = str(startdate)
    enddate1 = str(enddate)
    # removing the time section of the datetime
    startdate2 = startdate1[0:10]
    # removing the time section of the datetime
    enddate2 = enddate1[0:10]
    # searching between the range of dates
    keydate = stocksdf.loc[startdate2:enddate2]
    symbol_keydate = keydate[keydate['symbol'] == symbol]
    # adding the event_number to the data frame symbol_keydate
    symbol_keydate['Event_Number'] = eventnumber
    # calculating the percent change from close to close
    closedict = []
    perchange = []
    # calculating the percent change of close prices from one day to the next
    for closeprice in symbol_keydate['close']:
        if closedict == '':
            closedict.append(closeprice)
        else:
            change = ((closedict / closeprice) - 1) * 100
            perchange.append(change)
            closedict = closeprice
    symbol_keydate['percent_change_close'] = perchange
    print(perchange)
    print(symbol_keydate)
    # Adding this in so Jason L. can work from his laptop which is apple, push to github, pull on his desktop, and continue working in the windows environment
    if platform.system() == 'Darwin':
        try:
            with open('/Users/analyticsmachine/Desktop/MyLife/SchoolWork/UVA/CS_5010/project/biotech/stockoutput.csv', 'a') as f:
                symbol_keydate.to_csv(f, header=True)
        except:
            symbol_keydate.to_csv('/Users/analyticsmachine/Desktop/MyLife/SchoolWork/UVA/CS_5010/project/biotech/stockoutput.csv', header=True)
    else:
        try:
            with open('C:\\Users\Jason\Desktop\MyLife\\UVA\CS_5010\Python\Python_Project\\biotech\output.csv', 'a') as f:
                symbol_keydate.to_csv(f, header=True)
        except:
            symbol_keydate.to_csv('C:\\Users\Jason\Desktop\MyLife\\UVA\CS_5010\Python\Python_Project\\biotech\output.csv', header=True)


for value in zip(list, list.values()):
    test = value[1].split(',')
    symbol1 = test[0]
    event_date1 = test[1]
    event_number = value[0]
    stockhunter(event_number, event_date1, symbol1)








