__author__ = 'Jason'

import pandas as pd
import numpy as np
import pandas.io.date_converters as conv

# the stocks in the csv file include AMGN, GILD, LLY, BIIB, PFE, GILD, BMS, and MRK

# below are the dates of interest, the company, and the expected sign(postive or negative)

# Date              Company             Expected Sign          Phase
# 3/19/2013         AMGN                Positive               3
# 3/5/2013          GILD                Positive               2
# 2/7/2013          LLY                 Negative               3
# 1/24/2013         BIIB                Positive               3
# 1/3/2013          BIIB                Negative               3
# 12/5/2012         PFE                 Positive               2
# 11/10/2012        GILD                Positive               2
# 10/11/2012        PFE                 Positive               3
# 9/26/2012         BIIB                Positive               3
# 8/8/2012          AMGN                Negative               3
# 8/6/2012          PFE                 Negative               3
# 8/2/2012          BMS                 Negative               3
# 7/11/2012         LLY                 Negative               3
# 7/2/2012          BMS                 Positive               1
# 5/22/2012         LLY                 Positive               2
# 5/16/2012         AMGN                Positive               2
# 3/28/2012         AMGN                Positive               2
# 3/28/2012         LLY                 Positive               2
# 3/25/2012         AMGN                Positive               1
# 3/5/2012          MRK                 Positive               3
# 2/3/2012          GILD                Positive               2
# 12/22/2011        BMS                 Negative               3
# 8/9/2011          BIIB                Positive               2
# 2/2/2011          BMS                 Negative               3

stocksdf = pd.read_csv('stocks_historical.csv', names = ['symbol', 'date', 'open', 'high', 'low', 'close', 'volume'],
                       parse_dates = 'date',
                       infer_datetime_format = True,
                       keep_date_col = True,
                       index_col = 1)

# subsetting each stock into its own dataframe for futher analysis
amgn_df = stocksdf[stocksdf['symbol'] == 'AMGN']
mrk = stocksdf[stocksdf['symbol'] == 'MRK']
gild = stocksdf[stocksdf['symbol'] == 'GILD']
lly = stocksdf[stocksdf['symbol'] == 'LLY']
bms = stocksdf[stocksdf['symbol'] == 'BMS']
pfe = stocksdf[stocksdf['symbol'] == 'PFE']
biib = stocksdf[stocksdf['symbol'] == 'BIIB']

# retrieving stock values for this key date 3/19/2013 for AMGN
# first is to the retrieve the 10 days prior to the event and the 10 days after the event, including event date
print(amgn_df.ix['2013-03-08':'2013-03-18'])
print(type(amgn_df))

def keydate1():
    keydatebefore = stocksdf.ix['2013-03-08':'2013-03-18']
    keydate = stocksdf.ix['2013-03-19']
    keydateafter = stocksdf.ix['2013-03-19':'2013-03-29']
    amgn_keybefore = keydatebefore[keydatebefore['symbol'] == 'AMGN']
    amgn_keydate = keydate[keydate['symbol'] == 'AMGN']
    amgn_keyafter = keydateafter[keydateafter['symbol'] == 'AMGN']
    # calculating average before event date of closing price
    sum = 0
    count = 0
    for average in amgn_keybefore['close']:
        sum = sum + average
        count = count + 1
    avg_before = sum / count
    print('The average price before the event occurred was:', avg_before)
    event_close = amgn_keydate['close']
    print('The closing price on the day of the event was: ', event_close)
#keydate1()

# Retrieving keydate 2: 3/5/2013          GILD
def keydate2():
    keydate2 = stocksdf.ix['2013-02-23':'2013-03-15']
    print(keydate2)
    gild_keydate2 = keydate2[keydate2['symbol'] == 'GILD']
    print(gild_keydate2)

# Retrieving keydate 3: 2/7/2013          LLY
def keydate3():
    keydate3 = stocksdf.ix['2013-01-28':'2013-02-17']
    lly_keydate3 = keydate3[keydate3['symbol'] == 'LLY']
    print(lly_keydate3)

# Retrieiving keydate 4: 1/24/2013         BIIB
def keydate4():
    keydate4 = stocksdf.ix['2013-01-14':'2013-02-03']
    biib_keydate4 = keydate4[keydate4['symbol'] == 'BIIB']
    print(biib_keydate4)

# Retrieving keydate 5: 1/3/2013          BIIB
def keydate5():
    keydate5 = stocksdf.ix['2012-12-24':'2013-01-13']
    biib_keydate5 = keydate5[keydate5['symbol'] == 'BIIB']
    print(biib_keydate5)

# Retrieving keydate 6 12/5/2012         PFE
def keydate6():
    keydate6 = stocksdf.ix['2012-11-25':'2012-12-15']
    pfe_keydate6 = keydate6[keydate6['symbol'] == 'PFE']
    print(pfe_keydate6)
    print(len(pfe_keydate6))

# Retrieving keydate 7 11/10/2012        GILD :
def keydate7():
    keydate7 = stocksdf.ix['2012-10-31':'2012-11-20']
    gild_keydate7 = keydate7[keydate7['symbol'] == "GILD"]
    print(gild_keydate7)

# Retrieving keydate 8 10/11/2012 PFE:
def keydate8():
    keydate8 = stocksdf.ix['2012-10-01':'2012-10-21']
    pfe_keydate8 = keydate8[keydate8['symbol'] == 'PFE']
    print(pfe_keydate8)

# Retrieving keydate 9 9/26/2012 BIIB
def keydate9():
    keydate9 = stocksdf.ix['2012-09-16':'2012-10-05']
    biib_keydate9 = keydate9[keydate9['symbol'] == 'BIIB']
    print(biib_keydate9)

# Retrieving keydate 1- 8/8/2012 AMGN
def keydate10():
    keydate10 = stocksdf.ix['2012-07-28':'2012-08-18']
    amgn_keydate10 = keydate10[keydate10['symbol'] == 'AMGN']
    print(amgn_keydate10)
keydate10()





# 8/8/2012          AMGN


#mask = (stocksdf['date'] > '2013-3-08') & (stocksdf['date'] < '2013-3-30')
#print(stocksdf.loc[mask])
#print(stocksdf[stocksdf['date'] < '2013-Jan-30'])
