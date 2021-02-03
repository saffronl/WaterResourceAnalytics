# Import libraries
import pandas as pd
import numpy as np
import statistics as st
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas.core.common import flatten

# Creating dataset
file = pd.read_excel(r'/Users/saffron/Documents/PWDdryweather.xlsx',sheet_name='USGS')

df = pd.DataFrame(file)
df = df.dropna(subset=['parameter','gage','data.value'])

# Make a list of only the unique locations and bacteria types
Before = [1475530,1473900,1467086,1467042]
After = [1475548,1474000,1467087,1467048]
BacteriaList = df['parameter'].unique().tolist()


mergeddf = pd.DataFrame()

for L in range(len(Before)):
    for B in range(len(BacteriaList)):

        DATA = (df.loc[(df['parameter'] == BacteriaList[B])
                           & (df['gage'] == Before[L])])
        date = DATA['datetime'].dt.strftime("%Y-%m-%d").tolist()
        bacteria = DATA['parameter'].tolist()
        gage = DATA['gage'].tolist()
        data = DATA['data.value'].tolist()
        beforedf = pd.DataFrame(list(zip(date,bacteria,gage,data)),columns=["date", "bacteria", "before gage", "before data"])

        DATA = (df.loc[(df['parameter'] == BacteriaList[B])
                           & (df['gage'] == After[L])])
        date = DATA['datetime'].dt.strftime("%Y-%m-%d").tolist()
        bacteria = DATA['parameter'].tolist()
        gage = DATA['gage'].tolist()
        data = DATA['data.value'].tolist()
        afterdf = pd.DataFrame(list(zip(date, bacteria, gage, data)), columns=["date", "bacteria", "after gage", "after data"])

        merge = pd.merge(beforedf, afterdf, how='inner', on=['date', 'bacteria'])

        mergeddf = mergeddf.append(merge)

def rel_percent(initiallist,finallist):
    i = 0
    percentlist = []
    while i < len(initiallist):
        percent = round((finallist[i]-initiallist[i])/initiallist[i],4)
        percentlist.append(percent)
        i+=1
    return percentlist

BacteriaList = mergeddf['bacteria'].unique().tolist()

relpercentlist = []
for L in range(len(Before)):
    for B in range(len(BacteriaList)):
        DATA = (mergeddf.loc[(mergeddf['bacteria'] == BacteriaList[B])
                       & (mergeddf['before gage'] == Before[L])])
        beforegage = DATA['before gage'].tolist()
        beforelist = DATA['before data'].tolist()
        afterlist = DATA['after data'].tolist()
        relpercentlist.append(rel_percent(beforelist,afterlist))

print('rel percent\n',relpercentlist)
print(len(list(flatten(relpercentlist))))

mergeddf['rel percent'] = list(flatten(relpercentlist))
print('all ',mergeddf)

file_name = 'PWDdrydata_merge.xlsx'

# saving the excel
mergeddf.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')


