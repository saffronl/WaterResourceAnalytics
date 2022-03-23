# Import libraries
import pandas as pd
import numpy as np
import statistics as st
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas.core.common import flatten

### This is for the tributary data!
## Want to compare upstream and downstream values


# Creating dataset
file = pd.read_excel(r'/Users/saffron/Documents/PWDdryweather.xlsx',sheet_name='USGS')

#Make a pandas datafram
df = pd.DataFrame(file)
df = df.dropna(subset=['parameter','gage','data.value'])

# Make a list of only the unique locations and bacteria types
Before = [1475530,1473900,1467086,1467042]
After = [1475548,1474000,1467087,1467048]
BacteriaList = df['parameter'].unique().tolist() # make a list of all the bacteria types


mergeddf = pd.DataFrame()

for L in range(len(Before)):
    for B in range(len(BacteriaList)):
        DATA = (df.loc[(df['parameter'] == BacteriaList[B]) # just for the UPSTREAM values
                           & (df['gage'] == Before[L])]) # get the data for one location and one bacteria type
        date = DATA['datetime'].dt.strftime("%Y-%m-%d").tolist() # get a list of the dates for the filtered data ^
        bacteria = DATA['parameter'].tolist() # put the bacteria data into a list for the filtered data
        gage = DATA['gage'].tolist() # put the gage data into a list for the filtered data
        data = DATA['data.value'].tolist() # get list of the data values for the filtered data
        beforedf = pd.DataFrame(list(zip(date,bacteria,gage,data)),columns=["date", "bacteria", "before gage", "before data"])
        # put all of the lists into one dataframe^

        DATA = (df.loc[(df['parameter'] == BacteriaList[B])
                           & (df['gage'] == After[L])]) # repeat, but for the DOWNSTREAM values
        date = DATA['datetime'].dt.strftime("%Y-%m-%d").tolist()
        bacteria = DATA['parameter'].tolist()
        gage = DATA['gage'].tolist()
        data = DATA['data.value'].tolist()
        afterdf = pd.DataFrame(list(zip(date, bacteria, gage, data)), columns=["date", "bacteria", "after gage", "after data"])

        merge = pd.merge(beforedf, afterdf, how='inner', on=['date', 'bacteria'])
        # merge the upstream and downstream (before and after) based on the same data and bacteria

        mergeddf = mergeddf.append(merge) # merge for all locations and bacteria

def rel_percent(initiallist,finallist): 
    i = 0
    percentlist = []
    while i < len(initiallist):
        percent = round((finallist[i]-initiallist[i])/initiallist[i],4) ## calculating the percent change!!!
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
        relpercentlist.append(rel_percent(beforelist,afterlist)) # put the percent change into the dataframe!

print('rel percent\n',relpercentlist)
print(len(list(flatten(relpercentlist))))

mergeddf['rel percent'] = list(flatten(relpercentlist))
print('all ',mergeddf)

file_name = 'PWDdrydata_merge.xlsx'

# saving the excel
mergeddf.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')


