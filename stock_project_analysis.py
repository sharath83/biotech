__author__ = 'Jason'

import pandas as pd
import numpy as np
import pandas.io.date_converters as conv

# the stocks in the csv file include AMGN, GILD, LLY, BIIB, PFE, GILD, BMS, and MRK

# below are the dates of interest, the company, and the expected sign(postive or negative)

# Date              Company             Expected Sign          Phase
# 3/19/2013         AMG                 Positive               3
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

print(stocksdf.ix['2013-01-01':'2013-01-03'])


#mask = (stocksdf['date'] > '2013-3-08') & (stocksdf['date'] < '2013-3-30')
#print(stocksdf.loc[mask])
#print(stocksdf[stocksdf['date'] < '2013-Jan-30'])
